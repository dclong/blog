UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2016-06-11 17:37:32
Slug: rcpp-questions
Title: Some Questions About R
Category: Computer Science
Tags: questions, Rcpp, programming, C++

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
1. rstudio server, read.table('clipboard') does not work (clipboard not due to server ...)

2. how to perserve C++ object after C++ function terminates when using Rcpp?

3. is it possible to capture c++ output in rcpp?

4. is RNGScope thread safe?

5. because with RcppArmadillo, subview, matrix ...

6. is there a way to check whether an Rcpp compiled object is valid?

7. Rcpp Module mustStart=T?

8. how to keep an C++ object after c++ function is terminated? use pointer?

9. uniform_real_distribution, etc., 
do they change internal state after generating a random number?
you can check this using 2 different objects with the same parameters.
see whether you get the same sequence of numbers using 1 instance and using 2 instances in turn.

1. R里面的特殊数据, e.g.,  NA, NaN, Inf, etc. pass to C++, what happens?
