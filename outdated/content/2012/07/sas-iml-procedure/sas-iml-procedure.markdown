UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Tips for the IML Procedure in SAS
Date: 2015-02-19 15:30:52
Tags: SAS, matrix, programming, IML
Category: Computer Science
Slug: sas-iml-procedure
Author: Ben Chuanlong Du
Modified: 2015-02-19 15:30:52

<img src="http://dclong.github.io/media/sas/sas.jpg" height="200" width="240" align="right"/>


1. End an `IML` procedure with `quit;`.
You should never use `run;` to end an IML procedure
because it is used for calling user-defined functions in IML procedures.

2. Until SAS 9.3,
the `IML` procedure does not support overloading functions or recursive functions. 

3. You can define functions in the `IML` procedure, and the definition can be nested. 
That is you can define another function in a user-defined function. 
Note that the order of definition of functions matter (similar to C). 
A function must be defined before it is called. 

5. In the `IML` procedure, 
every data object is a matrix.
There is no concept of vector in the IML procedure like R does.
However, elements of a matrix can be accessed by a single index (e.g., x[3]),
so you can a matrix with 1 row/column as if it is a vector (as in R).
When a matrix has multiple rows and columns, 
you can still access its elements using a single index,
but be aware that elements are read by ROW 
which is different from R.
For example, 
the following code prints out 2 and 10.

```SAS
proc iml;
    x = {1 2 3, 10 100 1000};
    m = nrow(x);
    n = ncol(x);
    print (x[2]);
    print(x[4]);
quit;
```

7. In SAS, 
data sets are global which means that any procedure can use a created data set.
However, 
variables defined in a `IML` procedure is local, 
which means that variables defined in different `IML` procedures are not shared. 

8. You can define subroutines in a `IML` procedure. 
A subroutine is just a bunch of statment putted together. 
A subroutine does not have any argument, 
which means that it must invoked without parentheses. 
A module/function can have argument(s), 
and must be invoked with parentheses. 
Another important difference is that 
variables defined in a function takes effect only in the function 
while variables in a module takes effect in the whole `IML` procedure after its definition. 
Based on these comparision, 
function is more useful and better than module in the `IML` procedure. 

9. The slicing of vectors and matrices in the IML procedure is similar to that in R.

10. The name of a function in the `IML` procedure can exceeds 8 characters, but I am not
sure about the maximum length.

11. You can use `mattrib` to modify attributes of matrix in the `IML` procedure. 

1. You cannot print value of an expression directly in the IML procedure. 
You must either assign the value of the expression to a variable first or put the expression into parentheses. For example, 
proc iml;
	print 1+2;
quit;
raises an error while the following two ways of coding works.
proc iml;
	print (1+2);
quit;
proc iml;
	x = 1+2;
	print x;
quit;

2. You cannot use the `put` command to print value of variables in the IML procedure,
instead, 
you should use the `print` command. 
However, 
unlike `put`, 
`print` cannot format (e.g., date9.) output values.

12. You can `||` to combine matrix horizontally and `//` to combine matrix vertically. 

1. You can define a same module multiple times in an IML procedure.
The last defintion will be used.

1. By default, 
modules defined in an IML procedure is not visible to another IML procedure.
However,
you can store modules (to a library) defined in an IML procedure 
using the statement 
    store module=LocNonMissingRows; 
And you probably want to change the library for storing modules to a permanent one
before you storing a module.
You can do this using 
    reset storage=BlogDir.BlogModules; 
You can then use a stored module in aother IML procedure by loading it first.
    load module=LocNonMissingRows;


2. You can read files using the `%include` command in an IML procedure.
This means that you can define modules and put them into sas files 
and read them in when needed. 
This makes your SAS code more resuable and easier to manage.
You can also store user-defined modules 
and load them to be accessible later. 
However, it is not as convenient as `%include`. 
And store a module to a permannet location make it inconvenint to update these moduels.
It is suggested that you always use `%include` to read definition of modules from files.

## Questions

4. not very sure how to use default arguments in user-defined functions in the `IML` procedure.

