Status: published
Date: 2020-06-23 14:48:35
Author: Benjamin Du
Slug: pylint-tips
Title: Tips on pylint
Category: Computer Science
Tags: programming, Python, pylint, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## pylint

1. Show ERROR messages only.
```
pylint -E some_script.py
```

2. Show ERROR and WARNING messages only.
```
pylint --disable=R,C some_script.py
```

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

Add the following to `settings.json` for Visual Studio Code to work with `cv2`.

    "python.linting.pylintArgs": ["--extension-pkg-whitelist=numpy,cv2", "--generated-members=cv2.*"]

https://github.com/PyCQA/pylint/issues/2426

## Examples

https://github.com/kubeflow/examples/blob/master/.pylintrc

My copy of `.pylintrc`.

    [MASTER]
    unsafe-load-any-extension=no
    extension-pkg-whitelist=numpy,cv2
    generated-members=cv2.*

    [TYPECHECK]
    ignored-classes=Namespace

## References

https://stackoverflow.com/questions/31907762/pylint-to-show-only-warnings-and-errors

https://stackoverflow.com/questions/35990313/avoid-pylint-warning-e1101-instance-of-has-no-member-for-class-with-dyn
