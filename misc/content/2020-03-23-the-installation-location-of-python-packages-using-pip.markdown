Status: published
Date: 2020-03-23 00:16:46
Author: Benjamin Du
Slug: the-installation-location-of-python-packages-using-pip
Title: the Installation Location of Python Packages Using Pip
Category: Computer Science
Tags: Computer Science, Python, pip, package, installation, location

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


When installing a Python package using `pip` 
without using `sudo` or the `root` user,
the package is installed into the user's local directory at 
`~/.local/lib/python3.7/site-packages` (using Python 3.7 as example).
if `sudo` or the `root` user is used with `pip`,
then the package is installed to the system-wide location at 
`/usr/local/lib/python3.7/site-packages` (using Python 3.7 as example).

There are a few options to give users fine control on the destination directory 
to install Python packages.

## --user

Install to the Python user install directory for your platform. 
Typically `~/.local/`, 
or `%APPDATA%Python` on Windows. 
(See the Python documentation for site.USER_BASE for full details.)
Generally speaking,
you do not have to specify this option manually 
as Python packages are installed to the user's local directory by default
unless `sudo` or the `root` user is used.
The `--user` can be useful if you install a Python package using `setup.py`.

    :::bash
    python setup.py install --user

## --root <dir>

Install everything relative to this alternate root directory.

## --prefix <dir>

Installation prefix where lib, bin and other top-level folders are placed

## -t, --target <dir>

Install packages into <dir>. 
By default this will not replace existing files/folders in <dir>. 
Use --upgrade to replace existing packages in <dir> with new versions.

## References

[Install a Python package into a different directory using pip?](https://stackoverflow.com/questions/2915471/install-a-python-package-into-a-different-directory-using-pip)

[Where does pip install its packages?](https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages)

[pip installing in global site-packages instead of virtualenv](https://stackoverflow.com/questions/20952797/pip-installing-in-global-site-packages-instead-of-virtualenv)

[VirtualEnv/Pip trying to install packages globally](https://stackoverflow.com/questions/20942982/virtualenv-pip-trying-to-install-packages-globally)
