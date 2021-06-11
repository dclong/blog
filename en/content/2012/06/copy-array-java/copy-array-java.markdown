UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2014-10-19 13:48:18
Slug: copy-array-java
Author: Ben Chuanlong Du
Title: Copy Arrays in Java
Category: Computer Science
Tags: array, copy, Java, programming
Modified: 2014-10-19 13:48:18

There are several different ways to copy arrays of object (primitive types) in Java. 
However, 
the fastest way seems to be `System.arraycopy`. 
This methed is implemented using native code and only performs a shallow copy. 
Acutally most methods for copying arrays in Java perform shallow copy.


    int arr1[] = {0, 1, 2, 3, 4, 5};
    int arr2[] = {0, 10, 20, 30, 40, 50};
    // copies 3 elements from arr1 to arr2 
    System.arraycopy(arr1, 0, arr2, 0, 3);
