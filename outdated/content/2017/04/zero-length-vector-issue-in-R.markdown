UUID: 8ff87f2a-2070-4701-9062-1fd2efd9a400
Status: published
Date: 2017-04-10 19:21:27
Author: Ben Chuanlong Du
Slug: zero-length-vector-issue-in-R
Title: Zero-length Vector Issue in R
Category: Programming
Tags: programming, CRAN, R, issue, trick, trap, vector, zero-length, 0-length

The corner case of 0-length vectors is not well considered in R. 
It causes issues in several situations. 
First, `1:n` is probably not what you want when `n = 0`. 
Second, `df$col = 0` throws error when `df` is an empty (0 row) data frame.
To avoid these issues, 
it is suggested that you write more robust R code. 

```R
# use 
seq_len(n)
# instead of 
1:n
```

```R
# use 
for (i in seq_len(n)) {
    ...
}
# instead of 
for (i in 1:n) {
    ...
}
```

```R
# use 
df$col = rep(x, nrow(df))
# instead of 
df$col = x             
```

Strings function in base R do not behavior well when zero-length vectors are involved. 
For example, 
`paste('a', character(0))` returns a character vector of length 1 
rather than length 0. 
Functions in the `stringi` packages works well when zero-length vectors are involved.
For example, the code below returns a 0-length vector.
```
library(stringi)
'a' %s+% character(0)
```
It is suggested that you always use string functions in the `stringi` package 
rather than string functions in base R.

