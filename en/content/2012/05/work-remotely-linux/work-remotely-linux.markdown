UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Working Remotely in Linux
Date: 2017-03-01 23:20:51
Slug: work-remotely-linux
Author: Ben Chuanlong Du
Category: OS
Tags: software, remote, Linux

## From Linux to Linux:

- Command Line Mode: `ssh`

    + Using X forwarding, you can also run GUI applications on the server.
	This is not recommended unless it's short quick work.

- Remote File System: `sshfs`

    + You'd better use a mount point which you have full access to,
	otherwise, you have use the root user to access the mount point. 

    + You'd better add yourself to the `fuse` (which is required by sshfs) group.

- Remote Desktop

    + NX (NoMachine)

    + VNC (e.g., vino or tight vnc, remmina)

    + Teamviewer

## From Linux to Windows:

- Remote Desktop:

    + Remmina

    + rdesktop

    + NoMachine

    + Teamviewer

- Remote File System: `smb`

    1. Open nautilus file manager and press `CTRL + L` to show the address field.

    2. Type in `smb://host_name/folder` in the address field and press enter.

    3. Type in your user name and password in the prompt to login. 

## From Windows to Linux:

- Comand Line Mode: `ssh` (e.g., Security Shell)
