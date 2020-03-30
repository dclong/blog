Status: published
Date: 2020-03-29 23:32:05
Author: Benjamin Du
Slug: call-java-code-using-jpype-from-python
Title: Call Java Code Using Jpype from Python
Category: Computer Science
Tags: Computer Science, JPype1, JPype, Java, JVM, Python

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**



JPype is easy and intuitive to use.
It is the most popular Java interface for Python currently.

    :::python
    import jpype
    import jpype.imports
    jpype.addClassPath("/path/to.jar")
    jpype.startJVM()
    print(java.lang.System.getProperty('java.class.path'))
    import ...
    obj = SomeClass(...)
    obj.someMethod(...)
    StaticClass.someMethod(...)

1. `jpype.addClassPath` must be called before starting the JVM.

## References

- [jpype-project/jpype](https://github.com/jpype-project/jpype)

- [StartJVM and other upgrading issues with 0.7.0](https://github.com/jpype-project/jpype/issues/498)
