Status: published
Date: 2021-01-10 17:44:33
Author: Benjamin Du
Slug: python-logging
Title: Python Logging
Category: Computer Science
Tags: programming, Python, logging, loguru, rich
## General Tips

1. [logging](http://www.legendu.net/misc/blog/python-logging-module/)
    is a Python module for logging coming with the standard library
    while
    [loguru](http://www.legendu.net/misc/blog/python-logging-made-stupidly-simple-with-loguru/)
    is a popular 3rd-party logging library.
    Unless you do not want your Python package/script to depend on 3rd-party libraries,
    `loguru` is preferred to `logging` for multiple reasons.

        - loguru is easy and fun to use 
        - Good out-of-box experience. They default settings work well for most situations. 
            For example,
            loguru works with Spark by default while logging needs additional configurations.

2. [rich](https://github.com/willmcgugan/rich)
    is a Python library for rich text and beautiful formatting in the terminal.

## References

https://github.com/Delgan/loguru/issues/120

https://realpython.com/python-logging/

https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels

[PyLint message: logging-format-interpolation](https://stackoverflow.com/questions/34619790/pylint-message-logging-format-interpolation)

http://www.legendu.net/misc/blog/python-logging-made-stupidly-simple-with-loguru/