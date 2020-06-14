Status: published
Date: 2020-06-14 11:44:25
Slug: markdown-tips
Author: Ben Chuanlong Du
Category: Computer Science
Tags: Markdown, Jekyll, programming
Title: Tips for Markdown

<img src="http://dclong.github.io/media/markdown/markdown.gif" height="200" width="240" align="right"/>

## Markdown Standard

1. [CommonMark](https://commonmark.org/)
    is the Markdown standard.
    Its specs can be found at [commonmark-spec](https://github.com/commonmark/commonmark-spec).
    https://talk.commonmark.org/
    is the community forum for CommonMark.
    Note that CommonMark is supported by GitHub.

## Misc 

1. Jekyll interprete contents in two nested curly brackets as a variable 
(white spaces around the vairable are trimmed).
For example, if we have `{{ abcd }}` in the markdown code, 
then `abcd` is interpreted as a variable.
So you should avoid using two nested braces for other purpose in Markdown code, 
otherwise, 
Jekyll might fail to build your web pages. 
If you do want to dispaly two nested curly brackets, 
you can either insert a space between the two left curly brackets and the two
right curly brackets. Also you can also put it into a literal block (might be 
changed to raw later). There are also other preserved symbol combinations in Jekyll 
(e.g. { followed by %). Use these for other purpose might result in failure of 
building your web pages. 


1. A block indented 4 spaces is treated as a code block in Markdown. 
However, if this block is after a list item, 
you have to indent 8 spaces for it to be treated as code block. 
Indenting 4 spaces means that it is continued part of the list item. 
The addition 4-space means that it is a code block of the list item.
Even though back tildes (see the following examples) can be use specify a code block,
you'd better use the 8-space indentation as back tildes block does not work correctly in list.
> ```
> example of code block
> ```

1. Nature numbers in ordred list only indicate order items. 
The actually order of items is according to the order you list them, 
not the order of prefixed nutuarl numbers. 
The values of natural numbers does not matter in ordered list. 
You can use a same nature number if you want. 
Later items do not have to start with bigger nature numbers.

3. Images of format `jpg`, `png`, `gif`, etc. can be embeded in Markdown,
however, PDF images cannot.


2. To insert a link in Markdown, 
you can use `[link name](url)`. 
If you want the url to show up as it is, 
you can use `[url](url)`.
However, 
this is not convenient. 
A better way is to use `<url>`.


## LaTex

1. `$$` or `\(\)` (depends on configuration) are used for inline LaTex equations usually.  

2. In Latex, you have to use `\\` instead of `\newline` to indicate a new line in equations. 
In contrast, when you use Latex in Markdown, 
you have to use `\newline` instead of `\\`.

4. In LaTex, you can supress equation numbers using the star version of equation environments
(e.g., `align*`). 
However, when you use LaTex in Markdown,
you'd better use `\nonumber` to supress equation numbers manually 
instead of using the star version of equation environments. 
This is because `*` has special meaning in Markdown.



