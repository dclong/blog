UUID: d78ff64f-d909-4efd-9b98-eb54493e67f0
Status: published
Date: 2016-07-09 22:24:39
Author: Ben Chuanlong Du
Slug: install-terminator-on-cygwin
Title: Install Terminator on Cygwin
Category: Software
Tags: software, Cygwin, Terminator, backports, cygwinports

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



1. Update your Cygwin to the latest

2. Open a Cygwin terminal and run (the idea of this step is to use Cygwin Ports)
```bash
cygstart -- path_to_cygwin_setup.exe -K http://cygwinports.org/ports.gpg
```
3. In the section of "Choose A Download Site":

    - Add "http://downloads.sourceforge.net/cygwin-ports"
    - Add " ftp://ftp.cygwinports.org/pub/cygwinports"
    - Select another mirror close to you

Check that you have a total of three URLs selected

4. It may show you warning about not loading the .ini configuration 
but ignore them 
(Note: I looked for different port URLs but the official ones threw me errors and I could not pass this step, 
that is why I used alternatives URLs)

5. First, you need to install the packages for the X Window:

http://x.cygwin.com/docs/ug/setup.html

Basically they are:

xorg-server (required, the Cygwin/X X Server)
xinit (required, scripts for starting the X server: xinit, startx, startwin (and a shortcut on the Start Menu to run it), startxdmcp.bat )
xorg-docs (optional, man pages)

font-* packages (required to resolve wrong encoding problems)

Also search and select the terminator package

It takes quite a while before it finishes.

Go to Start->All Programs->Cygwin-X->X Win Server (windows tool bar)

An icon of both Cygwin and X Win Server will show up in the system tray.
You can open terminator by right click on the X Win Server icon and then choose Terminator.


The terminator con Cygwin works well. 
However, it might crash after a long time. 
so be careful when you use it. 
Use tmux/screen if you ssh into other servers. 
And use Vim to edit files to avoid losing your job in terminator.

Since this terminato is installed in Cygwin, the copy, etc. operations are similar to that of in cygin. 
Check the post about Cygwin tips for details.


## Tips

1. Terminator in Cygwin is not as stable as Cygwin in Linux distributions (e.g., Linux Mint, Ubuntu, etc.).
It is suggested that you avoid draging and dropping tabs in terminator on Cygwin ... it might work but might crash ..., restart your windows workstation regularly ...

2.  terminator in cgywin have problems with the right-click menu, only pop up in the main monitor, so you'd better use temrinator in the main monitor

## Questions
1. it seems that terminator on Cygwin has the same problem of using user's home directory 
rather than the location of the parent window
tmux on Cygwin has the same problem ...
this is annoying ...
is it possible to let it use the parent window/tab's working directory?
