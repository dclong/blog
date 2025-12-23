Status: published
Date: 2025-12-22 15:29:11
Modified: 2025-12-22 23:59:49
Author: Benjamin Du
Slug: environment-variables-and-secure-path-for-sudo
Title: Environment Variables and Secure Path for sudo
Category: Computer Science
Tags: Computer Science, programming, sudo, environment, variable, PATH, secure path, env

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

    sudo -E command_to_run

    sudo $(which command_to_run)

    sudo env "PATH=$PATH" nvim

The "correct" way is to update the secure path using the commanding `sudo visudo`.

For more discussions,
please refer to
[Chat with Gemini - sudo nvim Not Found, Fixes](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221eecorE7tx_iICYiZGqR4veuaXD_AmzHL%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## References 

- [Proxy for sudo]( https://www.legendu.net/en/blog/proxy-for-sudo ) 

