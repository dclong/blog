Status: published
Date: 2019-10-15 20:52:22
Author: Benjamin Du
Slug: tips-on-xonsh
Title: Tips on Xonsh
Category: Computer Science
Tags: programming, Python, shell, xonsh, Python evaluation
Modified: 2019-10-15 20:52:22

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

https://github.com/xonsh/xonsh/wiki/Cheatsheet

## Tricks and Traps

1. While `$()` in xonsh works similar to `$()` in (all variants of) shell, 
    it cannot be used in the middle of argument of a shell command. 
    Please refer to 
    [issue 1022](https://github.com/xonsh/xonsh/issues/1022)
    and
    [issue 3290](https://github.com/xonsh/xonsh/issues/3290)
    for more details.
    My suggestion is to stick to xonsh as much as possible (as Python is much better than shell)
    unless you encounter the above issues.

2. xonsh messes up console flush sometimes.
    Please refer to 
    [issue 3320](https://github.com/xonsh/xonsh/issues/3320)
    for more details.

3. `source` sources in a xonsh script.
    `source-bash` sources in a Bash script.

    https://xon.sh/aliases.html#source-bash

    https://github.com/xonsh/xonsh/issues/2978

## Python Evaluation

### [Python Evalation with `@()`](https://xon.sh/tutorial.html#python-evaluation-with)

The code below prints `1 2 3` in xonsh.
```xonsh
x = [1, 2, 3]
echo @(x)
```

### Python Evalation with f-string.

The Python variales are casted to string directly.
For example, 
the code below prints `[1, 2, 3]` in xonsh.
```xonsh
x = [1, 2, 3]
echo f'{x}'
```

## Force (Shell) Subprocess

1. use `os.system` or `subprocess.run`

2. wrap the command in `$()`. 
    Notice that `$()` cannot be used in the middle of arguments currently.

2. wrap the command in `$[]`

3. for some commands, you just need to put part of it into single/double quotes.
    For example, 
    xonsh fails to recognize `pip3 install dask[complete]` as a shell command 
    while it recognize `pip3 install "dask[complete]"` as a shell command.

## Background Mode for Subprocess

https://github.com/xonsh/xonsh/issues/1477#event-2481368935

## References

[Bash to Xonsh Translation Guide¶](https://xon.sh/bash_to_xsh.html)

[Run Control File](https://xon.sh/xonshrc.html)

[Updating and customizing xonsh](https://xon.sh/customization.html)

[Environment Variables](https://xon.sh/envvars.html)

[Xonribs](https://xon.sh/xontribs.html)

[Environment Variables](https://xon.sh/envvars.html)

https://github.com/xonsh/xonsh/issues/1477#event-2481368935

https://stackoverflow.com/questions/39724184/how-to-write-a-multi-command-alias-in-xonsh/39761905#39761905
