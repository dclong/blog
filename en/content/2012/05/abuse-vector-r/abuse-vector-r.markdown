UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Abuse of Vector in R
Date: 2012-05-16 00:00:00
Tags: programming, matrix, data sturcture, data, vector, R
Category: Computer Science
Slug: abuse-vector-r
Author: Ben Chuanlong Du

R is a language that is friendly to vector operation, 
so vector is an important data structure in R. 
A single data (of basic types, e.g., numeric or character) is essentially a
vector of length 1. A matrix or an array in R is essentially a vector. 
R make extensive use of vectors. A vector in R can either be a column vector or
a row vector depending on how you write the code. This is perhaps OK with most
people though it invites chances to make mistakes. One annoying thing about
vector is that When you extract a row or a column from a
matrix, you get a vector. 
I think this is one place that R abuse vectors. When you extract a sub matrix,
you want it to be a matrix as well most of the time. Even if you do want a
vector, most functions in R coerce a matrix to vector automatically, so return a
matrix instead of a vector doesn't hurt. MATLAB goes to another
extreem on vectors. There is no separate data structre for vector in MATLAB. 
A vector in MATLAB is either a matrix with 1 row or a matrix with 1 column. 

R is famous for its simple and flexible syntax, however, it's too
flexible and as coinsequence that it's slow compared to many other programming 
languages, and it's easy to make tricky mistakes in R. 
