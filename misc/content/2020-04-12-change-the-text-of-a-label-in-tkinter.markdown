Status: published
Date: 2020-04-12 09:53:35
Author: Benjamin Du
Slug: tkinter-label-tips
Title: The Label Widget in Tkinter
Category: Computer Science
Tags: Computer Science, Python, programming, Tkinter, GUI, Label, text, config

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## General Tips

1. `ttk.Label` is preferred over `tk.Label`.

## Change the Text of a Label

After creating a Label (whose text has already been set),
there are 3 different approaches that you can change its text.

### Dict-like Access

    :::python
    label["text"] = "new text for the label"

### Via the `.config` Method

This is the recommended way to update the text of a label in Tkinter.

    :::python
    label.config(text="new text for the label")

### Via a StringVar

This way is more complicated 
and it requires that the a text variable is specified 
when the label is created.

    :::python
    import tkinter as tk
    var_text = tk.StringVar()
    label = Label(root, textvariable=var_text)
    label.pac()
    var_text = "new text for the label"

Notice that if you have set `textvariable`
when creating a label,
you cannot use the first 2 approaches to update its text.
Instead,
you must update the StringVar to update the text of the label.

## Change the Image of a Label

After creating a Label (whose image has already been set),
there are 2 ways you can change its image.

### Dict-like Access

    :::python
    label["image"] = some_photo_image_obj

### Via the `.config` Method

    :::python
    label.config(image=some_photo_image_obj)

Unlike the text of a Label object, 
there is no `imagevariable` option for a Label.

## Size 

If you don’t specify a size, 
the label is made just large enough to hold its contents. 
You can also use the height and width options to explicitly set the size. 
If you display text in the label, these options define the size of the label in text units. 
If you display bitmaps or images instead, they define the size in pixels (or other screen units). 
See the Button description for an example how to specify the size in pixels also for text labels.
