UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Alike Objects/Functions in R
Date: 2013-12-05 00:19:25
Tags: programming, regex, data frame, matrix, R, warning
Category: Computer Science
Slug: alike-objects-in-r
Author: Ben Chuanlong Du


## Matrix VS Data Frame: 

1. The data in a matrix must be of the same type while different columns 
in a data frame can have different types.

2. A data frame is much bigger than a matrix with the same dimension. 
If possible, always use matrix instead of data frame to do computation.
Especially, 
when you creating arrays using the function `array`,
you should avoid using a data frame as the data source 
(even if all columns of the data frame have the same type).
A way to work around this is to first convert a data frame to a matrix 
and then use the matrix as the data source.

3. A data frame has names for rows and columns by default while a matrix not.

## `sub` VS `gsub`

1. The function `sub` substitute only the first occurence of the string 
that matches the given pattern 
while function `gsub` substitute all occurences of strings that matches the given pattern.

## `warning` VS `warnings`

3. The function `warning` shows a user-defined warning message 
while the function `warnings` displays previously generated warning messages.
