Status: published
Date: 2019-09-24 23:05:01
Author: Benjamin Du
Slug: python-logging
Title: Python Logging
Category: Programming
Tags: programming, Python, logging, loguru

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## [loguru](https://github.com/Delgan/loguru)

The best logging package for Python!

1. Note that the default logging level is `DEBUG` in loguru
  and it is not allowed to change the logging level of an created logger object in loguru.
  You can refer to
  [changing-the-level-of-an-existing-handler](https://loguru.readthedocs.io/en/latest/resources/recipes.html#changing-the-level-of-an-existing-handler)
  and
  [Change level of default handler](https://github.com/Delgan/loguru/issues/51)
  on ways to changing logging level in loguru.

2. Log an exception using luguru and then throws an exception without logging redundant error messages.

        :::python
        def throw(_, error, message, *args, **kwargs):
            message = message.format(*args, **kwargs)
            logger.opt(depth=1).error(message)
            raise error(message)

        logger.__class__.throw = throw

        logger.throw(ValueError, "Something bad happened")

    Or if you do not care what kind of exception is thrown to user, 
    you can use the following way which is more concise.

        :::python
        logger.error(message)
        sys.exit()

## [logging](https://docs.python.org/3/library/logging.html)

### Format keywords

process

levelname

message

## References

https://github.com/Delgan/loguru/issues/120

https://realpython.com/python-logging/

https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels
