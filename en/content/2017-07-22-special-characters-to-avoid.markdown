Status: published
Date: 2020-10-24 09:18:04
Author: Ben Chuanlong Du
Slug: special-characters-to-avoid
Title: Special Characters to Avoid in Strings
Category: Computer Science
Tags: programming, special characters, avoid, password, file name, Shell

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

This articles talks about special characters to avoid in various places. 
You might not encounter issues most of the time when violating rules stated below,
however, 
you never know when things will break.
It is more for a good-practice suggestion.

## String for Shell

1. When you pass parameters from one program to another one,
    do not make assumptions on how shell is handled.
    For this reasons,
    you might want to avoid `` `something `` and `$(something)` in parameters 
    passed to another program which might be part of a shell command.

## File Names

1. Avoid the following special characters in file names.
    - spaces (` `)   
        Spaces in paths might cause issues in Shell
        as paths have to be quoted in double/single strings.
        However,
        some Shell commands/applications might handle this well.
    - dollar signs (`$`)  
        The dollar sign (`$`) has special meanings in various places (e.g., in Shell).
    - double quotes (`"`)  
        A double quotes sign might need escape.
    - single quotes (`'`)  
        A single quotes sign might need escape.
    - tilde (`~`)  
        The tilde sign (`~`) has special meanings (e.g., the name of some buffer files starts with tilde) in various places.
    - dash/minus (`-`)   
        Dash is OK but underscore (`_`) as an alternative is more readable.
    - backtick (`` ` ``) 
        Backticks have special meanings in various places.
    - shell command (`$()`)   
        Self explained.
    - semicolon (`;`) 
        Semicolon indicating the end of a shell command. 
        It might cause issues when used carelessly in shell commands.
        This also applies when your application take a string of delimited paths,
        in which case you want to avoid using semicolon (`;`) as the delimiter.
        Comma (`,`) is a better alternative in this case.

2. When you programmally get the path of a file, 
    it is best to convert it to its absolute representation.

## Password

1. Avoid the following special characters in passwords.
    - space (` `)  
        Some applications does not allow spaces in passwords.
    - dollar signs (`$`)   
        Dollar signs (`$`) have special meanings in various places.
    - double quotes (`"`) 
        A double quote sign (`"`) might need to be escaped in code.
    - single quotes (`'`)   
        A single quote sign (`'`) might need to be escaped in code.
    - backtick (`` ` ``) 
        Backticks have special meanings in various places.
    - shell command (`$()`)  
        Self explained.