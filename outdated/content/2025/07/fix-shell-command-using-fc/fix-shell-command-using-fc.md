Status: published
Date: 2025-07-06 11:08:48
Modified: 2025-07-06 16:17:25
Author: Benjamin Du
Slug: fix-shell-command-using-fc
Title: Fix Shell Commands Using fc
Category: Computer Science
Tags: Computer Science, programming, shell, command, bash, zsh, fc

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Fish Shell]( https://www.legendu.net/misc/blog/tips-on-the-fish-shell ) 
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.


[fzf.history](https://github.com/legendu-net/icon/blob/dev/utils/data/bash-it/plugins/custom.plugins.bash#L149)
is a better alternative to `fc`'s core functionality (edit and re-execute command).

## Tips & Traps

1. In Linux shells like Bash and Zsh, 
    `fc` is a built-in command that stands for "Fix Command".
    Its primary purpose is to let you edit and re-execute commands 
    from your history using `$EDITOR`.

2. `fc -l 1` might throw the error `-bash: fc: history specification out of range` in bash
    (some people say that this won't be an issue in zsh as zsh is smart enough to handle specification out of range but I haven't verified it yet)
    if the (absolute) first bash history command has been pruned (due to large number of history commands).
    `HISTTIMEFORMAT="" history | sed -E 's/^[ ]*[0-9]+[ ]*//'` is a more robust command for the same purpose.

<table>
    <thead>
        <tr>
            <th>Command</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>fc</code></td>
            <td>Edit the last shell command using <code>$EDITOR</code> and send it for execution.
        </tr>
        <tr>
            <td><code>fc 123</code></td>
            <td>Edit and execute command number 123 from history.</td>
        </tr>
        <tr>
            <td><code>fc git</code></td>
            <td>Edit and execute the last command starting with "git".</td>
        </tr>
        <tr>
            <td><code>fc -l</code></td>
            <td>
                List all history commands.
            </td>
        </tr>
        <tr>
            <td><code>fc -ln</code></td>
            <td>
                List all history commands without numbers.
            </td>
        </tr>
        <tr>
            <td><code>fc -ln 100 110</code></td>
            <td>
                List commands from 100 to 110 without numbers.
            </td>
        </tr>
        <tr>
            <td><code>fc -ln -5</code></td>
            <td>
                List the last 5 historical commands without numbers.
            </td>
        </tr>
        <tr>
            <td><code>fc -s</code></td>
            <td>Re-execute the last command without editing.</td>
        </tr>
        <tr>
            <td><code>fc -s old=new</code></td>
            <td>Re-execute the last command, replacing <code>old</code> with <code>new</code>.</td>
        </tr>
        <tr>
            <td><code>fc -s old=new git</code></td>
            <td>Re-execute the last <code>git</code> command, replacing <code>old</code> with <code>new</code>.</td>
        </tr>
    </tbody>
</table>