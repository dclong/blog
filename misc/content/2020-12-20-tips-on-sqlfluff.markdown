Status: published
Date: 2020-12-30 14:01:53
Author: Benjamin Du
Slug: tips-on-sqlfluff
Title: Tips on Sqlfluff
Category: Computer Science
Tags: Computer Science, sqlfluff, SQL, lint, linter, format, issue, error

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## General Tips and Traps 

1. SQLfluff supports Jinja template! 

## Safe to fix
2. L001: Unneccessary trailing whitespace.
3. L008: Commas should be followed by a single whitespace unless followed by a comment.


## Ignore 

L:  75 | P:   5 |  LXR | Unable to lex characters: ''${candidat'...'

## Parsing Error

1. PRS: Found unparsable section: '-- /*Select list of users to choose from...'
