UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-02-20 10:59:38
Slug: dual-monitor-for-linux-desktop
Author: Ben Chuanlong Du
Title: Dual Monitor for Linux Desktop
Category: OS
Tags: DE, Linux, monitor, dual
Modified: 2015-02-20 10:59:38


1. Type `xrandr` or `xrandr -q` in terminal to dispaly information of all available output device.
Then you can use the following commands to set dual display.

        xrandr --output VGA1 --auto 
        xrandr --output VGA1 --same-as LVDS1 --auto
        xrandr --output VGA1 --mode 1024x800
        xrandr --output VGA1 --off

where `VGA1` and `LVDS1` should be replaced by with appropriate device names. 

10. When use multi-monitors in Linux, 
you need to have close resolutions in order for same (mirorr) display to work well.
