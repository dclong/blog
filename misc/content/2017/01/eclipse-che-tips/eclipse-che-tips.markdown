Status: published
Date: 2020-03-21 10:54:21
Author: Ben Chuanlong Du
Slug: eclipse-che-tips
Title: Tips on Eclipse Che
Category: Software
Tags: software, cloud IDE, Eclipse Che, tips
Modified: 2020-03-21 10:54:21

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

You can launch an Eclipse Che server using the command below.
```
docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v /workdir/che:/data eclipse/che start
```
The launched Eclipse Che server can be visited at `server_ip:8080`,
where `server_ip` is the ip of your server.
Please refer to the [Quick Start](https://www.eclipse.org/che/docs/quick-start.html#docker) for more details.

## Git/GitHub & SSH Keys

I encountered issues import a project from enterprise version of GitHub.
An alternative way was to manually clone the project in terminal.
Of course,
the SSH public key has to be configured in GitHub.
Here is a [related ticket](https://github.com/eclipse/che/issues/1938) on GitHub.

## [Language Servers](https://microsoft.github.io/language-server-protocol/implementors/servers/)

## Shortcuts

Ctrl + Insert: Copy

Shift + Insert: Paste

## Question

Does not seem easy to edit a file outside the current project?

## References

https://www.eclipse.org/che/docs/che-7/running-che-locally/

https://www.eclipse.org/che/docs/che-7/using-a-visual-studio-code-extension-in-che/

https://eclipsesource.com/blogs/2019/10/17/how-to-add-extensions-and-plugins-to-eclipse-theia/
