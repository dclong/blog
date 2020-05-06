Status: published
Author: Ben Chuanlong Du
Date: 2020-05-05 23:50:13
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

3. Regular expression modifiers makes regular expression more flexible and powerful. 
    It is also a more universal way 
    than remembering different options in different programming languages or tools. 
    It is suggested that you use regular expression modifiers when possible.


<table style="width:100%">
    <tr>
        <th> </th>
        <th> grep </th>
        <th> sed </th>
        <th> Vim search </th>
        <th> Python </th>
        <th> JavaScript </th>
        <th> Teradata SQL </th>
        <th> Oracle SQL </th>
    </tr>
    <tr>
        <td> Regular expression modifiers </td>
        <td> Fully suppoted via Perl style regular (the `-P` option) expressions. </td>
        <td> 
        </td>
        <td> 
            Partially supported. 
            Turning modifiers on is supported
            however turning modifiers off is not supported.
            Modifiers (once turned on) are applied to the entire regular expression
            and cannot be turned off.
        </td>
        <td> 
            Partial supported.
            Tunning modifiers on is supported
            however turnning modifiers off is not supported.
            Modifiers (once turned on) are applied to the entire regular expression
            and cannot be turned off.
        </td>
        <td> Fully supported. </td>
        <td> 
            Not supported. 
            Behavior of regular expressions are control via parameters of regular expression functions.
        </td>
    </tr>
    <tr>
        <td> Greedy match or not </td>
        <td> 
            Greedy by default.
            However, 
            in the Perl style syntax you use the modifer `?` after the quantifier to perform a non-greedy match.
            For example, 
            instead of `.*` you can use `.*?` to do a non-greedy match.
        </td>
        <td> </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> Popular functions </td>
        <td> 
        </td>
        <td> </td>
        <td> 
        </td>
        <td> 
            re.search, re.sub
        </td>
        <td> 
        </td>
        <td> 
            regexp_instr
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> White spaces </td>
        <td> 
            `\s` or `[[:space:]]`
        </td>
        <td> 
            `[[:space:]]` (recommended) or `\s`
        </td>
        <td> 
            `\s`
        </td>
        <td> 
            `\s`
        </td>
        <td> 
        </td>
        <td> 
            [[:blank:]]
            [[:space:]]
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> Non-white space </td>
        <td> 
            `\S`
        </td>
        <td> 
            `[^[:space:]]` or `\S`
        </td>
        <td> 
            `\S`
        </td>
        <td> 
            `\S`
        </td>
        <td> 
        </td>
        <td> 
            [[:blank:]]
            [[:space:]]
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Lower-case letters
        </td>
        <td> 
            `[a-z]`
        </td>
        <td> 
            `[a-z]`
        </td>
        <td> 
            `[a-z]` or `\l`
        </td>
        <td> 
            `[a-z]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non lower-case characters
        </td>
        <td> 
            `[^a-z]`
        </td>
        <td> 
            `[^a-z]`
        </td>
        <td> 
            `[^a-z]` or `\L`
        </td>
        <td> 
            `[^a-z]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Upper-case letters
        </td>
        <td> 
            `[A-Z]`
        </td>
        <td> 
            `[A-Z]`
        </td>
        <td> 
            `[A-Z]` or `\u`
        </td>
        <td> 
            `[A-Z]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non upper-case characters
        </td>
        <td> 
            `[^A-Z]`
        </td>
        <td> 
            `[^A-Z]`
        </td>
        <td> 
            `[^A-Z]` or `\U`
        </td>
        <td> 
            `[^A-Z]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Letters
        </td>
        <td> 
            `[a-zA-Z]`
        </td>
        <td> 
            `[a-zA-Z]`
        </td>
        <td> 
            `[a-zA-Z]` or `\a`
        </td>
        <td> 
            `[a-zA-Z]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non letters
        </td>
        <td> 
            `[^a-zA-Z]`
        </td>
        <td> 
            `[^a-zA-Z]`
        </td>
        <td> 
            `[^a-zA-Z]` or `\A`
        </td>
        <td> 
            `[^a-zA-Z]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Digits
        </td>
        <td> 
            `[[:digit:]]`
        </td>
        <td> 
            `\d`
        </td>
        <td> 
            `\d`
        </td>
        <td> 
            `\d`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non digits
        </td>
        <td> 
            `[^[:digit:]]`
        </td>
        <td> 
            `\D`
        </td>
        <td> 
            `\D`
        </td>
        <td> 
            `\D`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Hex digits
        </td>
        <td> 
            `[0-9a-fA-F]`
        </td>
        <td> 
            `[0-9a-fA-F]`
        </td>
        <td> 
            `[0-9a-fA-F]` or `\x`
        </td>
        <td> 
            `[0-9a-fA-F]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non-Hex digit characters
        </td>
        <td> 
            `[^0-9a-fA-F]`
        </td>
        <td> 
            `[^0-9a-fA-F]`
        </td>
        <td> 
            `[^0-9a-fA-F]` or `\X`
        </td>
        <td> 
            `[^0-9a-fA-F]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Octal digits
        </td>
        <td> 
            `[0-7]`
        </td>
        <td> 
            `[0-7]`
        </td>
        <td> 
            `[0-7]` or `\o`
        </td>
        <td> 
            `[0-7]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non-octal digit Characters
        </td>
        <td> 
            `[^0-7]`
        </td>
        <td> 
            `[^0-7]`
        </td>
        <td> 
            `[^0-7]` or `\O`
        </td>
        <td> 
            `[^0-7]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Head of word
        </td>
        <td> 
            `[a-zA-Z_]`
        </td>
        <td> 
            `[a-zA-Z_]`
        </td>
        <td> 
            `[a-zA-Z_]` or `\h`
        </td>
        <td> 
            `[a-zA-Z_]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non-head of word
        </td>
        <td> 
            `[^a-zA-Z_]`
        </td>
        <td> 
            `[^a-zA-Z_]`
        </td>
        <td> 
            `[^a-zA-Z_]` or `\H`
        </td>
        <td> 
            `[^a-zA-Z_]`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Printable Characters
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            `\p`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non printable Characters
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            `\P`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Word characters
        </td>
        <td> 
            `\w`
        </td>
        <td> 
            `\w`
        </td>
        <td> 
            `\w`
        </td>
        <td> 
            `\w`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non word characters
        </td>
        <td> 
            `\W`
        </td>
        <td> 
            `\W`
        </td>
        <td> 
            `\W`
        </td>
        <td> 
            `\W`
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
</table>


## Grouping
### Python
`()`
### sed
`()`
### grep
`\(\)`
### Vim
`\(\)`


## Alternation
### Python

### sed

### grep

### Vim



## 0 or More Matches
### Python
`*`
### sed
`*`
### grep
`*`
### Vim
`*`


## 0 or 1 match
### Python
`?`
### sed
`?`
### grep
`?`
### Vim
`\=`


## 1 or More Matches
### Python
`+`
### sed
`+`
### grep
`+`
### Vim
`\+`


## Any Character Except a Newline
### Python
`.`
### sed
`.`
### grep
`.`
### Vim
`.`


## Start of a Line
### Python
`^`
### sed
`^`
### grep
`^`
### Vim
`^`


## End of a Line
### Python
`$`
### sed
`$`
### grep
`$`
### Vim
`$`


## Exactly `m` Matches
### Python
`{m}`
### sed
`{m}`
### grep
`{m}`
### Vim
`\\{m\\}`


## `m` or More Matches
### Python
`{m,}`
### sed
`{m,}`
### grep
`{m,}`
### Vim
`\\{m,\\}`


## `m` to `n` Matches
### Python
`{m,n}`
### sed
`{m,n}`
### grep
`{m,n}`
### Vim
`\\{m,n\\}`


## At Most `n` Matches
### Python
`{,n}`
### sed
`{,n}`
### grep
`{,n}`
### Vim
`\\{,n\\}`


## 0 or More Matches (as few as possible)
### Python
NA
### sed
NA
### grep
NA
### Vim
`\\{-\\}`


## m to n matches, as few as possible
### Python
NA
### sed
NA
### grep
NA
### Vim
`\\{-m,n\\}`


## at least m matches, as few as possible
### Python
NA
### sed
NA
### grep
NA
### Vim
`\\{-m,\\}`


## at most m matches, as few as possible
### Python
NA
### sed
NA
### grep
NA
### Vim
`\\{-,m\\}`



## Word Boundry 
### Python
`\b`
### sed
`\b`
### grep
`\b`
### Vim
`\b`

## Escape Special Characters
### Teradata SQL
1. No need to escape `/`.
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

