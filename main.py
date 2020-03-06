#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path
from argparse import ArgumentParser
import subprocess as sp
import getpass
try:
    import pelican
except ImportError:
    sp.run("python3 -m pip install --user pelican", shell=True, check=True)
    import pelican
from blog import Post, Blogger, BASE_DIR, HOME, EN, CN, MISC, OUTDATED
USER = getpass.getuser()
EDITOR = "code"
VIM = "nvim" if shutil.which("nvim") else "vim"
DASHES = "\n" + "-" * 100 + "\n"
INDEXES = [""] + [str(i) for i in range(1, 11)]


def query(blogger, args):
    rows = blogger.query(" ".join(args.sql))
    for row in rows:
        print(row)


def move(blogger, args):
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.files:
        blogger.move(args.files, args.target)
    blogger.commit()


def trash(blogger, args):
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.all:
        sql = "SELECT path FROM srps"
        args.files = [row[0] for row in blogger.query(sql)]
    if args.files:
        for index, file in enumerate(args.files):
            print(f"\n{index}: {file}")
        answer = input("\nAre you sure to delete the specified files in the srps table (y/N): ")
        if answer.lower() in ("y", "yes"):
            blogger.trash(args.files)
    else:
        print("No file to delete is specified!\n")
    blogger.commit()


def find_name_title_mismatch(blogger, args):
    blogger.find_name_title_mismatch()
    show(blogger, args)


def match_post(blogger, args):
    if re.search(r"^mp\d+$", args.sub_cmd):
        args.indexes = [int(args.sub_cmd[2:])]
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.all:
        sql = "SELECT path FROM srps"
        args.files = [row[0] for row in blogger.query(sql)]
    total = len(args.files)
    if not args.files:
        print("No specifed file to be matched!\n")
    if args.name:
        answer = input("Are you sure to edit post title for the specified files in the srps table (yes or no): \n")
        if answer == "yes":
            for index in range(total):
                blogger.match_post_name(args.files[index])
    if args.title:
        answer = input("Are you sure to edit post name for the specified files in the srps table (yes or no): \n")
        if answer == "yes":
            for index in range(total):
                blogger.match_post_title(args.files[index])


def edit(blogger, args):
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.files:
        # todo: best to unify the it or make a feature request to shutil.which
        if args.editor != "gp open" and not shutil.which(args.editor):
            args.editor = VIM
        blogger.edit(args.files, args.editor)
    else:
        print("No post is specified for editing!\n")
    blogger.commit()


def search(blogger, args):
    update(blogger, args)
    filter_ = []
    args.filter = " ".join(args.filter)
    if args.filter:
        filter_.append(args.filter)
    if args.sub_dir:
        args.sub_dir = ", ".join(f"'{dir_}'" for dir_ in args.sub_dir)
        filter_.append(f"dir IN ({args.sub_dir})")
    if args.neg_sub_dir:
        args.neg_sub_dir = ", ".join(f"'{dir_}'" for dir_ in args.neg_sub_dir)
        filter_.append(f"dir NOT IN ({args.neg_sub_dir})")
    if args.categories:
        args.categories = ", ".join(f"'{cat}'" for cat in args.categories)
        filter_.append(f"category IN ({args.categories})")
    if args.neg_categories:
        args.neg_sub_dir = ", ".join(f"'{cat}'" for cat in args.neg_catgories)
        filter_.append(f"category NOT IN ({args.neg_categories})")
    if args.tags:
        args.tags = "".join(f"% {tag},%" for tag in args.tags).replace(
            "%%", "%")
        filter_.append(f"tags LIKE '{args.tags}'")
    if args.neg_tags:
        args.neg_tags = "".join(f"% {tag},%" for tag in args.neg_tags).replace(
            "%%", "%")
        filter_.append(f"tags NOT LIKE '{args.neg_tags}'")
    if args.status:
        args.status = ", ".join(f"'{stat}'" for stat in args.status)
        filter_.append(f"status IN ({args.status})")
    if args.neg_status:
        args.neg_status = ", ".join(f"'{stat}'" for stat in args.neg_status)
        filter_.append(f"status NOT IN ({args.neg_status})")
    args.author = " ".join(args.author)
    if args.author:
        filter_.append(f"author = '{args.author}'")
    args.neg_author = " ".join(args.neg_author)
    if args.neg_author:
        filter_.append(f"author != '{args.neg_author}'")
    args.title = " ".join(args.title)
    if args.title:
        filter_.append(f"title LIKE '%{args.title}%'")
    args.neg_title = " ".join(args.neg_title)
    if args.neg_title:
        filter_.append(f"title NOT LIKE '%{args.neg_title}%'")
    blogger.search(" ".join(args.phrase), " AND ".join(filter_), args.dry_run)
    show(blogger, args)


def show(blogger, args) -> None:
    sql = "SELECT count(*) FROM srps"
    total = blogger.query(sql)[0][0]
    print(f"\nNumber of matched posts: {total}")
    for rowid, path in blogger.fetch(args.n):
        print(f"\n{rowid}: {Post(path).title()}    |    {path}")
    print("")


def reload(blogger, args):
    blogger.reload_posts()


def add(blogger, args):
    file = blogger.add_post(" ".join(args.title), args.sub_dir)
    args.indexes = None
    args.files = file
    edit(blogger, args)


def categories(blogger, args):
    cats = blogger.categories(dir_=args.sub_dir, where=args.where)
    for cat in cats:
        print(cat)


def update_category(blogger, args):
    if re.search(r"^ucat\d+$", args.sub_cmd):
        args.indexes = int(args.sub_cmd[4:])
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.files:
        for file in args.files:
            blogger.update_category(file, args.to_cat)
    elif args.from_cat:
        sql = "SELECT path FROM posts WHERE category = ?"
        posts = (row[0] for row in blogger.query(sql, [args.from_cat]))
        for post in posts:
            blogger.update_category(post, args.to_cat)
    blogger.commit()


def update_tags(blogger, args):
    if re.search(r"^utag\d+$", args.sub_cmd):
        args.indexes = int(args.sub_cmd[4:])
    if args.indexes:
        args.files = blogger.path(args.indexes)
    if args.files:
        for file in args.files:
            blogger.update_tags(Post(file), args.from_tag, args.to_tag)
    else:
        sql = f"""
            SELECT path
            FROM posts
            WHERE tags LIKE '%, {args.from_tag},%' OR tags LIKE '%: {args.from_tag},%'
            """
        posts = (row[0] for row in blogger.query(sql))
        for post in posts:
            blogger.update_tags(Post(post), args.from_tag, args.to_tag)
    blogger.commit()


def tags(blogger, args):
    tags = blogger.tags(dir_=args.sub_dir, where=args.where)
    for tag in tags:
        print(tag)


def update(blogger, args):
    blogger.update()
    blogger.commit()


def _github_repos_url(dir_: str, https: bool = False) -> str:
    repos = {
        "home": "dclong.github.io",
        "en": "en",
        "cn": "cn",
        "misc": "misc",
        "outdated": "outdated",
    }[dir_]
    url = f"git@github.com:dclong/{repos}.git"
    if https:
        url = f"https://github.com/dclong/{repos}.git"
    return url


def _push_github(dir_: str, https: bool):
    path = BASE_DIR / dir_ / "output"
    os.chdir(path)
    # commit
    if dir_ == "home":
        shutil.copy("pages/index.html", "index.html")
    cmd = "git init && git add --all . && git commit -a -m ..."
    sp.run(cmd, shell=True, check=True)
    # push
    url = _github_repos_url(dir_, https)
    cmd = f"git remote add origin {url} && git push origin master --force"
    sp.run(cmd, shell=True, check=True)


def _pelican_generate(dir_: str):
    """Generate the (sub) blog/site using Pelican.
    :param dir_: the sub blog directory to generate.
    """
    blog_dir = BASE_DIR / dir_
    os.chdir(blog_dir)
    config = blog_dir / "pconf.py"
    settings = pelican.settings.read_settings(path=str(config))
    pelican.Pelican(settings).run()


def publish(blogger, args):
    """Publish the blog to GitHub
    """
    auto_git_push(blogger, args)
    print(DASHES)
    for dir_ in args.sub_dirs:
        _pelican_generate(dir_)
        if not args.no_push_github:
            _push_github(dir_, args.https)
        print(DASHES)


def auto_git_push(blogger, args):
    """Push commits of this repository to dclong/blog on GitHub.
    """
    update(blogger, args)
    cmd = f"""git -C {BASE_DIR} add . \
            && git -C {BASE_DIR} commit -m ..."""
    sp.run(cmd, shell=True, check=False)
    cmd = f"""git -C {BASE_DIR} push origin master"""
    sp.run(cmd, shell=True, check=True)


def update_plugins(blogger, args):
    plugins = BASE_DIR / "plugins"
    cmd = f"""git -C {plugins} submodule init \
            && git -C {plugins} submodule update --recursive --remote
        """
    sp.run(cmd, shell=True, check=True)


def install_vim(blogger, args):
    cmd = "curl -sLf https://spacevim.org/install.sh | bash"
    os.system(cmd)


def link(blogger, args):
    (Path().home() / ".local/bin/blog").symlink_to(Path(__file__).resolve())


def _subparse_link(subparsers):
    subparser_link = subparsers.add_parser(
        "link", aliases=["ln", "lk"], help="Link main.py to blog in a searchable path.")
    subparser_link.set_defaults(func=link)


def parse_args(args=None, namespace=None):
    """Parse command-line arguments for the blogging util.
    """
    parser = ArgumentParser(description="Write blog in command line.")
    subparsers = parser.add_subparsers(dest="sub_cmd", help="Sub commands.")
    _subparse_jupyterlab(subparsers)
    _subparse_utag(subparsers)
    _subparse_ucat(subparsers)
    _subparse_tags(subparsers)
    _subparse_cats(subparsers)
    _subparse_update(subparsers)
    _subparse_reload(subparsers)
    _subparse_list(subparsers)
    _subparse_search(subparsers)
    _subparse_add(subparsers)
    _subparse_edit(subparsers)
    _subparse_move(subparsers)
    _subparse_publish(subparsers)
    _subparse_update_plugins(subparsers)
    _subparse_query(subparsers)
    _subparse_auto(subparsers)
    _subparse_space_vim(subparsers)
    _subparse_clear(subparsers)
    _subparse_git_status(subparsers)
    _subparse_git_diff(subparsers)
    _subparse_git_pull(subparsers)
    _subparse_empty_posts(subparsers)
    _subparse_trash(subparsers)
    _subparse_find_name_title_mismatch(subparsers)
    _subparse_match_post(subparsers)
    _subparse_exec_notebook(subparsers)
    _subparse_trust_notebooks(subparsers)
    _subparse_link(subparsers)
    return parser.parse_args(args=args, namespace=namespace)


def clear(blogger, args):
    blogger.clear()


def launch_jupyterlab(blogger, args):
    cmd = "jupyter lab --allow-root --ip='0.0.0.0' --port=8888 --no-browser --notebook-dir=/workdir &"
    sp.run(cmd, shell=True, check=True)


def _subparse_jupyterlab(subparsers):
    subparser_jlab = subparsers.add_parser(
        "jupyterlab", aliases=["jupyter", "jlab"], help="Launch the JupyterLab server.")
    subparser_jlab.set_defaults(func=launch_jupyterlab)


def exec_notebook(bloger, args):
    if args.indexes:
        args.notebooks = blogger.path(args.indexes)
    if args.notebooks:
        cmd = ["jupyter", "nbconvert", "--to", "notebook", "--inplace", "--execute"] + args.notebooks
        sp.run(cmd, check=True)


def _subparse_trust_notebooks(subparsers):
    subparser_trust_notebooks = subparsers.add_parser(
        "trust_notebooks", aliases=["trust"], help="Trust notebooks.")


def _subparse_exec_notebook(subparsers):
    subparser_exec_notebook = subparsers.add_parser(
        "exec_notebook", aliases=["exec"], help="Execute a notebook.")
    subparser_exec_notebook.add_argument(
        "-i",
        "--indexes",
        nargs="+",
        dest="indexes",
        type=int,
        default=(),
        help="Row IDs in the search results.")
    subparser_exec_notebook.add_argument(
        "-n",
        "--notebooks",
        nargs="+",
        dest="notebooks",
        default=(),
        help="Notebooks to execute.")
    subparser_exec_notebook.set_defaults(func=exec_notebook)


def _subparse_clear(subparsers):
    subparser_clear = subparsers.add_parser(
        "clear", aliases=["c"], help="Remove the underlying SQLite3 database.")
    subparser_clear.set_defaults(func=clear)


def _subparse_utag(subparsers):
    # parser for the update_tags command
    subparser_utag = subparsers.add_parser(
        "update_tags",
        aliases=["utag" + i for i in INDEXES],
        help="update tags of posts.")
    subparser_utag.add_argument(
        "-i",
        "--indexes",
        nargs="+",
        dest="indexes",
        type=int,
        default=(),
        help="Row IDs in the search results.")
    subparser_utag.add_argument(
        "--files",
        nargs="+",
        dest="files",
        default=(),
        help="Paths of the posts whose categories are to be updated.")
    subparser_utag.add_argument(
        "-f",
        "--from-tag",
        dest="from_tag",
        default="",
        help="The tag to change from.")
    subparser_utag.add_argument(
        "-t",
        "--to-tag",
        dest="to_tag",
        default="",
        help="The tag to change to.")
    subparser_utag.set_defaults(func=update_tags)


def _subparse_ucat(subparsers):
    # parser for the update_category command
    subparser_ucat = subparsers.add_parser(
        "update_category",
        aliases=["ucat" + i for i in INDEXES],
        help="Update category of posts.")
    subparser_ucat.add_argument(
        "indexes",
        nargs="*",
        type=int,
        default=(),
        help="Row IDs in the search results.")
    subparser_ucat.add_argument(
        "--files",
        nargs="+",
        dest="files",
        default=(),
        help="Paths of the posts whose categories are to be updated.")
    subparser_ucat.add_argument(
        "-f",
        "--from-category",
        dest="from_cat",
        default="",
        help="the category to change from.")
    subparser_ucat.add_argument(
        "-t",
        "--to-category",
        dest="to_cat",
        default="",
        help="the category to change to.")
    subparser_ucat.set_defaults(func=update_category)


def _subparse_tags(subparsers):
    subparser_tags = subparsers.add_parser(
        "tags", aliases=["t"], help="List all tags and their frequencies.")
    subparser_tags.add_argument(
        "-w",
        "---where",
        dest="where",
        default="",
        help="A user-specified filtering condition.")
    subparser_tags.add_argument(
        "-d",
        "---dir",
        dest="sub_dir",
        default="",
        help=
        "The sub blog directory to list categories; by default list all categories."
    )
    subparser_tags.set_defaults(func=tags)


def _subparse_cats(subparsers):
    subparser_cats = subparsers.add_parser(
        "cats",
        aliases=["c"],
        help="List all categories and their frequencies.")
    subparser_cats.add_argument(
        "-w",
        "---where",
        dest="where",
        default="",
        help="A user-specified filtering condition.")
    subparser_cats.add_argument(
        "-d",
        "---dir",
        dest="sub_dir",
        default="",
        help=
        "The sub blog directory to list categories; by default list all categories."
    )
    subparser_cats.set_defaults(func=categories)


def _subparse_update(subparsers):
    subparser_update = subparsers.add_parser(
        "update", aliases=["u"], help="Update information of changed posts.")
    subparser_update.set_defaults(func=update)


def _subparse_reload(subparsers):
    subparser_reload = subparsers.add_parser(
        "reload", aliases=["r"], help="Reload information of posts.")
    subparser_reload.set_defaults(func=reload)


def _subparse_list(subparsers):
    subparser_list = subparsers.add_parser(
        "list", aliases=["l"], help="List last search results.")
    subparser_list.add_argument(
        "-n",
        dest="n",
        type=int,
        default=10,
        help="Number of matched records to show.")
    subparser_list.add_argument(
        "-F",
        "--full-path",
        dest="full_path",
        action="store_true",
        help="whether to show full (instead of short/relative) path.")
    subparser_list.set_defaults(func=show)


def _subparse_search(subparsers):
    subparser_search = subparsers.add_parser("search", aliases=["s"],
        help="Search for posts. "
            "Tokens separated by spaces ( ) or plus signs (+) in the search phrase "
            "are matched in order with tokens in the text. "
            "ORDERLESS match of tokens can be achieved by separating them with the AND keyword. "
            "You can also limit match into specific columns. "
            "For more information, please refer to https://sqlite.org/fts5.html")
    subparser_search.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Print out the SQL query without running it.")
    subparser_search.add_argument(
        "phrase",
        nargs="*",
        default=(),
        help="The phrase to match in posts. "
            "Notice that tokens "a" and "the" are removed from phrase, "
            "which can be used as a hack way to make phrase optional. "
            "For example if you want to filter by category only without constraints on full-text search, "
            "you can use ./blog.py s the -c some_category.")
    subparser_search.add_argument(
        "-i",
        "--title",
        nargs="+",
        dest="title",
        default="",
        help="Search for posts with the sepcified title.")
    subparser_search.add_argument(
        "-I",
        "--neg-title",
        nargs="+",
        dest="neg_title",
        default="",
        help="Search for posts without the sepcified title.")
    subparser_search.add_argument(
        "-a",
        "--author",
        nargs="+",
        dest="author",
        default="",
        help="Search for posts with the sepcified author.")
    subparser_search.add_argument(
        "-A",
        "--neg-author",
        nargs="+",
        dest="neg_author",
        default="",
        help="Search for posts without the sepcified author.")
    subparser_search.add_argument(
        "-s",
        "--status",
        nargs="+",
        dest="status",
        default="",
        help="Search for posts with the sepcified status.")
    subparser_search.add_argument(
        "-S",
        "--neg-status",
        nargs="+",
        dest="neg_status",
        default="",
        help="Search for posts without the sepcified status.")
    subparser_search.add_argument(
        "-t",
        "--tags",
        nargs="+",
        dest="tags",
        default="",
        help="Search for posts with the sepcified tags.")
    subparser_search.add_argument(
        "-T",
        "--neg-tags",
        nargs="+",
        dest="neg_tags",
        default="",
        help="Search for posts without the sepcified tags.")
    subparser_search.add_argument(
        "-c",
        "--categories",
        nargs="+",
        dest="categories",
        default="",
        help="Search for posts with the sepcified categories.")
    subparser_search.add_argument(
        "-C",
        "--neg-categories",
        nargs="+",
        dest="neg_categories",
        default="",
        help="Search for posts without the sepcified categories.")
    subparser_search.add_argument(
        "-d",
        "--sub-dir",
        dest="sub_dir",
        nargs="+",
        default="",
        help="Search for posts in the specified sub blog directory.")
    subparser_search.add_argument(
        "-D",
        "--neg-sub-dir",
        dest="neg_sub_dir",
        nargs="+",
        default="",
        help="Search for posts not in the specified sub blog directory.")
    subparser_search.add_argument(
        "-f",
        "--filter",
        dest="filter",
        nargs="+",
        default=(),
        help="Futher filtering conditions in addition to the full-text match.")
    subparser_search.add_argument(
        "-n",
        dest="n",
        type=int,
        default=10,
        help="Number of matched records to show.")
    subparser_search.add_argument(
        "-F",
        "--full-path",
        dest="full_path",
        action="store_true",
        help="Whether to show full (instead of short/relative) path.")
    subparser_search.set_defaults(func=search)


def _subparse_add(subparsers):
    subparser_add = subparsers.add_parser(
        "add", aliases=["a"], help="Add a new post.")
    subparser_add.add_argument(
        "-g",
        "--gp-open",
        dest="editor",
        action="store_const",
        const="gp open",
        default=EDITOR,
        help="Edit the post using Vim.")
    subparser_add.add_argument(
        "-v",
        "--vim",
        dest="editor",
        action="store_const",
        const=VIM,
        default=EDITOR,
        help="Edit the post using Vim.")
    subparser_add.add_argument(
        "-e",
        "--en",
        dest="sub_dir",
        action="store_const",
        const=EN,
        default=MISC,
        help="Create a post in the en sub blog directory.")
    subparser_add.add_argument(
        "-c",
        "--cn",
        dest="sub_dir",
        action="store_const",
        const=CN,
        help="Create a post in the cn sub blog directory.")
    subparser_add.add_argument(
        "title", nargs="+", help="Title of the post to be created.")
    subparser_add.set_defaults(func=add)


def _subparse_edit(subparsers):
    subparser_edit = subparsers.add_parser(
        "edit", aliases=["e"], help="Edit a post.")
    subparser_edit.add_argument(
        "indexes",
        nargs="*",
        type=int,
        help="Row IDs in the search results.")
    subparser_edit.add_argument(
        "-g",
        "--gp-open",
        dest="editor",
        action="store_const",
        const="gp open",
        default=EDITOR,
        help="Edit the post using Theia's built-in editor.")
    subparser_edit.add_argument(
        "-v",
        "--vim",
        dest="editor",
        action="store_const",
        const=VIM,
        default=EDITOR,
        help="Edit the post using Vim.")
    subparser_edit.add_argument(
        "-f", "--files", dest="files", help="Path of the post to be edited.")
    subparser_edit.set_defaults(func=edit)


def _subparse_move(subparsers):
    subparser_move = subparsers.add_parser(
        "move", aliases=["m"], help="Move a post.")
    subparser_move.add_argument(
        "indexes",
        type=int,
        nargs="*",
        help="Rowid in the search results.")
    subparser_move.add_argument(
        "-f", 
        "--files", 
        nargs="*",
        dest="files", 
        help="Path of the post to be moved.")
    subparser_move.add_argument(
        "-t",
        "--target",
        dest="target",
        default=MISC,
        help="Path of destination file")
    subparser_move.add_argument(
        "-c",
        "--cn",
        dest="target",
        action="store_const",
        const=CN,
        help="Move to the cn sub blog directory.")
    subparser_move.add_argument(
        "-e",
        "--en",
        dest="target",
        action="store_const",
        const=EN,
        help="Move to the en sub blog directory.")
    subparser_move.add_argument(
        "-m",
        "--misc",
        dest="target",
        action="store_const",
        const=MISC,
        help="Move to the misc sub blog directory.")
    subparser_move.add_argument(
        "-o",
        "--out",
        "--outdated",
        dest="target",
        action="store_const",
        const=OUTDATED,
        help="Move to the outdated sub blog directory.")
    subparser_move.set_defaults(func=move)


def _subparse_publish(subparsers):
    subparser_publish = subparsers.add_parser(
        "publish", aliases=["p"], help="Publish the blog.")
    subparser_publish.add_argument(
        "-c",
        "--cn",
        dest="sub_dirs",
        action="append_const",
        const=CN,
        default=[HOME],
        help="Add the cn sub blog directory into the publish list.")
    subparser_publish.add_argument(
        "-e",
        "--en",
        dest="sub_dirs",
        action="append_const",
        const=EN,
        help="Add the en sub blog directory into the publish list.")
    subparser_publish.add_argument(
        "-m",
        "--misc",
        dest="sub_dirs",
        action="append_const",
        const=MISC,
        help="Add the misc sub blog directory into the publish list.")
    subparser_publish.add_argument(
        "-o",
        "--out",
        "--outdated",
        dest="sub_dirs",
        action="append_const",
        const=OUTDATED,
        help="Add the outdated sub blog directory into the publish list.")
    subparser_publish.add_argument(
        "--https",
        dest="https",
        action="store_true",
        default=(USER == "gitpod"),
        help="Use the HTTPS protocol for Git.")
    subparser_publish.add_argument(
        "--no-push-github",
        dest="no_push_github",
        action="store_true",
        help="Do not push the generated (sub) blog/site to GitHub.")
    subparser_publish.set_defaults(func=publish)


def _subparse_update_plugins(subparsers):
    subparser_update_plugins = subparsers.add_parser(
        "update_plugins", aliases=["plugins", "upp"], help="Update plugins.")
    subparser_update_plugins.set_defaults(func=update_plugins)


def _subparse_trash(subparsers):
    subparser_trash = subparsers.add_parser(
        "trash",
        aliases=["t"],
        help="Move posts to the trash directory.")
    subparser_trash.add_argument(
        "indexes",
        nargs="*",
        type=int,
        help="Row IDs of the files (in the search results) to be moved to the trash directory.")
    subparser_trash.add_argument(
        "-a",
        "--all",
        dest="all",
        action="store_true",
        help="Move all files in the search results to the trash directory.")
    subparser_trash.add_argument(
        "-f",
        "--files",
        dest="files",
        help="Paths of the posts to be moved to the trash directory.")
    subparser_trash.set_defaults(func=trash)


def _subparse_match_post(subparsers):
    subparser_match_post = subparsers.add_parser(
        "matchpost",
        aliases=["mp" + i for i in INDEXES],
        help="match post name and title")
    subparser_match_post.add_argument(
        "-i",
        "--indexes",
        dest="indexes",
        nargs="+",
        type=int,
        help = "Row IDs of the files (in the search results) to be matched.")
    subparser_match_post.add_argument(
        "-a",
        "--all",
        dest="all",
        action="store_true",
        help="Whether to edit all files in the search results.")
    subparser_match_post.add_argument(
        "-n",
        "--name",
        dest="name",
        action="store_true",
        help="Match the post title with its name.")
    subparser_match_post.add_argument(
        "-t",
        "--title",
        dest="title",
        action="store_true",
        help="Match the post name with its title.")
    subparser_match_post.set_defaults(func=match_post)


def _subparse_find_name_title_mismatch(subparsers):
    subparser_find_name_title_mismatch = subparsers.add_parser(
        "findmismatch",
        aliases=["fm"],
        help="Find posts where their name and title are mismatched.")
    subparser_find_name_title_mismatch.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Print out the SQL query without running it.")
    subparser_find_name_title_mismatch.add_argument(
        "-n",
        dest="n",
        type=int,
        default=10,
        help="Number of matched records to show.")
    subparser_find_name_title_mismatch.add_argument(
        "-F",
        "--full-path",
        dest="full_path",
        action="store_true",
        help="Whether to show full (instead of short/relative) path.") 
    subparser_find_name_title_mismatch.set_defaults(func=find_name_title_mismatch)


def _subparse_query(subparsers):
    subparser_query = subparsers.add_parser(
        "query", aliases=["q"], help="Run a SQL query.")
    subparser_query.add_argument("sql", nargs="+", help="the SQL to run")
    subparser_query.set_defaults(func=query)


def _subparse_auto(subparsers):
    subparser_auto = subparsers.add_parser(
        "auto_git_push",
        aliases=["auto", "agp", "ap"],
        help="Run a SQL query.")
    subparser_auto.set_defaults(func=auto_git_push)


def _subparse_space_vim(subparsers):
    subparser_vim = subparsers.add_parser(
        "space_vim", aliases=["isv", "sv", "svim"], help="Install SpaceVim.")
    subparser_vim.set_defaults(func=install_vim)


def _subparse_git_status(subparsers):
    subparser_status = subparsers.add_parser(
        "status",
        aliases=["st", "sts"],
        help="The git status command.")
    subparser_status.set_defaults(func=_git_status)


def _subparse_git_diff(subparsers):
    subparser_git = subparsers.add_parser(
        "diff",
        aliases=["df", "dif"],
        help="The git diff command.")
    subparser_git.add_argument(
        "file",
        nargs="*",
        default=(),
        help="Path of the post to run git diff on.")
    subparser_git.set_defaults(func=_git_diff)


def _git_status(blogger, args):
    os.system("git status")


def _git_diff(blogger, args):
    os.system(f"git diff {' '.join(args.file)}")


def _git_pull(blogger, args):
    os.system("git pull origin master")
    reload(blogger, args)


def _subparse_git_pull(subparsers):
    subparser_status = subparsers.add_parser(
        "pull",
        aliases=["pu"],
        help="The git pull command.")
    subparser_status.set_defaults(func=_git_pull)


def empty_posts(blogger, args):
    blogger.empty_posts(args.dry_run)
    show(blogger, args)


def _subparse_empty_posts(subparsers):
    subparser_status = subparsers.add_parser(
        "empty",
        aliases=["em"],
        help="Find empty post.")
    subparser_status.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Print out the SQL query without running it.")
    subparser_status.add_argument(
        "-n",
        dest="n",
        type=int,
        default=10,
        help="Number of matched records to show.")
    subparser_status.add_argument(
        "-F",
        "--full-path",
        dest="full_path",
        action="store_true",
        help="Whether to show full (instead of short/relative) path.")
    subparser_status.set_defaults(func=empty_posts)


def symlink():
    blog = Path.home() / ".local/bin/blog"
    main = Path(__file__).resolve()
    if blog.is_symlink():
        blog.unlink()
    blog.symlink_to(main)


if __name__ == "__main__":
    symlink()
    blogger = Blogger()
    args = parse_args()
    args.func(blogger, args)
