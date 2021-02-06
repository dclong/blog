UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Adjust Screen Brightness for Linux Desktops
Date: 2015-02-03 19:57:46
Slug: adjust-screen-brightness-for-linux-desktops
Author: Ben Chuanlong Du
Category: OS
Tags: screen, Linux, brightness

For many computers and laptops installed with Linux desktops, 
you can use shortcuts (usually Fn + Brightness_keys) to adjust screen brightness.
This does not work for some laptops. 
Another way to adjust screen brightness is to use the following command.

        sudo setpci -s 00:02.0 F4.B=brightness_value

The value is between 00 to ff. 
However, this is not a universal way either, 
i.e., it does not work on all laptops. 
As you see, 
you have to have root permission in order to run the command. 
Generally speaking,
you are not recommnend to use the latter way if the shortcuts works. 
