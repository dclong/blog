Status: published
Date: 2020-12-16 11:04:45
Author: Benjamin Du
Slug: security-tools-in-python
Title: Security Tools in Python
Category: Computer Science
Tags: Computer Science, security, Python, PyArmor, bandit
Modified: 2021-04-16 11:04:45

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## [bandit](https://github.com/PyCQA/bandit)
[bandit](https://github.com/PyCQA/bandit)
is a tool designed to find common security issues in Python code.

## [pyarmor](https://github.com/dashingsoft/pyarmor)
[pyarmor](https://github.com/dashingsoft/pyarmor)
is a tool used to obfuscate python scripts, 
bind obfuscated scripts to fixed machine or expire obfuscated scripts.

## [markupsafe](https://github.com/pallets/markupsafe)
MarkupSafe implements a text object that escapes characters 
so it is safe to use in HTML and XML. 
Characters that have special meanings are replaced so that they display as the actual characters. 
This mitigates injection attacks, meaning untrusted user input can safely be displayed on a page.