UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2017-04-09 23:47:21
Slug: traps-in-r
Author: Ben Chuanlong Du
Title: Traps in R
Category: Programming
Tags: R, global variable, programming, traps, CRAN
Modified: 2017-04-09 23:47:21

1. [Zero-Length Vector Issue in R](http://www.legendu.net/en/blog/zero-length-vector-issue-in-R/)

1. A really tricky problem about is global and local variables. 
You can use any global variable in a user-defined function, 
which is true at least in R with version 2.13 or older. 
For example if you have defined a global variable `a`, 
you can use variable `a` directly in user-defined functions. 
However, 
you cannot use `=`, `<-` or `->` to mutate global variables. 
Whenever you use these three operators, 
R thinks that you're either creating a new variable 
(if the variable is not defined before), 
or you're updating the value of an existing variable 
(if the variable already exists). 
For example, 
suppose there's still a global variable `a` in the R workspace. 
You can use variable `a` directly in user-defined functions, 
but if you use `a=2` (or `a<-2` or `2->a`) in the user-defined function, 
R won't think that you're updating the value of the global variable, 
instead it things that you're creating a new local variable `a`. 
For this reason, 
if a global variable `a` exists 
while there's no local variable `a` in a user-defined function, 
error message will be shown if you use `a[1]=1` (or other equivalent ways)
and try to run the function, 
because by doing this you're telling R 
that you want to update the value of the first element of local variable `a` 
but local variable `a` doesn't exist. 
If you really want to update the value of (or create) a global variable 
in a user-defined function, 
you should use operator `->>` or `<<-`. 
For example, 
if you want to update the value of global variable `a`, 
you can use `a<<-2` (or `2->>a`). 
Now you have seen that global variables can screw the execution result 
of your own defined function easily. 
The situation can become even trickier and thus harder to debug, 
if you define a local variable in a branch 
(e.g. a branch of `if()...else...` statement) of the code 
while forget to define the same local variable in other branches 
and at the same time a global variable with the same name exists. 
My suggestion is that you first remove all global variables 
in the R workspace if there is any, 
and then run your program. 
In this way,
you can avoid confusion resulting from global variables.

2. Always be careful when there is an operation based on two vectors.

3. Sequence operator (`:`) has a higher priority over arithmetic operators (`+`, `-`, `*`, `/`), 
but a lower priority than the power operator (`^`) and element operator (`[]`).

4. Expression `2^1^2` is calculated from right to left in R.

5. Avoid use function `median` if you can, 
because it returns two numbers when the vector has an even number of elements, 
which is usually not what statisticians want 
and might result in serious problems in many cases. 
Actually we can always use `quantile(x,prob=0.5)` to get the median of vector `x`.

6. For functions which takes `...` as one of its parameters, 
we have to be very careful.
Because this kind of functions accept any number and any kind of parameters. 
So sometime you think that you are passing values to some argument of a function, 
but actually not. 
For example if you use `seq(0,100,step=2)` you might be in trouble. 
The right command that works in this situations can be `seq(0,100,by=2)`.
Nowadays, 
there are many different programming languages, 
and all of them have their own advantages and disadvantages. 
So we might have learned several different programming languages. 
And we are probably told not to remember all functions by heart, 
instead, we can check the syntax of functions when we have to use them. 
This is an efficient way which is also my way to learn programming languages.
However, 
this might can lead to problems sometimes. 
Because we're lazy, 
we might just guess syntax of functions that we're going to use. 
This is not a big problem in complied languages, 
because anyway the syntax will be checked later 
and what is more usually we have good editors to help us (e.g. eclipse for Java). 
R is a interpreted language, 
so even if there're syntax errors you might can still run it. 
And because of high flexibility of R, 
it is very hard to editor for R to find these tricky mistakes. 
So if we can, 
we should always at least check the arguments of the functions 
we are going to use in R. 
A simple way is just to use function `args`. 
If we have used `args` to check the arguments of function `seq`, 
then the chance for us to make the mistakes mentioned above is very small. 
Also it is recommended to always pass arguments to functions 
using argument names, 
i.e., 
using the form `argname1=argvalue1` to pass arguments to functions.

7. To get the length of a vector, 
you can use `length`. 
However, 
to get the length of a string, 
you should use `nchar`.

8. `round` in use the close even number strategy which might not what you expect, 
so be careful when you use it.

9. In a `for` loop, 
the loop vector is immutable while the loop is running. 
This means that R calculates the loop vector only once, 
an for this reason, feel free to ...

10. It is often that one want to build a larger array based on small arrays. 
For example, 
one build a 3-D array by repeating a 2-D matrix. 
You should be careful if the "matrix" you used is obtained by reading data from a file, 
because it's really a data frame often times. 
All elements in an array have the same type, 
while elements in a data frame do not have to share the same type. 
For this reason, 
it is really inefficient to build an array based on a data frame 
(if even all columns of the data frame share the same type). 
If you do this for a large data frame, 
R can choke. 
A good way is to first convert the data frame to a matrix using `as.matrix`, 
and then build the array you want based on the matrix.

11. R runs commands in `Rprofile.site`, 
then loads the save image (if any), 
and then runs `.First` (if exists). 
This means that if you want to run something which depends the R image, 
you must put it into the `.First` instead of `Rprofile.site`. 
However, 
it seems that there is a bug with Rstudio (at least before version 0.94), 
who does not follow the above order when it starts R.

12. Usually the number of levels of a factor equals the number of distinct elements in the factor, 
however, 
it doesn't have to be.
Except factitious ones, 
the situation that the two quantities are not the same usually happens 
after subsetting a data frame or factor. 
If the number of levels of a factor is not the same 
with the number of its distinct elements, 
you can apply `factor` on itself to get a factor with the two quantities identical.

13. Never use a factor for the index of subsetting, 
because if used it will be coerced to an integer vector 
which is usually not what people expect.

14. R allows lazy evaluation to some extent, 
e.g., 
as almost all other languages do, 
boolean expression in R are evaluated using lazy evaluation. 
What is more important is that missing arguments are allowed for R functions 
(i.e. you do not have to pass values to some arguments, 
and everything runs OK as long as missing arguments are not involved in computing), 
and missing arguments can even be further passed to sub-functions 
(Everything runs OK as long as missing arguments are never used in computing). 
Here is an illustration.
```R
var = function(x, y = NULL, exact = FALSE, na.rm = FALSE, use) {
    if (exact) {
        return(mean((x - mean(x))^2))
    }
    stats::var(x = x, y = y, na.rm = na.rm, use = use)
}

var(c(1, 2, 3, 4))
```

```
[1] 1.667
```
However, 
R does not fully support lazy evaluation, 
and you shall not expect code involve advanced lazy evaluation 
(need an example there ...) to work well. 
Part of the reason for not supporting advanced lazy evaluation in R 
is that it invites many problems and can probably result in fetal mistakes.

15. Because of the way that computers stores double values, 
there are always tiny storing errors associated with double values. 
So if you want to compare whether a double value belongs to a range 
(a point is a closed interval with equal limts), 
you can change the limits (depends on what your want to do) 
of the range slightly to avoid storing errors.
