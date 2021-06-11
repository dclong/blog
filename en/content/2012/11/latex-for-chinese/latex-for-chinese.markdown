UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-07-13 00:04:39
Slug: latex-for-chinese
Author: Ben Chuanlong Du
Title: LaTeX for Chinese
Category: Computer Science
Tags: LaTeX, Chinese, programming, Tex Live, XeTex, Linux, fonts, markup
Modified: 2016-07-13 00:04:39


1. `xetex` is the state-of-art way for dealing with Chinese type setting.
You can install `xetex` on Debian series of Linux distributions (Debian, Ubuntu, Linux Mint, etc.)
using the following command. 
```bash
wajig install texlive-xetex 
```
You can use command `xelatex` to compile. 
The utf-8 format is preferred. 

There are 2 good ways for writing Chinese doc using LaTeX (TeX Live) in Linux.
You can use either the `ctex` or `xeCJK` package.
`ctex` is based on `xeCJK` and is more convenient, 
however `xeCJK` is more customizable. 
The following are minimum example using `ctex` and `xeCJK` respectively.
```Tex
\documentclass{article}
\usepackage{ctex}
\begin{document}
中文 English 
\end{document}
```
```Tex
\documentclass{article}
\usepackage{xeCJK}
\begin{document}
中文 English 
\end{document}
```
Both template uses the Fandole fonts coming with Tex Live by default (without manually specification of fonts to use). 
With Tex Live 2015 and above, 
the configuration is done automatically and no hassle of manual configuration. 
Both `ctex` and `xeCJK` need `xelatex` (see below) to compile.  
```bash
xelatex test.tex
```
Required packages (`texlive`, `xelatex`, `ctex`, `xeCJK`, etc.) can be installed 
on Debian sereis of Linux (Debian, Ubuntu, Linux Mint, etc.)
using the following command. 
```bash
wajig install texlive texlive-xetex texlive-lang-cjk
```
The following command installs all LaTeX components that I personally use frequently.
```bash
wajig install texlive latex-beamer wiki2beamer dvipng texlive-xetex texlive-lang-cjk texstudio
```
