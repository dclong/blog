Status: published
Date: 2025-06-07 09:45:35
Modified: 2025-06-07 09:45:35
Author: Benjamin Du
Slug: configuraing-terminal-in-visual-studio-code
Title: Configuraing Terminal in Visual Studio Code
Category: Computer Science
Tags: Computer Science, programming, IDE, editor, Visual Studio Code, VSCode, terminal, configuration

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## Configure The Shortcut `ctrl+x` `ctrl+e` 

The shortcut `ctrl+x` `ctrl+e` edits a bash prompt using `$EDITOR` in terminals.
However,
this doesn't work out-of-the-box in the teminal in Visual Studio Code.
This is because by default `ctrl+e` is binded to the command  
`workbench.action.quickOpen`
which is among the list of commands skipping shell by default.
You can remove `workbench.action.quickOpen`
from the list so that `ctrl+e` is pass to the shell 
by adding the following settings.

    "terminal.integrated.commandsToSkipShell": [
        "-workbench.action.quickOpen"
    ]
    
This will enable the shortcut `ctrl+x` `ctrl+e` to edit a bash prompt using an external editor.
However, 
if you are using Gitpod,
the shortcut will open a new tab to edit the bash prompt.
This is because the environment variable `VISUAL`
is set to `/ide/bin/remote-cli/gitpod-code` by default in Gitpod.
To make the shortcut `ctrl+x` `ctrl+e` editing a bash prompt 
using your preferred editor (say, NeoVim),
make sure to set both environment variables
`VISUAL` and `EDITOR`
.

## References

- [Inline chat](https://code.visualstudio.com/docs/copilot/chat/inline-chat#_use-terminal-inline-chat)

- [Getting started with the terminal](https://code.visualstudio.com/docs/terminal/getting-started)

- [Mastering VS Code's Terminal](https://www.growingwiththeweb.com/2017/03/mastering-vscodes-terminal.html)
