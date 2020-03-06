UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-05-17 18:24:11
Author: Ben Chuanlong Du
Slug: sas-IML-tips
Title: SAS IML Tips
Category: Computer Science
Tags: programming, SAS, IML, matrix

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**



0. SAS/IML 9.3 (and later) supports the SUBMIT and ENDSUBMIT statements. 
These statements delimit a block of statements that are sent to another language for processing.
The SUBMIT and ENDSUBMIT statements enable you
to call SAS procedures and DATA steps without leaving the IML procedure.

1. 1:3 is a row vector, i.e., a matrix with 1 row


even if you can use a matrix like a vector, don't do it!!! use matrix format instead!!!
it seems that if you use a matrix like a vector, then you get a column vector (i.e., a matrix with 1 column).
So my suggestion is that avoid treating a matrix like a vector!!!
 

the sum function reduce a matrix to a scalar. There's not rowSums or colSums in the IML procedure (as in R).
You need use row/column reductions instead, e.g., m[+, ], m[, +].

similar to R, index start from 1 instead of 0


= similar to R, depends on the object exists or not, ...

when the dimension of 2 matrices does not match, 
the auto fill (expanding) is very tricky. My suggestion is that you should avoid using this. 
it seems that it expand the unmatched dimension ...
never do operations on matrices whose dimention does not match for element-wise operations!!!!

make it convention to return column vectors if doesn't make difference



2. unlike R, a row/column of matrix won't automatically turn into a vector

3. you cannot have empty vector/matrix in iml?




## IML

0. i identity j constant matrices ...

4. when a matrix has many columns (variables), 
it is not very convenient to specify variables to read in (if you want to read in almost all of them). 
A good alternative is to read in all numeric/character columns into IML procedure and then drop unnecessary columns.

7. sas, shape to reshape matrix, by row ...

1. delimiter (dlm=...) you have done this before, not sure why you cannot find it ...

1. dm statement is the display manager ...


2. In most programming languges, 
(sequential) code is run sequentailly. 
In SAS, 
modules (data steps and procedures) are run sequentially. 
However, code in data steps and procedures are not necessarily run sequentially.
There is a invisible loop in 
This means sometimes the order of some statments in procedures are not important. 
