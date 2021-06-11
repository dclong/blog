Status: published
Date: 2021-04-15 11:56:53
Author: Benjamin Du
Slug: replace-single-quotes-with-double-quotes-in-python-code
Title: Replace Single Quotes With Double Quotes in Python Code
Category: Computer Science
Tags: Computer Science, programming, Python, code, format, single, double, quotes, string
Modified: 2021-03-15 11:56:53

There are 2 ways.

1. Format the Python code using black,
    which will automatically convert single quotes to double quotes when applicable.
    (Note that you can format the code again using yapf 
    if you want the code to formatted by yapf finally.)

2. Use the tool [myint/unify](https://github.com/myint/unify) to help you.