Status: published
Date: 2019-12-03 10:56:56
Author: Benjamin Du
Slug: get-resources-in-java
Title: Get Resources in Java
Category: Computer Science
Tags: programming, Java, getResource, resources, getClass, getClassLoader, getResourceAsStream
Modified: 2019-12-03 10:56:56

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. `getResource` and `getResourceAsStream` tries to find files in the `resources` directory 
    under `src/main/resources` or `src/test/resources` 
    (depending on whether you are running the application or tests for the application).
    If the specified file is not found,
    `null` is returned (which might cause NullPointerExceptions if you make a mistake specifying the resource to use).

2. `getClass.getResource` requires a leading `/` in the file name to find.

        getClass().getResource("/some_file_to_find")

    Another way is to use `getClass().getClassLoader().getResource`,
    and you must not have a leading `/` for files.

        getClass().getClassLoader().getResource("some_file_to_find")

3. `getResource` returns an [URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html) object.
    You can use the `getFile` or `getPath` method to get the path of the file. 
    Both of these 2 methods return a String.
