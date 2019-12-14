Status: published
Date: 2019-12-14 11:44:55
Author: Benjamin Du
Slug: precedence-of-operators-in-regular-expression
Title: Precedence of Operators in Regular Expression
Category: Programming
Tags: programming, regex, regular expression, POSIX, precedence

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


The order of precedence of operators in POSIX extended regular expression is as follows.

1. Collation-related bracket symbols `[==]`, `[::]`, `[..]`
2. Escaped characters `\`
3. Character set (bracket expression) `[]`
4. Grouping `()`
5. Single-character-ERE duplication `*`, `+`, `?`, `{m,n}`
6. Concatenation
7. Anchoring `^`, `$`
8. Alternation `|`


## References

[POSIX Extended Regular Expression Syntax](https://www.boost.org/doc/libs/1_56_0/libs/regex/doc/html/boost_regex/syntax/basic_extended.html#boost_regex.syntax.basic_extended.operator_precedence)

[Operator Precedence of POSIX Extended Regular Expression](https://www.boost.org/doc/libs/1_56_0/libs/regex/doc/html/boost_regex/syntax/basic_extended.html#boost_regex.syntax.basic_extended.operator_precedence)