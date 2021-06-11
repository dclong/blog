Status: published
Date: 2019-05-11 01:05:59
Author: Ben Chuanlong Du
Slug: tips-for-installing-debian
Title: Tips on Installing Debian Series Linux Distributions
Category: OS
Tags: install, Linux, software, Debian
Modified: 2019-05-11 01:05:59


## Before Installation

1. You can either create a boot CD/DVD or flash drive to install debian.
    The way I prefer is to instal debian using a bootable flash drive 
    because many laptops do not have CD/DVD trays. 
    To write a debian image to flash drive, you can use the following command.

        dd if=path_to_debian_image of=path_of_device bs=4M; sync

    Or can you also use

        cat path_to_debian_image > path_of_device

    where path of device is the path of the flash drive. 
    Note that you must use the whole device (e.g., /dev/sdb) not just a partition (e.g., /dev/sdb1),
    otherwise the flash drive is not bootable.
    You have to aware that both the 2 commands above are dangerous 
    as they can destory data on the device,
    so you'd better be sure about what you are doing. 
    For more information, see <http://www.debian.org/CD/faq/#write-usb>.
    (The two simple ways for creating bootable falsh drives also applies to many other Linux distributions.)
    It requires that the ISO image is hybrid. 
    If not, 
    you can use the following command to make it hybird if it uses isolinux/syslinux technology.

        isohybrid path_to_linux_image

    And then you can use either `dd` or `cat` to the write the image into a device.

1. You'd better have ethernet connection. 
    The wireless support for Linux is still not perfect.
    Depending on the brand of your laptop, 
    you might need to connect to internet through ethernet network during installation.
    What's more, 
    the ethernet network is faster than a wireless network. 
    So it is suggested that you alway use a ethernet network connection while installing debian.

2. Make sure the power of your laptop is plugged in. 

## During Installation

2. It is recommended that you use the text installation. 
    The text installation of Debian actually is pretty intuitive and easy to follow.
    The graphical installation of Debian did not work on any of my laptops.
    I am not sure whether the problem has been fixed or not, 
    but it does not hurt to use the text installation. 

3. Since Debian can keep data in the home directory during installation,
    it is suggested that you do not use a separate home directory. 
    Following this suggestion, 
    you have to set the mount point of the disk to install debian as `/` (root directory). 
    You also have to use a swap partition. 
    The size of the swap parition is controversial, 
    generally speaking it should be 1 to 2 times the memory of the computer.
    I often set the size of the swap partition to be 1.5 times the memory of the computer. 

3. If your network is not very fast, 
    you can choose not to use network mirrors especially 
    when your installation image is update to date. 

4. If you do not like the default desktop enviroment of Debian (currently Gnome),
    you can deselect the desktop environment during installation. 
    This also makes the installation faster.
    You can install a desktop enviroment you like manually after installtion of Debian. 

## After Installation

1. The first thing to do after installtion is 
    to edit the APT (advance package tool) configuration file `/etc/apt/sources.list`. 
    By default, debian uses the installing media as a repository after installation.
    However, the media is usually removed and thus unavailable after installation.
    So, you probably want to delete or comment out the repository using the installing media.
    Also, if you did not use a network mirror duing installation, 
    you have to add a debian repository into the APT configuration file manually.
    For example, you can add the following lines into the APT configuration file.

        deb http://ftp.us.debian.org/debian/ wheezy main contrib non-free
        deb http://ftp.us.debian.org/debian/ wheezy main contrib non-free

    It is suggested that you include `contrib` and `non-free` in the repository.
    This ensures that you can also use many non-open source but cost-free softwares.  

2. The second thing to do after installation of Debian is 
    to install the `sudo` package and configure it.
    You have to switch to root to install packages.
    To switch to root, type in `su` (super user) in the terminal. 
    You will be asked for the password of root.
    After authentication, you are in root user. 
    Notice that the prompt character is `#` (instead of `$`) for the root user. 
    You can type `apt-get install sudo` in the terminal (as root) to install the package `sudo`.
    After installation of `sudo`,
    you have to add your user name to the `sudo` group. 
    To do this, 
    run the following command as root.

        adduser your_user_name sudo

    However, 
    this will not take effect immediately. 
    To notify the change (of group permission) to the system, 
    you can run the following command as root.

        newgrp sudo

    If this does not work, 
    you can manually log out and then log in
    and the change of group permissions will take effect.
    Now you are in the `sudo` group, 
    you can use `sudo` (instead of the root user) to run commands
    that need root permission.
    You can now exit the root terminal (by running `exit`) 
    if you are still in the root terminal.

3. The third thing to do after installation of Debian is to install the `wajig` package.
    To do this, 
    type `sudo apt-get install wajig` in the terminal (as your own user).
    You will be prompt for your user password to install the package. 
    Surely, 
    you can install the `wajig` package together with the `sudo` package in the second step. 
    To do this, 
    you can run command `apt-get install sudo wajig` as root. 
    However, it is suggested that you avoid use th root user as much as possible. 

4. The last step is to install and configure other necessary packages.
    Now you have `sudo` and `wajig` installed, 
    you can use `wajig` to manage packages,
    and you should use `sudo` instead of the root user to operations need root permissions.
    For example, 
    to install other packages such as `vim` and `eclipse`, 
    you can type `wajig install vim eclipse` in the terminal (as your own user).
    You will be prompt for your user password to continue. 
    Notice that `wajig` is a little special command, 
    it automatically uses `sudo` to install packages when necessary. 
    For other operations that need root permission, 
    you have to use `sudo` before the command. 
    For example, if you use `apt-get` to install packages `vim` and `eclipse`,
    you must use `sudo apt-get install vim eclipse` manually.
    However, in practice I avoid using `sudo` as much as possible. 
    I often use a command first without prefixing it with `sudo`, 
    if it fails because of permission, 
    I then use command `sudo !!` to run it using `sudo` quickly.
    Generally speaking, this is safer than abusing `sudo`. 

## Wireless

1. You might have to install wireless dirvers manually 
    depending on the type of wireless card in your computer. 
    You can use the following command to check the type of the wireless card in your computer.

        lspci | grep -i wireless

    Then you can search for the driver/package that support your wireless card. 
    For example, the result of the above command on my laptop is:

        06:00.0 Network controller: Intel Corporation PRO/Wireless 5100 AGN [Shiloh] Network Connection

    This wireless card is supported by iwlwifi. 
    If you have included non-free softwares in your debian repository 
    (see the first step after installation),
    you can type `wajig install firmware-iwlwifi` in terminal to install it. 

2. If you have installed a desktop environment, 
    you usually have a network manager to manager the wireless interface. 
    In this case, 
    it is strongly suggested that 
    you comment everything out in the (or use an empty) configuration file `/etc/network/interface`.
    Otherwise, 
    you might not be able to use the wireless network 
    though the network manager shows that you have connected to it. 

## sshfs and fuse

1. If you want to be able to mount remove Linux filesystem on you computer, 
    you can install sshfs and fuse using the following command. 

        wajig install sshfs fuse

    It is suggested that you add you user name into the fuse group using the following command.

        sudo usermod -aG fuse user_name

    You have to restart your computer to make the action take effect. 

## Suggestions for Other Debian Series Linux Distributions

1. If you create a boot flash drive for Ubuntu in Windows using UNetbootin or other softwares, 
    then you'd better format the flash drive as `FAT` instead of `FAT32`. 
    Otherwise, 
    you might get the error information: "BOOTMGR is missing".


2. By default, LMDE installs 486 on 32 bit computers.
    If your computer has more than 1 cores/processors, 
    you can upgrade to 686-pae manually by running the following command in terminal
    and then reboot your computer.

        wajig install linux-image-3.0.0-1-686-pae
