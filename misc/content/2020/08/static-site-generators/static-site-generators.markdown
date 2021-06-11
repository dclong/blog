Status: published
Date: 2020-08-01 12:19:14
Author: Benjamin Du
Slug: static-site-generators
Title: Static Site Generators
Category: Computer Science
Tags: Computer Science, static site genertor, blog, blogging, gatsby, docusaurus, Pelican, ABlog, docusaurus, docsify, Sphinx, mkdocs, pandoc
Modified: 2021-05-01 12:19:14

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Site Generator 

### [gatsby](https://github.com/gatsbyjs/gatsby)
[gatsby](https://github.com/gatsbyjs/gatsby)

### [hugo](https://github.com/gohugoio/hugo)

Hugo is a static HTML and CSS website generator written in Go. 
It is optimized for speed, ease of use, and configurability. 
Hugo takes a directory with content and templates and renders them into a full HTML website.

Hugo relies on Markdown files with front matter for metadata, 
and you can run Hugo from any directory. 
This works well for shared hosts and other systems where you don’t have a privileged account.

Hugo renders a typical website of moderate size in a fraction of a second. 
A good rule of thumb is that each piece of content renders in around 1 millisecond.

Hugo is designed to work well for any kind of website including blogs, tumbles, and docs.

### [Pelican](http://www.legendu.net/misc/blog/pelican-tips/)
[Pelican](http://www.legendu.net/misc/blog/pelican-tips/)

### [ABlog](https://github.com/sunpy/ablog)
[ABlog](https://github.com/sunpy/ablog)
is for blogging with Sphinx.

## Documentation Generator 

### [docusaurus](https://github.com/facebook/docusaurus)
[docusaurus](https://github.com/facebook/docusaurus)

### [docsify](https://github.com/docsifyjs/docsify)
[docsify](https://github.com/docsifyjs/docsify)

### [Sphinx](https://github.com/sphinx-doc/sphinx)
[Sphinx](https://github.com/sphinx-doc/sphinx)

### [mkdocs](https://github.com/mkdocs/mkdocs)
[mkdocs](https://github.com/mkdocs/mkdocs)

### [pandoc](https://github.com/jgm/pandoc)
[pandoc](https://github.com/jgm/pandoc)

## Jupyter/Lab Notebook Parsers

### [nbsphinx](https://github.com/spatialaudio/nbsphinx)
[nbsphinx](https://github.com/spatialaudio/nbsphinx)
is a Sphinx extension that provides a source parser for `*.ipynb` files. 
Custom Sphinx directives are used to show Jupyter Notebook code cells 
(and of course their results) in both HTML and LaTeX output. 
Un-evaluated notebooks (i.e., notebooks without stored output cells) 
will be automatically executed during the Sphinx build process.

### [jupyter-book](https://github.com/executablebooks/jupyter-book)
[jupyter-book](https://github.com/executablebooks/jupyter-book)
is an open-source tool for building publication-quality books 
and documents from computational material.
[jupyter-book](https://github.com/executablebooks/jupyter-book)
uses
[MyST-Parser](https://github.com/executablebooks/MyST-Parser)
as the underlying markdown/notebook parser.

### [jupter nbconvert](https://github.com/jupyter/nbconvert)

`jupyter nbconvert` is a built-in command of Jupyter/Lab. 

## Copy the Content of Code Block 

https://tiborsimon.io/articles/tools/code-copy/
