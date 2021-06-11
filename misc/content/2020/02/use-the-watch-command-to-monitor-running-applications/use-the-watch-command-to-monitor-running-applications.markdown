Status: published
Date: 2020-02-17 13:13:30
Author: Benjamin Du
Slug: use-the-watch-command-to-monitor-running-applications
Title: Use the Watch Command to Monitor Running Applications
Category: Computer Science
Tags: programming, Shell, Linux, watch, monitor
Modified: 2020-02-17 13:13:30

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Report the number of PNG images in the directory `000` every 2 seconds.

    :::bash
    watch "ls 000/*.png | wc -l"
