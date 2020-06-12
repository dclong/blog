Status: published
Date: 2020-06-12 10:35:12
Author: Benjamin Du
Slug: visual-studio-code-server
Title: Visual Studio Code Server
Category: Software
Tags: Software, Visual Studio Code, server, VS Code, IDE, web, vscode

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


[dclong/docker-vscode-server](https://github.com/dclong/docker-vscode-server)

## Setup Password

https://github.com/cdr/code-server/issues/940

## Settings

https://github.com/cdr/code-server/issues/965

https://github.com/cdr/code-server/issues/148

## Install Extensions

If you install extension in Dockerfile using `root`,
the extensions are installed into `/root/.local/share/code-server/extensions`.
You change the the permissions of `/root` and all its subcontents to 777 
(using the command `chmod -R 777 /root`) 
so that other users can use the installed extensions.

    :::bash
    code-server --install-extension ms-python.python
    code-server --install-extension njpwerner.autodocstring

https://github.com/cdr/code-server/issues/171

## JupyterLab Within VS Code 

https://github.com/cdr/code-server/issues/524

## Shortcuts

https://github.com/cdr/code-server/issues/112

https://github.com/cdr/code-server/issues/924

## Useful Tools

https://github.com/cdr/sshcode

## References

[VSCode Shortcuts](http://www.legendu.net/misc/blog/vscode-tips/#shortcuts)

[VSCode Server Guidance](https://github.com/cdr/code-server/blob/master/doc/guide.md)

https://dev.to/babak/how-to-run-vs-code-on-the-server-3c7h

[Securing Visual Studio Code Server](https://www.pomerium.io/recipes/vs-code-server.html#background)
