Status: published
Date: 2020-04-26 12:07:50
Author: Benjamin Du
Slug: tips-on-pillow
Title: Tips on Pillow
Category: Computer Science
Tags: programming, Pillow, image, mask
Modified: 2020-04-26 12:07:50

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## PIL.Image.Image.crop

Notice that the bounding box is inclusive/EXCLUSIVE like the `range` function.

## PIL.Image.Image.resize

1. `img.resize(img.size)` returns a new copy and the new copy is not necessarily the same as the original one.

2. `Image.resize` might return different results in different versions of Pillow.
    To ensure that you get the same result,
    make sure to have the same version of Pillow,
    and best to use a Docker environment to ensure identical environment.

## Mask (Image) in Pillow

1. A Mask (image) in Pillow must be a binary image.

## References

https://pillow.readthedocs.io/en/stable/reference/Image.html

https://python-pillow.org/

https://stackoverflow.com/questions/9983263/how-to-crop-an-image-using-pil

https://pillow.readthedocs.io/en/stable/