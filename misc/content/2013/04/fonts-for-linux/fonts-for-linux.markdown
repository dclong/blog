UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Fonts for Linux
Date: 2016-07-13 00:07:00
Slug: fonts-for-linux
Author: Ben Chuanlong Du
Category: OS
Tags: fonts, LaTeX, Chinese, Linux, Tex Live, TexLive
Modified: 2016-07-13 00:07:00

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 

1. `ttf-arphic-uming`, `ttf-wqy-microhei`, `ttf-wqy-zenhei`, `xfonts-wqy` and `ttf-opensymbol` 
are some packages related to Chinese fonts.

2. If you have Adobe Reader installed on your computer, 
you can use Adobe Chinese fonts for free.

2. To check Chinese fonts installed on your computer,
you can use the command `fc-list :lang=zh-cn | sort`.

3. To install extra fonts in linux, 
you can just copy the font files to the directory '$HOME/.fonts'.
To make them in effect, 
you have to run `fc-cache` to update the system fonts cache.

4. If you ever have any fonts problem with Tex Live in Linux, 
install the package `texlive-fonts-extra` (if you haven't done so) and try again.

