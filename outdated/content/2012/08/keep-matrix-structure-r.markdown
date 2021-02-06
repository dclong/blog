UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-05-14 22:04:52
Slug: keep-matrix-structure-r
Author: Ben Chuanlong Du
Title: Keep Matrix Structure when Extract a Row/Column from a Matrix
Category: Programming
Tags: programming, data structure, algebra, matrix, R, vector, CRAN

[Abuse of Vector in R]: http://dclong.github.io/en/2012/05/abuse-vector-r/
I talked in the post [Abuse of Vector in R]() that 
it is often the case that we want keep the matrix sturcture when 
extracting a row/column from a matrix,
i.e., we often want to return a matrix with 1 row/column when extracting 
a row/column from a matrix. 
By default R returns a vector when you extract a row/column from a matrix.
To override this behavior, you can specify the option `drop=FALSE` when 
extracting submatrix from matrix. A illustrative example is given below. 

    a = matrix(1:16,nrow=4)
    a[1,,drop=FALSE] -> b
    b
    [,1] [,2] [,3] [,4]
    [1,]    1    5    9   13

On the contrary, if you want to keep the sturcture of a matrix with multiple
rows and columns but convert a matrix with 1 row/column to a vector in R, 
you can the function `drop`. See the following example. 

    drop(a)
    [,1] [,2] [,3] [,4]
    [1,]    1    5    9   13
    [2,]    2    6   10   14
    [3,]    3    7   11   15
    [4,]    4    8   12   16
    drop(b)
    [1]  1  5  9 13

