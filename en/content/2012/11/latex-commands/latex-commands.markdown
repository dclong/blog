UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: LaTeX Commands for Compiling
Date: 2016-07-13 00:03:31
Tags: compile, LaTeX, programming
Category: Computer Science
Slug: latex-commands
Author: Ben Chuanlong Du
Modified: 2016-07-13 00:03:31


1. LaTeX
	- If your LaTeX code contains only EPS figures, you can use the `latex` command (also OK to use `pdflatex`) to compile your code.   
	- If you use bibtex, you have to compile your code using commands `latex`, `bibtex`, `latex` and `latex` in sequence.
	- If you use the `psfrag` package to edit EPS figures (only work for EPS figures), you have to compile your LaTeX code using commands `latex`, `dvi2ps` and `ps2pdf` in sequence.
	- To use the `tex4ht` tool to convert LaTeX to other formats, you have to use the `latex` command to compile. See [this post]() for more information.
2. pdflatex
	- If you use non-EPS figures in your LaTeX code, you have to use the `pdflatex` command to compile your code.
	- If you use bibtex, you have to compile your code using commands `pdflatex`, `bibtex`, `pdflatex` and `pdflatex` in sequence.
	- Generally speaking the `pdflatex` command is preferred to `latex`.
3. xelatex
	- For compiling LaTeX code containing CJK characters.

4. pdfTexify
	- A command seen in WinEdt for compiling LaTeX code repeatedly until all issues are resolved. This can be a more convenient alternative to apply commands `pdflatex`, `bibtex`, `pdflatex` and `pdflatex` when you use bibtex in your LaTeX code. Surely one can write bash functions to simplify this process in Linux easily.
