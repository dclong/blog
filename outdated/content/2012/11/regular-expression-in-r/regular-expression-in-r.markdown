Status: published
Date: 2019-12-14 11:56:44
Slug: regular-expression-in-r
Author: Ben Chuanlong Du
Title: Regular Expression in R
Category: Programming
Tags: R, regex, programming, CRAN, regular expression
Modified: 2019-12-14 11:56:44

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

There are two flavors of regular expression in R.
One is the regular expression (grep, sub, etc.) comes with base. 
The other good one comes with the stringi package.
Both of the versions of regular expression support modifiers.
Generally speaking, regular expression modifiers overwrite function options if confliction happens. 

### Regular Expression in the `stringi` Package
1. `.` matches anything except (by default) `\n` 
which is very confusing and error-prone 
as it is not the default behavior in other versions of regular expression.
The modifier `(?s)` changes the default behavior of `.` and matches `\n`.

## Regular Expression in the `base` Package
1. Use `regexpr` instead of `grepl` in some cases if you want to check whether something exists.

2. Be default, many functions use regular expression match. 
If you do not want to use regular expression match, 
turn it off using the option `fixed = TRUE`.
For example, 
if you want split strings by `|` using the function `strsplit`. 
You have to use 
```R
strsplit(str, "|", fixed = TRUE)
```
instead of
```R
strsplit(str, "|")
```
which has `fixed = FALSE`.
