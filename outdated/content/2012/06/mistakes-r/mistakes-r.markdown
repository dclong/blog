UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2012-06-14 22:04:09
Slug: mistakes-r
Author: Ben Chuanlong Du
Title: Easy Made Mistakes when Writing R code
Category: Programming
Tags: vector, operator, mistake, programming, R, CRAN
Modified: 2015-05-14 22:04:09

<img src="http://dclong.github.io/media/r/mistake.jpg" height="200" width="240" align="right"/>

Being flexible is a two-side sword to R. 
While it make it convenient and productive to use R,
it is also very easy to make mistakes when writing R code. 
The following is list of mistakes that happens all the time.

1. Miss passed arguments  
This is often due the to "dots" argument (...). 
For example, I used to use VB a lot, so when I 
use the function `seq`, I wrote code like this

    seq(1,10,step=2)

Another example is 

    cat(data,file_name)

You thought you write `data` into the file `file_name`,
however you just print `data` and `file_name` to the
console. The annoying things about dots argument is that
it accept any kind of arguments. So whatever you pass to
a function accepting a dots argument, no warning or error 
about argument passing will be shown. The dots argument
opens the Pandor's box. <!---'-->

2. Global variables  
While you can assign values to global variables using `=`,
`<-` and `->` inside a user-defined function, the change (of the global
variable) is only in effect in the duration of the function. 
When the function ends, the change is no longer in effect. 
In another words, the global variable remains unchanged 
outside the function. To make the change in effect outside the 
function, you must use `<<-` and `->>` to assign values to the
global variable. 

3. Priority of operators
The colon (:) operator precede over arithmatic operators 
such as +, -, *, / and so on. However, [] precede over the 
colon operator. When you write code `1:n-1`, you thought
you get a vector from `1` to `n-1` while you actually get
a vector from `0` to `n-1`.

4. Miss used functions
The function `length` is used for querying length of 
vectors not the length of characters. For the later purpose,
use the function `nchar`.

5. Use && or || on vectors  
For vector operation, you should use & and |.

5. Use vectors or missing value as conditions  
For if and while statement, the condition must be a non-missing
scaler (a vector of length 1).

6. Use `*apply` functions to operate on rows of data frames.
A row of data frame is still a data frame (with 1 row). R is 
evil in the sence that it coerce data type wheneve necessary 
without noticing users. ...

