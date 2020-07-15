Status: published
Date: 2020-06-15 11:31:01
Author: Benjamin Du
Slug: python-logging
Title: Python Logging
Category: Computer Science
Tags: programming, Python, logging, loguru

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## General Tips

1. Do NOT use `%`, `str.format` or f-string to format strings 
    when you log messages.
    Instead, 
    passing parameters to logging methods so that lazy string evaluation can be leveraged.

        :::python
        # for the logging module
        logger.info("%s is copied to %s", src_file, des_file)

        # for the loguru module
        logger.info("{} is copied to {}", src_file, des_file)

2. `loguru` is preferred to `logging` for multiple reasons.

    - loguru is easy and fun to use 
    - Good out-of-box experience. They default settings work well for most situations. 
        For example,
        loguru works with Spark by default while logging needs additional configurations.

## [loguru](http://www.legendu.net/misc/blog/python-logging-made-stupidly-simple-with-loguru/)

## [logging](https://docs.python.org/3/library/logging.html)

It is often desirable to control the logging level using a command-line option.
Let's say that you use the option `--level` to accept names (warning, debug, info, etc) of logging levels,
and the corresponding variable is `args.level`. 
You can retrive the corresponding logging level using `getattr(logging, args.level.upper())`.
And thus you can easily set the logging level with the following code.

    :::python
    level = getattr(logging, args.level.upper())
    logging.setLevel(level)

### Format keywords

process

levelname

message

## [rich](https://github.com/willmcgugan/rich)

Rich is a Python library for rich text and beautiful formatting in the terminal.

## References

https://github.com/Delgan/loguru/issues/120

https://realpython.com/python-logging/

https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels

[PyLint message: logging-format-interpolation](https://stackoverflow.com/questions/34619790/pylint-message-logging-format-interpolation)

http://www.legendu.net/misc/blog/python-logging-made-stupidly-simple-with-loguru/