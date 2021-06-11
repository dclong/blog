Status: published
Date: 2020-08-18 09:05:13
Author: Benjamin Du
Title: Static Type Checking of Python Scripts Using Mypy
Slug: static-type-checking-python-mypy
Category: Computer Science
Tags: programming, Python, mypy, tips
Modified: 2020-08-18 09:05:13

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


--check-untyped-defs

You can use the option `--ignore-missing-imports` to disable the annoying error messages `No library stub file for module...`.
Please see the [issue](https://github.com/python/mypy/issues/3905) for more details.

You can use `# type: ignore` to silence some errors.
Please see the [issue](https://github.com/python/mypy/issues/500) for more details.

import foo # type: ignore
foo.f()  # okay

## Third-party Stubs

[data-science-types](https://github.com/predictive-analytics-lab/data-science-types)

[pyspark-stubs](https://github.com/zero323/pyspark-stubs)

## Ingore Files and/or Directories

https://github.com/python/mypy/issues/4675

https://github.com/python/mypy/issues/626

## References

https://realpython.com/python-type-checking/#pros-and-cons

https://mypy.readthedocs.io/en/latest/index.html

https://mypy.readthedocs.io/en/latest/common_issues.html

https://mypy.readthedocs.io/en/latest/common_issues.html#displaying-the-type-of-an-expression

https://mypy.readthedocs.io/en/latest/kinds_of_types.html#kinds-of-types

https://realpython.com/python-type-checking/

https://github.com/python/mypy/issues/3905

https://mypy.readthedocs.io/en/latest/config_file.html