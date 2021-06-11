Status: published
Author: Ben Chuanlong Du
Date: 2021-01-10 11:48:21
Slug: comparison-of-collections-in-cpp-and-java
Title: Comparison of Collections in C++ and Java
Category: Computer Science
Tags: programming, cpp, C++, Java, tips, collection
Modified: 2021-01-10 11:48:21

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 

## Plain Old Array
1. The length/size of array is as in the declaration.
    Each element of the array is initialized to the default value (null for object).

2. Array in Java does not have a size method, 
    but it has a length member. 
    This is because the length of an array won't change.
    Since String in Java is immutable, 
    a string also has a length method instead of size method.
    But I think there inconsistent here, they should make String has a length member.

3. Array in Java is both static and dynatic while array is C/C++ is static. 
    Because array is Java is actually object, so the memory is managed automatically.
    In C++, array is not object, if you want to make it dynamic, you must manage memory automatically.

5. You almost never need to use array is C++. 
    You can use vector instead of array. 

## Class Collections

1. If you create a vector/list in C++ using the constructor taking a capacity parameter,
    the vector/list is fully initialized, 
    i.e., every element of the vector/list is initialized.
    This is different from Java.
    If you create an ArrayList in Java using the constructor taking a capacity parameter,
    there's no element in the ArrayList, i.e., the ArrayList is empty,
    not to mention initialization of elements.
    The difference is because, an element of a vector/list in C++ is an object 
    and it must have a valid value while an element of an ArrayList in in Java is a reference.
    A reference not necessarily has a valid value. 
    Rather than initialize every element to be null,
    Java is lazy not to do anything.
