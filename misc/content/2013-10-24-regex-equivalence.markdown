Status: published
Author: Ben Chuanlong Du
Date: 2017-11-07 22:34:00
Slug: regex-equivalence
Title: Regular Expression Equivalence
Category: Computer Science
Tags: tips, regex, equivalence, regular expression, regexp, Python, R, CRAN, Perl, SAS, grep, egrep

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**

[Regular Expression Tester](https://regex101.com/)


1. If you use a regular expression multiple times, 
    then there is advantage to complie it and use the compiled version ... 
    as everyone use a plain regrex, 
    it is compiled and then used ...

2. `\W` does not include `^` and `$`.

## Regular Expression Modifiers

Regular expression modifiers makes regular expression more flexible and powerful. 
It is also a more universal way 
than remembering different options in different programming languages or tools. 
It is suggested that you use regular expression modifiers when possible.

### R

Both regular expression in the base package and the stringi package fully supported modifiers.

### Python

Partial supported.
Turning modifiers on is supported
however turning modifiers off is not supported.
Modifiers (once turned on) are applied to the entire regular expression
and cannot be turned off.

### Teradata SQL

fully supported

### Oracle SQL

Not supported. 
Behavior of regular expressions are control via parameters of regular expression functions.

### Perl

fully supported

### grep

fully supported via Perl style regular (the -P option) expression

### JS

Partial supported.
Tunning modifiers on is supported
however turnning modifiers off is not supported.
Modifiers (once turned on) are applied to the entire regular expression
and cannot be turned off.

## Greedy Match or Not

### grep

Greedy by default.
However, 
in the Perl style syntax you use the modifer `?` after the quantifier to perform a non-greedy match.
For example, 
instead of `.*` you can use `.*?` to do a non-greedy match.


## Popular Regular Expression Functions 

### R

```R
grep(pattern, x, ignore.case = FALSE, perl = FALSE, value = FALSE, fixed = FALSE, useBytes = FALSE, invert = FALSE)
```
`grep(value = FALSE)` returns a vector of the indices of the elements of x that yielded a match 
(or not, for invert = TRUE). 
This will be an integer vector unless the input is a long vector, when it will be a double vector.
`grep(value = TRUE)` returns a character vector containing the selected elements of x 
(after coercion, preserving names but no other attributes).

```R
grepl(pattern, x, ignore.case = FALSE, perl = FALSE, fixed = FALSE, useBytes = FALSE)
```
`grepl` returns a logical vector (match or not for each element of x).

```R
sub(pattern, replacement, x, ignore.case = FALSE, perl = FALSE, fixed = FALSE, useBytes = FALSE)
```

```R
gsub(pattern, replacement, x, ignore.case = FALSE, perl = FALSE, fixed = FALSE, useBytes = FALSE)
```

```R
regexpr(pattern, text, ignore.case = FALSE, perl = FALSE, fixed = FALSE, useBytes = FALSE)
```

```R
gregexpr(pattern, text, ignore.case = FALSE, perl = FALSE, fixed = FALSE, useBytes = FALSE)
```

```R
regexec(pattern, text, ignore.case = FALSE, fixed = FALSE, useBytes = FALSE)
```



For sub and gsub return a character vector of the same length and with the same attributes as x (after possible coercion to character). Elements of character vectors x which are not substituted will be returned unchanged (including any declared encoding). If useBytes = FALSE a non-ASCII substituted result will often be in UTF-8 with a marked encoding (e.g. if there is a UTF-8 input, and in a multibyte locale unless fixed = TRUE). Such strings can be re-encoded by enc2native.

regexpr returns an integer vector of the same length as text giving the starting position of the first match or -1 if there is none, with attribute "match.length", an integer vector giving the length of the matched text (or -1 for no match). The match positions and lengths are in characters unless useBytes = TRUE is used, when they are in bytes. If named capture is used there are further attributes "capture.start", "capture.length" and "capture.names".

gregexpr returns a list of the same length as text each element 
of which is of the same form as the return value for regexpr, 
except that the starting positions of every (disjoint) match are given.

regexec returns a list of the same length as text each element 
of which is either -1 if there is no match, 
or a sequence of integers with the starting positions of the match 
and all substrings corresponding to parenthesized subexpressions of pattern, 
with attribute "match.length" a vector giving the lengths of the matches (or -1 for no match).

### Python

re.search
re.match

### Teradata SQL

regexp_instr


## White Space

### Python 

`\s` or `[ \t\n\r\f\v]`
```Python
import re
m = re.match("\s", "abc ")
s = re.search("\s", "abc ")
```
Notice that `re.match` checks for a match only at the beginning of the string, 
while `re.search` checks for a match anywhere in the string.
You will want to use `re.search` most of the time.

### R

`\\s` or `[[:space:]]`
```R
# find strings containing white spaces
grep('\\s', c("abc ", "hello"))
[1] 1
# return a vector of logical values indicating whether the corresponding strings contain white spaces
grep('\\s', c("abc ", "hello"))
# replace the first white space with "", i.e., remove the first white space
sub('\s', "", c("abc ", "hello"))
# replace all first white space with "", i.e., remove all white space
gsub('\s', "", c("abc ", "hello"))
```

### Teradata SQL

[[:blank:]]
[[:space:]]

### sed

[[:space:]] (recommended) or `\s`

### egrep

`\s, [[:space:]]`

### grep

`\s, [[:space:]]`

### Vim

`\s`

### Perl

`\s`

### SAS (Based on Perl Regular Expression)

`\s`

## Non-whitespace Characters

### Python

`\S`

### R

`\S` or `[^[:space:]]`

### sed

`\S`

### egrep

`\S`

### grep

`\S`

### Vim

`\S`

### Perl

`\S`

## Lower-case Letters

### Python

`[a-z]`

### R

`[a-z], [:lower:]`

### sed

`[a-z]`

### egrep

`[a-z]`

### grep

`[a-z]`

### Vim

`[a-z], \l`

### Perl

`[a-z]` 

## Non-lower-case Letters Characters

### Python

`[^a-z]`

### R

`[^a-z], [^[:lower:]]`

### sed

`[^a-z]`

### egrep

`[^a-z]`

### grep

`[^a-z]`

### Vim

`[^a-z], \L`

### Perl

`[^a-z]`

##  Upper-case Letters

### Python

`[A-Z]`

### R

`[A-Z], [[:upper:]]`

### sed

`[A-Z]`

### egrep

`[A-Z]`

### grep

`[A-Z]`

### Vim

`[A-Z], \u`

### Perl

`[A-Z]`

## Non-upper-case Letter Characters

### Python

`[^A-Z]`

### R

`[^A-Z], [^[:upper:]]`

### sed

`[^A-Z]`

### egrep

`[^A-Z]`

### grep

`[^A-Z]`

### Vim

`[^A-Z], \U`

### Perl

`[^A-Z]`

## Letters

### Python

`[a-zA-Z]`

### R

`[a-zA-Z], [[:alpha:]]`

### sed

`[a-zA-Z]`

### egrep

`[a-zA-Z]`

### grep

`[a-zA-Z]`

### Vim

`[a-zA-Z], \a`

### Perl

`[a-zA-Z]`

## Non-Letter Characters

### Python

`[^a-zA-Z]`

### R

`[^a-zA-Z], [^[:alpha:]]`

### sed

`[^a-zA-Z]`

### egrep

`[^a-zA-Z]`

### grep

`[^a-zA-Z]`

### Vim

`[^a-zA-Z], \A`

### Perl

`[^a-zA-Z]`

## Digits

### Python

`\d`

### R

`\\d` or `[[:digit:]]`

### sed

`\d`

### egrep

`[[:digit:]]`

### grep

`[[:digit:]]`

### Vim

`\d`

### Perl

`\d`

## Non-digit Characters

### Python

`\D`

### R

`\\\\D, [^[:digit:]]`

### sed

`\D`

### egrep

`[^[:digit:]]`

### grep

`[^[:digit:]]`

### Vim

`\D`

### Perl

`\D`

## Hex Digits

### Python

`[0-9a-fA-F]`

### R

`[0-9a-fA-F]`

### sed

`[0-9a-fA-F]`

### egrep

`[0-9a-fA-F]`

### grep

`[0-9a-fA-F]`

### Vim

`\x`

### Perl

`[0-9a-fA-F]`

## Non-Hex Digit Characters

### Python

`[^0-9a-fA-F]`

### R

`[^0-9a-fA-F]`

### sed

`[^0-9a-fA-F]`

### egrep

`[^0-9a-fA-F]`

### grep

`[^0-9a-fA-F]`

### Vim

`\X`

### Perl

`[^0-9a-fA-F]`

## Octal Digits

### Python

`[0-7]`

### R

`[0-7]`

### sed

`[0-7]`

### egrep

`[0-7]`

### grep

`[0-7]`

### Vim

`\o`

### Perl

`[0-8]`

## Non-Octal Digit Characters

### Python

`[^0-7]`

### R

`[^0-7]`

### sed

`[^0-7]`

### egrep

`[^0-7]`

### grep

`[^0-7]`

### Vim

`\O`

### Perl

`[^0-8]`

## Head of Word Characters

### Python

`[a-zA-Z_]`

### R

`[a-zA-Z_]`

### sed

`[a-zA-Z_]`

### egrep

`[a-zA-Z_]`

### grep

`[a-zA-Z_]`

### Vim

`\h`

### Perl

`[a-zA-Z_]`

## Non-Head of Word Characters

### Python

`[^a-zA-Z_]`

### R

`[^a-zA-Z_]`

### sed

`[^a-zA-Z_]`

### egrep

`[^a-zA-Z_]`

### grep

`[^a-zA-Z_]`

### Vim

`\H`


### Perl

`[^a-zA-Z_]`

## Printable Character

### Python

NA

### R

NA

### sed

NA

### egrep

NA

### grep

NA

### Vim

`\p`


## Printable Character Excluding Digits

### Python

NA

### R

NA

### sed

NA

### egrep

NA

### grep

NA

### Vim

`\P`


## Word Character

### Python

`\w`

### R

`\\w` or `[[:alnum:]]`

### ICU

`\w`

### sed

`\w`

### egrep

`\w`

### grep

`\w`

### Vim

`\w`


## Non-word Character

### Python

`\W`

### R

Not supported in base (no `\\W` in the regular expression in the base package)
but supported in the stringi package.

### ICU 

`\W`

### sed

`\W`

### egrep

`\W`

### grep

`\W`

### Vim

`\W`


## Grouping
### Python
`()`
### R
`()`
### sed
`()`
### egrep
`()`
### grep
`\(\)`
### Vim
`\(\)`


## Alternation
### Python

### R

### sed

### egrep

### grep

### Vim



||||||||\||\||

## 0 or More Matches
### Python
`*`
### R
`*`
### sed
`*`
### egrep
`*`
### grep
`*`
### Vim
`*`


## 0 or 1 match
### Python
`?`
### R
`?`
### sed
`?`
### egrep
`?`
### grep
`?`
### Vim
`\=`


## 1 or More Matches
### Python
`+`
### R
`+`
### sed
`+`
### egrep
`+`
### grep
`+`
### Vim
`\+`


## Any Character Except a Newline
### Python
`.`
### R
`.`
### sed
`.`
### egrep
`.`
### grep
`.`
### Vim
`.`


## Start of a Line
### Python
`^`
### R
`^`
### sed
`^`
### egrep
`^`
### grep
`^`
### Vim
`^`


## End of a Line
### Python
`$`
### R
`$`
### sed
`$`
### egrep
`$`
### grep
`$`
### Vim
`$`


## Exactly `m` Matches
### Python
`{m}`
### R
`{m}`
### sed
`{m}`
### egrep
`{m}`
### grep
`{m}`
### Vim
`\\{m\\}`


## `m` or More Matches
### Python
`{m,}`
### R
`{m,}`
### sed
`{m,}`
### egrep
`{m,}`
### grep
`{m,}`
### Vim
`\\{m,\\}`


## `m` to `n` Matches
### Python
`{m,n}`
### R
`{m,n}`
### sed
`{m,n}`
### egrep
`{m,n}`
### grep
`{m,n}`
### Vim
`\\{m,n\\}`


## At Most `n` Matches
### Python
`{,n}`
### R
`{,n}`
### sed
`{,n}`
### egrep
`{,n}`
### grep
`{,n}`
### Vim
`\\{,n\\}`


## 0 or More Matches (as few as possible)
### Python
NA
### R
NA
### sed
NA
### egrep
NA
### grep
NA
### Vim
`\\{-\\}`


## m to n matches, as few as possible
### Python
NA
### R
NA
### sed
NA
### egrep
NA
### grep
NA
### Vim
`\\{-m,n\\}`


## at least m matches, as few as possible
### Python
NA
### R
NA
### sed
NA
### egrep
NA
### grep
NA
### Vim
`\\{-m,\\}`


## at most m matches, as few as possible
### Python
NA
### R
NA
### sed
NA
### egrep
NA
### grep
NA
### Vim
`\\{-,m\\}`



## Word Boundry 
### Python
`\b`
### R
Notice that word boundry in R includes `_`, numbers, etc.
`\b`
### Python
`\b`
### sed
`\b`
### Perl
`\b`
### egrep
`\b`
### grep
`\b`
### Vim
`\b`

## Escape Special Characters
### Teradata SQL
1. No need to escape `/`.
### R
`\\$`, `\\{`, `\\|`
### Python 
1. Need to escape `/`.
### sed
1. `.` -> `\\.`

## Some Confusing Concept
1. white spaces vs word boundry
word boundry is a super set of white spaces.
2. `\w` vs [[:alnum:]]
[[:alnum:]] contains all letters and numbers 
while `\w` contains not only letters and numbers but also some special character such as `_`. 
So in short `\w` is a super set of `[[:alnum:]]`.

