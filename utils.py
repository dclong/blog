import shutil

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
