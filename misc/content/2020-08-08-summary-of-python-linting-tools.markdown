Status: published
Date: 2020-08-08 10:46:38
Author: Benjamin Du
Slug: summary-of-python-linting-tools
Title: Summary of Python Linting Tools
Category: Computer Science
Tags: Computer Science, Python, lint, linter, linting, pylint, flake8

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Flake8 vs MyPy vs pylint 

1. Flake8 focus on logical errors rather than stylistic errors.
    It strives to reduce false positives.

2. `mypy` does the best on type hint.

3. `pylint` performs deeper analysis and thus is slower.

To sum up,
I'd try the tools in the following order
`Flake8 > mypy > pylint`.
