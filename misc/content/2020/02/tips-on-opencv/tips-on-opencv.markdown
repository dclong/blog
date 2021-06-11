Status: published
Date: 2020-04-26 12:35:53
Author: Benjamin Du
Slug: tips-on-opencv
Title: Tips on OpenCV
Category: Computer Science
Tags: programming, OpenCV, tips, computer vision, CV
Modified: 2020-04-26 12:35:53

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation

You can install OpenCV for Python using the following commands.

    :::bash
    sudo apt-get install libsm6 libxrender-dev
    pip3 install opencv-python

If you have 
[xinstall](https://github.com/dclong/xinstall),
you can install OpenCV for Python with the following single command.

    :::bash
    sudo xinstall cv2 -ic

## Examples

[Extract Images from Video Using OpenCV in Python](http://www.legendu.net/misc/blog/python-opencv-video-to-image/)

## General Tips

1. `cv2.imread` returns a numpy ndarray in Python.
    This is different from `PIL.Image.Image.open` which returns a Pillow Image.
    `cv2.imread` can be more efficient if you want to manipulate the underlying data of image
    as you do not have to convert between the underlying data and image objects.

## References

https://opencv.org/

https://github.com/skvark/opencv-python

https://github.com/JimmyHHua/opencv_tutorials

https://github.com/ex2tron/OpenCV-Python-Tutorial
