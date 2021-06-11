Status: published
Date: 2021-04-30 12:19:38
Author: Benjamin Du
Slug: useful-visual-studio-code-extensions
Title: Useful Visual Studio Code Extensions
Category: Computer Science
Tags: Computer Science, programming, IDE, VSCode, Visual Studio Code, extension
Modified: 2021-03-30 12:19:38

## Places to Find Extensoins 

[Visual Studio Code Marketplace](https://marketplace.visualstudio.com/vscode)
and
[Open VSX Registry](https://open-vsx.org/)
are 2 places to find VSCode compatible extensions.

## Install VSCode Extensions from Command-line

https://stackoverflow.com/questions/34286515/how-to-install-visual-studio-code-extensions-from-command-line/34339780#34339780


## Install Code-Server Extensions from Command-line

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

## Generally Useful Extensions 

- [Terminal](https://marketplace.visualstudio.com/items?itemName=formulahendry.terminal)

- [Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)

- [vscode-neovim](https://marketplace.visualstudio.com/items?itemName=asvetliakov.vscode-neovim)

- [Visual Stuido IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

- [TabNine VSCode](https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode)

- [Snippet](https://marketplace.visualstudio.com/items?itemName=vscode-snippet.Snippet)

- [Visual Studio Codespaces](https://marketplace.visualstudio.com/items?itemName=ms-vsonline.vsonline)

- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)

## Useful Extensions for Python

- [Terminal](https://marketplace.visualstudio.com/items?itemName=formulahendry.terminal)

- [Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)

- [Python (by Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

- [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
    Thhe sphinx style is recommended.

- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

- [Python Snippets](https://marketplace.visualstudio.com/items?itemName=cstrap.python-snippets)

- [Python Type Hint](https://marketplace.visualstudio.com/items?itemName=njqdev.vscode-python-typehint)

- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)

## Useful Extensions for SQL

- [SQL Language Server](https://marketplace.visualstudio.com/items?itemName=joe-re.sql-language-server)

## Useful Extensions for Android Development

- [Android](https://marketplace.visualstudio.com/items?itemName=adelphes.android-dev-ext)

## References

- https://open-vsx.org/
