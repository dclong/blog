UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Useful Packages and Commands for LaTex
Date: 2016-05-29 11:37:43
Tags: color, programming, list, Latex, package, bibliography, enumerate, formula, math, graphics
Category: Computer Science
Slug: useful-packages-for-latex
Author: Ben Chuanlong Du
Modified: 2016-05-29 11:37:43

<img src="http://dclong.github.io/media/latex/latex.gif" height="200" width="240" align="right"/>

## Math Packages

1. \usepackage{amssymb} 
    - popular math fonts
2. \usepackage{dsfont} 
    - `\mathds` font
3. \usepackage{bm} % bold math symbols
    + bold math symbols
4. \usepackage{amsmath} 
    + math formulas.
5. \usepackage{amsthm} 
    + theorem environments
    + proof enviroment

## List Packages

1. \usepackage{enumerate} 
    - universal list

## Graphics Packages

1. \usepackage{ifpdf} 
    - allow including figures without extensions and select the right type of figures according to the compiler used
2. \usepackage{graphicx} 
    - for including pictures
    - the graphics driver is selected automatically if none is specified (via arguments of the package) 
3. \usepackage{psfrag} 
    - for editing eps figures in Latex (e.g., replacing text)
    - need to compile using command `latex`, `dvips` and `ps2pdf` in sequence
4. \usepackage{epsfig} 
    - for including eps figures

## Bibliography

1. \usepackage{natbib} 
    - for citing refernce
    - compatible with bibtex
    - compile using `pdflatex/latex`, `bibtex`, `pdflatex/latex`, `pdflatex/latex`, `pdflatex/latex` in sequence
    - some Latex IDE (e.g., WinEdt) has a single button/command (PDFTexify) for simplifying the compiling process

## Color
1. \usepackage[usenames,dvipsnames]{color} 
    - using color by name

## Mutiple Files
1. You can use command `\input` or `\include` to include Latex source files. 
Generally speaking, 
`\input` is preferred over `\include`.
2. \usepackage{subfiles}
For more information, please refer to [wiki book](http://en.wikibooks.org/wiki/LaTeX/General_Guidelines).

## Chinese Packages

1. \usepackage{xeCJK} 
    + no need if use ctexart, ctexbook and so on
2. \usepackage{fontspec}
    + choose font theme 
3. \setCJKmainfont{Adobe Song Std} 
    + use adobe fonts as the main font

