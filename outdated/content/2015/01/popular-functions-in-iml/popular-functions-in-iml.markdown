UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-01-02 18:09:00
Author: Ben Chuanlong Du
Slug: popular-functions-in-iml
Title: Popular Functions in IML
Category: Computer Science
Tags: programming, SAS, IML, function, module
Modified: 2015-03-02 18:09:00

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**


`dif`: lagged difference, keep missing values, may or may not what you want,
can use negative lag,
always return a matrix, with columns corresponding to differences of specified lags
if only 1 lag is specified, return a matrix with 1 column.

`lag`: the usage is similar to dif

the `dif<n>` and `lag<n>` are for the data steps

`loc` equivalence of `which` in R

`j`

`repeat`
REPEAT Function
Returns a character value that consists of the first argument repeated n+1 times.

colvec
rowvec

`shape`
SHAPE Function
SHAPE (matrix, nrow <, ncol> <, pad-value> ) ;
The SHAPE function reshapes and repeats values in a matrix.

`choose`, kind of like `ifelse` in R

`cuSum` 

`cuProd` 

`diag`


`sample` (x <, n> <, method> <, prob> ) ;

`ssq`

`shape` for numeric

`cshape` for character

`concat` like paste in R

`change` like replace


`qntl` Call for sample quantile

`quantile`

`corr`

`standard`

`var`

`mean`

`mod`

EXPANDGRID Function
EXPANDGRID (x1, x2 <, x3> …<, x15>) ;
The EXPANDGRID function is part of the IMLMLIB library. The arguments to the EXPANDGRID function are $k$ vectors, $2 \leq k \leq 15$. The EXPANDGRID function returns a matrix that contains the Cartesian product of elements from the specified vectors. If the $i$th argument has $n_ i$ elements, the return matrix has $\Pi _{i\leq k}n_ i$ rows and $k$ columns.

ROWVEC Function
ROWVEC (matrix) ;

SHAPECOL Function
SHAPECOL (matrix, nrow <, ncol> <, pad-value> ) ;
The SHAPECOL function reshapes and repeats values in a matrix. It is similar to the SHAPE function except that the SHAPECOL function produces the result matrix by traversing the argument matrix in column-major order.
## String

strip works both in the data step and the iml procedure

