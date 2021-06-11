Status: published
Title: Use Git Behind a Proxy
Author: Chuanlong (Ben) Du
Date: 2014-07-07 23:42:48
Slug: use-git-behind-a-proxy
Category: Software
Tags: software, Git, proxy, protocol
Modified: 2019-03-07 23:42:48

Here is a good article on [Git Behind a Proxy or Firewall](http://www.librebyte.net/en/git/git-behind-a-proxy-or-firewall/).

1. If you do not already know the proxy in use (in your office), 
    read the post [Find out Proxy in Use](http://www.legendu.net/en/blog/find-out-proxy-in-use/)
    to figure the proxy (in your office).

1. Run the following commands in terminal or Windows command prompt to configure Git.

        git config --global http.proxy http://username:password@proxy_ip:port
        git config --global https.proxy https://username:password@proxy_ip:port

    Or you can directly add the following lines into your Git configuration file,
    which is usually `~/.gitconfig`.

        [http]
            proxy = http://username:password@proxy_ip:port
        [https]
            proxy = http://username:password@proxy_ip:port

2. The Git protocol is usually not supported in office.
    In this case,
    you have to use the https protocols.
    When using the https protocols,
    you will be prompted for password every time you pull from a private repository 
    or push to a repository,
    which is annoying.
    To make this less painful,
    you can define shortcuts/hotstrings to auto fill passwords for you using AutoHotkey/AutoKey.
    This is not very secure,
    but I do not worry too much about it as the password is saved on the office laptop only
    and is unlikely to be exposed to other people.
    There are other solutions to cache Git passwords on Windows,
    but I will not go into the hassle.

3. If you come across the error of "SSL certificate problem: unable to get local issuer certificate",
    you have to run the following command.

        git config --global http.sslVerify false
        git config --global https.sslVerify false

    Or you can add
    
        sslVerify = false

    to the [http] and [https] section in the git configuration directly.

Note that working in a Linux virtual machine on your office laptop with Windows OS
can possibly help you circumvent the proxy issue.

## Question

Can a socks proxy be used as a HTTP/HTTPS proxy for Git?