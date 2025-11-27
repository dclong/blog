Status: published
Date: 2025-11-27 01:05:39
Modified: 2025-11-27 01:05:39
Author: Benjamin Du
Slug: enable-and-disable-key-repeating-in-macos
Title: Enable and Disable Key Repeating in macOS
Category: Computer Science
Tags: Computer Science, programming, macOS, Apple, keyboard, key, repeating

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Run the following command in terminal and then **restart your Mac** to enable key repeating by pressing and holding.

        :::bash
        defaults write -g ApplePressAndHoldEnabled -bool false

2. Run the following command in terminal and then **restart your Mac** to disable key repeating by presing and holding.

        :::bash
        defaults write -g ApplePressAndHoldEnabled -bool true

For more details please refer to
[How to Enable Key Repeating in macOS](https://www.howtogeek.com/267463/how-to-enable-key-repeating-in-macos/)
.
