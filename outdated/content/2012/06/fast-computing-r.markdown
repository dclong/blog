UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-08-26 22:08:17
Slug: fast-computing-r
Author: Ben Chuanlong Du
Title: Write R Code that Runs Faster
Category: Programming
Tags: DLL, programming, HPC, high performance computing, parallel, R, memory, GC, speedup, fast, CRAN

<img src="http://dclong.github.io/media/r/run-fast.jpg" height="200" width="240" align="right"/>

R is a popular statistical software which is famous for enormous amout of
packages. The syntax of R is very flexible with make it convenient at the cost
of performance. R is indeed slow compared to many other scripting languages, but
there are a few tricks which can make your R code run faster.

1. Use vector and matrix operation if possible. Theses `*apply` functions
are very helpful for this purpose.

2. Avoid changing the type and size of object in R. Though we use R object
as if they are typeless, they have type actually. Changing the type and size
of a R object forces R to reallocate a memory space which is of course
ineffecient. I have seen so many people writing R code like 

        s = NULL
        while(condition)    
        s = c(s,fun())

or

        s = rbind(s,fun())

If you know the length of `s` ahead, it is better to allocate `s` as a
vector/list and access its elements in the loop instead of changing its
size. R coerces between different types of object implicitly whenever necessary.
For example, if you have a data frame with columns of the same type, 
you can do many matrix operations on it because R coerces the data frame to 
a matrix when needed. This is very inefficient especially when you have a large 
data frame. A better way is first convert the data frame to a matrix,
and then operate on the matrix. 

3. Use `foreach(i=1:n) %dopar% {}` to do parallel computing if applicable
(you check my another post on parallel computing). Even if a `for` loop is
not parallelizeable, `foreach(i=1:n) %do% {}` is a better alternative. 

4. Use native code (e.g., Fortran, C/C++) for computationally intensive job if applicable. 
Though native code can increase the performance, there is overheading to invoke native code. 
It is less benefitial to invoke native code many times to do a smart part of job each time. 
You have to use command `R CMD SHLIB file_to_compile` to compile native code, 
and use the function `dyn.load` to load the shared library object. 
A more convenient way is to use R package "Rcpp" if you are confident about writing C++ code. 
However, you have to pay extra attention when you interact between R and other programming language. 
For example, passing arrays betwwen R and other languages can be tricky. 
For more information about this, refer to [this post](http://dclong.github.io/en/2012/05/r-interface-other-languages/).    

5. Split big data object (e.g., big data frame or matrix) to smaller ones,
and operate on these smaller objects.

6. Avoid creating too many objects in the each working environment. Not having
enough memeory can not only make your code run slower but also make it fail
to run if have to allocate big vectors. One way to do this is to writing
small functions and run your functions instead of running everything
directly in a working environment. Small functions make sure that objects
can be garbage collected quickly when they are no longer needed. If you leave them in
the working environment, they will never release memory seized. Partition
big work into smaller functions also helps reducing bugs. Aftering creating
and remove big data objects, you can also call the function `gc` manually to
collect garbage. 

7. Use `double(n)` to create a vector of length `n` instead of using code
`rep(0,n)`, and similar for others.

8. Use matrix instead of data frame wheneve possible. Actually data frame
cause problem in many cases. Only use data frame when necessary.


8. to be continued ...
