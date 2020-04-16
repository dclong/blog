Status: published
Date: 2019-09-16 22:12:27
Author: Benjamin Du
Slug: tips-on-yapf
Title: Tips on yapf
Category: Computer Science
Tags: programming, Python, yapf, code formatting

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


[yapf Online Demo](https://yapf.now.sh/)


1. There are 4 predefined styles: google, facebook, chromium, and pep8.
    You can specify a style to use using the `--style` option 
    or you can specify the style to use in the file `.style.yapf` under the root directory of your project.

        [style]
        # YAPF uses the feacebook style
        based_on_style = facebook

    YAPF searches for the formatting style in the following manner:
    1. Specified on the command line
    2. In the [style] section of a .style.yapf file in either the current directory or one of its parent directories.
    3. In the [yapf] section of a setup.cfg file in either the current directory or one of its parent directories.
    4. In the [style] section of a ~/.config/yapf/style file in your home directory.
    If none of those files are found, the default style is used (PEP8).

2. You can control the behavior of yapf via settings in the file `.style.yapf` under the root directory of your project.

```
[style]
EACH_DICT_ENTRY_ON_SEPARATE_LINE = True
ALLOW_SPLIT_BEFORE_DICT_VALUE = False
```

## Tricks and Traps

1. When `--diff/-d` is supplied, YAPF returns zero when no changes were necessary, 
  non-zero otherwise (including program error).
  You can use this in a CI workflow to test that code has been YAPF-formatted.

## References

https://github.com/google/styleguide

https://github.com/google/yapf
