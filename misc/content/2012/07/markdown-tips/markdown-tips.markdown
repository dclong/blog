Status: published
Author: Ben Chuanlong Du
Date: 2020-06-22 09:25:23
Title: Writing Docs Using Markdown
Slug: markdown-tips
Category: Computer Science
Tags: Markdown, Jekyll, programming
Modified: 2020-06-22 09:25:23

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


<img src="http://dclong.github.io/media/markdown/markdown.gif" height="200" width="240" align="right"/>

## Markdown Standard

1. [CommonMark](https://commonmark.org/)
    is the Markdown standard.
    Its specs can be found at [commonmark-spec](https://github.com/commonmark/commonmark-spec).
    https://talk.commonmark.org/
    is the community forum for CommonMark.
    Note that CommonMark is supported by GitHub.

 
[TableConvert Online](https://tableconvert.com/)
helps generating Markdown tables easily.

[HTML color codes and names](https://www.computerhope.com/htmcolor.htm)

1. There are 2 ways to include (other Markdown) files in a Markdown file. 
    The first way is to use the tool [markdown-include](https://github.com/sethen/markdown-include).
    Another way is to use the tool pandoc.
    Please see discussions on [stackoverflow](http://stackoverflow.com/questions/4779582/markdown-and-including-multiple-files).


## Markdown Related Tools

grip
markdown-include
pandoc
python-markdown ..
knitr (R package)

## Editors

1. ReText
2. MdCharm
3. UberWriter

## Questions 

1. how to define a link variable in jekyll or in markdown?

2. does markdown support include and so on? if there are mutiple md file in a folder, 
    several of them are use by a main file. what happens? 
    can we tell jekyll not to compile some of the markdown files?	

3. markdown small size? right aliganment?	

4. categories, hierarchical? ...? 
    it seems that jekyll support both	

5. can we include a pdf in jekyll? 
    I guess the problem is that whether html can do that

6. how to add a title for a figure?

1. The list environment does not work as expected sometimes. 
    Why does this happen? 
    Do we have to add two extra spaces so that it works?
    The list environment problem might actually the problem of firefox. 
    It seems that Chrome displays pages correctly.


2. It seems that the comment separate one paragraph into two. 

3. how to indent list?


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

## References

- [John Gruber](http://daringfireball.net/projects/markdown/)

- [Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)

- [cheet sheet](http://stationinthemetro.com/storage/dev/Markdown_Cheat_Sheet_v1-1.pdf)

## Mind Map

- [MemoFon](http://www.memofon.com/)
