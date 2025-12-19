Status: published
Date: 2025-12-07 17:20:04
Modified: 2025-12-19 19:33:48
Author: Benjamin Du
Slug: universal-blue-atomic-linux-distributions
Title: Universal Blue Atomic Linux Distributions
Category: Computer Science
Tags: Computer Science, programming, Linux, Universal Blue, Aurora, Origami, Atomic, Fedora

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[Universal Blue](https://universal-blue.org/)
is a manufacturing process 
that focuses on community-driven sharing of best practices 
via automation to make awesome desktop and server operating systems (based on Fedora Atomic distributions).

I've built a [Gemini App - Aurora Linux Assistant](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221X_u1z8lHjUZ3YytBLP4zwmVlmUoH_o9i%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
which makes it easy to learn and use Universal Blue Linux distributions.

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

Please see discussion in
[Change the Default Shell in Linux](https://misc.legendu.net/blog/change-the-default-shell-in-linux/)
.

## Install Docker

It is suggested that you switch to the development mode using the following command.

    ujust devmod
    
The development mode has lots of development tools (including Docker) installed.

## Update the Operating System

    ujust upgrade

## Configure Grub

1. You can use the command `ujust configure-grub`
  to configure

Do not edit `/etc/default/grub` to add kernel parameters (like nomodeset or nvidia-drm.modeset=1).
Changes there for kernel args will be ignored or overwritten.
Use `rpm-ostree kargs` instead.

1. Show kernel arguments.

        rpm-ostree kargs

2. Append kernel arguments.

      rpm-ostree kargs --append="your-argument-here"

## rpm-ostree

1. Homebrew, flatpaks and containers are preferred to rpm-ostree.
    Use rpm-ostree only when absolutely necessary.


### Check System Status

See which deployment you are booted into, which one is pending, and what packages you have layered.

    rpm-ostree status

### Update the System

This downloads the latest base image updates and keeps your layered packages on top.

    rpm-ostree upgrade  # ujust upgrade is preferred for Universal Blue

### Search for a Package

    rpm-ostree search <query>

### Install a Package (Layering)

To install a package directly into the OS (e.g., zsh or neovim):

    rpm-ostree install <package_name>

### Apply Changes Live (Experimental but useful)

If you don't want to reboot immediately, you can try to apply changes to the live filesystem. This works for many packages but not all (e.g., not kernels).
rpm-ostree rollback

    rpm-ostree install --apply-live <package_name>

### Remove a Package

    rpm-ostree uninstall <package_name>

### Rollback to the Previous Version

    rpm-ostree rollback

### Pinning a Deployment

If you have a perfectly working system state and want to save it so it never gets deleted by future updates,

    rpm-ostree admin pin 0

### Replacing Base Packages

Sometimes you need to replace a package that comes with the base OS (e.g., swapping a driver).

    rpm-ostree override replace <path_to_rpm>

Or to reset a package to the default version provided by the OS image:

    rpm-ostree override reset <package_name>

### Deploy a Commit

    rpm-ostree deploy <digest_id>

## References

- [Gemini App - Aurora Linux Assistant](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221X_u1z8lHjUZ3YytBLP4zwmVlmUoH_o9i%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

- [Install Dropbox Using Flatpak]( https://www.legendu.net/misc/blog/install-dropbox-using-flatpak )

- [Universal Blue - Forum](https://universal-blue.discourse.group/)

- [Doc Bluefin - Based on LLM](https://app.dosu.dev/e3630b91-3a35-46b9-a8d3-b0c1b3ef6331/ask)
