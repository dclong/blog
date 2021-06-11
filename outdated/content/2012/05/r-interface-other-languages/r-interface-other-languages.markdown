UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2012-05-02 13:10:12
Slug: r-interface-other-languages
Author: Ben Chuanlong Du
Title: Passing Arrays Between R and Other Programming Languages
Category: Computer Science
Tags: array, R, C/C++, programming, Java
Modified: 2015-03-02 13:10:12

<img src="http://dclong.github.io/media/r/r.png" height="200" width="240" align="right"/>
A matrix or an array in R is essentially a vector with dimension attribute. 
For this reason, no matter you pass a vector, matrix or an array
to an external call, you essentially pass a 1 dimensional array to the call. 
As a coinsequence, 
it's usually not conveneint to pass 2 dimensional arrays between R and other programming languages. 
To pass arrays from R to an external call, 
always use 1 dimensional array.
If the 1-d array you pass to an external call stores data of a 2-d array, 
you have to pass extra arguments about the
dimension information to the external call.

In C, an array name is an address. 
There's no way to figure out the length of the array from its address, 
so you have to pass information about the length of array to a C function if you want to call it from R. 
An array is an object in Java, and you can access its length attribute, so you don't have to pass
information about the length to a Java method if you want to call it in R.
Because of the way that R calls C functions, there's simple no way to return a
2-d array from a C function to R. However, since an 2-d array in Java is an
object, you can return it to R. Applying function `.jevalArray` on the 2-d array
object, you get a vector of addresses. Applying function `.jevalArray` on these
addresses again (most conveniently with the help of function `sapply` or
`lapply`), you get values of the 2-d array. For example, suppose `x` is an 2-d
array object returned from a Java method to R, you can use the following code to
get its content.

    x = .jevalArray(x)
    x = t(sapply(x,.jevalArray))

If a C function returns an array of unkown length, there is no directly way to
return it to R. There are two ways to solve this problem. First, if you know the
maximum length of the array to be returned, you can pass an array with this
length from R to C to accept the returned result. Second, you can write data
from C into a file and then read the data into R. 

From these aspect, interfacing with Java in R is more convenient than
interfacing with C in R. However, R offers APIs written in C for generating
random numbers and manipulating states of random number generators. Another
thing is that you probably have to debug and modify C code and Java code when
you call them in R. For C, you have to unload and reload dynamic libraries; for
Java, you have to restart the JVM. For some reason I'm not sure about (probably
because of other loaded libraries requiring rJava package), restarting the JVM
may not work. These are advantages and disadvantages of interfacing with C and
Java in R. You can choose the most convenient one for you work. 

