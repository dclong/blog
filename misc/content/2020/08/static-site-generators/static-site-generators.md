Status: published
Date: 2020-08-01 12:19:14
Author: Benjamin Du
Slug: static-site-generators
Title: Static Site Generators
Category: Computer Science
Tags: Computer Science, static site genertor, blog, blogging, gatsby, docusaurus, Pelican, ABlog, docusaurus, docsify, Sphinx, mkdocs, pandoc
Modified: 2026-01-17 22:55:34

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://jamstack.org/generators/

<table border="1">
  <thead>
    <tr>
      <th>Tool</th>
      <th>Implementation Language</th>
      <th>Popularity (GitHub Stars)</th>
      <th>Active Development</th>
      <th>Markup/Markdown Support</th>
      <th>Speed</th>
      <th>Ease of Use</th>
      <th>Ecosystem</th>
      <th>Jupyter Notebook Support</th>
      <th>Built-in Search</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Next.js</strong></td>
      <td>JavaScript / TypeScript (with Rust-based tooling)</td>
      <td>~137,000+</td>
      <td>Yes, very active.</td>
      <td>MDX supported. MyST and Typst would require custom integration.</td>
      <td>Fast, with features like Incremental Static Regeneration (ISR).</td>
      <td>Moderate to complex, as it's a full-stack framework. Steeper learning curve for simple static sites.</td>
      <td>Very large and mature, with a vast library of components, plugins, and integrations.</td>
      <td>Possible through custom integration, but not a primary focus.</td>
      <td>No, requires third-party libraries like Fuse.js or Algolia.</td>
    </tr>
    <tr>
      <td><strong>MkDocs</strong></td>
      <td>Python</td>
      <td>~21,600+</td>
      <td>Yes, actively maintained.</td>
      <td>Markdown. MyST can be integrated via plugins. Typst support is not native.</td>
      <td>Fast for small to medium-sized sites.</td>
      <td>Easy to learn, with a simple configuration file.</td>
      <td>Good, with a catalog of third-party themes and plugins.</td>
      <td>Yes, via plugins.</td>
      <td>Yes, client-side search is a core feature.</td>
    </tr>
    <tr>
      <td><strong>Zola</strong></td>
      <td>Rust</td>
      <td>~13,000+</td>
      <td>Yes, active.</td>
      <td>CommonMark with some extensions. MyST and Typst not natively supported.</td>
      <td>Blazing fast, often compiling sites in seconds.</td>
      <td>Easy, with a single binary and straightforward conventions.</td>
      <td>Growing, with a good number of themes and some community plugins.</td>
      <td>No native support.</td>
      <td>Yes, built-in full-text search.</td>
    </tr>
    <tr>
      <td><strong>Hugo</strong></td>
      <td>Go</td>
      <td>~86,100+</td>
      <td>Yes, very active with frequent releases.</td>
      <td>Markdown (Goldmark). MyST and Typst not natively supported.</td>
      <td>Extremely fast, often cited as the fastest static site generator.</td>
      <td>Moderate learning curve, templating can be complex.</td>
      <td>Very large and active, with a wide variety of themes and a strong community forum.</td>
      <td>Possible with workarounds, but not a first-class citizen.</td>
      <td>No, requires third-party solutions like Fuse.js or Algolia.</td>
    </tr>
    <tr>
      <td><strong>Astro</strong></td>
      <td>JavaScript / TypeScript</td>
      <td>~46,000+</td>
      <td>Yes, very active development.</td>
      <td>Markdown, MDX, Markdoc. MyST and Typst would require custom integration.</td>
      <td>Fast by default, with a focus on shipping zero JavaScript.</td>
      <td>Easy to get started, especially for those familiar with HTML and JavaScript.</td>
      <td>Rapidly growing ecosystem of integrations, themes, and components.</td>
      <td>Possible through community integrations.</td>
      <td>Not built-in, but can be added with integrations.</td>
    </tr>
    <tr>
      <td><strong>Quarto</strong></td>
      <td>TypeScript / Deno</td>
      <td>~10,000+</td>
      <td>Yes, very active.</td>
      <td>Pandoc Markdown, including support for Jupyter notebooks. MyST is supported. Typst can be used for PDF output.</td>
      <td>Good, but can be slower for very large sites with many computations.</td>
      <td>Easy to use for those familiar with R Markdown or Jupyter.</td>
      <td>Growing, with support for custom templates and extensions.</td>
      <td>Excellent native support for Jupyter Notebooks (.ipynb) and plain text (.qmd) formats.</td>
      <td>Yes, built-in full-text search.</td>
    </tr>
    <tr>
      <td><strong>mdBook</strong></td>
      <td>Rust</td>
      <td>~17,000+</td>
      <td>Yes, active.</td>
      <td>CommonMark with some extensions. MyST support is not native. Typst output is possible via a backend.</td>
      <td>Very fast.</td>
      <td>Easy, designed for creating books from Markdown files.</td>
      <td>Moderate, with some themes and preprocessors available.</td>
      <td>No native support.</td>
      <td>Yes, built-in client-side search.</td>
    </tr>
    <tr>
      <td><strong>Jupyter Book</strong></td>
      <td>Python</td>
      <td>~3,500+</td>
      <td>Yes, active development as part of the Executable Books Project.</td>
      <td>MyST (Markedly Structured Text) is a core feature. Can produce PDFs via Typst.</td>
      <td>Performance can vary depending on the complexity and number of notebooks being executed.</td>
      <td>Easy for those within the Jupyter ecosystem.</td>
      <td>Growing, with a focus on extensions for scientific and educational content.</td>
      <td>Core feature, designed to build books from Jupyter Notebooks and Markdown files.</td>
      <td>Yes, built-in search functionality.</td>
    </tr>
    <tr>
      <td><strong>Nikola</strong></td>
      <td>Python</td>
      <td>~2,700+</td>
      <td>Yes, actively maintained.</td>
      <td>reStructuredText, Markdown, Jupyter Notebooks, and more via plugins. MyST and Typst support would likely require custom plugins.</td>
      <td>Fast, with incremental builds.</td>
      <td>Moderate learning curve, with a rich set of features and a command-line interface.</td>
      <td>Good, with a collection of themes and plugins available.</td>
      <td>Yes, native support for Jupyter Notebooks.</td>
      <td>Can be added via plugins.</td>
    </tr>
    <tr>
      <td><strong>Starlight</strong></td>
      <td>JavaScript / TypeScript (based on Astro)</td>
      <td>(Part of Astro's ecosystem)</td>
      <td>Yes, as part of the active development of Astro.</td>
      <td>Markdown, MDX, Markdoc.</td>
      <td>Fast, inherits the performance benefits of Astro.</td>
      <td>Very easy, specifically designed for building documentation sites with minimal setup.</td>
      <td>Leverages the Astro ecosystem for integrations.</td>
      <td>Possible through Astro's integrations.</td>
      <td>Yes, built-in search functionality.</td>
    </tr>
    <tr>
      <td><strong>Lume</strong></td>
      <td>Deno (TypeScript)</td>
      <td>~2,200+</td>
      <td>Yes, active.</td>
      <td>Markdown, Nunjucks, JSX, Liquid, Pug, and more.</td>
      <td>Fast, with benchmarks showing competitive performance.</td>
      <td>Easy to use and configure, especially for those familiar with Deno.</td>
      <td>Growing, with a focus on plugins for various template engines and features.</td>
      <td>No native support mentioned.</td>
      <td>Yes, has a built-in search helper.</td>
    </tr>
  </tbody>
</table>

[Chat with Gemini - Static Site Generators Comparison Table](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%2214nWlukgUBmd53ZCCjsgNMXdIcKXQ4BED%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

## [zola](https://github.com/getzola/zola)
[Zola](https://github.com/getzola/zola)
is a fast static site generator in a single binary with everything built-in.

## [mdbook](https://www.legendu.net/misc/blog/tips-on-mdbook)

## [next.js](https://nextjs.org/docs/advanced-features/static-html-export)
`next export` allows you to export your Next.js application to static HTML, 
which can be run standalone without the need of a Node.js server. 
It is recommended to only use next export 
if you don't need any of the unsupported features requiring a server.

## [Pelican](http://www.legendu.net/misc/blog/pelican-tips/)
[Pelican](http://www.legendu.net/misc/blog/pelican-tips/)

## [jupyter-book](https://github.com/executablebooks/jupyter-book)
[jupyter-book](https://github.com/executablebooks/jupyter-book)
is an open-source tool for building publication-quality books 
and documents from computational material.
[jupyter-book](https://github.com/executablebooks/jupyter-book)
uses
[MyST-Parser](https://github.com/executablebooks/MyST-Parser)
as the underlying markdown/notebook parser.

## [mkdocs](https://github.com/mkdocs/mkdocs)
[mkdocs](https://github.com/mkdocs/mkdocs)

## [jupter nbconvert](https://github.com/jupyter/nbconvert)

`jupyter nbconvert` is a built-in command of Jupyter/Lab. 

## [gatsby](https://github.com/gatsbyjs/gatsby)
[gatsby](https://github.com/gatsbyjs/gatsby)

## [hugo](https://github.com/gohugoio/hugo)

Hugo is a static HTML and CSS website generator written in Go. 
It is optimized for speed, ease of use, and configurability. 
Hugo takes a directory with content and templates and renders them into a full HTML website.

Hugo relies on Markdown files with front matter for metadata, 
and you can run Hugo from any directory. 
This works well for shared hosts and other systems where you don’t have a privileged account.

Hugo renders a typical website of moderate size in a fraction of a second. 
A good rule of thumb is that each piece of content renders in around 1 millisecond.

Hugo is designed to work well for any kind of website including blogs, tumbles, and docs.

## [ABlog](https://github.com/sunpy/ablog)
[ABlog](https://github.com/sunpy/ablog)
is for blogging with Sphinx.
[A new blog with Sphinx](https://predictablynoisy.com/posts/2020/sphinx-blogging/)
is a good example of using ABlog + Sphinx.

## [docusaurus](https://github.com/facebook/docusaurus)
[docusaurus](https://github.com/facebook/docusaurus)

## [docsify](https://github.com/docsifyjs/docsify)
[docsify](https://github.com/docsifyjs/docsify)

## [Sphinx](https://github.com/sphinx-doc/sphinx)
[Sphinx](https://github.com/sphinx-doc/sphinx)

## [pandoc](https://github.com/jgm/pandoc)
[pandoc](https://github.com/jgm/pandoc)

## [nbsphinx](https://github.com/spatialaudio/nbsphinx)
[nbsphinx](https://github.com/spatialaudio/nbsphinx)
is a Sphinx extension that provides a source parser for `*.ipynb` files. 
Custom Sphinx directives are used to show Jupyter Notebook code cells 
(and of course their results) in both HTML and LaTeX output. 
Un-evaluated notebooks (i.e., notebooks without stored output cells) 
will be automatically executed during the Sphinx build process.

## Copy the Content of Code Block 

https://tiborsimon.io/articles/tools/code-copy/

## References
- [A new blog with Sphinx](https://predictablynoisy.com/posts/2020/sphinx-blogging/)
