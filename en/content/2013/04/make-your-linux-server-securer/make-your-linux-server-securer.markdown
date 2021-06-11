UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Make Your Linux Server Securer
Date: 2020-10-16 11:02:36
Tags: security, Linux, server
Category: OS
Slug: make-your-linux-server-securer
Author: Ben Chuanlong Du
Modified: 2020-10-16 11:02:36


3. Define host access rules in `/etc/hosts.allow` and `/etc/hosts.deny`. 
    Usually I only allow login to my private server from my home and work ip. 
    If I have to login into my private server from some other network, 
    I login to a computer at my workplace, 
    login into my private server from the computer at my workplace,
    editing the access rules on my private server,
    and then login into my private server from the new network directly. 

1. Disable root SSH login (edit the file `/etc/ssh/sshd_config`).
    With root SSH login disabled, 
    a hacker has to guess both your login name and password,
    which is much harder than guessing the password alone.

2. Use a non-default port for the SSH server (edit the file `/etc/ssh/sshd_config`).
    With a non-default port set up,
    a hacker has to also guess the port number,
    which makes the brute-forth break-in even harder.
    You can use the command `sudo nmap -sS -O 127.0.0.1` to scan open ports.

4. Use the package `fail2ban` to automatically ban ips which attemps to break into your server by brute-forth. 

