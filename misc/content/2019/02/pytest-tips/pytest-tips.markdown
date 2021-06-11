Status: published
Date: 2019-02-05 19:29:39
Author: Benjamin Du
Slug: pytest-tips
Title: Write Unit Tests Using PyTest in Python
Category: Computer Science
Tags: programming, Python, PyTest, fixtures, plugins
Modified: 2021-03-05 19:29:39

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Run `pytest` in the root directory of your project to run all test suites. 
You can run test cases in a specific test file (e.g., `test_file.py`) 
using the command `pytest test_file.py`.
You can run a specific test (e.g., `test_func`) 
in a test file (e.g., `test_func`) using `pytest test_file.py -k test_func`.
you can also pass parameters to a test function using
`pytest test_file.py:::test_func[0-0-0-invalid]`.

[pytest import mechanisms and sys.path/PYTHONPATH¶](https://docs.pytest.org/en/stable/pythonpath.html#import-modes)

--tb=short
--lf (last failure)


## Markers

`@pytest.mark.foo` where `foo` can be any arbitrary string you like, 
e.g., `@pytest.mark.slow` tells pytest that the marked test takes a long time to run.

[@pytest.mark.skipif](http://doc.pytest.org/en/latest/reference.html#pytest-mark-skipif)

http://doc.pytest.org/en/latest/reference.html#pytest-mark-skip-ref

http://doc.pytest.org/en/latest/skipping.html

https://stackoverflow.com/questions/38442897/how-do-i-disable-a-test-using-py-test

## Capturing of the stdout/stderr output

You can disable all capturing using the `-s` option 
(which is equivalent to `--capture=no`).

    pytest -s

For more details,
please refer to
[Capturing of the stdout/stderr output](https://docs.pytest.org/en/reorganize-docs/capture.html)
.

## Parameterized Tests

[Talk: Brian K Okken - Multiply your Testing Effectiveness with Parameterized Testing](https://www.youtube.com/watch?v=2R1HELARjUk)


## Plugins

https://github.com/ClearcodeHQ/pytest-elasticsearch

https://github.com/ClearcodeHQ/pytest-postgresql


https://github.com/ClearcodeHQ/pytest-dynamodb

https://github.com/ClearcodeHQ/pytest-rabbitmq

https://github.com/ClearcodeHQ/pytest-mysql

https://github.com/ClearcodeHQ/pytest-redis

https://github.com/ClearcodeHQ/pytest-mongo


## References

[Good Integration Practices](https://docs.pytest.org/en/stable/goodpractices.html#test-package-name)

[Changing standard (Python) test discovery¶](https://docs.pytest.org/en/stable/example/pythoncollection.html)

[Is there a way to specify which pytest tests to run from a file?](https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file)

https://medium.com/python-in-plain-english/unit-testing-in-python-structure-57acd51da923