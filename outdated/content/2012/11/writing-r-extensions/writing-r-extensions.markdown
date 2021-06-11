UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-10-23 17:13:18
Slug: writing-r-extensions
Author: Ben Chuanlong Du
Title: Writing R Extensions
Category: Programming
Tags: R, Rcpp, programming, CRAN
Modified: 2016-10-23 17:13:18

<img src="http://dclong.github.io/media/r/r.png" height="200" width="240" align="right"/>

The following are some tips for using the old fashioned way (using `.C` and `.Call`) 
to write R extensions. 
The state-of-art way to extend R via C/C++ is to use the `Rcpp` package.
Check [this post](http://dclong.github.io/en/2012/09/rcpp-rocks/) For tips on using `Rcpp` package.

1. If you want to call C code from R, 
the arguments of C functions to be called by `.C` must be pointers. 
This means that only simple data sturcture (primitive types and array) 
can be passed between R and C.
By default, 
`.C` makes a copy of the arguments to be passed to C functions, 
and thus the corresponding variables/objects in R are unchanged. 
If a large array/vector is to be passed to C, 
you can suppress copying using the option `DUP=FALSE` to increase performance.  
However, 
the corresponding variables/objects in R will be changed if the C code mutates them.

2. It is very annoying to work with pointer in C, 
however, 
you are forced to work with pointer if you want to C functions for calling in R. 
One suggestions is to avoid using pointers in functions except
the call that you directly call from R.

3. A matrix in R is essentially a vector with "dim" property, 
so when you pass a matrix to a C function from R, 
you actually pass a 1-dimensional array to the C function. 
This is a place inviting errors. 
Because of the way that a 2-D array is saved in C/C++, 
it is more nature to stretch a 2-D array to a 1-D array by rows 
while a matrix in R is stretched to a vector by columns by default. 
So you have be careful that the matrix you passed to C/C++ is 
in the right form that you want. 
If this is a problem, 
tranposing the matrix can be an easy solutions many times.

4. A good thing about interface with C in R is that the RNG in R can be synced easily. 
To do this, 
you just have to call the C functions that R supplies for generating random numbers, 
and surround them in `GetRNGstate();` and  `PutRNGstate();`. 
For more details, 
please refer to the R extension.

5. To call C++ code from R, 
you can write C wrapper functions/interfaces (surrounded by  `extern "C"{}`) in your C++ code, 
and then call the C wrapper functions/interaces using the `.C` function from R.

6. When writing a R package which use external code, 
you do not have to compile it manually on different platforms. 
You just need to place the code into the "src" folder, 
and it will be automatically compiled 
(to the right type of library according to which platform you use) 
when you compile your package. 
What's more, 
`library.dynam` helps you to automatically load the compiled code on differently platforms, 
i.e. you don't have to check the type of the platform 
and use `dyn.load` to load the compiled code accordingly. 
However, 
you must pass the name of the compiled code to `library.dynam` without extension.

