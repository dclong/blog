UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Linear Algebra in MATLAB
Date: 2012-12-04 00:00:00
Tags: algebra, programming, MATLAB
Category: Computer Science
Slug: linear-algebra-in-MATLAB
Author: Ben Chuanlong Du
Modified: 2012-12-04 00:00:00


1. Unlike most other programming languages, 
to get elements of an array in MATLAB, 
you have to parentheses to specify index. 
See more information in [this post](http://dclong.github.io/en/2012/05/containers-summary-in-popular-languages/).
If you want to get or set elements of a cell in MATLAB, 
you have to use curly braces. 
If you use parentheses to extract elements of a cell,
the result will still be a cell.

2. `vrrotmat2vec` converts a rotation matrix to its axis-angle representation. 
Conversely, 
`vrrotvec2mat` converts an axis-angle
(the axis do not have to be a unit one, as long as it is not a zero vector) 
representation of a rotation matrix to a matrix form.
There are also many other representations of a rotation matrix, 
e.g. Euler angle representation and quaternion representation.
`dcm2angle` and `angle2dcm` converts between a rotation matrix and its Euler angle representation; 
`quat2dcm` and `dcm2quat` converts between a rotation matrix and its quaternion representation;
`quat2angle` and `angle2quat` converts between the Euler angle representation 
and quaternion representation of a rotation matrix.

3. You can use `all` to check whether the elements of a vector 
(either a column vector or a row vector) are all `true` (or non-zero values). 
How ever if you apply `all` on an matrix or a multi-dimensional array, 
you will get vectors or arrays of boolean values depending on the dimension you specified. 
To check whether all elements of a matrix or multi-dimensional array are `true` 
(or non-zero values), 
you have use `all` more than once. 
For example, 
if `bmat` is a boolean matrix in MATLAB, 
you can use `all(all(bmat))` to check whether all elements of `bmat` are `true`. 
`any` works similarly to `all`.

4. You can use `size` to get the dimensions of an array. 
You can specify more output variables than necessary for `size`, 
and these redundant variables will have value `1`. 
If you specify less output variables than the dimension of the array, 
then the last output variable is the product of these left dimensions. 
To get the $k^`th`$ dimension of an array `a`, 
you can simply use `size(a,k)`. 
If you are just interested in the first two dimensions of a multi-dimensional array `a`, 
then you can use $[n_1, n_2, \sim]$ to extract the first two dimensions, 
where $\sim$ means that the left dimensions will be ignored.

5. To get the largest dimension of an array, 
you can use `length`, 
which is different from R that uses `length` to get the total number of elements in an array or list. 
To get the total number of elements of an array in MATLAB, you have to use `numel`.

6. `arrayfun` applies a given function to each element of an array,
which is similar to `apply` in R. 
`arrayfun` in MATLAB is not as convenient as `apply` in R 
which can also apply a function to marginals of an arrays instead of only elements of the array,
however there are some functions (mostly statistical summary functions) 
in MATLAB that allows you to work on specified marginals of an array, 
e.g. `size`, `max`, `mean` and so on. 
Use these functions can avoid inconvenient loops in MATLAB. 
Sometimes, 
you might want to pass extra parameters to the function 
that is to be applied to each element of an array. 
<To do this, please refer to ...>
Similar to `arrayfun`, `cellfun` applies a given function to each element in a cell array. 
From my experience, `cellfun` has advantage when its elements have different sizes (or even types), 
which make coding simpler. 
It does not seem to speed up the code compared to loops. 
There is also another `spfun` which applies a given function to non-zero elements of a sparse matrix.

7. In `R` a vectors is very flexible, 
and it can be a row vector or a column vector depends on different situations.
A vector in R is different from a matrix.
In MATLAB a vector is a matrix (either $1\times n\)' or $n\times1\)') 
and thus there are both column vectors and row vectors in MATLAB.
Function and operations usually behave differently on row vector and column vector in MATLAB. 
Since a vector in MATLAB is essentially a matrix, operations on vectors must
be compatible matrix operations. Since in Mathematics vectors are
column vectors by default, you'd better use column vectors in MATLAB
if both row and column vectors are OK.

8. You can use `isempty` to check whether an array is empty in MATLAB, 

9. `null` calculates the null space of a matrix.

10. `repmat` replicates and tile array.

11. `eigs` is frequently used to find the eigenvalues of sparse square
matrices. Because a sparse square matrix usually has a very large
dimension, it has a large amount (the same as its dimension) of
eigenvalues. Usually only a few of them are interesting. To
calculate the $k\)' large eigenvalue of a sparse matrix `spm`, you
can use `eigs(spm,k)`.

