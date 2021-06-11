UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-01-04 20:30:49
Author: Ben Chuanlong Du
Slug: rstudio-tips
Title: RStudio Tips
Category: Software
Tags: software, RStudio, IDE, CRAN, R, tips
Modified: 2016-12-04 20:30:49

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**


1. RStudio (both desktop and server edition) supports auto complete. 
Sometime the auto completion of the server edition might not work well, 
this is probably because the brower you use hijacks the hot keys of RStudio.
For example, 
I use the Vimperator plugin which makes the auto completion of RStudio (server edition) not to work. 
After disabling Vimperator temporarily (using ESC + SHIFT), 
the auto completion of RStudio (server edition) works fine.

2. `read.table('clipboard')` does not work (clipboard not due to server ...)
check whether this is due to firefox hijack too ...

you can also set a cool looking theme

Menu -> Tools -> Global Options... -> Appearance (left panel) -> select a theme that you like
e.g., Idle Fingers

you can also set fonts here ..
sounds like you should keep a configuration file for RStudio ...

4. RStudio support markdown files nicely ...

5. it seems that you can open multiple RStudio instances if you open it from cygwin command line on Windows

6. RStudio supports vim editing mode. 
Follow the foolowing instructions to enable Vim editing mode.

Menu -> Tools -> Global Options... -> Code Editing (left panel) 
-> Check Enable vim editing mode (towards the bottom) -> Click OK or Apply

1. Error in tools:::httpdPort <= 0L :    comparison (4) is possible only for atomic and list types,     
a problem of interaction between RStudio and R, upgrade RStudio might solve the problem ...

2. If you want to open multiple RStudio (desktop edition) at the same time, 
start different RStudio sessions from command line rather than from the UI menu. 
