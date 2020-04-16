UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Some Tips for Cygwin
Date: 2019-03-04 23:56:02
Slug: cygwin-tips
Category: Software
Tags: tips, software, Cygwin

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**

http://x.cygwin.com/docs/faq/cygwin-x-faq.html

1. There are some commands that you can use in Cygwin 
    but has no manual, i.e., `man some_cmd` does not return you a help documentation.
    These commands probably come with Windows rather than Cygwin.
    collect these kind of commands ...


1. Sometimes Cygwin doesn't seem to work, 
    cannot install new components behind a firewall,
    reinstall can often solve the problem

I can use http://mirrors.kernel.org for cygwin, 
not others, 
not sure this is due to proxy or apt-cyg


C:\cygwin\bin\mintty.exe -i /Cygwin-Terminal.ico -

## Python

8. `FuzzyWuzzy` and `NLTK` are available in Python3 not Python2 in Cygwin.  
    Check whether they are available from cygwinports ...


## [CygwinPortable](https://github.com/CybeSystems/CygwinPortable)

1. [CygwinPortable](https://github.com/CybeSystems/CygwinPortable) support multiple users.
    You can set a default user to be used at startup.

9. CygwinPortable does not work well in Win XP.

1. Right click on the title bar to pop up the menu and choose "Settings...".

3. To copy in Mintty/ConEmu, 
    press the `Shift` key and select the text to be copied. 
    To paste in the terminal in ConEmu, 
    just right click;
    to paste in Vim in ConEmu,
    use `Shift` + `Insert`.

7. Right click on a tab and select "Close tab" to close a tab. 
    Or you can use "Win + Alt + Delete" to close the current tab.

### Settings

5. In the settings dialog, 
    click on "Main" in the left panel to open the "Main" settings dialog. 
    In the group, 
    set "Font Charset" to "ANSI"
    (Note that each font belongs to a  charset. 
    To set the font, you must first choose a right charset.),
    Font to "Courier New", 
    "size" to 18 and check the "Bold" checkbox.

3. In the settings dialog,
    click on "TExt cursor" under "Features" to open the cursor dialog.
    In the "Active console Text Cursor" group, select the "Block" radio button,
    check the "Color" and "Blinking" checkboxes.

6. In the settings dialog, 
    click on "Colors" under "Features" to open the colors dialog.
    Set "Schemes" to "<Ubuntu>".
    Check the "Fae when inactive" checkbox.

## Misc
1. it seems that placing a Rconsole in your cygwin home confused R on windows, probably because cygwin exported environment variables ...

2. cygwin: -> LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
