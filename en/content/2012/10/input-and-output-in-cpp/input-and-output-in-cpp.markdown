UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-03-24 22:22:41
Slug: input-and-output-in-cpp
Author: Ben Chuanlong Du
Title: Input and Output in C++
Category: Computer Science
Tags: C/C++, IO, C++, programming


Check the `io` directory on the page <https://bitbucket.org/dclong/cpp-learn/src>
for some illustrative examples for the following discussions. 

0. You can format output of numbers using functions 
`std::setpresicion` and `std::setw` in the <imanip> header.

1. When you read data from a file into an array or write data from an array to a file,
you can just use the address of the array.
However, 
if a vector (e.g., vector `x`) is used instead of an array,
you have to use the address of the underlying data in the vector `x` which is `&x[0]`. 
Also, 
when you read/write data into/from a vector, 
you have use the size of the vector `x` multiplied by the memory used by each element 
to calculate the total number of bytes, 
i.e. 

```C++
x.size() * sizeof(x[0]);
```

or if `x` is a vector of double values you can use 

```C++
x.size() * sizeof(double);
```

You cannot use `sizeof(x)`, 
because it is the size of the vector itself 
(without counting the underlying array) and is always the same (12 bytes). 


