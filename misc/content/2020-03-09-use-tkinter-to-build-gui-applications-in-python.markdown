Status: published
Date: 2020-04-09 10:49:57
Author: Benjamin Du
Slug: use-tkinter-to-build-gui-applications-in-python
Title: Use Tkinter to Build GUI Applications in Python
Category: Computer Science
Tags: Computer Science, Python, Tkinter, GUI

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## General Tips

1. You need to use multithreading to make GUI application more responsive
    if any event triggers a long-run task.
    Please refer to 
    [Concurrency and Parallel Computing in Python](http://www.legendu.net/misc/blog/python-concurrency-parallel-computing/)
    for more discussions. 

2. When you develop a GUI application using Tkinter in Python, 
    `root = tk.Tk()` must be the first statement after imports.

        :::python
        import tkinter as tk
        import ...
        root = tk.Tk()
        ...

3. It is suggested that you use the `ttk` module (Tk Themed Widgets) when possible. 
    It has more advanced and better looking widgets. 
    However, the `Text` widget is only available in `tk`.

4. It is suggested that you name a widget using the `name` option 
    when creating it,
    and use the name to refer to the widget later. 
    Avoid keeping referencing to widgets by yourself!

        :::python
        root.nametowidget("name1.name2.name3")

2. A Button object has the option `command` to set a callback function when clicked
    while a Label object does not have this option.

        :::python
        def button_click():
            ...


        Button(root, text="Scrrenshot", command=button_click)

    Nevertheless, 
    you can bind a callback function to any widget using the method `widget_obj.bind`.

        :::python
        import tkinter as tk
        root = tk.Tk()


        def label_left_click(event):
            ...


        label = tk.Label(root, text="my label")
        label.bind("<Button-1>", label_left_click)

    A few things to keep in mind. 
    When you bind a callback function using the `command` option,
    the callback function takes no argument. 
    However, 
    when you bind a call back function using the method `widget_obj.bind`,
    the callback function takes an `Event` object as argument.

3. To make a label visible no matter there are text/image in it or not,
    you can set a border to it.

        :::python
        label = tk.Label(root, bd=1)

    You can ke it even more visible by giving a sunken effect.

        :::python
        label = tk.Label(root, bd=1, relief=tk.SUNKEN)

4. A Frame object has its own grid.
    This makes frames and grid the best combinations to manage the layout of your GUI application.
    You can use frames to group components.
    Inside each frame, 
    use grid to control the layout of widgets. 

5. It seems to me that you must keep a reference to a PhotoImage object
    in order to use it for a label. 
    A temporary PhotoImage object does not work.
    The image object can then be used wherever an image option is supported by some widget (e.g. labels, buttons, menus). In these cases, Tk will not keep a reference to the image. When the last Python reference to the image object is deleted, the image data is deleted as well, and Tk will display an empty box wherever the image was used.

6. There are 2 kinds of PhotoImage objects that you can use with Tkinter.
    The first is `Tkinter.PhotoImage` 
    while the second is `PIL.ImageTk.PhotoImage`.
    The latter is preferred as it is more flexible,
    supports more data format,
    and is easier to use.
    `Tkinter.PhotoImage` supports only GIF pictures 
    if you use the `file` option to load an image,
    and it seems to me that it does not accept `PIL.Image`.


### Size of Widgets

https://stackoverflow.com/questions/17398926/how-to-set-a-widgets-size-in-tkinter/17399180

## Grid

Set minimum size of rows and columns of the grid.

    :::python
    col_count, row_count = root.grid_size()
    for col in xrange(col_count):
        root.grid_columnconfigure(col, minsize=20)
    for row in xrange(row_count):
        root.grid_rowconfigure(row, minsize=20)

https://stackoverflow.com/questions/28019402/tkinter-grid-spacing-options

## Bind Keys

https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

Keyboard events are sent to the focused widget.

    :::python
    widget.bind("<Key>", callback_func)

## Tutorials

https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d

## References

https://docs.python.org/3/library/tkinter.html

https://docs.python.org/3/library/tk.html

http://effbot.org/tkinterbook/

http://stupidpythonideas.blogspot.com/2013/10/why-your-gui-app-freezes.html

https://www.reddit.com/r/Python/comments/7rp4xj/threading_a_tkinter_gui_is_hell_my_least_favorite/