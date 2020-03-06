Status: published
Title: General Tips for Java
Date: 2020-02-10 10:07:24
Slug: general-tips-for-java
Author: Ben Chuanlong Du
Category: Computer Science
Tags: tips, programming, Java

## Package Dependency Management

1. It is suggested that you use Gradle (instead of Maven or sbt) for JVM projects.

## Collections

1. You can use `Arrays.fill` to set a value to all elements of an array at once.


## Code Flow Control

1.  There is not `goto` statement in Java, 
    however you have several ways to make the program in Java jump to other place.

    - The `break` and `continue` statements allow you 
        to jump out of a block in a loop or switch statement.

    - A labeled statement and `break label;` allow you 
        to jump out of an arbitrary compound statement 
        to any level within a given method (or initializer block).

3.  For multi-threads programs in Java, 
    it is hard to debug the whole program directly. 
    To make sure that the program works, 
    you can test each class in the program 
    by writing a testing class for each of them.

    - Throwing and catching exceptions allows you 
        to (effectively) jump out of many levels of method call. 
        However, exceptions is relatively expensive 
        and are considered to be a bad way to do "ordinary" control flow.)

    - And of course, there is `return`.

## Keyword `final`

1. Even if you make an object `final`, 
    you might still be able to mutate it. 
    This is because `final` describes the name of the object,
    which means that the variable cannot point to a new address, 
    but the content of the address (where the variable points to) might still be changed. 
    For example, if you define 

         `public final int[] a = new int[10]`

    you cannot point `a` to another address, 
    but you are still able to change the elements of `a`, 
    i.e., you're able to change the value of `a[i]` for $i=0,\ldots,9`\). 
    This is one reason that defensive copy is preferred when you pass around a mutable object. 
    Generally speaking, defensive copy is preferred if it doesn't affect performance badly. 
    Also, if a getter method returns a mutable object, 
    you'd better make a defensive copy.

2. You can use the `final` keyword to tell the compiler that an object won't be reassigned value.
    This guarantees that a primitive variable marked as `final` is a constant.
    But there is no guarantee that an object marked as `final` is a constant. 
    You cannot reassign value to the object but you might still be able to change its internal content.
    For example, the the object is an ArrayList, 
    you can still change its elements.  
    Notice that the `const` keyword is reserve but not used in Java.

## Print and Log

1. Always print some indicating information to the console 
    when you expect some input from the console. 
    Otherwise, 
    you when you run the application, 
    it waits for your input but you might think that it's not running. 
    Also if you do an intensive computing in Java, 
    you'd better print the progress (if you can) to the console. 
    At least you should print message to the console after the simulation is done!

2. In many programming languages, 
    you can print out more than one variables (not necessarily the same type) at a time. 
    In Java, 
    the method `println()` (or other similar methods) of `System.out` 
    can only accept one parameter. 
    However, you can concatenate different variables as a string 
    and print out the string.

## Operators

1. There are many operators in C/C++ 
    which makes operations faster and calculation faster, 
    e.g. `++`, `–`, `+=`, `\*=`, and so on. 
    Similarly to C/C++, you can also use them in Java. 
    Specially, for the increase (`++`) and decrease `–` operator, 
    you can use them both before and after numerical variables in Java.

    you can throw out exceptions, 
    or you can use method `System.err.println()` to print error information 
    to the console and end the program.

## Misc

1. `getClass` returns the RUNTIME class of the object not the declared type!

2. `Objects.hash` can be used to create hash code for an object easily.

3. `Double.compare` is the recommended way to compare whether 2 double values are equal.

9.  Since you do not have to assign the returned value of method to any object in Java, 
    you can use any method as if it is a `void` method.
    This means that for any method that is `void` it does not hurt 
    to declare it as a method that returns some object (or primitive type value). 
    Actually this might be very convenient sometimes, 
    because by doing so you can do the operation you want 
    and at the time you have extra information about the operation. 
    For example, 
    if you want to insert a value to a sorted array, 
    you can make the method return an integer which is the index of the inserted place. 
    This extra information (the index of the inserted place) is highly useful in may cases.

10. It is expensive to allocating a new block of memory 
    (not only in Java but also in other languages), 
    so you should avoid allocating new block of memory all the time. 
    If it is impossible to avoid allocating memory, 
    you can allocate a bigger memory than needed each time. 
    In this way, you waste some space, but might save much time.

11. Method `getClass` can return the class of an object.

13. If you have an array of objects of some super class, 
    you can cast the whole array to sub class at once. 
    However, usually you cannot cast all elements of an array at a time. 
    For example, 
    if you have an array of `double`, 
    you cannot cast the whole array into `int` at a time.
    Instead, you must cast each element one by one.

14. If you want let the compiler know that a number you use in your code
    is a double precision number you can add suffix `d` to the number.
    For example if you want to do double precision calculation for `3 / 6`, 
    you can write it as `3 / 6d` instead of casting integer to
    double using `(double)`.

15. Avoid using a local variable which has the same name as an instance variable.

## Eclipse for Java

1. You can use `format` button under `source` menu to tidy the code.
