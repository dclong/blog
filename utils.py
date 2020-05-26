from typing import Union, List
import shutil
import subprocess as sp
from loguru import logger
import dsutil
VIM = "nvim" if shutil.which("nvim") else "vim"


def get_editor() -> str:
    """Get the path of a valid editor.
        Vim is used as the default (fallback) editor.
    """
    if shutil.which("code"):
        return "code"
    if shutil.which("gp"):
        return "gp open"
    return VIM


def install_if_not_exist(pkgs: Union[str, List[str]], pip: str = "python3 -m pip"):
    """Install specified Python packages if they are not installed.

    :param pkgs: A (list of) Python package(s) to install.
    :param pip: The pip command to use (to install packages).
    """
    frame = dsutil.shell.to_frame(f"{pip} list", split="\s+", header=0, skip=1)
    print(frame)
    print(frame.query("'pelican' in package"))
    if isinstance(pkgs, str):
        pkgs = [pkgs]
    for pkg in pkgs:
        pkg = pkg.lower()
        if frame.query(f"package == '{pkg}'").empty:
            sp.run(f"{pip} install --user {pkg}", shell=True, check=True)
