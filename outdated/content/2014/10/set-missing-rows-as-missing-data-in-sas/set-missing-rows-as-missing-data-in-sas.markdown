UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-03-13 00:59:10
Author: Ben Chuanlong Du
Slug: set missing rows as missing data in sas
Title: Insert Rows Missing as Missing Records in SAS
Category: Computer Science
Tags: programming, SAS, missing
Modified: 2015-03-13 00:59:10

I recent come across a problem.
I have a table `A` in SAS with columns `x`, `y` and `z`.
The table almost exhaust the Cartesian product of `x` and `y` but has some rows missing.
I need to create macro variables with the Cartesian product of `x` and `y` as names 
and `z` as corresponding values.
If a combination of `x` and `y` is missing from the table, 
then set it as missing value.
I came up with 2 approaches to this problem.
The first way is to create macro variables based on table `A`,
and then loop through the Cartesian product of `x` and `y` 
to check whether a macro variable exists or not (with the help of `%symexists`).
If a macro variable does not exists,
then create it with missing value.
The second approach is to complete table `A` with missing rows (with the help of left/right join in SQL)
and then create macro variables based on it.
The first approach is a little bit tedious
and took the second approach. 
Here I demonstrate in detail how I did it.

To make illustration convenient,
suppose `A` is as below,

|x|y|z|
|:-:|:-:|:-:|
|a|1|0.33|
|a|3|0.91|
|b|1|1.38|
|b|2|8.7|
|b|3|5.1|
|c|2|5.78|
|c|3|8.6|

and 
`x = (a, b, c)` 
and 
`y = (1, 2, 3)`
.
First, 
we need to create a table of the Cartesian product of `x` and `y`.
Please refer to [this post]() about how to do it. 
Now suppose we have the Cartesian product of `x` and `y` in the table `cart`,
we can complete missing rows with `z` set as missing value using the following SQL code.

    proc sql;
        select
            cart.*,
            A.z
        from 
            A
        right join
            cart
        on
            A.x = cart.x
        and 
            A.y = cart.y
        ;
    quit;
