UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-07-13 00:02:34
Slug: graphics-in-latex
Author: Ben Chuanlong Du
Title: Graphics in LaTeX
Category: Computer Science
Tags: image, vector, LaTeX, graphics, programming
Modified: 2016-07-13 00:02:34


1. Generally PDF figures are preferred for LaTeX code.

2. There are many useful commands in Linux for converting between different types of figures, e.g., `convert`, `pdf2ps`, etc. So it does not matter much which types of figures you produce. You can always convert them into other format when needed.

3. The `psfrag` package is useful for editing EPS figures.
If you use it in your LaTeX code, you have to compile your code using commands `latex`, `dvi2ps` and `ps2pdf` in sequence.

4. Vector figures (EPS, PDF, etc) can be too big sometimes (e.g., if you do scatter plot). In this case, you'd better use non-vector pictures (e.g., png, jgp, etc).

5. To include figures in a frame in beamer, you must use the option `[fragile]` for that frame. For example
\begin{frame}[fragile]
\begin{figure}
\includegraphics{graph1}
\caption{captiontext}
\label{figurelabel}
\end{figure}
\end{frame} 
