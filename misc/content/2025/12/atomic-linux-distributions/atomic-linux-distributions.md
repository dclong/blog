Status: published
Date: 2025-12-07 13:27:17
Modified: 2025-12-22 11:25:19
Author: Benjamin Du
Slug: atomic-linux-distributions
Title: Atomic Linux Distributions
Category: Computer Science
Tags: Computer Science, programming, Linux, atomic, Fedora Kinoite, Universal Blue, Aurora

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Atomic Linux distributions (often called "immutable" distros) 
are a modern breed of operating system designed to be 
more reliable, secure, and maintainable than traditional Linux distributions.
See 
[chat with Gemini](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221Fp4BfzFT25qVSs5KM6opO5tcpO8-oyfY%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## Some Good Atomic Linux Distributions

- [Universal Blue]( https://www.legendu.net/misc/blog/universal-blue-images-for-atomic-linux-distributions )
    - recommended 
    - based on Fedora Atomic distributions
- [Fedora Atomic](https://www.fedoraproject.org/atomic-desktops/)
    - personally prefer Fedora Kinoite
- [AerynOS](https://aerynos.dev/users/desktops/cosmic/)

## Package Managements for Atomic Linux Distributions

See 
[chat with Gemini](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221hUaLtZQXDzQeZwfjTkeBJzBWh0_DWpQk%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

1. Core OS
    - Fedora Atomic: rpm-ostree
    - AerynOS: moss
2. GUI applications 
    - flatpak 
    - snap
    - Distrobox / Toolbx
        - GUI applications might fail to launch
    - Virtual Machine Manager
        - based on KVM, great performance
        - the ultimate (but heavy) solution 
3. CLI utilities
    - Homebrew
    - [Distrobox / Toolbx](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221G2PCEp2tK5VUzgmEp70m2oHfkTysj1Q6%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
4. Dev environment
    - Podman
    - Docker
