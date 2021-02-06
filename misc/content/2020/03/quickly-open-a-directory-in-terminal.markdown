Status: published
Date: 2020-03-11 16:25:01
Author: Benjamin Du
Slug: quickly-open-a-directory-in-terminal
Title: Quickly Open a Directory in Terminal in Mac
Category: Computer Science
Tags: Computer Science, macOS, OpenInTerminal, terminal, Hyper, iTerm

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


[OpenInTerminal](https://github.com/Ji4n1ng/OpenInTerminal)
is a `Finder Toolbar` app for macOS 
to open the current or selected directory in Terminal, iTerm, Hyper or Alacritty.

## Installation and Configuration

1. Install OpenInTerminal

        :::bash
        brew cask install openinterminal

2. Launch OpenInTerminal from Applications.

3. An icon (looks like a terminal) will show up in the top bar. 
    Click on it and chose "Open in terminal". 
    A prompt will show up to ask you 
    to select the default terminal application (Terminal, iTerm, Hyper, etc.)
    to use to open directories.

4. Once you've selected the default terminal application (to open directories), 
    a prompt from Mac Security might show up 
    to ask you whether to grant permission to the terminal application that you chose
    (if it hasn't been granted permission before). 
    Please grant access to the terminal application.

5. Enable Finder Extension permission 
    by going to System Preferences -> Extensions -> Finder Extensions 
    and then checking the permission button.
    ![Finder Extension Permission](https://user-images.githubusercontent.com/824507/97831360-9ff7a580-1c84-11eb-80df-8ae2ddb3ee6d.png)