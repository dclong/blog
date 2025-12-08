Status: published
Date: 2024-07-22 13:39:40
Modified: 2025-06-09 02:49:30
Author: Benjamin Du
Slug: editing-shell-commands-using-vim
Title: Editing Shell Commands Using Vim
Category: Computer Science
Tags: Computer Science, programming

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Fish Shell]( https://www.legendu.net/misc/blog/tips-on-the-fish-shell ) 
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.

1. A bash prompt can be editted in both Vi mode and Emacs mode.
    The default is Emacs mode.
    You can turn on the Vi mode by `set -o vi` in `.bashrc`.
    This will make all bash prompts be edited in a limited single-line Vi mode.

2. The `fc` command edits the last shell command (using `$EDITOR`) and then send it for execution.

3. The shortcut `ctrl+x` `ctrl+e`
    edits the current shell prompt using `$VISUAL` or `$EDITOR`.
    If you want to use neovim as the editor,
    add the following configuration into your shell configuration.

        export VISUAL=nvim
        export EDITOR=nvim

    This is the recommended way to edit shell prompts
    as it allows your the full power and flexibility of the Vim editor.
    For example,

    - You are not limited to single-line editing of a single command.
         - You can span a complicated command to multiple lines using `\`.
         - You can split a complicated command into multiple simpler commands on multiple lines.
            On quiting Vim,
            those commands will be run in sequential.
    - If you find that you need information from historical commands
        while editing a prompt,
        you can bring historical commands in using the following command in Vim.

            :r ! fc -ln -10
            
    Notice that the shortcut `ctrl+x` `ctrl+e`
    doesn't work out-of-the-box in the terminal in Visual Studio Code.
    For more discussions,
    please refer to
    [Configuraing Terminal in Visual Studio Code]( https://www.legendu.net/misc/blog/configuraing-terminal-in-visual-studio-code )  
    .


4. [fzf.history](https://github.com/legendu-net/icon/blob/dev/utils/data/bash-it/plugins/custom.plugins.bash#L124)
    allows you to search through shell command history,
    select one, editing it in `$EDITOR`,
    and then send the edited command for execution.

## References

- [VISUAL vs. EDITOR – what’s the difference?](https://unix.stackexchange.com/questions/4859/visual-vs-editor-what-s-the-difference)

- [How do I edit current shell command in VI](https://apple.stackexchange.com/questions/88515/how-do-i-edit-current-shell-command-in-vi)

- [Recall the Previous Command or Its Arguments in Bash](https://www.baeldung.com/linux/bash-recall-previous-command)

- [After years of bash, I actually found a shortcut I never heard about.](https://www.reddit.com/r/linux/comments/13q4l4s/after_years_of_bash_i_actually_found_a_shortcut_i/)

- [Edit any command line in vim](https://www.reddit.com/r/vim/comments/9atgsj/edit_any_command_line_in_vim/)
