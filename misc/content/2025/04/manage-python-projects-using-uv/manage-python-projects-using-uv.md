Status: published
Date: 2025-04-30 06:16:38
Modified: 2025-05-31 17:13:52
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

### Ad-hoc Python Shell & Scripts

1. You can start an ad-hoc Python shell (
   e.g., Python 3.13 with 3rd-party packages dockeree and aituil
   ) using the following command.

    ```bash
    uv run --python 3.13 --with dockeree aiutil python
    ```

2. Initialize a uv managed Python script.

    ```bash
    uv init --python 3.13 --script example.py 
    ```

    Notice that if the script `example.py` already exists,
    uv will just append metadata lines into it.
    
3. You can add dependencies to a uv managed Python scripts 
    using the following command.

    ```bash
    uv add --script example.py 'requests<3' 'rich'
    ```

2. You can run a uv managed Python script using the following command.

    ```bash
    uv run /path/to/uv_init_pyscript
    ```

    This can be simplified by add the shebang `#!/usr/bin/env -S uv run --script` into the Python script,
    so that you can invoke the script as an executable directly.
    
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

4. Update the lock file (changing as little as possible).

    ```bash
    uv lock
    ```

5. Update the lock file ensuring that dependencies are the newest version allowed by the spec.

    ```bash
    uv lock --upgrade
    ```

6. Create a virtual environment if one doesn't already exist
    and install all dependencies.

    ```bash
    uv sync
    ```

    Install all dependencies including optional ones.

    ```bash
    uv sync --all-extras
    ```

    Install all dependencies but not the current project.

    ```
    uv sync --no-install-project
    ```
    
7. Build the project.

    ```bash
    uv build
    ```
    
8. Publish the project.

    ```bash
    uv publish
    ```

## References

- [uv Docs](https://docs.astral.sh/uv/)

- [uv @ GitHub](https://github.com/astral-sh/uv)

- [Adding a Trusted Publisher to an existing PyPI project](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)

- [How to Run a Python REPL with uv](https://pydevtools.com/handbook/how-to/how-to-run-a-python-repl-with-uv/)

- [Using uv as your shebang line](https://akrabat.com/using-uv-as-your-shebang-line/)
