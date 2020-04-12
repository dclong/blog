Status: published
Date: 2020-04-12 11:54:46
Author: Benjamin Du
Slug: pytest-tips
Title: Write Unit Tests Using PyTest in Python
Category: Computer Science
Tags: programming, Python, PyTest, fixtures, plugins

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Run `pytest` in the root directory of your project to run all test suites. 
You can run test cases in a specific test file (e.g., `test_file.py`) 
using the command `pytest test_file.py`.
You can run a specific test (e.g., `test_func`) 
in a test file (e.g., `test_func`) using `pytest test_file.py -k test_func`.

## Tags

[@pytest.mark.skipif](http://doc.pytest.org/en/latest/reference.html#pytest-mark-skipif)

http://doc.pytest.org/en/latest/reference.html#pytest-mark-skip-ref

http://doc.pytest.org/en/latest/skipping.html

https://stackoverflow.com/questions/38442897/how-do-i-disable-a-test-using-py-test


## Plugins

https://github.com/ClearcodeHQ/pytest-elasticsearch

https://github.com/ClearcodeHQ/pytest-postgresql


https://github.com/ClearcodeHQ/pytest-dynamodb

https://github.com/ClearcodeHQ/pytest-rabbitmq

https://github.com/ClearcodeHQ/pytest-mysql

https://github.com/ClearcodeHQ/pytest-redis

https://github.com/ClearcodeHQ/pytest-mongo


## References

[Is there a way to specify which pytest tests to run from a file?](https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file)