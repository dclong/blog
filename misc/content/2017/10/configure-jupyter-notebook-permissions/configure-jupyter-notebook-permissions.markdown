Status: published
Date: 2017-11-12 15:07:59
Author: Ben Chuanlong Du
Slug: configure-jupyter-notebook-permissions
Title: Configure Jupyte Notebook Permissions
Category: Software
Tags: software, Jupyter Notebook, JupyterLab, permission, umask
Modified: 2017-11-12 15:07:59

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. umask in /etc/profile or /etc/bashrc doesn't work in docker,
    which is strange.
    Changing UMASK 022 in /etc/login.defs doesn't work either ...

Had issues, 
tried to set /etc/profile, /etc/bashrc, in an init script, none of them worked worked well,
For JupyterHub, you can configure in the *.py file
https://github.com/jupyterhub/jupyterhub/issues/1402

2. setfacl, getfacl, umask all are useful ...

setfacl, etc. works partially, 
there is currently a bug in jupyter notebook 
and I have file a issue on GitHub for them for fix it.

3. inotify can be used as a temporary solution 

    #!/bin/bash
    dir=/jupyter
    inotifywait -m -r -e create --format '%w%f' "$dir" | while read f; do
        if [[ -d "$f" ]]; then
            chmod 775 "$f"
        fi
    done
