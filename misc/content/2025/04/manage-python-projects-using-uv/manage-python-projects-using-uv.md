Status: published
Date: 2025-04-30 06:16:38
Modified: 2025-11-18 18:29:13
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

curl -LsSf https://astral.sh/uv/install.sh | sudo env UV_INSTALL_DIR="/usr/local/bin" sh
```

## Usage

### Ad-hoc Python Shell & Scripts

1. You can start an ad-hoc Python shell (
   e.g., Python 3.14 with 3rd-party packages dockeree and aituil
   ) using the following command.

        uv run --python 3.14 --with dockeree --with aiutil python
        
2. Similar to the above but start an Ipython shell instead.

        uv run --python 3.14 --with dockeree --with aiutil --with IPython python -m IPython

3. Initialize a uv managed Python script.

        uv init --python 3.14 --script example.py 

    Notice that if the script `example.py` already exists,
    uv will just append metadata lines into it.
    
4. You can add dependencies to a uv managed Python scripts 
    using the following command.

        uv add --script example.py 'requests<3' 'rich'

5. You can run a uv managed Python script using

        uv run /path/to/uv_managed_script.py

    or

        # preferred
        uv run --script /path/to/uv_managed_script.py

    Those 2 commands will automatically resolve and install dependencies specified in the script.
    This can be simplified by add the shebang 
    `#!/usr/bin/env -S uv run`
    or `#!/usr/bin/env -S uv run --script`
    into the Python script,
    so that you can invoke the script as an executable directly.

6. You might want to pass Python interpretor options (e.g., the `-P` option)
    while running a script using `uv`.
    This can be done using the command below.

        uv run python -P /path/to/uv_managed_script.py

    However,
    it has one drawback.
    It doesn't automatically resolve and install dependencies specified in the script.
    Luckily,
    with [PR](https://github.com/astral-sh/uv/pull/12763) merged,
    this is possible through the option `--with-requirements script_with_deps.py` 
    which includes inline dependency metadata from `script_with_deps.py`.
    So, 
    you can use the following command (though it's verbose).

        uv run python -P /path/to/uv_managed_script.py --with-requirements uv_managed_script.py

### Manage Projects

1. Migrate from other Python projects to uv.

        uvx migrate-to-uv

2. Initialize a new uv project with the given name. 

        uv init --package new_project_name
    
3. Initialize the current project as a uv project.    

        uv init --package

4. Update the lock file (changing as little as possible).

        uv lock

5. Update the lock file ensuring that dependencies are the newest version allowed by the spec.

        uv lock --upgrade

6. Create a virtual environment if one doesn't already exist
    and install all dependencies.

        uv sync

    Install all dependencies including optional ones.

        uv sync --all-extras

    Install all dependencies but not the current project.

        uv sync --no-install-project
    
7. Build the project.

        uv build
    
8. Publish the project.

        uv publish

## References

- [uv Docs](https://docs.astral.sh/uv/)

- [uv @ GitHub](https://github.com/astral-sh/uv)

- [Adding a Trusted Publisher to an existing PyPI project](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)

- [How to Run a Python REPL with uv](https://pydevtools.com/handbook/how-to/how-to-run-a-python-repl-with-uv/)

- [Using uv as your shebang line](https://akrabat.com/using-uv-as-your-shebang-line/)
