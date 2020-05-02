UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-06-14 18:44:56
Author: Ben Chuanlong Du
Slug: sas enterprise guide tips
Title: SAS Enterprise Guide Tips
Category: Computer Science
Tags: programming, SAS, SAS Enterprise Guide, GUI, SEG

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

0. You can open multiple SAS Enterprise Guide instances.
This allows you to work on another project if your SAS code takes a long time to run.

1. You can set the workplace layout to be "side by side" or "stacked".
This makes things convenient as you can see both your code and the execuation results at the same time.


1. "Selected Server: ..."

2. "Profile" at right bottom corner

3. CTRL +SHIFT + s WITH/WITHOUT SHIFT
save/save as

4. select then tab or shift + tab >> <<

1. SAS Enterprise Guide does not auto load changed code 
if it is updated in another place/editor.
You have to close the file and reopen it to get the updated version. 

2. show line number 
Menu -> Program -> Editor Options... -> General Tab -> check "Show line numbers"

## Shotcurts
Convert case
Convert selected text to upper case: Ctrl + Shift + U
Convert selected text to lower case: Ctrl + Shift + L

Quick commenting
Wrap selection (or current line) in a comment: Ctrl + /
Unwrap selection (or current line) from a comment: Ctrl + Shift + /

Hyperjump to a line
Go to line: Ctrl + G (prompts for a line number)
Be sure to turn on Show line numbers in Program->Editor Options, or you'll be navigating blind!

Jump to the "end of scope"
Move caret to matching parenthesis/brace: Ctrl + [, Ctrl + ]
Move caret to matching DO/END keyword: Alt + [, Alt + ]

There are dozens of other shortcut keys and commands available in the program editor. In SAS Enterprise Guide, you can view them all by selecting Program->Enhanced Editor Keys. From this window you can customize the keypress behaviors to your liking, and you can also combine commands and assign them to new keys. If you're a "keyboard person", then you'll want to visit this window and explore. Be sure to click "Include commands without key assignments" to see the full list of available commands.
