UUID: 714cb0b0-3623-478f-91a5-d67b00f92527
Status: published
Date: 2017-04-10 19:05:41
Author: Ben Chuanlong Du
Slug: add-a-user-to-the-sudo-group-on-linux
Title: Add Users to a Group in Linux
Category: OS
Tags: Linux, sudo, user, groups, gpasswd, usermod
Modified: 2017-04-10 19:05:41

There are several ways to add users to a group in Linux. 
The following uses the `sudo` group as illustration.

1. `gpasswd`, `usermod` and `adduser` can all be used to add a user to a given group.
    However, it is suggested that you use `gpasswd` as it is more portable and intuitive. 

        gpasswd -a user_name sudo
        newgrp sudo

        usermod -aG sudo user_name
        newgrp sudo

        # works on Ubuntu but not CentOS
        adduser user_name sudo
        newgrp sudo

    Just adding an user to a group might not make it work right away.
    The command `newgrp sudo` make the group `sudo` in effect right away.
    Of course, you can log out and then log in to make it work.

3. Some desktop environment (e.g., GNome, Cinnamon, KDE, etc.) can also do this for you. 
    Taking Cinnamon as an example, 
    you can follow the steps below to add/remove groups for a user. 

    1. Open `System Settings`.

    2. Click `Users and Groups`.

    3. Select the user you want modify.

    3. Click on `Groups`.

    4. Check/uncheck groups from the prompt list.

    5. Click the OK to save the changes.
