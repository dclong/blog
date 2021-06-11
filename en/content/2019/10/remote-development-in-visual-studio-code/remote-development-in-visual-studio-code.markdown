Status: published
Date: 2019-10-10 13:07:08
Author: Benjamin Du
Slug: remote-development-in-visual-studio-code
Title: Remote Development in Visual Studio Code
Category: Software
Tags: Software, Visual Studio Code, vscode, VS Code, remote development, Visual Studio Code server, vscode server
Modified: 2021-03-10 13:07:08

There are 2 approaches to develop remotely in Visual Studio Code.
The first way is to leverage the extension pack
[Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).
For more details, 
please refer to 
[Remote Development with VS Code](https://code.visualstudio.com/blogs/2019/05/02/remote-development)
and
[VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview).


The second (prefered) approach is to leverage 
[cdr/code-server](https://github.com/cdr/code-server).
For more details, 
please refer to 
[Visual Studio Code Server](http://www.legendu.net/misc/blog/visual-studio-code-server/).
Visual Studio Code Server is prefer to the Remote Development extension pack 
as Visual Studio Code Server requires no installation or configuration on the client machine.
A browser is all your need to use Visual Studio Code Server once it is setup.

## References 

[Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)

[Advanced Container Configuration](https://code.visualstudio.com/docs/remote/containers-advanced)


https://code.visualstudio.com/docs/remote/containers-advanced#_developing-inside-a-container-on-a-remote-docker-host