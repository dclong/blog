Status: published
Author: Ben Chuanlong Du
Title: Tips on Debian
Date: 2020-02-29 17:08:42
Slug: debian-tips
Category: OS
Tags: tips, Linux, Debian

**Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!**
 

[Debian Apt Sources List Generator](http://debgen.simplylinux.ch/)

 
- [Debian downgrade from SID to testing ](http://www.fakeroot.info/2012/12/debian-downgrade-from-sid-to-testing.html)
- [Listing & Downgrading Unstable/Testing Debian Packages](http://archives.ryandaigle.com/articles/2005/10/31/listing-downgrading-unstable-testing-debian-packages)
- [Debian Linux 6: Install and Configure Compiz Eye Candy Effects](http://www.cyberciti.biz/howto/debian-linux/aptget-install-and-configure-compiz-eye-candy-effects/)
- [Intel Wireless WiFi Link, Wireless-N, Advanced-N, Ultimate-N devices](http://wiki.debian.org/iwlwifi)


1. it seems that even Debian testing is outdated, the package ...

2. use apt-file update/search to find the right file ...

3. use sudo dpkg-reconfigure tzdata to change time zone

4. do not use the unstable/sid version unless you are a package developer

5. use all package sources instead of just stable, testing or sid
and use pin

6. wajig install pkg/wheezy-backports 
not wajig install pkg/stable-backports
you can use stable-backports in source.list, however

## Installation

2. You'd better not install back ported Linux images, 
because this makes it harder to use Virtualbox.
It's suggested that 
    - you use the Linux image in the testing repository.
    - you always install headers corresponding to images you installed on your machine. 
    - you install virtualbox in the same repository as the Linux image

24. If you install Linux using command line tools 
and then install a desktop environment, you might not boot into DE automatically 
because you also have to install a DE manager, e.g., gdm or lightdm
without the login/DE manager, Linux won't boot into DE.
so removing login/DE manager is a dirty trick to suppress X if you don't know 
how to editing init scripts.
You can always manually start X using `startx`

