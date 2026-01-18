Status: published
Date: 2026-01-17 17:22:31
Modified: 2026-01-17 23:37:46
Author: Benjamin Du
Slug: writing-scientific-docs-using-typst
Title: Writing Scientific Docs Using Typst
Category: Computer Science
Tags: Computer Science, programming, doc, documentation, writing, typst, markup, LaTex

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[Typst](https://typst.app/)
is a modern, open-source, markup-based typesetting system 
designed as a **user-friendly and powerful alternative to LaTeX**
for creating high-quality documents, presentations, and equations, featuring fast compilation, integrated scripting, 
and intuitive syntax that blends Markdown-like simplicity with rich formatting capabilities. 
It handles complex tasks like math typesetting, 
bibliography management, and automation, making it great for scientific papers, theses, and reports. 
Below are key features of Typst.
- Easy Syntax: Uses familiar markup similar to Markdown but adds powerful functions and a scripting language for advanced control.
- Performance: Offers fast, incremental compilation and friendly error messages, improving workflow.
- Versatility: Creates various content, from simple text and equations (including colored math) to diagrams, charts, and web pages.
- Automation: Built-in scripting allows for powerful document automation and creation of reusable templates.
- Open Source: The compiler is written in Rust and released under an Apache-2.0 license, with a web app providing a seamless editing experience.

## Jupyter Notebook Support

```
pandoc your_notebook.ipynb -f ipynb -t typst -o output.typ
# or
quarto render your_notebook.ipynb --to typst
```


[callisto](https://typst.app/universe/package/callisto/)
is a Typst package for reading from Jupyter notebooks.
It currently addresses the following use cases:

- Extracting specific cell sources and cell outputs, for example to include a plot in a Typst document.
- Rendering a notebook in Typst (embedding selected cells or the whole notebook).

## Python Support

```
#import "@preview/pyrunner:0.3.0" as py


#let some_code = ```
a = 1.3;
b = 2.5;
c = a * b;

def values(v):
  return globals().get(v)
```
#let some_compiled = py.compile(some_code);

#let get(v) = {
  float(py.call(some_compiled , "values", v))
}

Using $A = get("a")$, $B = get("b")$, $c = get("c")$
```

https://github.com/messense/typst-py
