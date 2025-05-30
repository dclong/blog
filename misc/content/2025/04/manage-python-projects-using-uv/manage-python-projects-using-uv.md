Status: published
Date: 2025-04-30 06:16:38
Modified: 2025-05-28 19:00:18
Author: Benjamin Du
Slug: manage-python-projects-using-uv
Title: Manage Python Projects Using uv
Category: Computer Science
Tags: Computer Science, programming, Python, uv, project, management, virtualenv, dependency

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

curl -LsSf https://astral.sh/uv/install.sh | sh

curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh

## Usage

1. Migrate from other Python projects to uv.

        uvx migrate-to-uv


```
uv init --package new_project_name
uv init --package
uv init --script example.py --python 3.12
uv lock
uv lock --upgrade
uv sync
uv run python ...
uv run /path/to/uv_init_pyscript
uv build
uv publish
```

## References

- [uv Docs](https://docs.astral.sh/uv/)

- [uv @ GitHub](https://github.com/astral-sh/uv)

- [Adding a Trusted Publisher to an existing PyPI project](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)

