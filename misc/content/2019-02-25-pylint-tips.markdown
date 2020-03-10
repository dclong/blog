Status: published
Date: 2020-03-09 17:22:30
Author: Benjamin Du
Slug: pylint-tips
Title: Tips on pylint
Category: Computer Science
Tags: programming, Python, pylint, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
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
## References

https://stackoverflow.com/questions/31907762/pylint-to-show-only-warnings-and-errors

https://stackoverflow.com/questions/35990313/avoid-pylint-warning-e1101-instance-of-has-no-member-for-class-with-dyn
