Status: published
Date: 2019-02-10 13:28:49
Slug: cygwin-ports
Author: Ben Chuanlong Du
Title: Cygwin Ports
Category: Software
Tags: Linux, Windows, virtualization, software, Cygwin, ports
Modified: 2019-02-10 13:28:49

[Cygwin Ports Project](http://cygwinports.org/)


If you want to use a package that is missing in Cygwin 
(especially on the x86_64 version as some packages has not been ported to it yet),
You can install it from 
[Cygwin Ports](https://sourceware.org/cygwinports/)
following the instruction below if available.

1. Download the newest version of Cygwin installtion program.

2. Launch the Cygwin installation program with the `-K` flag in a Cygwin shell.
    For example,

        cygstart -- /path/to/setup-x86.exe -K http://cygwinports.org/ports.gpg

3. On the "Choose Installation Type" page, 
    select "Install from Internet".

4. On the "Choose Download Site(s)" page, 
    select a distro mirror, 
    then enter <ftp://ftp.cygwinports.org/pub/cygwinports> 
    in the User URL field and press Add (making sure that both are highlighted).
    You can just select the download site and proceed with it if you have added it before.

5. Proceed with package selection and installation, 
    making sure to install any indicated dependencies.