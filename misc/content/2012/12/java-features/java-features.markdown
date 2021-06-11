UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Java Features
Date: 2012-12-03 00:00:00
Tags: switch, string, Java, programming, features
Category: Computer Science
Slug: java-features
Author: Ben Chuanlong Du
Modified: 2012-12-03 00:00:00

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 
1. #String in Switch

Java 7 allows use of strings in switch instead of just integers,
which make things much more convenient (see the following example).

    public void foo(Foo t) {
        String name = t.getName();
            switch (name) {
            case John:
                ...
                break;
            case Jackie:
                ...
                break;
            case Ben:
                ...
                break;
            default:
                break;
        }
    }

In the above program, the variable `name` is always compared to `John`, `Jackie` and `Ben` using the `String.equals` method.

2. #Better Way to Handle Exceptions

Java 7 has a better way to handle exceptions

3. #Auto Resource Management

4. #Infinity in Float Computing

Java support "infinity" in float computing, 
for example `Math.log(0)` return $-\infty$ in Java.

5. # Unavailable Features Seen in Other Languages
As a compiled language, 
Java does not support variant number of parameters and default parameters directly, 
but this is totally unnecessary in Java since Java allows overriding functions. 
The only inconvenient place is the `main` function in Java. 
The main method cannot be override, 
so you must use its argument `args` of type `String[]` 
to parse input arguments passed to the `main` function. 
This is not as convenient as varadic template in C++11.

