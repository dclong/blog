UUID: c2d2b45c-d164-4bc5-9dd8-a8adb4472857
Status: published
Date: 2017-06-06 08:03:00
Author: Ben Chuanlong Du
Slug: stringi-tips
Title: stringi Tips
Category: Programming
Tags: programming, stringi, CRAN
Modified: 2017-09-06 08:03:00

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

1. It is suggested that you use the package `stringi` instead of string utilities in R base. 
    There are multiple reasons.
        
        - stringi has consistent namings and signatures
        - the behavior of functions in stringi is more reasonable from engineering perspective


## Regular Expression

1. Use `$1` instead of `\\1` to capture the nth capture group,
and similarly for other capture groups.

