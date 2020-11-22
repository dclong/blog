Status: published
Date: 2020-11-21 22:30:14
Author: Benjamin Du
Slug: proxychains-ng-issues-on-mac
Title: Proxychains-Ng Issues on Mac
Category: Software
Tags: Software, ProxyChains, ProxyChains-ng, issue, macOS, SIP, System Integration Protection

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

ProxyChains-ng does not work on macOS 
due to System Integration Protection (SIP).
There are basically 3 ways to fix/avoid it. 

1. The issue only happens if you execute a system binary using proxychains, 
    e.g. `proxychains4 ssh user@server`.
    For now, 
    a workaround is to copy the executable to another location 
    (e.g. `cp /usr/bin/ssh ~/.local/bin/`), 
    and use it (e.g. `proxychains4 ~/.local/bin/ssh user@server`). 
    You can modify the path variable so that `~/.local/bin/ssh` is executed 
    instead of `/usr/bin/ssh`, 
    when you just type `ssh`.

1. Disable SIP (which is not recommended generally speaking).
    Please refer to
    [How to turn off System Integrity Protection on your Mac](https://www.imore.com/how-turn-system-integrity-protection-macos)
    for instructions.

2. Use ProxyChains/ProxyChains-ng in a Linux Docker container on Mac.
    For example, 
    [dclong/jupyterhub-ds](https://github.com/dclong/docker-jupyterhub-ds)
    is a Ubuntu-based Docker image with ProxyChains4 (i.e., ProxyChains-ng) installed.

For more discussions,
please refer to
[Not working on OS X 10.11 due to SIP](https://github.com/rofl0r/proxychains-ng/issues/78)
.

## References

https://github.com/rofl0r/proxychains-ng/issues/78
