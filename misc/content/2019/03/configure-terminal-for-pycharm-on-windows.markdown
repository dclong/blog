Status: published
Date: 2019-03-05 01:48:55
Author: Benjamin Du
Slug: configure-terminal-for-pycharm
Title: Configure Terminal for PyCharm on Windows
Category: Computer Science
Tags: programming

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Ubuntu Shell

1. Install Ubuntu Shell on Windows 10 if it hasn't been installed.

2. File -> Settings -> Tools -> Terminal 

3. Replace the Shell path with `C:\Windows\System32\bash.exe`.


Unfortunately the Python virtual environment created in Ubuntu shell cannot be used by PyCharm
as PyCharm (or more precisely, the Windows File System) does not recognize Linux symbolic links.


See whether you can request this as a feature to PyCharm.


Even if the Python virtual environment created in Ubuntu shell can be used by PyCharm,
I'm concerned as it sounds to me that you are accessing Linux filesystem from Windows
which is not supported currently.



## Cygwin Shell

Similarly to Ubuntu Shell, 
the Python virtual environement created in Cygwin cannot be used by PyCharm.
However, 
the Python virtual environment created by PyCharm cannot be used in Cygwin without any issues.



https://engineroom.teamwork.com/using-cygwins-bash-terminal-in-a-jetbrains-ide-d22dd71b52b4
