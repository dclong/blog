Status: published
Title: Good C++ Libraries
Date: 2015-10-18 11:46:12
Tags: library, programming, gsl, package, GMP, boost, it++, C++, armadillo, NTL
Category: Computer Science
Slug: good-cpp-libraries
Author: Ben Chuanlong Du

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Good C++ Libraries

1. Armadillo: linear algebra
2. it++: signal processing
1. shogun: a large scale machine learning toolbox
0. boost: an advanced general purpose C++ library 
1. dlib: a general purpose cross-platform C++ library designed using contract programming and modern C++ techniques.
0. R: a popular statistic software. 
4. Blitz++: linear algebra and random number generator 
5. GMP: the GNU Multiple Precision Arithmetic Library
6. NTL: a library for doing number theory 
7. HPX: high performance parallel library
8. Cinder (graphics, audio, video, networking, image processing and computational geometry)
8. libcurl: a free and easy-to-use client-side URL transfer library
3. GSL: a comprehensive C/C++ scientific library
1. ODB: an object-relational mapping (ORM) system for the C++ language.

## Database

1. sqlpp11

## Scitific Computing

### Armadillo

1. The C++ standard library supports methods `at` and `operator[]` for accessing elements of containers. 
    Armadillo supports these two methods as no-bound-checking versions. 
    `operator()` is the bound-checking (and thus preferred) version for accessing elements of matrices and arrays.

2. Armadillo use `*` for matrix multiplication and `%` element-wise multiplication,
    which is different from R and MATLAB.

### GSL

1. The GSL library implements popular special functions many of which 
    are not implemented in other libraries 
    (e.g., the Lambert-W function is not implemented in Boost).

2. The distribution related functions (quantile, cdf, PDF, etc) in 
    GSL is more convenient to use than the Boost library. 
    You can define macros to match the GSL version of distribution functions with 
    R version of distribution functions.

### R

There are some useful distribution related C functions in R.h.
You can use these C functions which do not require an session of R 
(random number generating functions require a session of R and thus cannot be used in C/C++ code directly) 
in your C/C++ code.
A more general and powerful way to call R related functions is via the "Rinside" package. 
Using the "Rinside" package, 
you can call any R function not just C functions in R header files.
On the contrary, "Rcpp" is a way to extened R via C++. 
The most convenient way to use "Rcpp" is to expose C++ classes/methods/functions to R via `RCPP_MODULE`.
Note that "Rcpp" is for R users not C/C++ users,
i.e., you must come back to R. 
Tring to compile C/C++ based on "Rcpp" and the binary code will result in segmentation fault. 

## Unit Testing

1. Catch

## Other General Purpose Libraries

## Boost

0. The boost random library (and thus the standard library of C++11) does not have a way to generate 
    random numbers from the beta distribution directly, 
    however, you use $X/(X+Y)$ where $X$ and $Y$ are independent 
    random variables from the gamma distribution.

1. `boost::accumulator` is good for incremental calculations,
    especially when several quantities having dependent relationships need 
    be calculated. 

## Debugging Tools

1. [gdb](http://www.gnu.org/software/gdb/)

2. [Valgrind](http://valgrind.org/)

3. [CppCheck](http://cppcheck.sourceforge.net/)

## Compilers

1. gcc/g++
2. clang/clang++
3. xlc (for IBM AIX)
