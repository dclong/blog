Status: published
Date: 2021-03-10 23:12:02
Author: Benjamin Du
Slug: visual-studio-code-server
Title: Visual Studio Code Server
Category: Software
Tags: Software, Visual Studio Code, server, VS Code, IDE, web, vscode

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Places to Find Extensoins 

[Visual Studio Code Marketplace](https://marketplace.visualstudio.com/vscode)
and
[Open VSX Registry](https://open-vsx.org/)
are 2 places to find VSCode compatible extensions.

## Advanced Tips
--link                 (beta) Securely bind code-server via Coder Cloud with the passed name. You'll get a URL like
                             https://myname.coder-cloud.com at which you can easily access your code-server instance.
                             Authorization is done via GitHub.

--home a customized "Go Home" button

[Hashed Password](https://github.com/cdr/code-server/blob/v3.8.0/doc/FAQ.md#can-i-store-my-password-hashed)

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

You can install a specific version of an extension using `@`.

    :::bash
    code-server --install-extension ms-python.python@2020.5.86806 \

https://github.com/cdr/code-server/issues/171

## [Debug Python Project](http://www.legendu.net/misc/blog/debug-python-project-in-visual-studio-code)

## Shortcuts

https://github.com/cdr/code-server/issues/112

https://github.com/cdr/code-server/issues/924

## Useful Tools

https://github.com/cdr/sshcode

## Snippets

[Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

## References

[Visual Studio Code Server Documentation](https://github.com/cdr/code-server/tree/master/doc)

[Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

[VSCode Shortcuts](http://www.legendu.net/misc/blog/vscode-tips/#shortcuts)

[VSCode Server Guidance](https://github.com/cdr/code-server/blob/master/doc/guide.md)

https://dev.to/babak/how-to-run-vs-code-on-the-server-3c7h

[Securing Visual Studio Code Server](https://www.pomerium.io/recipes/vs-code-server.html#background)
