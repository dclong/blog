#!/usr/bin/env python3
# encoding: utf-8
"""Main logic of the blogging system."""

from concurrent.futures import InterpreterPoolExecutor
from collections import namedtuple
import datetime
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess as sp
import sys
from typing import TypeAlias, Sequence, Iterable
import yaml
from loguru import logger
from tqdm import tqdm
from utils import BASE_DIR, qmarks

AnyPath: TypeAlias = str | Path
AUTHOR = "Benjamin Du"
EN = "en"
CN = "cn"
HOME = "home"
MISC = "misc"
OUTDATED = "outdated"
DISCLAIMER_MISC = "**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**"
DISCLAIMER_OUTDATED = "**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**"
CATEGORY = "Computer Science"
TAGS = "Computer Science, programming"
MARKDOWN = ".md"
IPYNB = ".ipynb"
NOW_DASH = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
TODAY_DASH = NOW_DASH[:10]
YYYYMM_slash = TODAY_DASH[:7].replace("-", "/")
with Path("words.yaml").open(encoding="utf-8") as _:
    WORDS = yaml.load(_, Loader=yaml.FullLoader)
POSTS_COLS = [
    "path",
    "dir",
    "status",
    "date",
    "modified",
    "author",
    "slug",
    "title",
    "category",
    "tags",
    "content",
    "empty",
    "updated",
    "name_title_mismatch",
]
SRPS_COLS = ["path", "title", "dir", "slug"]

Record = namedtuple("Record", POSTS_COLS)


def is_post(path: Path | str) -> bool:
    if isinstance(path, str):
        path = Path(path)
    return path.suffix in (MARKDOWN, IPYNB)


def parse_records() -> list[Record]:
    logger.info("Parsing posts into records ...")
    paths = list(
        path
        for path in BASE_DIR.glob("*/content/**/*")
        if is_post(path) and not path.parent.name.startswith(".")
    )
    with InterpreterPoolExecutor() as executor:
        return executor.map(lambda p: Post(p).record(), paths)


class Post:
    """A class abstracting a post."""

    def __init__(self, path: AnyPath):
        if isinstance(path, str):
            path = Path(path)
        path = path.resolve()
        if not is_post(path):
            raise ValueError(f"{self.path} is not a {MARKDOWN} or {IPYNB} file.")
        self.path = path

    def __str__(self):
        return str(self.path)

    def is_markdown(self):
        return self.path.suffix == MARKDOWN

    def is_notebook(self):
        return self.path.suffix == IPYNB

    def diff(self, content: str) -> bool:
        """Check whether there is any difference between this post's content and the given content.
        :param content: The content to compare against.
        """
        return self.record().content != content

    def blog_dir(self):
        """Get the corresponding blog directory (home, en, cn or misc) of a post."""
        return self.path.parent.parent.parent.parent.parent.stem

    def update_after_move(self) -> None:
        """Update the post after move.
        There are 3 possible change.
        1. The disclaimer might be added/removed
            depending on whether the post is moved to the misc sub blog directory.
        2. The slug of the post is updated to match the path of the post.
        3. The title should be updated to match the file name.
            Both 2 and 3 will prompt to user for confirmation.
        """
        if self.is_markdown():
            self._update_after_move_markdown()
        else:
            self._update_after_move_notebook()

    def _update_after_move_notebook(self) -> None:
        notebook = self._read_notebook()
        blog_dir = self.blog_dir()
        if blog_dir in (MISC, OUTDATED):
            DISCLAIMER = DISCLAIMER_MISC if blog_dir == MISC else DISCLAIMER_OUTDATED
            DISCLAIMER_OTHER = (
                DISCLAIMER_OUTDATED if blog_dir == MISC else DISCLAIMER_MISC
            )
            if notebook["cells"][1]["source"][0] == DISCLAIMER_OTHER:
                notebook["cells"][1]["source"][0] = DISCLAIMER
            if notebook["cells"][1]["source"][0] != DISCLAIMER:
                notebook["cells"].insert(
                    1, {"source": [DISCLAIMER], "cell_type": "markdown", "metadata": {}}
                )
            self._write_notebook(notebook)
        elif notebook["cells"][1]["source"][0] in (
            DISCLAIMER_MISC,
            DISCLAIMER_OUTDATED,
        ):
            notebook["cells"].pop(1)
        self._write_notebook(notebook)

    def _write_notebook(self, notebook: dict):
        self.path.write_text(json.dumps(notebook, indent=1), encoding="utf-8")

    def _update_after_move_markdown(self) -> None:
        blog_dir = self.blog_dir()
        if blog_dir in (MISC, OUTDATED):
            DISCLAIMER = DISCLAIMER_MISC if blog_dir == MISC else DISCLAIMER_OUTDATED
            with self.path.open(encoding="utf-8") as fin:
                lines = fin.readlines()
            index = [line.strip() for line in lines].index("")
            with self.path.open("w", encoding="utf-8") as fout:
                fout.writelines(lines[:index])
                fout.writelines("\n" + DISCLAIMER + "\n")
                index_5 = index + 5
                fout.writelines(
                    line
                    for line in lines[index:index_5]
                    if line.strip() not in (DISCLAIMER_MISC, DISCLAIMER_OUTDATED)
                )
                fout.writelines(lines[index_5:])
            return
        text = (
            self.path.read_text(encoding="utf-8")
            .replace(DISCLAIMER_MISC, "")
            .replace(DISCLAIMER_OUTDATED, "")
        )
        self.path.write_text(text, encoding="utf-8")

    @staticmethod
    def format_title(title):
        title = title.title()
        for origin, replace in WORDS:
            title = title.replace(f" {origin} ", f" {replace} ")
            if title.startswith(origin + " "):
                title = title.replace(origin + " ", replace + " ")
            if title.endswith(" " + origin):
                title = title.replace(" " + origin, " " + replace)
        if title.startswith("the "):
            title = "The " + title[4:]
        if title.startswith("a "):
            title = "A " + title[2:]
        return title

    def _read_notebook(self) -> dict:
        notebook = json.loads(self.path.read_text(encoding="utf-8"))
        if notebook["cells"][0]["cell_type"] != "markdown":
            raise SyntaxError(
                f"The first cell of the notebook {self.path} is not a markdown cell!"
            )
        return notebook

    def update_tags(self, from_tag: str, to_tag: str) -> list[str]:
        """Update the tag from_tag of the post to the tag to_tag.
        :param from_tag: The tag to be changed.
        :param to_tag: The tag to change to.
        :return: The new list of tags in the post.
        """
        # TODO: need to be updated: 1. support both markdown and notebook;
        # 2. leverage update_meta_field? Is it possible?
        with self.path.open(encoding="utf-8") as fin:
            lines = fin.readlines()
        for idx, line in enumerate(lines):
            if line.startswith("Tags: "):
                tags = (tag.strip() for tag in line[5:].split(","))
                tags = [to_tag if tag == from_tag else tag for tag in tags]
                lines[idx] = f"Tags: {', '.join(tags)}"
                break
        else:
            tags = []
        with self.path.open("w", encoding="utf-8") as fout:
            fout.writelines(lines)
        return tags

    def record(self) -> Record:
        if self.is_markdown():
            return self._parse_markdown()
        return self._parse_notebook()

    def _read_lines_markdown(self) -> tuple[list[str], list[str]]:
        """Read lines of a markdown post.

        return: A tuple of the format (meta, content),
            where meta is a list containing lines of meta fields
            and content is a list containing lines of content.
        """
        meta = []
        content = []
        with self.path.open(encoding="utf-8") as fin:
            for line in fin:
                if re.match("[A-Za-z]+: ", line):
                    meta.append(line)
                else:
                    content.append(line)
                    break
            for line in fin:
                content.append(line)
        return meta, content

    def _parse_markdown(self) -> Record:
        meta, content = self._read_lines_markdown()
        # parse metadata
        status = ""
        date = ""
        modified = NOW_DASH
        author = ""
        slug = ""
        title = ""
        category = ""
        tags = ""
        for line in meta:
            if line.startswith("Status: "):
                status = line[8:].strip()
            elif line.startswith("Date: "):
                date = line[6:].strip()
            elif line.startswith("Modified: "):
                modified = line[10:].strip()
            elif line.startswith("Author: "):
                author = line[8:].strip()
            elif line.startswith("Slug: "):
                slug = line[6:].strip()
            elif line.startswith("Title: "):
                title = line[7:].strip()
            elif line.startswith("Category: "):
                category = line[10:].strip()
            elif line.startswith("Tags: "):
                tags = line[6:].strip()
                if not tags.endswith(","):
                    tags = tags + ","
        # content
        empty = self._is_ess_empty(content)
        content = title + "\n" + category + "\n" + tags + "\n" + "".join(content)
        name_title_mismatch = self.is_name_title_mismatch(title)
        return Record(
            str(self.path.relative_to(BASE_DIR)),
            self.blog_dir(),
            status,
            date,
            modified,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            0,
            name_title_mismatch,
        )

    def _parse_notebook(self) -> Record:
        content = self.path.read_text(encoding="utf-8")
        cells = json.loads(content)["cells"]
        empty = 1 if len(cells) <= 1 else 0
        if cells[0]["cell_type"] != "markdown":
            raise SyntaxError(
                f"The first cell of the notebook {self.path} is not a markdown cell!"
            )
        meta = cells[0]["source"]
        status = ""
        date = ""
        modified = NOW_DASH
        author = ""
        slug = ""
        title = ""
        category = ""
        tags = ""
        for line in meta:
            if not re.search("^- [a-zA-Z]+:", line):
                raise SyntaxError(
                    f"The meta line '{line}' of the notebook {self.path} does not confront to the format '- MetaField: Value'!"
                )
            if line.startswith("- Status:"):
                status = line[9:].strip()
            elif line.startswith("- Date:"):
                date = line[7:].strip()
            elif line.startswith("- Modified:"):
                modified = line[11:].strip()
            elif line.startswith("- Author:"):
                author = line[9:].strip()
            elif line.startswith("- Slug:"):
                slug = line[7:].strip()
            elif line.startswith("- Title:"):
                title = line[8:].strip()
            elif line.startswith("- Category:"):
                category = line[11:].strip()
            elif line.startswith("- Tags:"):
                tags = line[7:].strip()
        name_title_mismatch = self.is_name_title_mismatch(title)
        return Record(
            str(self.path.relative_to(BASE_DIR)),
            self.blog_dir(),
            status,
            date,
            modified,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            0,
            name_title_mismatch,
        )

    def is_name_title_mismatch(self, title: str) -> int:
        """Check whether the file anme and the title of the post does not match.

        :param title: The title of the post.
        :return: 1 if mismatch and 0 otherwise.
        """
        # TODO: seems that title is not needed!!!
        title_new = Post.format_title(self.stem_name().replace("-", " "))
        title_old = title.replace("-", " ")
        return 1 if title_old != title_new else 0

    def stem_name(self) -> str:
        return self.path.stem[11:]

    def _is_ess_empty(self, lines: list[str]) -> int:
        """Check whether the lines are essentially empty.
        :param lines: A list of lines.
        """
        content = "".join(line.strip() for line in lines)
        is_empty = re.sub(r"\*\*.+\*\*", "", content).replace("**", "") == ""
        return 1 if is_empty else 0

    def update_meta_field(self, mapping: dict[str, str]) -> None:
        if self.is_markdown():
            meta, content = self._read_lines_markdown()
            self._update_meta_field_lines(meta, mapping)
            with self.path.open("w", encoding="utf-8") as fout:
                fout.writelines(meta)
                fout.writelines(content)
            return
        mapping = {f"- {field}": value for field, value in mapping.items()}
        notebook = self._read_notebook()
        meta = notebook["cells"][0]["source"]
        self._update_meta_field_lines(meta, mapping)
        self._write_notebook(notebook)

    @staticmethod
    def _update_meta_field_lines(lines: list[str], mapping: dict[str, str]) -> None:
        nrow = len(lines)
        for field, value in mapping.items():
            for idx in range(nrow):
                line = lines[idx]
                if line.startswith(f"{field}:"):
                    lines[idx] = f"{field}: {value}\n"
                    break
                if line.startswith(f"- {field}:"):
                    lines[idx] = f"- {field}: {value}\n"
                    break
            else:
                lines.append(f"{field}: {value}\n")

    def match_name(self):
        title = Post.format_title(self.stem_name().replace("-", " "))
        slug = title.lower().replace(" ", "-")
        self.update_meta_field(
            {
                "Title": title,
                "Slug": slug,
            }
        )

    def match_title(self) -> None:
        """Make the post's slug and path name match its title."""
        # file name
        stem_name = self.stem_name()
        title = self.title()
        slug = title.lower().replace(" ", "-")
        name = self.path.name.replace(stem_name, slug)
        path = self.path.with_name(name)
        os.rename(self.path, path)
        self.path = path
        # meta field Slug
        self.update_meta_field({"Slug": slug})

    def title(self) -> str:
        """Get the title of the post.
        :return: The title of the post.
        """
        if self.is_markdown():
            return self._title_markdown()
        return self._title_notebook()

    def _title_notebook(self):
        with self.path.open(encoding="utf-8") as fin:
            cell = json.load(fin)["cells"][0]
        if cell["cell_type"] != "markdown":
            raise SyntaxError(
                f"The first cell of the notebook {self.path} is not a markdown cell!"
            )
        meta = cell["source"]
        for line in meta:
            if not re.search("^- [a-zA-Z]+:", line):
                raise SyntaxError(
                    f"The meta line {line} of the notebook {self.path} does not confront to the format '- MetaField: Value'!"
                )
            if line.startswith("- Title:"):
                return line[8:].strip()
        raise SyntaxError(f"No title in the post {self.path}!")

    def _title_markdown(self) -> str:
        with self.path.open(encoding="utf-8") as fin:
            for line in fin:
                if line.startswith("Title: "):
                    return line[7:].strip()
        raise SyntaxError(f"No title in the post {self.path}!")

    @staticmethod
    def slug(title: str) -> str:
        """Create a slug from the title.
        :param title: The title to create the slug from.
        :return: A slug created from the title.
        """
        return title.replace(" ", "-").replace("/", "-")

    def create(self, title: str):
        if self.is_markdown():
            return self._create_markdown(title)
        return self._create_notebook(title)

    def _create_notebook(self, title: str):
        text = self._replace_meta(
            title=title, slug=Post.slug(title), category=CATEGORY, tags=TAGS
        )
        if self.blog_dir() == MISC:
            text = text.replace("${DISCLAIMER}", DISCLAIMER_MISC)
        else:
            text = text.replace("${DISCLAIMER}", "")
        with self.path.open("w", encoding="utf-8") as fout:
            fout.write(text)

    def _create_markdown(self, title: str):
        with self.path.open("w", encoding="utf-8") as fout:
            fout.writelines("Status: published\n")
            fout.writelines(f"Date: {NOW_DASH}\n")
            fout.writelines(f"Modified: {NOW_DASH}\n")
            fout.writelines("Author: Benjamin Du\n")
            fout.writelines(f"Slug: {Post.slug(title)}\n")
            fout.writelines(f"Title: {Post.format_title(title)}\n")
            fout.writelines(f"Category: {CATEGORY}\n")
            fout.writelines(f"Tags: {TAGS}\n")
            if self.blog_dir() == MISC:
                fout.writelines("\n")
                fout.writelines(DISCLAIMER_MISC)
                fout.writelines("\n")

    @staticmethod
    def _replace_meta(title, slug, category, tags) -> str:
        text = (BASE_DIR / "themes/template.ipynb").read_text()
        return (
            text.replace("${AUTHOR}", AUTHOR)
            .replace("${DATE}", NOW_DASH)
            .replace("${MODIFIED}", NOW_DASH)
            .replace("${TITLE}", Post.format_title(title))
            .replace("${SLUG}", slug)
            .replace("${CATEGORY}", category)
            .replace("${TAGS}", tags)
        )

    def convert(self):
        """Convert a markdown post to a notebook blog, vice versa."""
        if self.is_markdown():
            self._md_to_nb()
        else:
            self._nb_to_md()

    def _nb_to_md(self):
        raise NotImplementedError("Post._nb_to_md is not implemented yet!")

    def _md_to_nb(self):
        record = self.record()
        text = self._replace_meta(
            title=record.title,
            slug=record.slug,
            category=record.category,
            tags=record.tags,
        )
        notebook = json.loads(text)
        notebook["cells"][1]["source"] = re.split(r"(?<=\n)", record.content)
        path = self.path.with_suffix(IPYNB)
        with path.open("w", encoding="utf-8") as fout:
            json.dump(notebook, fout, indent=1)
        dir_ = BASE_DIR / "trash" / self.path.parent.name
        dir_.mkdir(parents=True, exist_ok=True)
        self.path.rename(dir_ / self.path.name)
        self.path = path


class Blogger:
    """A class for managing blog."""

    def __init__(self, db: str = ""):
        """Create an instance of Blogger.

        :param dir_: the root directory of the blog.
        :param db: the path to the SQLite3 database file.
        """
        self._db = db if db else str(BASE_DIR / ".blogger.sqlite3")
        self._conn = sqlite3.connect(self._db)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._create_vtable_posts()

    def _create_vtable_posts(self):
        sql = f"""
            CREATE VIRTUAL TABLE IF NOT EXISTS posts USING fts5 (
                {", ".join(POSTS_COLS)},
                tokenize = porter
            )
            """
        self.execute(sql)

    def _create_table_srps(self):
        sql = f"CREATE TABLE IF NOT EXISTS srps ({', '.join(SRPS_COLS)})"
        self.execute(sql)

    def clean_db(self):
        """Remove the SQLite3 database."""
        os.remove(self._db)

    def commit(self):
        """Commit changes made to the SQLite3 database."""
        self._conn.commit()

    def update_category(self, post: Post | AnyPath, category: str):
        if isinstance(post, (str, Path)):
            post = Post(post)
        post.update_meta_field("Category", category)
        self.update_records(paths=[post.path], mapping={"category": category})

    def update_tags(self, post: Post, from_tag: str, to_tag: str):
        """Update the tag from_tag of the post to the tag to_tag."""
        tags = post.update_tags(from_tag, to_tag)
        self.update_records(paths=[post.path], mapping={"tags": ", ".join(tags) + ","})

    def trust_notebooks(self):
        for dir_ in (EN, CN, MISC):
            cmd = f"jupyter trust {dir_}/content/*.ipynb"
            sp.run(cmd, shell=True, check=True)

    def reload_posts(self):
        """Reload posts into the SQLite3 database."""
        self._create_vtable_posts()
        self.execute("DELETE FROM posts")
        records = parse_records()
        logger.info("Inserting records into SQLite3 ...")
        batch = 1000
        for i in tqdm(range(0, len(records), batch)):
            self.load_records(records[i : i + batch])
        self.commit()

    def load_records(self, records: Iterable[Record]):
        sql = f"""
            INSERT INTO posts (
                {", ".join(POSTS_COLS)}
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """
        self._conn.executemany(sql, records)

    def load_post(self, post: Post):
        sql = f"""
            INSERT INTO posts (
                {", ".join(POSTS_COLS)}
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """
        self.execute(sql, post.record())

    def trash(self, paths: str | list[str]):
        """Move the specified posts to the trash directory.

        :param paths: Paths of posts to be removed.
        """
        if isinstance(paths, str):
            paths = [paths]
        dir_ = BASE_DIR / "trash"
        if not dir_.is_dir():
            dir_.mkdir(0o700, True, True)
        for path in paths:
            shutil.move(path, dir_)
        self.delete_by_path(paths)

    def delete_by_path(self, paths: str | list[str]):
        if isinstance(paths, str):
            paths = [paths]
        sql = f"""
            DELETE FROM posts
            WHERE path in ({qmarks(paths)})
            """
        self.execute(sql, paths)

    def move(self, src: AnyPath | Sequence[AnyPath], dst: str) -> None:
        """Move specified posts into a destination directory.

        :param src: A (sequence of) path(s).
            A path can be of either the str or the Path type.
        :param dst: The destination path or directory to move posts to.
        """
        if isinstance(src, (str, Path)):
            self._move_1(src, dst)
            return
        if len(src) > 1 and not os.path.isdir(dst):
            sys.exit("dst must be a directory when moving multiple files")
        for file in src:
            self._move_1(file, dst)

    def _move_1(self, src: AnyPath, dst: AnyPath) -> None:
        """Move a post to the specified location."""
        if isinstance(src, str):
            src = Path(src)
        if dst in (EN, CN, MISC, OUTDATED):
            dst = BASE_DIR.joinpath(dst, "content", *src.parts[-4:])
        elif isinstance(dst, str):
            dst = Path(dst)
        if src.resolve() == dst.resolve():
            Post(dst).update_after_move()
            return
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(src, dst)
        post = Post(dst)
        post.update_after_move()
        self.update_records(paths=[src], mapping={"path": dst, "dir": post.blog_dir()})

    def _reg_param(self, param):
        if isinstance(param, (int, float, str)):
            return param
        return str(param)

    def execute(self, operation: str, parameters=()):
        parameters = [self._reg_param(param) for param in parameters]
        return self._conn.execute(operation, parameters)

    def edit(self, paths: str | list[str], editor: str) -> None:
        """Edit the specified posts using the specified editor."""
        if not isinstance(paths, list):
            paths = [paths]
        self.update_records(paths=paths, mapping={"updated": 1})
        paths = " ".join(f"'{path}'" for path in paths)
        os.system(f"{editor} {paths}")

    def update_records(self, paths: list[str] | list[Path], mapping: dict) -> None:
        """Update records corresponding to the specified paths.
        :param mapping: A dictionary of the form dict[field, value].
        :param paths: Paths of records to be updated.
        """
        sql = f"""
            UPDATE posts 
            SET {", ".join(f"{key} = ?" for key in mapping)} 
            WHERE path in ({qmarks(paths)})
            """
        self.execute(sql, list(mapping.values()) + paths)

    def update(self, reset: bool):
        """Update information of the changed posts.

        :param reset: If true, reset updated = 0 for updated = 1 but not changed posts.
        """
        sql = "SELECT path, content FROM posts WHERE updated = 1"
        rows = self.execute(sql).fetchall()
        # posts that were not changed
        if reset:
            paths = [path for path, content in rows if not Post(path).diff(content)]
            self.update_records(paths=paths, mapping={"updated": 0})
        # posts that were changed
        paths = [path for path, content in rows if Post(path).diff(content)]
        self.delete_by_path(paths)
        for path in paths:
            post = Post(path)
            post.update_meta_field({"Modified": NOW_DASH})
            self.load_post(post)

    def add_post(
        self, title: str, dir_: str, notebook: bool = True, load_to_db: bool = False
    ) -> Path:
        """Add a new post with the given title."""
        path = self._find_post(title)
        if not path:
            stem = Post.slug(title)
            dir_ = BASE_DIR / dir_ / "content" / YYYYMM_slash / stem
            dir_.mkdir(parents=True, exist_ok=True)
            suffix = IPYNB if notebook else MARKDOWN
            path = dir_ / (stem + suffix)
            post = Post(path)
            post.create(title)
            if load_to_db:
                self.load_post(post)
        print(f"\nThe following post is added.\n{path}\n")
        return path.resolve()

    def _find_post(self, title: str) -> Path | None:
        """Find existing post matching the given title.

        :return: Return the path of the existing post if any,
        otherwise return empty string.
        """
        # find all posts and get rid of leading dates
        sql = "SELECT path FROM posts WHERE path LIKE ?"
        row = self.execute(sql, [f"%{Post.slug(title)}.%"]).fetchone()
        if row:
            return Path(row[0])
        return None

    def empty_posts(self, dry_run=False) -> None:
        """Load all empty posts into the table srps."""
        self.reload_posts()
        self.clear_srps()
        sql = f"""
            INSERT INTO srps
            SELECT {", ".join(SRPS_COLS)}
            FROM posts
            WHERE empty = 1
            """
        if dry_run:
            print(sql)
            return
        self.execute(sql)
        self.commit()

    def find_name_title_mismatch(self, dry_run=False):
        self.clear_srps()
        sql = """
            INSERT INTO srps
            SELECT path
            FROM posts
            WHERE name_title_mismatch = 1 AND dir <> 'cn'
            """
        if dry_run:
            print(sql)
            return
        self.execute(sql)
        self.commit()

    def search(self, phrase: str, filter_: str = "", dry_run=False):
        """Search for posts containing the phrase.

        :param phrase: The phrase to search for in posts.
        :param filter_: Extra filtering conditions.
        :param dry_run: Dry run the search,
            i.e., print out SQL queries without executing them.
        """
        self.clear_srps()
        conditions = []
        if phrase:
            conditions.append(f"posts MATCH '{phrase}'")
        if filter_:
            filter_ = conditions.append(filter_)
        where = " AND ".join(conditions)
        if where:
            where = "WHERE " + where
        sql = f"""
            INSERT INTO srps
            SELECT path, title, dir, slug
            FROM posts
            {where}
            ORDER BY rank
            """
        if dry_run:
            print(sql)
            return
        self.execute(sql)
        self.commit()

    def clear_srps(self):
        """Clean contents of the table srps."""
        self._create_table_srps()
        self.execute("DELETE FROM srps")

    def last(self, n: int):
        """Get last (according to modification time) n posts.
        :param n: The number of posts to get.
        """
        self.clear_srps()
        sql = f"""
            INSERT INTO srps
            SELECT path, title, dir, slug
            FROM posts
            ORDER BY modified DESC
            LIMIT {n}
            """
        self.execute(sql)
        self.commit()

    def path(self, idx: int | list[int]) -> list[str]:
        if isinstance(idx, int):
            idx = [idx]
        sql = f"SELECT path FROM srps WHERE rowid in ({qmarks(idx)})"
        return [row[0] for row in self.execute(sql, idx).fetchall()]

    def query(self, sql: str, params: Sequence = ()):
        return self.execute(sql, params).fetchall()

    def tags(self, where=""):
        """Get all tags and their frequencies in all posts.

        :param where:
        """
        if where:
            where = "WHERE " + where
        sql = f"SELECT tags FROM posts {where}"
        cursor = self.execute(sql)
        tags = {}
        row = cursor.fetchone()
        while row is not None:
            for tag in row[0].split(","):
                tag = tag.strip()
                if tag == "":
                    continue
                if tag in tags:
                    tags[tag] += 1
                else:
                    tags[tag] = 1
            row = cursor.fetchone()
        return sorted(tags.items(), key=lambda pair: pair[1], reverse=True)

    def categories(self, where=""):
        """Get all categories and their frequencies in posts.

        :param where:
        """
        if where:
            where = "WHERE " + where
        sql = f"""
            SELECT category, count(*) as n
            FROM posts
            {where}
            GROUP BY category
            ORDER BY n desc
            """
        cats = (row for row in self.execute(sql).fetchall())
        return cats
