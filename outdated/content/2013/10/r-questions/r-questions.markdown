UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2013-10-20 20:30:22
Slug: r-questions
Title: Some Questions About R
Category: Software
Tags: questions, CRAN, Rcpp
Modified: 2016-11-20 20:30:22

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
1. rstudio server, read.table('clipboard') does not work (clipboard not due to server ...)
this is a probablem of vimperator, not rstudio ...

## Rcpp
2. how to perserve C++ object after C++ function terminates when using Rcpp?

3. is it possible to capture c++ output in rcpp?

4. is RNGScope thread safe?

5. because with RcppArmadillo, subview, matrix ...

6. is there a way to check whether an Rcpp compiled object is valid?


7. Rcpp Module mustStart=T?

8. how to keep an C++ object after c++ function is terminated? use pointer?

9. do.call('&', list(j1)) is not as expected, the best way to this?
do.call('|', list(j1, j2))

## Misc
10. sometimes 
`values = setdiff(values, "")`
and 
`values = values[values!=""]`
are exchangeable,
but which is better?
I guess the latter one is faster,
check this ...

## Calls
1. is it possible to pass argument by ref? even so, you'd be careful!

2. how to parse R code to extract function definitions? 
It seems that peperr::extract.fun can do this partially
