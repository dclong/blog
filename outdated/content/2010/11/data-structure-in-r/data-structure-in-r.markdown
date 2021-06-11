UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2010-11-09 18:57:36
Slug: data-structure-in-r
Author: Ben Chuanlong Du
Title: Data Structure in R
Category: Programming
Tags: programming, list, data structure, container, matrix, vector, R, CRAN
Modified: 2016-07-09 18:57:36

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
## Vector, Matrix and Array

1. A matrix in R is actually a vector with a `dim` attribute. 
This means that the fastest way to switch between a vector and matrix 
is to modify the `dim` attribute. 
Also since a matrix in R is essentially a vector, 
you have to treat it as a 1-dimensional array 
when you pass it as an argument into C/C++ code .

## Data Frame

1. A data frame is essentially a list with columns being elements.

## List

1. [] slicing vs [[]] 

## Other

1. To convert a matrix `x` to a list with columns being elements of the list, 
you can use `as.list(data.frame(x))` 
(Notice that `as.list(x)` does not work in this way. 
This is another example demonstrate the difference between data frame and matrix.). 
Though it is neat way, 
it is not the fastest. 
A faster way is to use `lapply`, 
e.g., you can use `lapply(seq_len(ncol(x)), function(i) x[,i])` to achieve the same purpose.
On the contrary, 
you can use `do.call` to convert a list (of vectors/matrices) to a matrix. 
The following is such an example.
```R
> do.call(cbind, list(matrix(0,2,2),matrix(1,2,2)))
[,1] [,2] [,3] [,4]
[1,]    0    0    1    1
[2,]    0    0    1    1
```

2. We can put functions into a list and then call functions 
using their index, 
which can be very convenient sometimes. 
To put functions into a list, 
we can use either function `list` or `c`. 
However, 
there're some differences between functions `list`, `as.list` and `c`.
Function `as.list` coerce an object to a list object. 
If the argument passed to function `as.list` is already a list object, 
then it does nothing. 
Function `list` puts objects into a list. 
If an argument passed to function `list` is already list object, 
it will still put this list object into a list. 
Basically, function `c` combine objects passed to it. 
However, if a list and a vector are passed to it, 
each element of the vector becomes an element of the list object (argument). 
If you want the entire vector to be an element of the list, 
you must first use function `list` to put it 
into a list and then use function `c` to combine these two lists.

3. Most built-in functions in R work differently on data frames 
from vectors (matrix and array are similar to vectors), 
because many of them are written in S3 method. 
You have to be very carefully about the object that you are working with. 
For example, 
you can use `apply` on both a matrix and a data frame. 
But if you apply a function on the each row of a data frame, 
elements on each row will first be coerced to the same type and then be operated on. 
Since the data in a data frame is usually not the same type, 
this can lead to mistake easily.

4. Sometimes you must be very careful about vectors. 
You need to know how the operations work. 
That's very important!! 
For example `|` and `||` work different on vectors.

5. Function `rep` is useful to get a vector that has a clear structure.
Be careful that the option `each` can not be a vector. 
The role of option `each` is played by `times` in vector case.

6. Function `aperm` is very useful to transpose an array.

7. Though a matrix and a data frame are both rectangular in R, 
they are fundamentally different. 
All elements in a matrix have the same type, 
while elements in a data frame do not have share the same type.
It is only required that elements in the same column of a data frame have the same type. 
A column in a data frame usually represent a variable. 
For this reason, 
data frames are frequently used for data environment for fitting models. 
However, sometimes we want to work on rows instead of columns 
(e.g. when fitting model for gene for microarray data), 
then it is not convenient to use data frame. 
You can convert a data frame to a matrix (if possible) by `as.matrix`.

8. The difference among `apply`. `tapply`, `lapply` and `sapply`.
`apply` can be used in many cases and the marginal dimension need to be specified. 
The specified function is applied over the specified margins, 
i.e. for each combination of the specified margin/dimension combination, 
the specified function is applied on the left dimensions. 
For example, `apply(aMatrix,MARGIN=1,FUN=aFun)`, 
where `aMatrix` is a matrix of dimension $n_1\times n_2$ 
and `aFun` is a function, 
means applying `aFun` over the first dimension (which is row) of `aMatrix`, 
i.e., for each $i=1,\ldots,n_1$ applying `aFun` to `aMatrix[i,]`;
`apply(threeDArray,MARGIN=3,FUN=aFun)`, 
where `threeDArray` is an array of dimension $n_1\times n_2\times n_3$ 
and `aFun` is as before, 
means applying `aFun` over the third dimension, 
i.e. for each $i=1, \ldots,n_3$ applying `aFun` to `threeDArray[,,i]`;
`apply(threeDArray, MARGIN=C(1,2),FUN=aFun)`, 
where `threeDArray` and `aFun` are as before, 
means applying `aFun` over the first and second dimension, 
i.e., for each $i=1,\ldots,n_1$ and $j=1,\ldots,n_2$, 
applying `aFun` to `threeDArray[i,j,]`.  
`tapply` can be used according to factor levels 
which requires a specific factor 
(the INDEX argument can also be a vector and it will be coerced to a factor automatically) index of course. 
`lapply` and `sapply` are very similar to each other and `sapply` is more friendly. 
They can be used to vectors, data frames and lists.

9. If you just want to calculate the row/column means/sums, 
then there is no necessary to use `apply`, 
instead, 
you can use `rowMeans`, `colMeans`, `rowSums` and `colSums`. 
`rowMeans` and `rowSums` calculate the mean and sum of each row respectively.

10. A matrix in R has both row names and column names. 
A vector in R also have names but not row names nor column names. 
There's no problem to treat a matrix as a vector but error will occur 
if you treat a vector as a matrix. 
To avoid error, 
you must use function `as.matrix` to change the vector into a matrix 
and then do operations on the matrix.

11. In R, by default a matrix will be filled by columns. 
If you have to deal with matrices and vectors at the same time, 
e.g. you want to add a vector onto a matrix or so, 
you'd better define the matrix with number of rows equals the length of the vector.

12. Function `drop` can delete dimensions of an array with only one level, 
which can be convenient when displaying results.

13. Vectors in R can be interpolated both as row vectors and column vectors according to different cases, 
which is for convenience
because whether row or column vectors will be used depend on
conventions. 
However, 
this might cause very serious problems, some times. 
For example, 
if we want to calculate the trace of $\boldU\boldV\)' 
where $\boldU$ and $\boldV$ are both column vectors here, 
we can calculate $\boldU'\boldV$ instead for convenience. 
So we might write code $u\%*\%v$ to do this. 
A potential serous problem is that $v$ might be a $$1\times n$ matrix
(which is essentially a row vector) in R, 
and will result a $n\times n$ matrix instead of a number. 
So you write code
(especially for important projects and so on), 
you'd better avoid using these code which can introduce ambiguity. 
For example, 
instead of using $\boldU\'\boldV$, 
we can use `sum(u*v)`, 
then no matter what kind of vectors, 
either row vector (a matrix with one row in R) or column vector, 
`u` and `v` are, 
we will always get the right answer.

14. There are many ways to construct a vectors 
(double, character and so on) with a given length in R. 
To construct a list with a given length, 
there are two ways. 
The first way is to first construct a vector of the given length 
and coerce it to a list using `as.list`.
For example, 
you can use `as.list(rep(0,3))` to construct a list with length 3 in R. 
The other way is to using `vector`. 
For example `vector("list",3)` constructs a list of length 3 
with all elements being `NULL` for you.

15. If you have a list called `myList` 
and you use `is.vector(myList)` to check whether it is a vector of not, 
you will get a result `TRUE`.
This is not surprising, 
because a list in R is actually a vector with mode `list`. 
The default value of option `mode` in `is.vector` is `any`, 
that is why you get the answer `TRUE` for the code `is.vector(myList)`. 
The usual vectors we talk about are vectors of `numeric`, `character` and so on. 
So to check whether an R object is a usual sense vector (i.e. not a list), 
you can code like `is.vector(myList,"numeric")`.

16. In many situations a vector is equivalent to a matrix with 1 row/column. 
However, there's difference between them. 
The fundamental difference is that they are of different data types. 
So for many functions, 
if you pass a vector to it you get vector, 
and if you pass a matrix with (1 row/column) to it you get a matrix (with 1 row/column).

17. A null data frame for column combination operation 
is a data frame/matrix 
(Strictly speaking, 
the null data frame is data frame, 
but an empty matrix can be coerced to an empty data frame.
) with 0 column 
(use `matrix(nrow=n,ncol=0)` 
to generate a matrix with 0 column) 
and the same number of rows with data frames involved in the operation. 
Similarly, 
a null data frame for row combination operation is a data frame 
with 0 row and the same number of columns 
with data frames involved in the operation.

18. A convenient and efficient way to repeat rows of a matrix/data frame is to extract rows repeatedly.

19. `nlevels` returns the number of levels of a factor, 
which is equivalent to `length(levels(aFactor))`. 
However, 
the former way is faster and more convenient than the later one.


27. good idea to pass column names if data format is not consistent
also applies to other programming languages

5. A very tricky problem: R silently coerce data between different types if needed, 
this is again proved to be a very bad idea. 
For example integers and boolean value, in your problem, that's very bad ...
actually this might not because of the silent coerce problem, 
[] as a function might takes different arguments, the problem is that R never checks type of argument,
this is error-prone,
in future, you should pay extra attension to [], never mix different types ... 
a safe is to alway check the type in the function which is tedious ...

22. mixing integers and row names is a bad idea ...
if you pass integers as rownames ...


1. In R, max/min, etc. does not keep matrix structure.
If you want to keep matrix structure, use `ifelse` instead.

2. cbind, specify colnames
cbind(x, Scenario=T)
cbind(x, "name with space"=T)
similarly for rbind

