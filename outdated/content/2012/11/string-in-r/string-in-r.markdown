UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-11-20 19:36:57
Author: Ben Chuanlong Du
Slug: string-in-r
Title: String in R
Category: Programming
Tags: R, programming, characters, string, CRAN
Modified: 2016-11-20 19:36:57

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

The R package `stringi` is a great one. 
It is suggested you used string functions in the `stringi` package
rather than in the base package (`grep`, `sub`, etc.) when possible. 

## Functions in the "stringi" Package
1. `stri_trans_totitle`
`%s+%` pastes 2 strings together. 
Vector is opteration is supported. 
However, 
there is one difference between `%s+%` and `paste`.
Applying `%s+%` on `NA` returns `NA`
while paste treats `NA` as an empty string.
Actually all `stri_*` functions respect `NA` propagation, 
that is applying any `stri_*` function on `NA` returns `NA`.

## Misc
0. R 3.3.0 and above: validUTF8(x)

5. Function `chartr` can be used to substitute old characters to new characters. 
If new character is null then this functions can be used
to drop characters from the original string.

6. Function `nchar` can be used to get the length of characters 
while function `length` can only be used to get the length of vectors or matrixs.

7. For special characters, 
we can put a backslash before it to get it,
or I think we can put it into a pair of single quotation mark.

8. R function `paste` can concatenate several vectors 
and it can also concatenate the elements in a vector. 

11. Using function `expression` and `eval` we can achieve symbolic computation. 
In addition, function `parse` might be useful.

12. Function `match.arg` can be used to partially match strings.

14. To replace a substring of a string with a new one, 
you can use `sub` or `gsub`. 
The difference between `sub` and `gsub` is that `sub` only replaces the first occurrence 
while `gsub` replaces all occurrences. 
However, sometimes, 
you might want to replace substring by index 
which gives more accurate control of substituting. 
For example, 
when there are multiple  occurrences of a substring 
and you only want to replace the 2nd one,
then neither `sub` nor `gsub` works well here. 
`substr` and `substring` are good alternatives in this situation. 
These two functions work similarly to vectors and matrices, 
which means that you can use these two functions to both extract and replace substrings. 
If you want to replace an element of a vector/matrix to a new one, 
you can just assign a new value to the element. 
Similarly to replace substring of an object string using `substr` or `substring`, 
you can simply assign a new value for the substring. 
However, `substr` and `substring` can only replace a substring with the same length, 
if the argument `replacement` is not long enough, 
then only partial of the substring specified will be replaced; 
if the argument `replacement` is too long, 
then it will be truncated to have the same length with the substring to be replaced. 
If you want to replace a substring specified by index with any new string, 
you can use `dclong.String::strReplace`.

15. `strwidth` calculates the width of a string when displayed on a graphics device.

16. `strsplit` splits a string according to specified delimiters.
strsplit` is based on regular expression by default. 
You can use literal string by specifying the option `fixed = TRUE`
(similar to other regular expression functions).
For example, 
you can use the following code 
to split `NCO_MTG_Per_L1 + LHPIRT_b + URD_b` using the plus sign.
```R
strsplit("NCO_MTG_Per_L1 + LHPIRT_b + URD_b", "+", fixed=TRUE)
```
Notice that splitting an empty string results in an empty string,
which is not a good behavior. 
Returning an empty string is better.
```R
> strsplit(c("", "1:2:3"), ":")
[[1]]
character(0)

[[2]]
[1] "1" "2" "3"
```
If none of the strings end with the delimiter, 
then a trick to resolve the issue is to add an extra delimiter to each string before splitting.
```R
> strsplit(c(":", "1:2:3"), ":")
[[1]]
[1] ""

[[2]]
[1] "1" "2" "3"
```

## IO
1. By default, 
characters read into R by `read.table` (and alike functions) is converted to factors. 
While it makes modeling convenient in R, 
it's usually inconvenient if you have to manipulate the data. 
The problem is nicely solved with the option `stringasis=T`.

4. Function `cat` can be used to display numbers 
and characters without quotation marks.

## Encoding
2. Function `iconv` is very useful for transforming codings 
between different encoding schemes.

## Formatting
3. Function `format` is very useful to display numbers 
and characters in the same length.

## Regular Expression
13. Sometimes we use `\\1` to stand for the string in the first parenthesis in `patter` argument. 
When we use `\\11` it the string in the first parenthesis in `pattern` argument followed by `1`, 
even if there're at least `11` parenthesis in the pattern argument. 
This means that while regular expression is convenient to work with strings, 
it's easy to make mistakes. 
It's a two-sided sword.
