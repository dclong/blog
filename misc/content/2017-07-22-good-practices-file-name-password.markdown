Status: published
Date: 2020-10-23 12:19:10
Author: Ben Chuanlong Du
Slug: speical-characters-to-avoid
Title: Speical Characters to Avoid in Strings
Category: Computer Science
Tags: programming, speical characters, avoid, password, file name, Shell

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. When you pass parameters from one program to another one,
    do not make any assumption on how shell is handled.
    For this reasons,
    you want to avoid `` `...` `` and `$(...)` in parameters 
    passed to another program which might be part of a shell command.

## File Names

1. Avoid the following special characters in file names.
    - spaces (` `) 
    - dollar signs (`$`)
    - double quotes (`"`)
    - single quotes (`'`)
    - tilde (`~`)
    - dash/minus (`-`) 
    - backtick (`` ` ``) 
    - shell command (`$()`) 
    - semicolon (`;`) 
        Semicolon indicating the end of a shell command. 
        It might cause issues when used carelessly in shell commands.
        This also applies when your application take a string of delimited paths,
        in which case you want to avoid using semicolon (`;`) as the delimiter.
        Comma (`,`) is a better alternative in this case.

2. When you programmally get the path of a file, 
    it is best to convert it to its absolute form.

## Password

1. Avoid the following special characters in passwords.
    - space (` `)
    - dollar signs (`$`) 
    - double quotes (`"`) 
    - single quotes (`'`) 
    - backtick (`` ` ``) 
    - shell command (`$()`) 