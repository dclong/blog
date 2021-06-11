UUID: 7e7ffd4d-69ad-4127-83da-06b4c0e3d721
Status: published
Date: 2017-04-22 22:09:13
Author: Ben Chuanlong Du
Slug: sharing-files-between-linux-and-ipad
Title: Sharing Files Between Linux and iPad
Category: Software
Tags: Software, Linux, iPad, Apple, Mac
Modified: 2017-04-22 22:09:13

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Synchronization Software

Install a sycnhronization software on both your computer and iPad.

## Connecting Using USB

Install libimobiledevice-utils and ifuse on your Linux computer.
```bash
sudo apt-get install libimobiledevice-utils ifuse
```
And then run the following commands to pair your iPad.
```bash
idevicepair unpair 
idevicepair pair
```

## Using a File Server

Download a file manager app from the App Store with sharing functionality.
For example:

- Filemanager App has wifi web server functionality
- FileBrowser App handles the samba protocol

## VLC

If you just want to sharing video/audio between you computer and iPad, 
you can install the VLC app on you iPad.
VLC supports sharing via wifi. 
Just type in the VLC web URL in your browser on your computer, 
you will be able to upload/download video/audio files to/from your iPad.

You can also stream media from your computer to iPad using VLC if you like.

[How to Stream Videos and Music Over the Network Using VLC](https://www.howtogeek.com/118075/how-to-stream-videos-and-music-over-the-network-using-vlc/)
