Status: published
Date: 2019-04-28 11:53:55
Author: Benjamin Du
Slug: regular-expression-in-bash
Title: Regular Expression in Bash
Category: Computer Science
Tags: programming, Bash, regular expression, regex

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


You can use `=~` for regular expression mathch in Bash.
This make Bash syntax extremely flexible and powerful.
For example, 
you can match multiple strings using regular expression.
```
if [[ value =~ ^(v1|v2|v3)$ ]]; then
    ...
fi
```
