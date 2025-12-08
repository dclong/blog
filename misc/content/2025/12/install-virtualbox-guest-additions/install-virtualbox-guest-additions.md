Status: published
Date: 2025-12-07 18:39:38
Modified: 2025-12-07 18:39:38
Author: Benjamin Du
Slug: install-virtualbox-guest-additions
Title: Install VirtualBox Guest Additions
Category: Computer Science
Tags: Computer Science, programming, VirtualBox, Guest, Additions, atomic, rpm, ostree

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Atomic Linux Distributions

### Fedora Atomic Linux Distributions

Open your terminal and run the following command to layer the package.
```
rpm-ostree install virtualbox-guest-additions
```

If you receive an error stating the package is "already provided" or part of the base image, 
run this command instead to explicitly enable it.
```
rpm-ostree install --allow-inactive virtualbox-guest-additions
```
See more details at
[chat with Gemini](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221ScgkgBOJw9XehhzPiM6VBZJCUIxepuWv%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## Traditional Mutable Linux Distributions

1. Devices -> Insert Guest Additions CD. 

2. Run the corresponding executable.
