Status: published
Date: 2020-12-19 15:16:58
Author: Benjamin Du
Slug: the-neovim-plugin-for-visual-studio-code
Title: The NeoVim Plugin for Visual Studio Code
Category: Computer Science
Tags: Computer Science, Software, NeoVim, IDE, Visual Studio Code, VSCode

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

https://github.com/asvetliakov/vscode-neovim

## Installation 

1. Install NeoVim 0.5+ using xinstall.

        :::bash
        xinstall nvim -ic --ppa

2. Install the VeoVim plugin from the extension market in VSCode or Code Server.

3. Set the path of NeoVim via the extension settings.
    You can also do this by editing the settings file directly.

        :::json
        {
            "editor.fontSize": 12,
            "editor.detectIndentation": false,
            "editor.suggestSelection": "first",
            "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
            "autoDocstring.docstringFormat": "sphinx",
            "keyboard.dispatch": "keyCode",
            "workbench.startupEditor": "newUntitledFile",
            "python.linting.mypyEnabled": false,
            "python.linting.pylintArgs": [
                "--extension-pkg-whitelist=numpy,cv2,pyspark",
                "--generated-members=cv2.*,pyspark.*",
                "--ignored-modules=pyspark.sql.functions"
            ],
            "extensions.autoUpdate": false,
            "workbench.colorTheme": "Default Dark+",
            "python.formatting.provider": "yapf",
            "vscode-neovim.neovimPath": "/usr/bin/nvim"
        }

## Tips 

1. There are various issues with the plugin current. 
    It is suggested that you avoid using this plugin but use the Vim plugin instead.

2. SpaceVim configuration works with this plugin. 
    Once you have the VSCode NeoVim plugin installed,
    you can install SpaceVim and you are ready to go.
