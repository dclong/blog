Status: published
Date: 2021-01-14 09:28:49
Author: Benjamin Du
Slug: pylint-tips
Title: Tips on pylint
Category: Computer Science
Tags: programming, Python, pylint, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tips and Traps 

[Optional Pylint checkers in the extensions module](https://docs.pylint.org/en/1.6.0/extensions.html#optional-pylint-checkers-in-the-extensions-module)

## Message Control

1. Show ERROR messages only.

        :::bash 
        pylint -E some_script.py

2. Show ERROR and WARNING messages only.

        :::bash 
        pylint --disable=R,C some_script.py

3. Disable warning associated with a specific line.

        :::bash
        proc = sp.run(cmd, shell=True)  # pylint: disable=W1510

## Configuration

.pylintrc 
```
[TYPECHECK]
ignored-classes=Fysom,MyClass
```
## Make pylint Work with cv2

```
[MASTER]
unsafe-load-any-extension=no
extension-pkg-whitelist=numpy,cv2
```

## Examples

https://github.com/dclong/xinstall/blob/dev/xinstall/data/pylint/pylintrc

https://github.com/kubeflow/examples/blob/master/.pylintrc

Please refer to 
[settings.json](https://github.com/dclong/xinstall/blob/dev/xinstall/data/vscode/settings.json)
for an example of pylint configuration for Visual Studio Code.

## References

https://stackoverflow.com/questions/31907762/pylint-to-show-only-warnings-and-errors

https://stackoverflow.com/questions/35990313/avoid-pylint-warning-e1101-instance-of-has-no-member-for-class-with-dyn

https://github.com/PyCQA/pylint/issues/2426

https://stackoverflow.com/questions/40163106/cannot-find-col-function-in-pyspark
