UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2014-10-23 15:52:51
Author: Ben Chuanlong Du
Slug: cartesian product in sas
Title: Cartesian Product in SAS
Category: Computer Science
Tags: programming, SAS, Cartesian product

Suppose we have 2 variables `x = ("a", "b", "c")` and `y = (1, 2, 3)`,
and we want to create a dataset containing the Cartesian product of `x` and `y` in SAS.
This can be achieved by manually input the Cartesian product of x and y in a data step.
However,
this is infeasible when `x` and/or `y` is very large or `x` and/or `y` can only be determined at run time. 
Here I provide 2 two general ways to generate Cartesian product of `x` and `y`.

## Use Outer Join of SQL

    data x;
        input x$;
        datalines;
    a
    b
    c
    ;
    run;

    data y;
        input y;
        datalines;
    1
    2
    3
    ;
    run;

    proc sql;
        create table cart as
        select * from x, y
        ;
    quit;

## Use Loop in Data Step

If one of the 2 variables (whose Cartesian product is to be calculated) 
has an explicit expression (e.g., $y_i = i$), 
then we can also use a loop in a data step to calculate the Cartesian product.

    data x;
        input x$;
        datalines;
    a
    b
    c
    ;
    run;

    data cart;
        set x;
        do y=1 to 3;
            output;
        end;
    run;

(Note: the loop trick a frequently used one in SAS to convert a "fat" data to a "thin" data.)


