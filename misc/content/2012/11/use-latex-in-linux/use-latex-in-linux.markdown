UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Use LaTeX in Linux
Date: 2012-11-10 07:49:45
Tags: LaTeX, TeX Live, Linux, software
Category: Software
Slug: use-latex-in-linux
Author: Ben Chuanlong Du
Modified: 2017-02-10 07:49:45

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
1. `Texlive` is the most popular package for LaTeX in Linux.

1. When installing texlive in linux, 
you'd better install the full version to avoid missing packages.
For example, in Debian you can do this using the following command.

        wajig instal texlive-full


```bash
# minimum LaTex
wajig install texlive texinfo
# Chinese support
wajig install texlive texinfo texlive-xetex texlive-lang-cjk 
# GUI
wajig install texstudio dvipng 
# full LaTex and GUI
wajig install texlive-full texstudio dvipng
```

