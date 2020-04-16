UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Tips for Vimperator
Date: 2017-03-04 16:49:54
Slug: vimperator-tips
Category: Software
Tags: tips, software, Vimperator, Firefox, Vim

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**

## Confliction with Some Webpages

Some web applications (e.g., Google apps, MS Apps, RStudio, etc.) have their own keybindings, 
and they do not cowork with Vimperator. 
Having Vimperator enabled on these web apps/pages make both fail to work.
Please refer to 
[Selectively Disable Vimperator on Webpages](http://www.legendu.net/en/blog/selectively-disable-vimperator/)
on how to selectively disable Vimperator on some web apps/pages.

## Enable/Disable Vimperator
 
Press `Shift + ESC` to temporarily disables Vimperator.
Press it again or press `insert` to enable Vimperator. 

### Tab Navigation

1. `gt` or `ctrl + n`: go to the next tab 

2. `gT`: go to the previous tab

3. `d`: close the current tab

4. `u`: reopen last closed tab

5. `o`: open a new page in the current tab

6. `t`: open a new page in a new tab

### Page Navigation

1. `ctrl + l`: focus on the search/url bar

8. when using f/F for navigation, 
you can also use words in the link that you want to navigate to instead of numbers. 
This make things very convenient.

9. use :hardcopy to print a web page

### Zomm In/Out

1. `zi`: zoom in

2. `zo`: zoom out

3. `zz`: reset zoom 

### Text Manipulation

3. `gi`: goto the textbox on the page and focus on it

6. `y`: yanks the current link to the clipboard

2. c, v

3. :bma -f=toolbar/blogs -k=... 

4. use :! to run command, but how can I can run user-defined command? 

7. you can define your own vimperator command to simply important jobs ...


8. or alternatively you can do: o or t and then ctrl + v and then edit on the link ... cool!!!

## Links

1. <http://sysphere.org/~anrxc/j/articles/vimperator/>

2. <http://superuser.com/questions/16286/vimperator-and-ctrlk>

3. <http://sheet.shiar.nl/vimperator> 


## Questions

1. sometimes no link, but can click (button, etc.), how to emulate a mouse left/right click even in vimperator?

