Status: published
Author: Ben Chuanlong Du
Date: 2021-03-10 09:54:11
Slug: regex-equivalence
Title: Regular Expression Equivalent
Category: Computer Science
Tags: tips, regex, equivalent, regular expression, regexp, Python, R, CRAN, Perl, SAS, grep, egrep

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**

[Regular Expression Tester](https://regex101.com/)


1. In some programming languages,
    you have to compile a plain/text pattern into a regular expression pattern object
    before using it.
    The Python module `re` automatically compiles a plain/text pattern 
    (using `re.compile`)
    and caches it,
    so there is not much benefit to compile regular expressions by yourself in Python.

2. `\W` does not include `^` and `$`.

3. Regular expression modifiers makes regular expression more flexible and powerful. 
    It is also a more universal way 
    than remembering different options in different programming languages or tools. 
    It is suggested that you use regular expression modifiers when possible.

4. Word boundry (`\b`) is a super set of white spaces (`\s`).

5. `[[:alnum:]]` contains all letters and numbers 
    while `\w` contains not only letters and numbers but also some special character such as `_`. 
    So in short `\w` is a super set of `[[:alnum:]]`.


<div style="overflow-x:auto;">
<table style="width:100%">
    <tr>
        <th> </th>
        <th> Vim search </th>
        <th> Python </th>
        <th> JavaScript </th>
        <th> Teradata SQL </th>
        <th> Oracle SQL </th>
        <th> grep </th>
        <th> sed </th>
    </tr>
    <tr>
        <td> Modifiers </td>
        <td> 
        </td>
        <td> 
            Partial<sup>[1]</sup>
        </td>
        <td> 
            Partial<sup>[1]</sup>
        </td>
        <td> Full </td>
        <td> 
            No<sup>[2]</sup> 
        </td>
        <td> Full[3] </td>
        <td> </td>
    </tr>
    <tr>
        <td> Greedy or not</td>
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
        <td> 
            Both<sup>[4]</sup>
        </td>
        <td> </td>
    </tr>
    <tr>
        <td> Popular functions </td>
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
        <td> </td>
        <td> </td>
    </tr>
    <tr>
        <td> White spaces </td>
        <td> 
            <code>\s</code>
        </td>
        <td> 
            <code>\s</code>
        </td>
        <td> 
        </td>
        <td> 
            [[:blank:]]
            [[:space:]]
        </td>
        <td> 
        </td>
        <td> 
            <code>\s</code> or <code>[[:space:]]</code>
        </td>
        <td> 
            <code>[[:space:]]</code> (recommended) or <code>\s</code>
        </td>
    </tr>
    <tr>
        <td> Non-white space </td>
        <td> 
            <code>\S</code>
        </td>
        <td> 
            <code>\S</code>
        </td>
        <td> 
        </td>
        <td> 
            [[:blank:]]
            [[:space:]]
        </td>
        <td> 
        </td>
        <td> 
            <code>\S</code>
        </td>
        <td> 
            <code>[^[:space:]]</code> or <code>\S</code>
        </td>
    </tr>
    <tr>
        <td> 
            Lower-case letters
        </td>
        <td> 
            <code>[a-z]</code> or <code>\l</code>
        </td>
        <td> 
            <code>[a-z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[a-z]</code>
        </td>
        <td> 
            <code>[a-z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non lower-case characters
        </td>
        <td> 
            <code>[^a-z]</code> or <code>\L</code>
        </td>
        <td> 
            <code>[^a-z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^a-z]</code>
        </td>
        <td> 
            <code>[^a-z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Upper-case letters
        </td>
        <td> 
            <code>[A-Z]</code> or <code>\u</code>
        </td>
        <td> 
            <code>[A-Z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[A-Z]</code>
        </td>
        <td> 
            <code>[A-Z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non upper-case characters
        </td>
        <td> 
            <code>[^A-Z]</code> or <code>\U</code>
        </td>
        <td> 
            <code>[^A-Z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^A-Z]</code>
        </td>
        <td> 
            <code>[^A-Z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Letters
        </td>
        <td> 
            <code>[a-zA-Z]</code> or <code>\a</code>
        </td>
        <td> 
            <code>[a-zA-Z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[a-zA-Z]</code>
        </td>
        <td> 
            <code>[a-zA-Z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non letters
        </td>
        <td> 
            <code>[^a-zA-Z]</code> or <code>\A</code>
        </td>
        <td> 
            <code>[^a-zA-Z]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^a-zA-Z]</code>
        </td>
        <td> 
            <code>[^a-zA-Z]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Digits
        </td>
        <td> 
            <code>\d</code>
        </td>
        <td> 
            <code>\d</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[[:digit:]]</code>
        </td>
        <td> 
            <code>\d</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non digits
        </td>
        <td> 
            <code>\D</code>
        </td>
        <td> 
            <code>\D</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^[:digit:]]</code>
        </td>
        <td> 
            <code>\D</code>
        </td>
    </tr>
    <tr>
        <td> 
            Hex digits
        </td>
        <td> 
            <code>[0-9a-fA-F]</code> or <code>\x</code>
        </td>
        <td> 
            <code>[0-9a-fA-F]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[0-9a-fA-F]</code>
        </td>
        <td> 
            <code>[0-9a-fA-F]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non-Hex digit characters
        </td>
        <td> 
            <code>[^0-9a-fA-F]</code> or <code>\X</code>
        </td>
        <td> 
            <code>[^0-9a-fA-F]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^0-9a-fA-F]</code>
        </td>
        <td> 
            <code>[^0-9a-fA-F]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Octal digits
        </td>
        <td> 
            <code>[0-7]</code> or <code>\o</code>
        </td>
        <td> 
            <code>[0-7]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[0-7]</code>
        </td>
        <td> 
            <code>[0-7]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non-octal digit Characters
        </td>
        <td> 
            <code>[^0-7]</code> or <code>\O</code>
        </td>
        <td> 
            <code>[^0-7]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^0-7]</code>
        </td>
        <td> 
            <code>[^0-7]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Head of word
        </td>
        <td> 
            <code>[a-zA-Z_]</code> or <code>\h</code>
        </td>
        <td> 
            <code>[a-zA-Z_]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[a-zA-Z_]</code>
        </td>
        <td> 
            <code>[a-zA-Z_]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non-head of word
        </td>
        <td> 
            <code<code>[^a-zA-Z_]</code> or <code>\H</code>
        </td>
        <td> 
            <code>[^a-zA-Z_]</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>[^a-zA-Z_]</code>
        </td>
        <td> 
            <code>[^a-zA-Z_]</code>
        </td>
    </tr>
    <tr>
        <td> 
            Printable Characters
        </td>
        <td> 
            <code>\p</code>
        </td>
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
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Non printable Characters
        </td>
        <td> 
            <code>\P</code>
        </td>
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
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Word characters
        </td>
        <td> 
            <code>\w</code>
        </td>
        <td> 
            <code>\w</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>\w</code>
        </td>
        <td> 
            <code>\w</code>
        </td>
    </tr>
    <tr>
        <td> 
            Word boundry
        </td>
        <td> 
            <code>\b</code>
        </td>
        <td> 
            <code>\b</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>\b</code>
        </td>
        <td> 
            <code>\b</code>
        </td>
    </tr>
    <tr>
        <td> 
            Non word characters
        </td>
        <td> 
            <code>\W</code>
        </td>
        <td> 
            <code>\W</code>
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            <code>\W</code>
        </td>
        <td> 
            <code>\W</code>
        </td>
    </tr>
    <tr>
        <td> 
            grouping
        </td>
        <td> 
            \(\)
        </td>
        <td> 
            ()
        </td>
        <td> 
            ()
        </td>
        <td> 
            ()
        </td>
        <td> 
            ()
        </td>
        <td> 
            \(\)
        </td>
        <td> 
            ()
        </td>
    </tr>
    <tr>
        <td> 
            0 or more matches
        </td>
        <td> 
            *
        </td>
        <td> 
            *
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            *
        </td>
        <td> 
            *
        </td>
    </tr>
    <tr>
        <td> 
            0 or more matches (as few as possible)
        </td>
        <td> 
            \\{-\\}
        </td>
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
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            0 or 1 matches
        </td>
        <td> 
            \=
        </td>
        <td> 
            ?
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            ?
        </td>
        <td> 
            ?
        </td>
    </tr>
    <tr>
        <td> 
            1 or more matches
        </td> 
        <td> 
            \+
        </td>
        <td> 
            +
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            +
        </td>
        <td> 
            +
        </td>
    </tr>
    <tr>
        <td> 
            Exactly m matches
        </td>
        <td> 
            \\{m\\}
        </td>
        <td> 
            {m}
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            {m}
        </td>
        <td> 
            {m}
        </td>
    </tr>
    <tr>
        <td> 
            m or more matches
        </td>
        <td> 
            \\{m,\\}
        </td>
        <td> 
            {m,}
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            {m,}
        </td>
        <td> 
            {m,}
        </td>
    </tr>
    <tr>
        <td> 
            m or more matches (as few as possible)
        </td>
        <td> 
            \\{-m,\\}
        </td>
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
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            m to n matches
        </td>
        <td> 
            \\{m,n\\}
        </td>
        <td> 
            {m,n}
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            {m,n}
        </td>
        <td> 
            {m,n}
        </td>
    </tr>
    <tr>
        <td> 
            m to n matches (as few as possible)
        </td>
        <td> 
            \\{-m,n\\}
        </td> 
        <td> </td> 
        <td> </td> 
        <td> </td> 
        <td> </td> 
        <td> </td> 
        <td> </td>
    </tr>
    <tr>
        <td> 
            up to n matches
        </td>
        <td> 
            \\{,n\\}
        </td>
        <td> 
            {,n}
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            {,n}
        </td>
        <td> 
            {,n}
        </td>
    </tr>
    <tr>
        <td> 
            up to n matches (as few as possible)
        </td>
        <td> 
            \\{-,n\\}
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
    </tr>
    <tr>
        <td> 
            Any character except a newline
        </td>
        <td> 
            .
        </td>
        <td> 
            .
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            .
        </td>
        <td> 
            .
        </td>
    </tr>
    <tr>
        <td> 
            Start of a line
        </td>
        <td> 
            ^
        </td>
        <td> 
            ^
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            ^
        </td>
        <td> 
            ^
        </td>
    </tr>
    <tr>
        <td> 
            End of a line
        </td>
        <td> 
            $
        </td>
        <td> 
            $
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
        </td>
        <td> 
            $
        </td>
        <td> 
            $
        </td>
    </tr>
    <tr>
        <td> 
            Literal /
        </td>
        <td> 
        </td>
        <td> 
            \/ (need to escape)
        </td> 
        <td> 
        </td>
        <td> 
            / (no need to escape)
        </td>
        <td> 
        </td>
        <td> 
        </td>
    </tr>
    <tr>
        <td> 
            Literal dot
        </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> 
            \\.
        </td>
    </tr>
</table>
</div>

[1]: Python/JavaScript partially supports regular expression modifiers.
    To be more specifically,
    turning modifiers on is supported
    but turning modifiers off is not supported.
    Modifiers (once turned on) are applied to the entire regular expression
    and cannot be turned off.

[2]: Behavior of regular expressions in Oracle SQL 
    is control via parameters of regular expression  functions 
    instead of via regular expression modifiers.

[3]: `grep` fully supports regular expression modifiers 
    via Perl style regular (the `-P` option) expressions.

[4]: `grep` matches pattern greedly by default.
    However, 
    in Perl style syntax you can use the modifer `?` after a quantifier to perform a non-greedy match.
    For example, 
    instead of `.*` you can use `.*?` to do a non-greedy match.
## References

[Regular Expression in Bash](http://www.legendu.net/misc/blog/regular-expression-in-bash/)
