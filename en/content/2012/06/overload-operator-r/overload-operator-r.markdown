UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Define Operator in R
Date: 2012-06-08 00:00:00
Tags: R, operator, overloading, override, programming
Category: Computer Science
Slug: overload-operator-r
Author: Ben Chuanlong Du
Modified: 2012-06-08 00:00:00

One thing I do not like R is that operations on String in R 
are not as convenient as in other programming langauges such as Java, Python and Ruby. 
In these 3 programming languages, 
you can simply use `+` to concatenate strings while in R you have to use the function `paste`.
The inconvenience result from unable to overload functions and operators in R. 
However, you can still define/override operators in R. 
For example,
the following code renew the definition of `+` to concatenate two strings.

    "+" = function(x,y){
        paste(x,y,sep="")
    }

