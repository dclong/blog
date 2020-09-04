#!/usr/bin/env python3
# encoding: utf-8

from typing import Union, Sequence, List, Iterable
import os
import os.path
import re
import sys
import sqlite3
import datetime
import shutil
from pathlib import Path
import json
import itertools
import subprocess as sp
EN = "en"
CN = "cn"
HOME = "home"
MISC = "misc"
OUTDATED = "outdated"
DECLARATION = """
**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

"""
MARKDOWN = ".markdown"
IPYNB = ".ipynb"
NOW_DASH = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
TODAY_DASH = NOW_DASH[:10]
BASE_DIR = Path(__file__).resolve().parent
WORDS = json.loads((BASE_DIR / "words.json").read_text())


def qmarks(n: Union[int, Sequence]) -> str:
    """Generate n question marks delimited by comma.
    """
    if isinstance(n, (list, tuple)):
        n = len(n)
    return ", ".join(["?"] * n)


class Post:
    """A class abstracting a post.
    """

    def __init__(self, path: Union[str, Path]):
        self.path = Path(path).resolve()
        if self.path.suffix not in (MARKDOWN, IPYNB):
            raise ValueError(f"{self.path} is not a {MARKDOWN} or {IPYNB} file.")

    def __str__(self):
        return str(self.path)

    def diff(self, content: str) -> bool:
        """Check whether there is any difference between this post's content and the given content.
        :param content: The content to compare against.
        """
        return self.path.read_text() != content
        
    def blog_dir(self):
        """Get the corresponding blog directory (home, en, cn or misc) of a post.
        """
        return self.path.parent.parent.stem

    def update_after_move(self) -> None:
        """ Update the post after move.
        There are 3 possible change.
        1. The declaration might be added/removed
            depending on whether the post is moved to the misc sub blog directory.
        2. The slug of the post is updated to match the path of the post.
        3. The title should be updated to match the file name.
            Both 2 and 3 will prompt to user for confirmation.
        """
        if self.path.suffix == MARKDOWN:
            self._update_after_move_markdown()

    def _update_after_move_markdown(self) -> None:
        if self.blog_dir() == MISC:
            with self.path.open() as fin:
                lines = fin.readlines()
            index = [line.strip() for line in lines].index("")
            with self.path.open("w") as fout:
                fout.writelines(lines[:index])
                fout.writelines(DECLARATION)
                fout.writelines(lines[index:])
            return
        text = self.path.read_text().replace(DECLARATION, "")
        self.path.write_text(text)

    def update_time(self) -> str:
        """Update the meta filed date in the post.
        """
        if self.path.suffix == MARKDOWN:
            return self._update_time_markdown()
        return self._update_time_notebook()

    def _update_time_markdown(self) -> str:
        # TODO: put the time into the databse as well
        with self.path.open() as fin:
            lines = fin.readlines()
        self.update_meta_field(lines, "Date", NOW_DASH)
        with self.path.open("w") as fout:
            fout.writelines(lines)
        return NOW_DASH

    def _update_time_notebook(self) -> str:
        notebook = self._read_notebook()
        self.update_meta_field(notebook["cells"][0]["source"], "- Date", NOW_DASH)
        self.path.write_text(json.dumps(notebook, indent=1))
        return NOW_DASH

    @staticmethod
    def format_title(title):
        title = title.title()
        for origin, replace in WORDS:
            title = title.replace(f" {origin} ", f" {replace} ")
            if title.startswith(origin + " "):
                title = title.replace(origin + " ", replace + " ")
            if title.endswith(" " + origin):
                title = title.replace(" " + origin, " " + replace)
        return title

    def update_category(self, category: str) -> str:
        """Change the category of the specified post to the specified category.
        :param category: The category to change to.
        :return: The new category of the post.
        """
        if self.path.suffix == MARKDOWN:
            return self._update_category_markdown(category)
        return self._update_category_notebook(category)

    def _update_category_markdown(self, category: str) -> str:
        """Change the category of the specified post to the specified category.
        :param category: The category to change to.
        :return: The new category of the post.
        """
        with self.path.open() as fin:
            lines = fin.readlines()
        for idx, line in enumerate(lines):
            if line.startswith("Category: "):
                lines[idx] = f"Category: {category}\n"
                break
        else:
            lines.insert(0, f"Category: {category}\n")
        with self.path.open("w") as fout:
            fout.writelines(lines)
        return category

    def _read_notebook(self) -> dict:
        notebook = json.loads(self.path.read_text())
        if notebook["cells"][0]["cell_type"] != "markdown":
            raise SyntaxError(f"The first cell of the notebook {self.path} is not a markdown cell!")
        return notebook

    def _update_category_notebook(self, category: str) -> str:
        notebook = self._read_notebook()
        self.update_meta_field(notebook["cells"][0]["source"], "- Category", category)
        self.path.write_text(json.dumps(notebook, indent=1))
        return category

    def update_tags(self, from_tag: str, to_tag: str) -> List[str]:
        """Update the tag from_tag of the post to the tag to_tag.
        :param from_tag: The tag to be changed.
        :param to_tag: The tag to change to.
        :return: The new list of tags in the post.
        """
        with self.path.open() as fin:
            lines = fin.readlines()
        for idx, line in enumerate(lines):
            if line.startswith("Tags: "):
                tags = (tag.strip() for tag in line[5:].split(","))
                tags = [to_tag if tag == from_tag else tag for tag in tags]
                lines[idx] = f"Tags: {', '.join(tags)}"
                break
        else:
            tags = []
        with self.path.open("w") as fout:
            fout.writelines(lines)
        return tags

    def record(self):
        if self.path.suffix == MARKDOWN:
            return self._parse_markdown()
        return self._parse_notebook()

    def _parse_markdown(self) -> List[str]:
        with self.path.open() as fin:
            lines = fin.readlines()
        index = 0
        for index, line in enumerate(lines):
            if not re.match("[A-Za-z]+: ", line):
                break
        # parse meta data 0 - index (exclusive)
        status = ""
        date = ""
        author = ""
        slug = ""
        title = ""
        category = ""
        tags = ""
        for line in lines[:index]:
            if line.startswith("Status: "):
                status = line[8:].strip()
            elif line.startswith("Date: "):
                date = line[6:].strip()
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
        # parse content index to end
        content = "".join(lines)
        empty = self._is_ess_empty(lines[index:])
        name_title_mismatch = self.is_name_title_mismatch(title)
        return [
            self.path.relative_to(BASE_DIR),
            self.blog_dir(),
            status,
            date,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            0,
            name_title_mismatch,
        ]

    def _parse_notebook(self) -> List[str]:
        content = self.path.read_text()
        cells = json.loads(content)["cells"]
        empty = 1 if len(cells) <= 1 else 0
        if cells[0]["cell_type"] != "markdown":
            raise SyntaxError(f"The first cell of the notebook {self.path} is not a markdown cell!")
        meta = cells[0]["source"]
        status = ""
        date = ""
        author = ""
        slug = ""
        title = ""
        category = ""
        tags = ""
        for line in meta:
            if not re.search("^- [a-zA-Z]+:", line):
                raise SyntaxError(f"The meta line {line} of the notebook {self.path} does not confront to the format '- MetaField: Value'!")
            if line.startswith("- Status:"):
                status = line[9:].strip()
                continue
            if line.startswith("- Date:"):
                date = line[7:].strip()
                continue
            if line.startswith("- Author:"):
                author = line[9:].strip()
                continue
            if line.startswith("- Slug:"):
                slug = line[7:].strip()
                continue
            if line.startswith("- Title:"):
                title = line[8:].strip()
                continue
            if line.startswith("- Category:"):
                category = line[11:].strip()
                continue
            if line.startswith("- Tags:"):
                tags = line[7:].strip()
                continue
        name_title_mismatch = self.is_name_title_mismatch(title)
        return [
            self.path.relative_to(BASE_DIR),
            self.blog_dir(),
            status,
            date,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            0,
            name_title_mismatch,
        ]

    def is_name_title_mismatch(self, title: str) -> int:
        """Check whether the file anme and the title of the post does not match.
        :param path: The path of the post.
        :param title: The title of the post.
        :return: 1 if mismatch and 0 otherwise.
        """
        # TODO: seems that title is not needed!!!
        title_new = Post.format_title(self.stem_name().replace("-", " "))
        title_old = title.replace("-", " ")
        return 1 if title_old != title_new else 0

    def stem_name(self) -> str:
        return self.path.stem[11:]

    def _is_ess_empty(self, lines: List[str]) -> int:
        """Check whether the lines are essentially empty.
        :param lines: A list of lines.
        """
        content = "".join(line.strip() for line in lines)
        is_empty = re.sub(r"\*\*.+\*\*", "", content).replace("**", "") == ""
        return 1 if is_empty else 0

    @staticmethod
    def update_meta_field(lines: List[str], field: str, value: str) -> None:
        for idx, line in enumerate(lines):
            if line.startswith(f"{field}:"):
                lines[idx] = f"{field}: {value}\n"
                break
        else:
            lines.insert(0, f"{field}: {value}")

    def match_name(self):
        title = Post.format_title(self.stem_name().replace("-", " "))
        slug = title.lower().replace(" ", "-")
        with self.path.open() as fin:
            lines = fin.readlines()
        Post.update_meta_field(lines, "Title", title)
        Post.update_meta_field(lines, "Slug", slug)
        with self.path.open("w") as fout:
            fout.writelines(lines)

    def match_title(self) -> None:
        """Make the post's slug and path name match its title.
        """
        # file name
        stem_name = self.stem_name()
        title = self.title()
        slug = title.lower().replace(" ", "-")
        name = self.path.name.replace(stem_name, slug)
        path = self.path.with_name(name)
        os.rename(self.path, path)
        self.path = path
        # meta field Slug
        with self.path.open() as fin:
            lines = fin.readlines()
        Post.update_meta_field(lines, "Slug", slug)
        with self.path.open("w") as fout:
            fout.writelines(lines)   

    def title(self) -> str:
        """Get the title of the post.
        :return: The title of the post.
        """
        if self.path.suffix == MARKDOWN:
            return self._title_markdown()
        return self._title_notebook()

    def _title_notebook(self):
        # TODO: dedup the code 
        content = self.path.read_text()
        cell = json.loads(content)["cells"][0]
        if cell["cell_type"] != "markdown":
            raise SyntaxError(f"The first cell of the notebook {self.path} is not a markdown cell!")
        meta = cell["source"]
        for line in meta:
            if not re.search("^- [a-zA-Z]+:", line):
                raise SyntaxError(f"The meta line {line} of the notebook {self.path} does not confront to the format '- MetaField: Value'!")
            if line.startswith("- Title:"):
                return line[8:].strip()
        raise SyntaxError(f"No title in the post {self.path}!")

    def _title_markdown(self) -> str:
        with self.path.open() as fin:
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
        if self.path.suffix == MARKDOWN:
            return self._create_markdown(title)
        return self._create_notebook(title)

    def _create_notebook(self, title: str):
        text = (BASE_DIR / "themes/template.ipynb").read_text()
        text = text.replace("${TITLE}", Post.format_title(title)) \
            .replace("${SLUG}", Post.slug(title)) \
            .replace("${DATE}", NOW_DASH)
        with self.path.open("w") as fout:
            fout.write(text)
            if self.blog_dir() == MISC:
                pass

    def _create_markdown(self, title: str):
        with self.path.open("w") as fout:
            fout.writelines("Status: published\n")
            fout.writelines(f"Date: {NOW_DASH}\n")
            fout.writelines("Author: Benjamin Du\n")
            fout.writelines(f"Slug: {Post.slug(title)}\n")
            fout.writelines(f"Title: {Post.format_title(title)}\n")
            fout.writelines("Category: Computer Science\n")
            fout.writelines("Tags: Computer Science\n")
            if self.blog_dir() == MISC:
                fout.writelines(DECLARATION)


class Blogger:
    """A class for managing blog.
    """
    POSTS_COLS = [ 
        "path",
        "dir",
        "status",
        "date",
        "author",
        "slug",
        "title",
        "category",
        "tags",
        "content",
        "empty",
        "updated",
        "name_title_mismatch"
    ]

    def __init__(self, db: str = ""):
        """Create an instance of Blogger.

        :param dir_: the root directory of the blog.
        :param db: the path to the SQLite3 database file.
        """
        self._db = db if db else str(BASE_DIR / ".blogger.sqlite3")
        self._conn = sqlite3.connect(self._db)
        options = self._conn.execute("pragma compile_options").fetchall()
        self._fts = "fts5" if ("ENABLE_FTS5", ) in options else "fts4"
        self._create_vtable_posts()

    def _create_vtable_posts(self):
        sql = f"""
            CREATE VIRTUAL TABLE IF NOT EXISTS posts USING {self._fts} (
                {", ".join(Blogger.POSTS_COLS)},
                tokenize = porter
            )
            """
        self.execute(sql)

    def _create_table_srps(self):
        sql = "CREATE TABLE IF NOT EXISTS srps (path)"
        self.execute(sql)

    def clear(self):
        """Remove the SQLite3 database.
        """
        os.remove(self._db)

    def commit(self):
        """Commit changes made to the SQLite3 database.
        """
        self._conn.commit()

    def update_category(self, post: Union[Post, str, Path], category: str):
        if isinstance(post, (str, Path)):
            post = Post(post)
        post.update_category(category)
        self.update_records(paths=[post.path], mapping={"category": category})

    def update_tags(self, post: Post, from_tag: str, to_tag: str):
        """Update the tag from_tag of the post to the tag to_tag.
        """
        tags = post.update_tags(from_tag, to_tag)
        self.update_records(paths=[post.path], mapping={"tags": tags + ","})

    def iter_content(self) -> Iterable[Path]:
        """Iterate all files and subdirectories under the content directory of cn, en and misc.
        :return: An iterator of Path object.
        """
        return itertools.chain.from_iterable(
            (BASE_DIR / dir_ / "content").iterdir() for dir_ in (CN, EN, MISC, OUTDATED))

    def trust_notebooks(self):
        for dir_ in (EN, CN, MISC):
            cmd = f"jupyter trust {dir_}/content/*.ipynb"
            sp.run(cmd, shell=True, check=True)

    def reload_posts(self):
        """Reload posts into the SQLite3 database.
        """
        self._create_vtable_posts()
        self.execute("DELETE FROM posts")
        for path in self.iter_content():
            if path.suffix in (MARKDOWN, IPYNB):
                self._load_post(Post(path))
        self.commit()

    def _load_post(self, post: Post):
        sql = f"""
            INSERT INTO posts (
                {", ".join(Blogger.POSTS_COLS)}
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """
        self.execute(sql, post.record())

    def trash(self, posts: Union[str, List[str]]):
        """Move the specified posts to the trash directory.
        :param posts:
        """
        if isinstance(posts, str):
            posts = [posts]
        path = BASE_DIR / "trash"
        if not path.is_dir():
            path.mkdir(0o700, True, True)
        for post in posts:
            shutil.move(post, path)
        sql = f"""
            DELETE FROM posts
            WHERE path in ({qmarks(posts)})
            """
        self.execute(sql, posts)

    def move(self, src: Union[str, Path], dst: str) -> None:
        if isinstance(src, (str, Path)):
            self._move_1(src, dst)
        if len(src) > 1 and not os.path.isdir(dst):
            sys.exit("dst must be a directory when moving multiple files")
        for file in src:
            self._move_1(file, dst)

    def _move_1(self, src: Union[str, Path], dst: str) -> None:
        """Move a post to the specified location.
        """
        if isinstance(src, str):
            src = Path(src)
        if dst in (EN, CN, MISC, OUTDATED):
            dst = BASE_DIR / dst / "content" / src.name
        else:
            dst = Path(dst)
        if src == dst:
            return
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

    def edit(self, paths: Union[str, List[str]], editor: str) -> None:
        """Edit the specified posts using the specified editor.
        """
        if not isinstance(paths, list):
            paths = [paths]
        self.update_records(paths=paths, mapping={"updated": 1})
        paths = " ".join(f"'{path}'" for path in paths)
        os.system(f"{editor} {paths}")

    def update_records(self, paths: List[str], mapping: dict) -> None:
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

    def _delete_updated(self) -> None:
        sql = "DELETE FROM posts WHERE updated = 1"
        self.execute(sql)

    def update(self):
        """Update information of the changed posts.
        """
        sql = "SELECT path, content FROM posts WHERE updated = 1"
        rows = self.execute(sql).fetchall()
        # posts that were not changed
        paths = [path for path, content in rows if not Post(path).diff(content)]
        self.update_records(paths=paths, mapping={"updated": 0})
        # posts that were changed
        self._delete_updated()
        posts = [Post(path) for path, content in rows if Post(path).diff(content)]
        for post in posts:
            post.update_time()
            self._load_post(post)

    def add_post(self, title: str, dir_: str, notebook: bool = True) -> str:
        """Add a new post with the given title.
        """
        if notebook:
            return self._add_post_notebook(title, dir_)
        return self._add_post_markdown(title, dir_)

    def _add_post_notebook(self, title: str, dir_: str):
        file = self.find_post(title, dir_)
        if not file:
            file = BASE_DIR / dir_ / "content" / f"{TODAY_DASH}-{Post.slug(title)}.ipynb"
            post = Post(file)
            post.create(title)
            self._load_post(post)
        print(f"\nThe following post is added.\n{file}\n")
        return file

    def _add_post_markdown(self, title: str, dir_: str):
        file = self.find_post(title, dir_)
        if not file:
            file = BASE_DIR / dir_ / "content" / f"{TODAY_DASH}-{Post.slug(title)}.markdown"
            post = Post(file)
            post.create(title)
            self._load_post(post)
        print(f"\nThe following post is added.\n{file}\n")
        return file

    def find_post(self, title: str, dir_: str) -> str:
        """Find existing post matching the given title.

        :return: Return the path of the existing post if any,
        otherwise return empty string.
        """
        # find all posts and get rid of leading dates
        sql = "SELECT path FROM posts WHERE path LIKE ? AND dir = ?"
        row = self.execute(
            sql, [f"%{Post.slug(title)}.%", dir_]).fetchone()
        if row:
            return row[0]
        return ""

    def empty_posts(self, dry_run=False) -> None:
        """Load all empty posts into the table srps.
        """
        self.clear_srps()
        sql = f"""
            INSERT INTO srps
            SELECT path
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
        sql = f"""
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
            SELECT path
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
        """Clean contents of the table srps.
        """
        self._create_table_srps()
        self.execute("DELETE FROM srps")

    def last(self, n: int):
        """Get last (according to modification time) n posts.
        :param n: The number of posts to get.
        """
        self.clear_srps()
        sql = f"""
            insert into srps
            select path
            from posts
            where 
            """
        self.execute(sql)
        self.commit()

    def path(self, idx: Union[int, List[int]]) -> List[str]:
        if isinstance(idx, int):
            idx = [idx]
        sql = f"SELECT path FROM srps WHERE rowid in ({qmarks(idx)})"
        return [row[0] for row in self.execute(sql, idx).fetchall()]

    def fetch(self, n: int):
        """Fetch search results.

        :param n: the number of results to fetch.
        """
        sql = "SELECT rowid, path FROM srps LIMIT {}".format(n)
        return self.execute(sql).fetchall()

    def query(self, sql: str, params: Sequence = ()):
        return self.execute(sql, params).fetchall()

    def tags(self, dir_: str = "", where=""):
        """Get all tags and their frequencies in all posts.
        :param dir_:
        :param where:
        """
        sql = "SELECT tags FROM posts {where}"
        if where:
            sql = sql.format(where=where)
        else:
            # todo you can support quicker specific filtering in future
            sql = sql.format(where=where)
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

    def categories(self, dir_: str = "", where=""):
        """Get all categories and their frequencies in posts.
        :param dir_: 
        :param where: 
        """
        sql = """
            SELECT category, count(*) as n
            FROM posts
            {where}
            GROUP BY category
            ORDER BY n desc
            """
        if where:
            sql = sql.format(where=where)
        else:
            # todo you can support quicker specific filtering in future
            sql = sql.format(where=where)
        cats = (row for row in self.execute(sql).fetchall())
        return cats
