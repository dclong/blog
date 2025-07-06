Status: published
Title: Cool Shell/Terminal Commands
Date: 2012-09-18 21:38:38
Tags: shell, terminal, Linux
Category: OS
Slug: cool-shell-commands
Author: Ben Chuanlong Du
Modified: 2025-07-06 11:06:17

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[Bash Reference Manual](http://www.gnu.org/software/bash/manual/bashref.html)

[ExplainShell](https://www.explainshell.com/)

## Seeking Help

The best way to seek for help is surely to use a search engine.
However, there are serveral terminal command that can help you quickly.

1. `whatis` briefly describes what a command does.
    For example,

        $ whatis man
        man (7)              - macros to format man pages
        man (1)              - an interface to the on-line reference manuals

2. `whereis` locate the binary, source, and manual page files for a command.

3. `apropos` searches description of commands
    and find these associated with the job you specify.
    For example,

        $ apropos gzip
        gzip (1) - compress or expand files
        zforce (1) - force a '.gz' extension on all gzip files

3. `man` display help documentation of commands.
    Note that you display the description of `man` itself by

        man man

    When display contents of a file in terminal,
    you can use `/` to search for strings that match the one you specify.
    When searching,
    you can use `n/N` to jump to the next/previous match.

### Retrieving History Commands

It is suggested that you search shell command history using `fzf`.
For more discussions,
please refer to
[Editing Shell Commands Using Vim]( https://www.legendu.net/misc/blog/editing-shell-commands-using-vim )
.

1. `!!` or `!:-1` stands for the last command.
    `!!` runs last command and `sudo !!` runs the last command with `sudo` permission.

2. `!n` (where $n$ is a natural number) stands for the $n^{th}$ command in the command history.

3. `!-n` stands for the last but $n-1$ command in the command history,

4. `!foo` stands for the most recent command starting with `foo`.

5. `history` prints out all historical commands (with numbers).

6. `history -s command` saves the specified command to the in-memory history.

7. You can also retrieving history shell commands using the built-in command `fc`.
    Please refer to 
    [Fix Shell Command Using Fc]( https://www.legendu.net/misc/blog/fix-shell-command-using-fc )
    for more discussion.

### Manipulating Commands

It is suggested that you use `ctrl+x` `ctrl+e` or `fzf.history` 
to edit shell commands.
For more discussions,
please refer to
[Editing Shell Commands Using Vim]( https://www.legendu.net/misc/blog/editing-shell-commands-using-vim )
.

1. You can use the suffix `:-` to get rid of
    the last parameter of the retrieved command.
    For example,
    `!!:-` stands for the last command without the last parameter.

2. `^foo^bar^` stands for the last command
    with the first occurence of `foo` replaced by `bar`.
    The last `^` can be omitted if no more manipulation on the command is neede.
    (Note that this trick only works for the last command.)

2. You can use the suffix `:s/foo/bar/` to replace the first occurrence of `foo` with `bar`
    in a retrieved command.
    For example,
    `!!:s/foo/bar/` stands for the last command
    with the first occurrence of `foo` replaced by `bar`.
    The last `/` can be omitted if no more manipulation on the command is needed.

2. You can use the suffix `:gs/foo/bar/` to replace all occurrences of `foo` with `bar`
    in a retrieved command.
    For example,
    `!!:gs/foo/bar/` stands for the last command
    with all occurences of `foo` replaced by `bar`.
    The last `/` can be omitted if no more manipulation on the command is needed.

3. You can add vanilla strings before and/or after a retrieved command.
    For example,

    1. `sudo !foo` runs the most recent command starting with `foo` with
        `sudo` permissions.

    2. `!n:gs/foo/bar/ | less` runs the $n^{th}$ command in the history
        with all occurrences of `foo` replaced by `bar`
        and displays the result in `less` mode.

    3. `sudo ^foo^bar^ | less` or `sudo !!:s/foo/bar/ | less` runs last command
        with `sudo` permissions and displays the results in `less` mode.

### Previeawing Commands

You can preview (rather than run) a retrived and manipulated (using string substitution) command
by adding the suffix `:p` to the command.  

In the above commands,
if you add suffix `:p` (e.g, `!!:p`),
then the corresponding command is printed to the console without being executed.
Notice that the previewed command will be added to the command history,
so you can press "Arrow Up" key to retrieve it.
`^foo^bar^:p` `!n:gs/foo/bar/:p`

## Retrieve Parameter of Commands

It is suggested that you use `ctrl+x` `ctrl+e` or `fzf.history` 
to edit shell commands.
For more discussions,
please refer to
[Editing Shell Commands Using Vim]( https://www.legendu.net/misc/blog/editing-shell-commands-using-vim )
.

1. `!$` stands for the last parameter of last command.

2. `$_` stands for the last parameter of last command.

3. `!:0` stands for the Linux command in the last command.

4. `!:3-5` stands for the third to fifth parameters of the last command.
    If the first argument index is 0, then it can be omitted.
    For example, `!:0-2` can be simplified as `!:-2`.
    If the "TO" argument index is omited,
    then the last argument is not included.
    For example, `!:3-` means the third argument to the last-but-1 argument.
    Specially, `!:-` stands for last command without the last argument.

5. `<ESC> .` or `ALT + .` retrieves the last parameter of any previous command.
    Pressed once, it retrives the last parameter of the last command;
    pressed twice, it retrives the last parameter of the 2nd last command,
    and so on and so forth.

## Retrieve Output of Commands

There is no direct way to retrieve the output of the last command.
However,
there are several indirect ways to do this.

1. Use substitution.
    For example,
    `` v=`ls` `` makes `v` a variable containing the result of last command.

2. Assign result to a variable.
    For example,
    `v=$(ls)` makes `v` a variable contining the result of last command.

3. Use `$(!!)` to retrieve the result of last command.
    Similarly,
    one can use `$(!-2)` to retrieve the result of the 2nd last command.

## References

- [Arch Wiki](https://wiki.archlinux.org/index.php/Keyboard_Shortcuts)
