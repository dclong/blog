UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-10-23 22:53:22
Slug: call-java-in-r
Author: Ben Chuanlong Du
Title: Call Java in R Using Package rJava
Category: Computer Science
Tags: programming, Java, array, rJava, R, vector, package

The package "rJava" offers a convenient way to call Java code from R. 
The following are some tips for using the "rJava" package.

1. You must first start a Java Virtual Machine 
using `.jinit` before calling Java code from R. 
You can specifiy a vector of paths for the function `.jinit`. 
If the Java code relies on some other package or jar files, 
their path must also be added to the search path of the Java
Virtual Machine. 
Notice the the class paths must be full paths rather than relative paths.
If you develop an R package depending on `rJava`, 
you can `.jpackage` to initializes a Java Virtual Machine (JVM) 
in the function `.onLoad`.

2. After creating an Java object, 
you can use `$` to invoke its public methods
and access its public fields directly instead of using the function `.jcall` or `.jfield`. 
This way preserves the flavor of object oriented programming, 
and is much more convenient. 

3. You can use boolean values, double values, strings directly 
when invoking Java methods in R. 
Because numerical numbers are double numbers be default in R, 
you should either add suffix "L" to a number or use function `as.integer` 
to convert it to an integer if you want to pass it as an integer to a Java method. 

4. You can call a static method of class using the function `.jcall`. 
Just replace the object argument with the name of the class whose 
static method you want to call. 

5. To pass an vector to a Java method, you have to use the function 
`.jarray` to convert the vector to a Java array. 

3. The table of JNI:  
`I`: integer 
`D`: double 
`J`: long F: float V: void Z: boolean C: char
`B`: byte 
`L<class\>`: java object of the class <class\>, 
e.g.,  `Ljava/lang/Object`
`[<type\>` array of objects of type `<type\>`,
e.g. `[D` for an array of doubles

