Status: published
Date: 2020-04-01 14:45:03
Author: Benjamin Du
Slug: call-java-code-using-jpype-from-python
Title: Call Java Code Using JPype from Python
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
    print(jpype.java.lang.System.getProperty("java.class.path"))
    import ...
    obj = SomeClass(...)
    obj.someMethod(...)
    StaticClass.someMethod(...)

1. `jpype.addClassPath` must be called before starting the JVM.
    You can use the following statement to check that the correct dependency has been added.

        :::python
        print(jpype.java.lang.System.getProperty("java.class.path"))

## Passing Arguments Between Java and Python

https://stackoverflow.com/questions/13637614/jpype-passing-args-to-java

https://jpype.readthedocs.io/en/latest/quickguide.html#primitives

## References

- [jpype-project/jpype](https://github.com/jpype-project/jpype)

- [StartJVM and other upgrading issues with 0.7.0](https://github.com/jpype-project/jpype/issues/498)

- [JPype Quickstart Guide](https://jpype.readthedocs.io/en/latest/quickguide.html#quickstart-guide)