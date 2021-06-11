Status: published
Date: 2021-04-24 11:28:44
Author: Benjamin Du
Slug: vscode-tips
Title: Tips on Visual Studio Code
Category: Software
Tags: software, vscode, Visual Studio Code, tips, IDE
Modified: 2021-04-24 11:28:44

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


## Fix the Caps Lock Mapping to Escape Issue

https://github.com/Microsoft/vscode/wiki/Keybinding-Issues

A simple fix is to add the following configuration into the user's setting.json file.

    :::json
    {
        "keyboard.dispatch": "keyCode"
    }


## Snippets

[Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

## Extensions

Please refer to 
[Useful Visual Studio Code Extensions](http://www.legendu.net/misc/blog/useful-visual-studio-code-extensions)
.

## Change Indention/Shift Width

https://stackoverflow.com/questions/34174207/how-to-change-indentation-in-visual-studio-code/45671704

## Launching VS Code from Command Line on Mac

https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line

## Shortcuts

Shift + CMD + V: Switch between view mode of Markdown. You can use it to open Markdown preview in VS Code.

Command + J: Show/Hide the terminal panel.

Ctrl + Command + F: Enter/Exit full screen mode.

Ctrl + Click: Togger menu on a variable (which contains Peek definition)
Ctrl + Alt + Click: variable definition

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax" rowspan="2">Descrption</th>
    <th class="tg-0lax" colspan="3">Shortcut</th>
  </tr>
  <tr>
    <td class="tg-0lax">Windows</td>
    <td class="tg-0lax">Mac</td>
    <td class="tg-0lax">Linux</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Format code</td>
    <td class="tg-0lax">shift + alt + f</td>
    <td class="tg-0lax">shift + option + f</td>
    <td class="tg-0lax">ctrl + shift + i</td>
  </tr>
</tbody>
</table>

## Auto Refresh Opened Files on Change

https://github.com/Microsoft/vscode/issues/28432

https://stackoverflow.com/questions/36333117/refresh-visual-studio-code-list-of-files/36338358

## References

- [Visual Studio Code Blog](https://code.visualstudio.com/blogs/2019/05/02/remote-development)

- [Visual Studio Code Updates](https://code.visualstudio.com/updates/)

- [Download Visual Studio Code Insiders](https://code.visualstudio.com/insiders/)

- https://stackoverflow.com/questions/29973357/how-do-you-format-code-in-visual-studio-code-vscode
