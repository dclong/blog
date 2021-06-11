Status: published
Date: 2020-03-25 18:28:38
Author: Ben Chuanlong Du
Slug: vim-tips
Title: Tips on Vim
Category: Software
Tags: tips, Linux, software, Vim, surround, repeat
Modified: 2020-03-25 18:28:38


**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**

## Vim Distributions

- [SpaceVim](https://spacevim.org/)

- [spf13-vim](https://vim.spf13.com/)


## Reload File

`:e!`

https://unix.stackexchange.com/questions/149209/refresh-changed-content-of-file-opened-in-vim

## Case Insensitive Search

/\cPatterToSearch

:set ignorecase

:set smartcase
/copyright      " Case insensitive
/Copyright      " Case sensitive
/copyright\C    " Case sensitive
/Copyright\c    " Case insensitive

[How to do case insensitive search in Vim](https://stackoverflow.com/questions/2287440/how-to-do-case-insensitive-search-in-vim)

## Tips

1. Look for good vim plugins on [Vim Awesome](https://vimawesome.com/).

## Tricks & Traps

1. To quickly comment a range of text, 
    you can substitute ^ with # in that range.

2. `:w !sudo tee %` helps write current content into the file 
    if you did not open the write-protected file with `sudo vim`.
    Another way is to use the `:w a_file` command to write to a file that you 
    have access to and then use it to replace the original file. 

## Search

1. `n` jumps to next occurrence of the search pattern 
    and `N` jumps to previous occurrence of the search pattern.

2. `/` (without specifying a search pattern) searches last searched string. 
    This trick can also be used in substitution.
    For example, 
    `:%s//new_string/gc` replaces the last search pattern with `new_string`.

## Command

1. You can use `:! external_command` to run external commands. 
    You can use the up and down arrow to scroll to last and next external command 
    after you have typed `:! ` in Vim. 
    This trick also works in other environment, 
    e.g., you can press the up and down key to scroll to last and next search string
    after you have typed `/` in Vim.

## Buffers

1. `:buffers`, `:ls`, `:bw` (have to write buffer to file first)

  :bn go to the next buffer 

  :bp go to the previous buffer 

  :e #: go to the previous buffer 

## Indent

1. Select lines that you want to indent
    and then use command `:le n` or `:ri n`.
    This sets the indent of the selected lines to `n` spaces (from the left/right).

2. `>>`, `n>>`

1. Use `>G` to shift the current line and lines after to the right.
    If you want shift all lines to the right,
    you can first go the first line by command `gg`,
    and then type in command `>G`.

## Read 

1. You can read the content of a file or the output of an external command into Vim.

        :r path_to_file
        :r !ls
        :r !date

## Misc

1. it is recommned to use `"+p` to paste text in clipboard copied from other places,
    especially text with indentions.

5. can user-defined commands operate on marked range? e.g., delete the last column of marked range?

7. vim plugin for other softwares, such as editors, pdf viewer, etc.

8. how to list all user-defined commands and macros?

1. `ge` goes to the end of the previous word

2. `''` (two apostrophes) or `````` (two backticks) to go to the previous position of cursor

2. Like most of the capitalized movement pairs, b moves by word, 
    but B moves by WORD. 
    The difference is that vim considers a "word" to be letters, numbers, 
    and underscores (and you can configure this with the iskeyword setting), 
    but a "WORD" is always anything that isn't whitespace.


## Addons

1. repeat

4. surround

4. airlight

5. VsVim: Plugin for Visual Studio.

6. tComment

## Macro

1. As with other commands in vi, you can playback a macro any number of times.
    The following command would playback the macro assigned to the key `w' 100
    times: 100@w

2. Macro letters are case-insensitive. 

2. Vim uses words that exist in your current buffer and any other buffer you may
    have open for auto-complete suggestions.

## Macro/Command/Function

1. Macro is best for simple and one-time task
    Command is best for frequently task, command is easy to use
    Functions are for more complicated task, not as convenient as command to use
    but you can define function and wrap it in a command

## Settings

1. It is good practice to set a central swap and backup directory.
    You'd better use 2 path separator (//) at the end of the path!
    This makes vim to use the full path of the swap file, 
    which ensures unique path name.

3. It is good practice to map the Caps Lock key to the Esc key or to swap them.

## Usage

1. Search in visual mode let you quick select large block of text.
    For example, if you search "quickly" in visual mode, 
    the text from cursor to the next occurrence of "quickly" will be selected.

2. You have to "\r" instead of "\n" for newline when substituting characters. 

6. You can execute more than one command by placing a `|` between two commands. 

3. The ability to run external command (prefixed by `!`) is great!
    For example, you can use `:r !basename % .sh` to insert the name of the current file.

3. Insert date (different ways) or you can use UltiSnips to do it which is recommended.
    normal mode
        "=strftime('%c')<C-M>p
        :r!date +\%c
        :call append(line('.'), strftime("%c"))
        :call setline(line('.'), getline(line('.')) . strftime("%c"))
        :call setline(line('.'), getline(line('.')) . " " . strftime("%c"))
insert mode
        <C-R>=strftime('%c')<C-M>

" -------- define some commands ---------
command! ShabangBash :normal! ggi#!/bin/bash<Esc>
command! AppendFileName :call append(line('.'), expand('%:t'))
command! FunScript :normal! Goif [ "$0" == ${BASH_SOURCE[0]} ]; then<Esc>:AppendFileName<CR>| :n    ormal! j$a $@<Esc>>>ofi<Esc>


switch to command mode                                                              ESC or Ctrl-C
switch to insertion mode placing the cursor at the same location it was previously  gi 
position cursor at middle, top, or bottom of screen                                 zz, zt, zb 
select                                                                              v                                     
select row(s)                                                                       SHIFT + v                             
select blocks (columns)                                                             CTRL  + q                             
select contents of entire file                                                      ggVG                                  
print                                                                               :hardcopy                             
sort selected rows                                                                  :sort                                 
search for word under cursor                                                        *                                     
open file under cursor (absolute path or relative)                                  gf 
format selected code                                                                =                                     
convert tabs to spaces                                                              :retab                                
auto-complete a word you are typing **                                              CTRL + n                              
bookmark current place in file                                                      mX (X = key to assign bookmark to)    
jump to bookmark                                                                    `X (X = key bookmark was assigned to and ` = back tick/tilde key)          
show all bookmarks                                                                  :marks                                
delete a bookmark                                                                   delm X (X = key bookmark to delete)   
delete all bookmarks                                                                delm!                                 
increase number under cursor                    CTRL + a
decrease number under cursor                    CTRL + x

## Vim folding commands

creates a fold from the cursor down # lines                                         zf#j 
creates a fold from the cursor to string                                            zf/string 
moves the cursor to the next fold                                                   zj 
moves the cursor to the previous fold                                               zk 
opens a fold at the cursor                                                          zo 
opens all folds at the cursor                                                       zO 
increases the foldlevel by one                                                      zm 
closes all open folds                                                               zM 
decreases the foldlevel by one                                                      zr 
decreases the foldlevel to zero (all folds will be open)                            zR 
deletes the fold at the cursor                                                      zd 
deletes all folds                                                                   zE 
move to start of open fold                                                          [z 
move to end of open fold                                                            ]z 


## Surround Commands

Note that the repeat command (`.`) works with `ds`, `cs` and `yss` if you have "repeat.vim" installed.

surround current line with `````     yss`

surround the next word with `"`   ysw" 

surround ... ySs}
There is also *yS* and *ySS* which indent the surrounded text and place it
on a line of its own.

surround the next 3 word under cursor with ()  ys3w)

surround the word under cursor with (  ) (notice the extra spaces) ysiw(

change surrounding ` to '     cs`'

delete surrounding () (without deleting surrounded text)                    ds( or ds)

delete a {...}, (...), [...] or "..." block (both surrounding symbols and surrounded text are deleted)     da{ da( da[ da"

change a {...}, (...), [...] or "..." block (both surrounding symbols and surrounded text will be changed)    ca{ ca( ca[ ca"

change text in a {...}, (...), [...] or "..." block (only surrounded text will be changed)    ca{ ca( ca[ ca"

## Upper/Lower Cases

convert selected text to uppercase                                                  U                                     
convert selected text to lowercase                                                  u                                     
convert the character after cursor to uppercase                                     gUl
convert current line to uppercase                                                   gUU or ^gU$
convert current line to lowercase                                                   guu or ^gu$
convert current line and following 3 lines to uppercase                                                   gU3j
convert current line and following 3 lines to lowercase                                                   gu3j
convert next word to uppercase                                                   gUW
convert next word to lowercase                                                   guW
title words (i.e., Capitalize the first letter of words)                         record gUlw as macro and apply it
invert case of selected text                                                        ~                                     

## Split Windows

split screen horizontally                                                           :split <file> or :sp <file>                               
split screen vertically                                                             :vsplit <file> or :vsp <file>                               
move down a screen in split mode                                                    :wincmd j or CTRL + w + j 
move up a screen in split mode                                                      :wincmd k or CRTL + w + k 
move left a screen in split mode                                                    :wincmd h or CRTL + w + h 
move right a screen in split mode                                                   :wincmd l or CRTL + w + l 
close all other split screens                                                       :only                                 

## Macro

start recording a macro to `x`                                                             qx (x = key to assign macro to)       
stop recording a macro                                                              q                                       
playback macro                                                                      @X (X = key macro was assigned to)    
replay previously played macro *                                                    @@                                    

## Indention and Unindention

indent selected text                                                                >                                     
unindent selected text                                                              <                                     
indent # rows                                                                       #>> (where # is a number)                                    
unindent # rows                                                                     #<< (where # is a number)                                    

## Buffers

list buffers                                                                        :ls                                   
open buffer                                                                         :bN (N = buffer number)               
close a buffer when multiple ones are open.                                         :bw (:x close all opened buffers)
open a file/buffer                                                                         :e file_path
open last file                                                                      :e #

## Spell Check

move the cursor to the next misspelled word                                         ]s
move the cursor back through the buffer to previous misspelled words                [s
suggest a list of alternatives for the word under cursor                            z=
add the word under cursor to dictionary                                             zg
undo adding word to dictionary                                                      zug
mark the word under cursor as incorrect                                             zw

## Block and Mark

1. After operating (copy/yank, idention, etc.) on a block (via marks),
    the cursor goes to the begin of the block.
    This is not covenient if the cursor was at the end of the block 
    and you want to continue work at the end of the block.
    You can go back to the previous location of cursor by `''` or ``````.

[VAM repository](http://vam.mawercer.de/)

[tComment](https://github.com/tomtom/tcomment_vim)

## tComment

Most of the time the default toggle keys will do what you want (or to be 
more precise: what I think you want it to do ;-).

                                                    *tcomment-operator*
As operator (the prefix can be customized via |g:tcommentMapLeaderOp1| 
and |g:tcommentMapLeaderOp2|):

    gc{motion}   :: Toggle comments (for small comments within one line 
                    the &filetype_inline style will be used, if 
                    defined)
    gc<Count>c{motion} :: Toggle comment text with count argument 
                    (see |tcomment#Comment()|)
    gcc          :: Toggle comment for the current line

Explicit commenting/uncommenting:

    g<{motion}   :: Uncomment region
    g<c          :: Uncomment the current line
    g<b          :: Uncomment the current region as block

    g>{motion}   :: Comment region
    g>c          :: Comment the current line
    g>b          :: Comment the current region as block

In visual mode:

    gc           :: Toggle comments
    g>           :: Comment selected text

CAVEAT: If you visually select text within a line, the visual mode map will 
comment out the selected text. If you selected text across several lines, the 
visual mode map will assume though that you wanted to comment out lines -- 
since this is how many vim maps work. In order to make tcomment use e.g. inline 
comments anyway, use the <c-_>i map -- see below.

By default the cursor stays put. If you want the cursor to the end of 
the commented text, set |g:tcommentOpModeExtra| to '>' (but this may not 
work properly with exclusive motions).

Primary key maps for normal and insert mode:

    <c-_><c-_>   :: :TComment
    <c-_><space> :: :TComment <QUERY COMMENT-BEGIN ?COMMENT-END>
    <c-_>b       :: :TCommentBlock
                    In insert mode, the cursor will be positioned inside 
                    the comment. In normal mode, the cursor will stay 
                    put.
    <c-_>a       :: :TCommentAs <QUERY COMMENT TYPE>
    <c-_>n       :: :TCommentAs &filetype <QUERY COUNT>
    <c-_>s       :: :TCommentAs &filetype_<QUERY COMMENT SUBTYPE>
    <c-_>i       :: :TCommentInline (in normal and insert mode, this map will 
                    create an empty inline comment, which isn't suitable for 
                    all filetypes though)
                    In insert mode, the cursor will be positioned inside 
                    the comment. In normal mode, the cursor will stay 
                    put.
    <c-_>r       :: :TCommentRight
    <c-_>p       :: Comment the current inner paragraph
    <c-_><Count> :: Set the count argument (a number from 1 to 9) for use with 
                    the subsequent tcomment map/command (see 
                    |tcomment#Comment()|)
                    E.g. in JavaScript, in order to get an empty /** */ 
                    comment for documentation purposes, in insert mode type 
                    <c-_>2<c-_>i
                    In order to get an empty block comment like >
                      /**
                       *
                       */
<                   type <c-_>2<c-_>b

Most of the above maps are also available in visual mode.

A secondary set of key maps is defined for normal and insert mode:

    <Leader>__       :: :TComment
    <Leader>_p       :: Comment the current inner paragraph
    <Leader>_<space> :: :TComment <QUERY COMMENT-BEGIN ?COMMENT-END>
    <Leader>_i       :: :TCommentInline
    <Leader>_r       :: :TCommentRight
    <Leader>_b       :: :TCommentBlock
    <Leader>_a       :: :TCommentAs <QUERY COMMENT TYPE>
    <Leader>_n       :: :TCommentAs &filetype <QUERY COUNT>
    <Leader>_s       :: :TCommentAs &filetype_<QUERY COMMENT SUBTYPE>

... and for select mode:

    <Leader>__       :: :TComment
    <Leader>_i       :: :TCommentInline

## Visual Mode

Capital V selects the current line in one key stroke; two, if you include the "shift" in shift+v.

## References

- [Vim Awesome](https://vimawesome.com/)

- [Learn Vim Progressively](http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)  
- [100 Vim Commands](http://www.catswhocode.com/blog/100-vim-commands-every-programmer-should-know)
- [Vim Tutorial](http://www.yolinux.com/TUTORIALS/LinuxTutorialAdvanced_vi.html)
- [Vim Macro Example](http://www.thegeekstuff.com/2009/01/vi-and-vim-macro-tutorial-how-to-record-and-play/)
- [Vim Substitution](http://vim.wikia.com/wiki/Search_and_replace)
- [Vivify](http://bytefluent.com/vivify/)
- [Linux vi and vim editor: Tutorial and advanced features](http://www.yolinux.com/TUTORIALS/LinuxTutorialAdvanced_vi.html)
- [Shifting Blocks Visually](http://vim.wikia.com/wiki/VimTip224)


https://github.com/tpope/vim-surround/blob/master/doc/surround.txt

http://vimgolf.com/

http://www.drbunsen.org/vim-croquet/

[Graphical vi-vim Cheat Sheet and Tutorial - ViEmu] (http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html)

