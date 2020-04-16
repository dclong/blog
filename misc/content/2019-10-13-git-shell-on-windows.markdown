Status: published
Date: 2019-10-14 01:01:31
Author: Benjamin Du
Slug: git-shell-on-windows
Title: Git Shell on Windows
Category: Software
Tags: Software, Git, shell, Windows, WSL, Windows Subsystem Linux

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

It is suggested that you use Git in Windows Subsystem Linux (WSL) 
instead of Git Shell in Windows.


1. git bash shell (on Windows) also uses shitf + insert to paste.

2. Git bash shell use /c, /d, /e, etc. for root path of drives.

3. It seems to me that
    `git config --global core.fileModel`
    has no effect on Windows.
    You can use `git -c core.fileMode=false command` as an alternative.

7. Git diff origin/master..HEAD

8. Git diff 15dc8^!
