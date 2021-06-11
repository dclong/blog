UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2012-12-20 10:40:42
Slug: string-in-MATLAB
Author: Ben Chuanlong Du
Category: Computer Science
Title: String in MATLAB
Tags: string, programming, MATLAB
Modified: 2015-02-20 10:40:42


1. To display special characters (e.g. `\n`, `\t` and so on),
you have to use `sprintf` to format it first. 
`fprintf` does the job of formatting and printing together.

2. Unlike R, 
numbers in MATLAB will not be silently converted to strings when needed.
You must use the function `num2str` to convert numbers to strings manually.
