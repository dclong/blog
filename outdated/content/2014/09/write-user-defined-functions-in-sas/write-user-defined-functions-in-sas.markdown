UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-08-28 16:57:06
Author: Ben Chuanlong Du
Slug: write user-defined functions in sas
Title: Write User-defined Functions in SAS
Category: Computer Science
Tags: programming, SAS, user-defined function, `FCMP`

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

## FCMP Procedure

1. The maximum length of string allowed in 7911 
in functions defined in the FCMP procedure in SAS 9.2.
This can probably be control by parameters ...

1. Arguments of functions and call routines defined in this procedure 
are constant (read-only) and you cannot change their values.

2. Functions and call routines defined in the `FCMP` procedure
can be used in the data step and most procedures (e.g., `SQL`, `FCMP`, etc.) in SAS.

3. functions and call routines defined in the `FCMP` procedure 
can only take scalor or an array as arguments.


4. When you define a function returning a string value 
(using the `FCMP` procedure), 
make sure the return value has a long enough length!
Otherwise, 
the return value might get truncated.

5. You can read a data set into an array/matrix in the fcmp proc 
or write an array/matrix from the fcmp proc to a data set.

6. only good for simple functions,
event though you can pass arrays to a function/subroutine in fcmp, it is tedious to do so
the iml procedure is more programming friendly but is only targeted for matrix calculation.


7. You can use the functions and subroutines that you create in PROC FCMP with the DATA step, the WHERE statement, the Output Delivery System (ODS), and with the following procedures:
PROC CALIS
PROC COMPILE
PROC COMPUTAB
PROC GA
PROC GENMOD
PROC MCMC
PROC MODEL
PROC NLIN
PROC NLMIXED
PROC NLP
PROC PHREG
PROC REPORT COMPUTE blocks
Risk Dimensions procedures
PROC SIMILARITY
PROC SQL (functions with array arguments are not supported)
## Function

10. Call routines are declared within routine-declarations 
using the `subroutine` keyword instead of the `function` keyword. 
Functions and call routines have the same form, 
except call routines do not return a value, 
and call routines can modify their parameters.

2. A function (e.g., `symget`) in SAS returns a value while a routinue (e.g., `symput`) in SAS has no return value. 
You must prefix a routine with call to use it,
For example,

        x = symget('macro_variable')
        call symput('macro_variable', today())

For this reason, 
routines are also called call routines in SAS.

3. A character variables in the fcmp procedure has a fixed length. 
It is truncated if you assigned a longer string to it.
To avoid the problem, 
you can define the character variable to have a long enough length.
For exampel,
```SAS
length rv $32; 
```
