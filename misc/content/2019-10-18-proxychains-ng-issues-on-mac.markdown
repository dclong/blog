Status: published
Date: 2019-11-28 10:28:33
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
There are basically 2 ways to fix/avoid it. 

1. Disable SIP (which is not recommended generally speaking).
    Please refer to
    [How to turn off System Integrity Protection on your Mac](https://www.imore.com/how-turn-system-integrity-protection-macos)
    for instructions.

2. Use ProxyChains/ProxyChains-ng in a Linux Docker container on Mac.
    For example, 
    [dclong/jupyterhub-ds](https://github.com/dclong/docker-jupyterhub-ds)
    is a Ubuntu-based Docker image with ProxyChains4 (i.e., ProxyChains-ng) installed.

## References

https://github.com/rofl0r/proxychains-ng/issues/78
