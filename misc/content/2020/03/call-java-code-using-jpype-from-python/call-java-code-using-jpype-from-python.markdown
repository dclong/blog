Status: published
Date: 2020-03-31 12:16:58
Author: Benjamin Du
Slug: call-java-code-using-jpype-from-python
Title: Call Java Code Using JPype from Python
Category: Computer Science
Tags: Computer Science, JPype1, JPype, Java, JVM, Python
Modified: 2020-10-31 12:16:58

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



JPype is easy and intuitive to use.
It is the most popular Java interface for Python currently.

    :::python
    import os
    import sys
    from pathlib import Path
    import jpype


    jpype.addClassPath("/path/to.jar")
    jpype.startJVM()
    print(jpype.java.lang.System.getProperty("java.class.path"))
    import ...
    obj = SomeClass(...)
    obj.someMethod(...)
    StaticClass.someMethod(...)


    import pyarrow
    import pyarrow.jvm
    classpath = ":".join(str(jar.resolve()) for jar in Path().glob("*.jar"))
    jpype.startJVM(jpype.getDefaultJVMPath(), f"-Djava.class.path={classpath}")
    ra = jpype.JPackage("org").apache.arrow.memory.RootAllocator(sys.maxsize)
    dm = jpype.JPackage("java").sql.DriverManager
    connection = dm.getConnection("jdbc:hive2://hive.server.example.com:10000/default", "user_name", "password")
    batch = jpype.JPackage("org").apache.arrow.adapter.jdbc.JdbcToArrow.sqlToArrow(
        connection, "SELECT * FROM some_table", ra
    )
    df = pyarrow.jvm.record_batch(batch).to_pandas()

Notice that you can import a Java class as usual after the following import.

    :::python
    import jpype.imports

1. `jpype.addClassPath` must be called before starting the JVM.
    You can use the following statement to check that the correct dependency has been added.

        :::python
        print(jpype.java.lang.System.getProperty("java.class.path"))

## Passing Arguments Between Java and Python

https://stackoverflow.com/questions/13637614/jpype-passing-args-to-java

https://jpype.readthedocs.io/en/latest/quickguide.html#primitives

## References

- [Java Interfaces for Python](http://www.legendu.net/misc/blog/java-interfaces-for-python)

- [jpype-project/jpype](https://github.com/jpype-project/jpype)

- [StartJVM and other upgrading issues with 0.7.0](https://github.com/jpype-project/jpype/issues/498)

- [JPype Quickstart Guide](https://jpype.readthedocs.io/en/latest/quickguide.html#quickstart-guide)