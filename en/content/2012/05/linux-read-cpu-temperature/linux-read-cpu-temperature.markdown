Status: published
Title: Read CPU Temperature in Linux
Date: 2012-05-17 11:24:31
Tags: modprobe, sensors, CPU, Linux, temperature
Category: OS
Slug: linux-read-cpu-temperature
Author: Ben Chuanlong Du
Modified: 2020-02-17 11:24:31

<img src="http://dclong.github.io/media/computer/hot.jpg" height="200" width="240" align="right"/>

First you have to install package "lm-sensors". 

    :::bash
    wajig install lm-sensors

To detect the cpu temperature, type the following command.

    :::bash
    modprobe coretemp
    sensors

For more instructions on this top, 
see [nixCraft](http://www.cyberciti.biz/faq/howto-linux-get-sensors-information/).
