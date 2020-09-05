from typing import Union, List
import shutil
import subprocess as sp
import dsutil
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
    for editor, cmd in editors:
        if shutil.which(editor):
            return cmd
    return VIM


def install_if_not_exist(pkgs: Union[str, List[str]], pip: str = "python3 -m pip"):
    """Install specified Python packages if they are not installed.

    :param pkgs: A (list of) Python package(s) to install.
    :param pip: The pip command to use (to install packages).
    """
    frame = dsutil.shell.to_frame(f"{pip} list", split="\s+", header=0, skip=1)
    if isinstance(pkgs, str):
        pkgs = [pkgs]
    for pkg in pkgs:
        pkg = pkg.lower()
        if frame.query(f"package == '{pkg}'").empty:
            sp.run(f"{pip} install --user {pkg}", shell=True, check=True)
