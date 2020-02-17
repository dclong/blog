Status: published
Date: 2020-02-17 13:13:30
Author: Benjamin Du
Slug: use-the-watch-command-to-monitor-running-applications
Title: Use the Watch Command to Monitor Running Applications
Category: Programming
Tags: programming, Shell, Linux, watch, monitor

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Report the number of PNG images in the directory `000` every 2 seconds.

    :::bash
    watch "ls 000/*.png | wc -l"
