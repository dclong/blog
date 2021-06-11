UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Inverse of a Special Class of Matrices with High Dimensions
Date: 2010-05-30 22:12:02
Tags: inverse, fun problems, matrix, math, statistics, R, high dimension
Category: Fun Problems
Slug: inverse-of-matrix
Author: Ben Chuanlong Du
Modified: 2013-10-30 22:12:02


<img src="http://www.legendu.net/media/math/matrix-inverse.png"
width="200" height="160" align="right"/>

One day, my officemate Tieming asked me about a problem that she met in her research. 
Suppose $\boldsymbol{B}$ is a symmetric matrix of huge dimension 
and $\boldsymbol{D}$ is a diagonal matrix with nonnegative diagonal elements. 
The inverse of $\boldsymbol{B}$ is already known, 
how can we calculate the inverse of $\boldsymbol{B}+\boldsymbol{D}$ efficiently? 
I thought for a while and found a good way to solve the problem. 
See solution in [Inverse of Matrix](http://dclong.github.io/media/inverse-of-matrix.pdf).

I haven't implemented the algorithm yet, 
but a roughly estimate of the complexity of this algorithm tells me that even R can handle it. 
I will write a R function to do this later when I have time.
