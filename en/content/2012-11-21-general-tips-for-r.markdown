UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: General Tips for R
Date: 2013-12-05 00:29:52
Tags: tips, R, generic, programming, argument
Category: Computer Science
Slug: general-tips-for-r
Author: Ben Chuanlong Du


1. Many R functions have lots of arguments which allows you get a full
control of their behaviors, so before you ask whether there is any R
function which have a little different behavior from a R function
you know, you'd better first check the arguments of the function you
know.

2. Many R functions are generic functions (e.g. `plot`, `residuals`, `coef`, etc), 
which means that they can be
applied to different types of objects, and the behavior varies
according to the type of objects.
