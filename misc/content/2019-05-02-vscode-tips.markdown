Status: published
Date: 2020-05-23 22:03:35
Author: Benjamin Du
Slug: vscode-tips
Title: Tips on Visual Studio Code
Category: Software
Tags: software, vscode, Visual Studio Code, tips, IDE

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

A MS brading/telementry/licensing free edition named 
[vscodium](https://github.com/VSCodium/vscodium)
is available.

## Tricks & Traps

1. It seems that Visual Studio Code installed using snap in Kubuntu 18.10 has issues.
    It is suggested that you install Visual Studio Code using the `.deb` package instead of snap.

## Useful Extensions

[Terminal](https://marketplace.visualstudio.com/items?itemName=formulahendry.terminal)

[Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)

[Visual Studio Codespaces](https://marketplace.visualstudio.com/items?itemName=ms-vsonline.vsonline)

[vscode-neovim](https://marketplace.visualstudio.com/items?itemName=asvetliakov.vscode-neovim)

[Visual Stuido IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

[Extensions for VS Code Compatible Editors](https://open-vsx.org/)

[SQL Language Server](https://marketplace.visualstudio.com/items?itemName=joe-re.sql-language-server)

[Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

## Fix the Caps Lock Mapping to Escape Issue

https://github.com/Microsoft/vscode/wiki/Keybinding-Issues

A simple fix is to add the following configuration into the user's setting.json file.

    :::json
    {
        "keyboard.dispatch": "keyCode"
    }

## Install Extensions from Command-line

https://stackoverflow.com/questions/34286515/how-to-install-visual-studio-code-extensions-from-command-line/34339780#34339780

## Change Indention/Shift Width

https://stackoverflow.com/questions/34174207/how-to-change-indentation-in-visual-studio-code/45671704

## Launching VS Code from Command Line on Mac

https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line

## Shortcuts

Shift + CMD + V: Switch between view mode of Markdown. You can use it to open Markdown preview in VS Code.

## References

- [Visual Studio Code Blog](https://code.visualstudio.com/blogs/2019/05/02/remote-development)

- [Visual Studio Code Updates](https://code.visualstudio.com/updates/)

- [Download Visual Studio Code Insiders](https://code.visualstudio.com/insiders/)
