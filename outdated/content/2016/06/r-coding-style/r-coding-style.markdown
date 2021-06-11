UUID: 7384a485-a364-4423-96ef-8e31ae546247
Status: published
Date: 2016-10-23 16:41:21
Author: Ben Chuanlong Du
Slug: r-coding-style
Title: R Coding Style
Category: Programming
Tags: programming, R, CRAN, formatting
Modified: 2016-10-23 16:41:21

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

1. You can use the function `tidy_souce` in the R package `formatR`
to format R code.
```R
tidy_source('unformatted.r', file = 'formatted.r')
```
However, 
there is a bug in the package `formatR`.
For example, 
the `formatR` fails to work with the following code.
```R
if { # this is comment
    ...
}
```

2. Avoid changing the type of object.

