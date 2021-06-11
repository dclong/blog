UUID: 51c3803b-93ae-494c-8354-f320c1613be9
Status: published
Date: 2016-07-10 20:33:23
Author: Ben Chuanlong Du
Slug: comparing-values-involving-NA-in-R
Title: Comparison of Values Involving NA in R
Category: Programming
Tags: programming, R, comparison, NA, missing, CRAN
Modified: 2016-07-10 20:33:23

The best way to compare values containing `NA` in R is to define customized comparison functions.
Here is an example.
```R
equals = function(x1, x2, na_as_na = FALSE, reverse = FALSE) {
    if (reverse) {
        return(!equals(x1, x2, na_as_na, reverse = FALSE))
    }
    if (na_as_na) {
        return(x1 == x2)
    }
    ifelse(
           is.na(x1), 
           ifelse(is.na(x2), TRUE, FALSE), 
           ifelse(is.na(x2), FALSE, x1 == x2)
       )
}
```
