UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-08-28 16:55:06
Author: Ben Chuanlong Du
Slug: the confusing string in sas
Title: The Confusing String in SAS
Category: Computer Science
Tags: programming, SAS, String, data type

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. the `min` function also works on string variables.

0. A missing character in SAS is represented by any number of white spaces. 
To see more detailed discussion on missing values, 
please refer to the post 
[Missing Values in SAS](http://www.legendu.net/en/blog/missing-values-in-sas/).

1. In the data step characters and number are implicitly converted to each other when necessary.
However, 
this is not the case in `proc iml`.
You have to use the `char` function to convert number to string in the `iml` procedure.

the convert of dot and blank values? ...
if I remember correctly,
A missing character value (any number of white spaces) becomes a missing numeric value (`.`) 
when converted to numeric. 
However,
a missing numeric value (`.`) becomes `"."` when converted to character.
The inconsistent behavior here is annoying.

1. When you define a variable in SAS, 
it has a fixed length (no matter it is numeric or character). 
Things can be really tricky for (fixed length) character variables.
Suppose we have a string variable `s`. 
If you concatenate `s` (using `||` or `cat`) with another string 
and assign it back to `s` as illustrated below

```SAS
s = cat(s, "another string");
```

you will find that the value of `s` is not changed. 
This is caused by the fact that a string in SAS has a fixed length. 
The value of a string variable is always truncated/padded to meet the length requirement.
When you assign 
`cat(s, "another string")` 
to `s` the concatenated part is truncated, 
so the value `s` stays the same.
To avoid this problem, 
you should always remove leading and trailing white spaces (using `strip`)in string variables 
before concatenating them unless you know what you are doing.
There is a function `catx` in SAS, 
which automatically strips string variables before concatenating them.
Another tricky issue caused by this is when you convert between numeric and character values. 
Always strip a value/variable before you convert it to the other type. 

3. The use of string in SAS is a little bit confusing. 
Some rules of them are summarized below.

	- You should not use single/double quotation marks in macro 
    (i.e., outside the data step and procedures) 
	except for numbers represented using string (e.g., '01aug11'd) 
    or literal quotations marks. 
	This is because that macros are essentially string.
	For example, 
    you should not quote `month` in the following code, 
	however, 
    you must quote `08aug2013`.  

```SAS
%let alertdatestr= %sysfunc(compress(%sysfunc(putn(%eval(%sysfunc(intnx(month, '08aug2013'd, 0))), YYMMDD10.)),'-'));
%put &alertdatestr;
```
	
	- You have to use single/double quotation marks 
    for strings (including informat/outformat) inside data steps or procedures.
    However, informat/outformat (e.g., `date9.`, `datetime19.`, etc.) 
    in a `put`, `%put` statement should not be quoted.
	For example, 
    you must quote `week` in the following code. 
    However, pay attention to when `date9.` should be quoted and when not.

```SAS
data _null_;
    x = intnx('week', '17oct03'd, 6);
    y = putn('17Oct2013'd, "date9.");
    put x date9.;
run;
```

2. The function `compress` removes specified characters from a string.
If the character list is not specified, 
then spaces are removed.
It is functionally equivalent to replace the specified characters with blank strings.
It is similar to `std::remove_if` on `std::string` in C++. 

3. The function `tranwrd` replaces a substring with another one.
It is similar to `sub/gsub` in R and `str.replace` in Python.
It takes 3 arguments; 
first is source string; 
second is string to be replaced and last one is string to be replaced by. 
`tranwrd` will find out every occurrence of the second argument 
in the first argument and will replace it with the third argument.

4. Do not pass numerical arguments to functions taking string arguments,
and vice versa.

1. Generally speaking, 
you do not have to quote macros.
However, 
when you use a macro variable in a string,
you must quote it in double quotes 
(A macro variable in single quotes does not expand.)
For example, 
you have to quote `&dir.` in the following SAS statement.

```SAS
libname N3D "&dir.";
```

2. The function `lowcase` converts all letters in a string to lower case. 
It is similar to the function tolower in R and str.lower in Python.

3. The function `upcase` converts all letters in a string to upper case.
It is similar to the functions `toupper` in R and `str.upper` in Python.

4. The function `substr` extracts a sub string from a string.
The length of the sub string cannot exceedes the maximum possible length.

5. The function `scan` is somewhat similar to 
the function `split` in R and `str.split` in Python.
However ,
it is different in the sense 
that it returns the nth word (from a string) instead of return a vector/list of words. 
You can use multiple delimiters for scan.

6. `left`/`%left` is equivalent to the function `ltrim` in VBA.

1. In most programming languages,
you have to escape the backslash (`\`) in Windows paths.
In SAS, 
it does not matter whether you escape it or not. 

2. To escape the double/single quotation mark, 
you can double it. 
For example,

```SAS
data _null_;
    x = 'How''s everything going?';
    put x;
    y = "What do you mean by ""BTW""?";
    put y;
run;
```

## Tricks and Traps

1. The function `trim` is a different from `trim` functions in other programming languages.
While in most programming languages 
`trim` removes both leading and trailing blanks,
the `trim` function in SAS removes only trailing blanks.
To remove both leading and trailing blanks in SAS,
you have to use the function `strip`.

2. You cannot set the delimiter to be blank in catx.
If you specify `""` as the delimiter, 
then `" "` will be used.
This is really really stupid.

## strip/trim/compress

strip removes both trailing and leading white spaces
TRIM Function
Removes trailing blanks from a character string, 
and returns one blank if the string is missing.
this is ugly as most languages, trim is strip

however, compress is much more diffrent!!!
Returns a character string with specified characters removed from the original string.

you will use strip to remove .. most of the time.
