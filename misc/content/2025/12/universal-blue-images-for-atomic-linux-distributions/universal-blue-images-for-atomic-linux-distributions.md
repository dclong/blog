Status: published
Date: 2025-12-07 17:20:04
Modified: 2025-12-16 16:13:21
Author: Benjamin Du
Slug: universal-blue-images-for-atomic-linux-distributions
Title: Universal Blue Images for Atomic Linux Distributions
Category: Computer Science
Tags: Computer Science, programming, Linux, Universal Blue, Aurora, Origami, Atomic, Fedora

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[Universal Blue](https://universal-blue.org/)
is a manufacturing process 
that focuses on community-driven sharing of best practices 
via automation to make awesome desktop and server operating systems (based on Fedora Atomic distributions).

## Good Images

- [Aurora](https://getaurora.dev/en)

- [Origami](https://origami.wf/)

## Universal Blue vs Fedora Atomic

1. Universal Blue Linux distributions are recommened.
    - Universal Blue Linux distributions have "batteries included".
        - provide ISO images with Nvidia drivers pre-installed
        - flatpak is ready to use out-of-the-box 
        - `ujust devmod` to switch to development mode
    - Universal Blue Linux distributions provide an exclusive tooling `ujust`
      which makes it easy to managing the operating system.
    - Universal Blue Linux distributions manage update automatically.

2. Generally speaking,
    you should NOT manually enable or use RPM Fusion on Universal Blue Linux distributions 
    (Bluefin, Bazzite, or Aurora).

For more discussions,
please refer to
[chat with Gemini](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221hqaNwYdRQnAUa7te-jk9ZLVN6py6th6o%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## Switch to the Fish Shell

## Install Docker

It is suggested that you switch to the development mode using the following command.

    ujust devmod
    
The development mode has lots of development tools (including Docker) installed.

## References

- [Install Dropbox Using Flatpak]( https://www.legendu.net/misc/blog/install-dropbox-using-flatpak )

- [Universal Blue - Forum](https://universal-blue.discourse.group/)

- [Doc Bluefin - Based on LLM](https://app.dosu.dev/e3630b91-3a35-46b9-a8d3-b0c1b3ef6331/ask)
