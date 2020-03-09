Status: published
Date: 2020-03-09 12:03:40
Author: Benjamin Du
Slug: get-coordinates-of-points-on-a-screen-or-image
Title: Get Coordinates of Points on a Screen or Image
Category: Software
Tags: Software, coordinate, point, macOS, GIMP, image, screen

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Get the Coordinate of a Pixle/Point on an Image

Most image editing software (e.g., [GIMP](https://www.gimp.org/)) can tell you the coordinate of a point on an image. 

## Get the Coordinate of a Pixle/Point on the Screen in macOS

`Shift + Command + 4` shows the coordinate of the current position of the mouse point. 
Notice that the coordinate shown by `Shift + Command + 4` 
need to be **multiplied by 2** 
if you use Python packages (Pillow, pyscreenshot, etc.) to take screenshots.

