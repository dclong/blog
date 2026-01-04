"""Utils for the blog module."""

from typing import List, Sequence
import os
from pathlib import Path
import shutil
import subprocess as sp
import pelican
import aiutil

BASE_DIR = Path(__file__).resolve().parent
VIM = "nvim" if shutil.which("nvim") else "vim"


def get_editor() -> str:
    """Get the path of a valid editor.
    Vim is used as the default (fallback) editor.
    """
    editors = {
        "code-server": "code-server",
        "code": "code",
        "gp": "gp open",
    }
    for editor, cmd in editors.items():
        if shutil.which(editor):
            return cmd
    return VIM


def install_if_not_exist(pkgs: str | List[str], pip: str = "python3 -m pip"):
    """Install specified Python packages if they are not installed.

    :param pkgs: A (list of) Python package(s) to install.
    :param pip: The pip command to use (to install packages).
    """
    frame = aiutil.shell.to_frame(f"{pip} list", split=r"\s+", header=0, skip=1)
    if isinstance(pkgs, str):
        pkgs = [pkgs]
    for pkg in pkgs:
        pkg = pkg.lower()
        if frame.query(f"package == '{pkg}'").empty:
            sp.run(f"{pip} install --user {pkg}", shell=True, check=True)


def qmarks(n: int | Sequence) -> str:
    """Generate n question marks delimited by comma."""
    if isinstance(n, (list, tuple)):
        n = len(n)
    return ", ".join(["?"] * n)


def _github_repos_url(dir_: str, https: bool = False) -> str:
    repos = {
        "home": "dclong.github.io",
        "en": "en",
        "cn": "cn",
        "misc": "misc",
        "outdated": "outdated",
    }[dir_]
    if https:
        return f"https://github.com/dclong/{repos}.git"
    return f"git@github.com:dclong/{repos}.git"


def push_github(dir_: str, https: bool):
    """Push compiled output to GitHub to generate GitHub pages.

    :param dir_: The name of sub blog directories (en, cn, etc.).
    :param https: If true, use the https protocol for Git.
    """
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


def pelican_generate(dir_: str, fatal: str):
    """Generate the (sub) blog/site using Pelican.

    :param dir_: The name of sub blog directories (en, cn, etc.).
    :param fatal: Pass values to the --fatal option of pelican.
        If empty the --fatal option is disabled,
        which means the compiling will ingore warnings and errors.
    """
    blog_dir = BASE_DIR / dir_
    os.chdir(blog_dir)
    # config = blog_dir / "pconf.py"
    # settings = pelican.settings.read_settings(path=str(config))
    # pelican.Pelican(settings).run()
    args = ["-s", str(blog_dir / "pconf.py")]
    if fatal:
        args.extend(["--fatal", fatal])
    pelican.main(args)


def option_indexes(subparser):
    """Add the positional option "indexes".

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "indexes",
        nargs="*",
        type=int,
        default=(),
        help="Row IDs in the search results.",
    )


def option_files(subparser):
    """Add the option --files.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "--files", nargs="+", dest="filels", default=(), help="Paths to files."
    )


def option_where(subparser):
    """Add the option --where.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-w",
        "--where",
        dest="where",
        default="",
        help="A user-specified filtering condition.",
    )


def option_dir(subparser):
    """Add the option --sub-dir.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-d",
        "--sub-dir",
        dest="sub_dir",
        default="",
        help="The sub blog directory to list categories; by default list all categories.",
    )


def option_num(subparser):
    """Add the option -n.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-n", dest="n", type=int, default=5, help="Number of matched records to show."
    )


def option_from(subparser):
    """Add the option --from.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "--from", dest="from", default="", help="the category/tag to change from."
    )


def option_to(subparser):
    """Add the option --to.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "--to", dest="to", default="", help="the category/tag to change to."
    )


def option_full_path(subparser):
    """Add the option --full-path.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-F",
        "--full-path",
        dest="full_path",
        action="store_true",
        help="whether to show full (instead of short/relative) path.",
    )


def option_dry_run(subparser):
    """Add the option --dry-run.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Print out the SQL query without running it.",
    )


def option_editor(subparser):
    """Add the option --editor.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-v",
        "--vim",
        dest="editor",
        action="store_const",
        const=VIM,
        default=get_editor(),
        help="Edit the post using NeoVim/Vim.",
    )
    subparser.add_argument(
        "--code",
        "--vscode",
        dest="editor",
        action="store_const",
        const="code",
        help="Edit the post using VSCode.",
    )
    subparser.add_argument(
        "-g",
        "--gp-open",
        dest="editor",
        action="store_const",
        const="gp open",
        help="Edit the post using the GitPod editor.",
    )


def option_all(subparser):
    """Add the option --all.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-a",
        "--all",
        dest="all",
        action="store_true",
        help="Select all files in the search results.",
    )
