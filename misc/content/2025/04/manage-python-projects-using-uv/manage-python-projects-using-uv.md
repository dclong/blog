Status: published
Date: 2025-04-30 06:16:38
Modified: 2025-05-30 14:59:32
Author: Benjamin Du
Slug: manage-python-projects-using-uv
Title: Manage Python Projects Using uv
Category: Computer Science
Tags: Computer Science, programming, Python, uv, project, management, virtualenv, dependency

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh
```

## Usage

### Ad-hoc Scripts

1. Initialize a uv managed Python script.
    ```bash
    uv init --script example.py --python 3.13
    ```

### Manage Projects

1. Migrate from other Python projects to uv.
    ```bash
    uvx migrate-to-uv
    ```

2. Initialize a new uv project with the given name. 
    ```bash
    uv init --package new_project_name
    ```
    
3. Initialize the current project as a uv project.    
    ```bash
    uv init --package
    ```
    
uv lock
uv lock --upgrade
uv sync
uv run --python 3.13 --with dockeree aiutil python
uv run /path/to/uv_init_pyscript
uv build
uv publish
```

## References

- [uv Docs](https://docs.astral.sh/uv/)

- [uv @ GitHub](https://github.com/astral-sh/uv)

- [Adding a Trusted Publisher to an existing PyPI project](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)

https://pydevtools.com/handbook/how-to/how-to-run-a-python-repl-with-uv/
How to Run a Python REPL with uv
