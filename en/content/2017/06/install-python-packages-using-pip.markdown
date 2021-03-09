Status: published
Date: 2021-03-08 17:54:02
Author: Ben Chuanlong Du
Slug: install-python-packages
Title: Install Python Packages Using pip
Category: Computer Science
Tags: programming, Python, package, module, install, pip, conda
## PyPi Statistics

You can check download statistics of Python Packages on PYPI at https://pypistats.org/.
This is especially helpful if you want to choose from multiple packages.

## Prefer [pip](https://pip.pypa.io/en/stable/reference/)

[pip](https://pip.pypa.io/en/stable/reference/)
is preferred over OS tools
(e.g., `apt-get`, `yum`, `wajig`, `aptitude`, etc.) for managing Python packages.
If you are using Anaconda Python,
use `conda` (instead of `pip`) to manage Python packages
especially when you encounter dependency issues.

## [Install pip](https://pip.pypa.io/en/stable/installing/)

### On Ubuntu

```Bash
apt-get install python3-pip
```

### On Mac

`pip` should have already been installed when you instal Python using Homebrew or Anaconda.

## Bootstrapping the pip Installer

The package [ensurepip](https://docs.python.org/3.8/library/ensurepip.html)
provides support for bootstrapping the pip installer into an existing Python installation or virtual environment.

```Bash
sudo python3 -m ensurepip
```

## Proper Way of Using pip

1. pip can be upgrade using the following command. 

        :::bash
        pip3 install --upgrade pip

    However,
    you should avoid doing this (as it might causes issues) 
    unless you have to upgrade and you are an experienced user.
    It is recommended that you upgrade pip via the system package management tools only.

2. Do NOT use `sudo pip install pkg1 pkg2` install packages to system-wide locations. 
    Instead, use `pip install --user pkg1 pkg2` to install packages to your local directory.

https://github.com/pypa/pip/issues/5599

https://stackoverflow.com/questions/49940813/pip-no-module-named-internal

## Install a Specific Version of a Python Package

1. List all available versions of a Python package. 

        :::bash
        pip3 install pylibmc==

2. Install a specific version of a Python package.

        :::bash
        pip3 install MySQL_python==1.2.2

3. Install pyarrow with a verison of at least 0.14.0.
    Notice that you must quote `pyarrow>=0.14.0` using single/double quotes.

        :::bash
        pip3 install 'pyarrow>=0.14.0'

4. Install a Python package with a version in a range.

        :::bash
        pip3 install "jupyterlab>=1.2.7,<2.0.0"

4. You can install the pre-release version of a package using the `--pre` option.
    For example, 
    the current version of pybuilder (0.11.7) is not compatible with Python 3.7.
    If you are using Python 3.7 and still want to use the pybuilder package, 
    you can install the pre-release version (0.12) which is compatible with Python 3.7.

        :::bash
        pip3 install --pre pybuilder

## Install Python Packages from Source

1. Install Python package from a `tar.gz` file which contains the source code.

        :::bash
        pip3 install xinstall-0.23.0.tar.gz

2. Install from the current directory

        :::bash
        pip3 install .

3. `pip` 20.0+ supports instaling a peotry managed Python project from GitHub directly.
    For example,
    the comamnd below installs the Python package dsutil from the GitHub repository dclong/dsutil directly.

        :::bash
        pip3 install git+ssh://git@github.com/dclong/dsutil 
        # or
        pip3 install git+https://github.com/dclong/xinstall
        # or install with optional components
        pip3 install --user -U "dsutil[all] @ git+https://github.com/dclong/dsutil@main"
        pip3 install "dsutil[cv] @ file:///home/dclong/dsutil-0.54.1-py3-none-any.whl"

    If you are behind a corporate proxy,
    you might need 2FA to visit the enterprise GitHub of your company.
    However, 
    2FA is usually not required for Git comamnd line (since it would too much hassle).
    The above way to install Python packages from GitHub repositories directly
    can be a good way to avoid 2FA authentication if you are behind a corporate proxy.

## Install Python Packages from Requirements.txt

You can install Python packages from a `requirements.txt` file.

    :::bash
    pip3 install -r requirements.txt

Notice that all formats accepted by `pip3 install` is valid in `requirements.txt`.
For example,
`git+https://github.com/dclong/dsutil@master` is valid to use in `requirements.txt`.

## Difference between --ignore-installed and --force-reinstall

Sometimes a package is installed by distutils
which cannot be reinstalled using `pip`, 
not even with the `--force-reinstall` option.
In that case, 
you have to use the `--ignore-installed` option.
For more discussions,
please refer to
[Difference Between Pip Install Options Ignore Installed and Force Reinstall](https://stackoverflow.com/questions/51913361/difference-between-pip-install-options-ignore-installed-and-force-reinstall)
and
[blockstack-core::Issues 504](https://github.com/blockstack/blockstack-core/issues/504)
.

## Install Python Packages Without Installing Dependencies

You can install a Python package without installing its dependencies
using the command below.

    :::bash
    pip3 install --no-deps some_package

## Upgrade Python Packages

You can upgrade an already installed Python package to the latest version
using the command below.

    :::bash
    pip3 install --upgrade wheel

## List All Installed Python Packages

1. List all installed modules.

        :::bash
        pip3 list --outdated

2. List outdated modules only.

        :::bash
        pip3 list --outdated

3. You can also use `help('modules')` to show all installed modules in Python.

## Use pip with Proxy

You can export environment variables `http_proxy` and `https_proxy`
or you can use `pip` with the `--proxy` option directly.
```Bash
pip3 --proxy http://proxy__server_ip:port install some_pkg
```
When using the `--proxy` with `pip`/`pip3`, 
you can omit `http://` and the port if the port is 80.
```Bash
pip3 --proxy 10.135.227.47 search notifiers
```

Notice that sometimes `pip` does not respect the environment variables.
In that case, 
you have to use the option `--proxy` to pass proxy to `pip`.
And even with the option `--proxy`,
pip might not work well if you install from a version control system. 
Just be ware of that.
[ProxyChains](http://www.legendu.net/misc/blog/proxychains-tips/)
is likely a solution when that issue happens.

## Misc

1. `pip` supports downloading Python packages without installing them.
    At the same time,
    you can disable `pip` caching using the option `--no-cache-dir`.
    For more discussions,
    please refer to
    [Caching](https://pip.pypa.io/en/latest/reference/pip_install/#caching)
    .

2. `export LC_ALL=C` resolves an issues (cannot remember which issue exactly) of pip3.

## Installation Location

Please refer to 
[The Installation Location of Python Packages Using Pip](http://www.legendu.net/misc/blog/the-installation-location-of-python-packages-using-pip/)
for more discussions.

## Check for Existence of a Python Package

https://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it

The most robust way turns out to be `pip3 list`,
because some packages are namespace sub packagess
which are not exposed (visible to importlib) by default.
However,
all installed packages (via pip) are visible to pip.

    :::bash
    pip3 list | grep -i pelican-render-math

## References

https://stackoverflow.com/questions/38613316/how-to-upgrade-pip3

https://adamj.eu/tech/2019/03/11/pip-install-from-a-git-repository/

http://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting

http://unix.stackexchange.com/questions/87745/what-does-lc-all-c-do

https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available

https://stackoverflow.com/questions/5226311/installing-specific-package-versions-with-pip

https://stackoverflow.com/questions/14149422/using-pip-behind-a-proxy

https://stackoverflow.com/questions/9510474/removing-pips-cache

https://stackoverflow.com/questions/36898474/how-to-install-a-module-for-all-users-with-pip-on-linux

[How to pip install a package with min and max version range?](https://stackoverflow.com/questions/8795617/how-to-pip-install-a-package-with-min-and-max-version-range)

[How to state in requirements.txt a direct github source](https://stackoverflow.com/questions/16584552/how-to-state-in-requirements-txt-a-direct-github-source)

['pip install' From a Git Repository](https://adamj.eu/tech/2019/03/11/pip-install-from-a-git-repository/)

https://github.com/pypa/pip/issues/4685

https://github.com/pypa/pip/pull/6391
