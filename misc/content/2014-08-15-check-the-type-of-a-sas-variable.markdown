UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2014-10-22 16:59:20
Author: Ben Chuanlong Du
Slug: check-the-type-of-a-sas-variable
Title: Check the Type of a SAS Variable
Category: Computer Science
Tags: programming, SAS, data type, variable, proc content, putn

**
Things on this page are 
fragmentary and immature notes/thoughts of the author.
It is not meant to readers 
but rather for convenient reference of the author and future improvement.
**


1. SAS has only 2 data types, numerical and character. 
Date, time and datetime, etc. are all represented as numerical values inside SAS. 
You have to manually format them to display more meaningful soutput.

2. prefer numerical values to character values: 
first, character variables has a default length of 8 which is usually too short
while numerical values are 64 bits. 
Second, the IML procedure accepts matrices only, 
so you cannot mix numeric and character values in the IML procedure.

3. prefer nested than distinct (many) levels,
for example, instead of 1-9, 
prefer 1-3 inside another factor of 3 levels. 
This is a performance concern. 

1. There is no concept of return types when you use macros in SAS,
as everything is text to macro. 
However, when you use functions in a data step or other procedures,
the return type of functions matter.

1. SAS implicitly convert a numeric value to a character one
and vice versa.
You should be very careful about implicit conversion 
from a numeric value to a character one. 
When the numeric value is too short (with length < 12), 
the returned character value is right aligned with leading blanks;
when the numeric value too long (with length > 12), 
the returned character value has a scientific representation.
It is suggested that you use a long enough format 
(`32.` is the longest format that SAS supports and is thus suggested)
to convert a numeric value to a character one 
and then strip out (using the function `strip`) the leading blanks.
For the same reason, 
you'd better alwasy strip a character variable 
converted from a numeric variable using the format `k.`.
	
2. I think it is very silly to define as macro variable with numerical or character suffix, 
because a macro variable does not have a type.

4. SAS can handle integers with lengths of at most 32.

5. A tricky thing in SAS is 
whether a semicolon in needed in certain statements (e.g., a SQL statement).
This become more tricky when you use macros functions.

6. The statement `retain` causes a variable created by an `input` or assignment statement 
to retain its value from one iteration of the data step to the next.
It is helpful when you want to operate on 2 consecutive records at the same time,
e.g., 
when you want to calculate lag/difference of variables.



## Check the Type of Variables

You can use the procedure content to output descriptions (e.g., type of columns) of a data set.
For example,
the following code checks the types of output of the function `putn`.

    data date;
        d = "07Aug2014"d;
        x1 = putn(d, "date9.");
        x2 = putn(d, "date7.");
        x3 = putn(d, "yymmdd10.");
        x4 = putn(d, "yymmdd8.");
        x5 = putn(d, "yymmdd6.");
        x6 = putn(d, "mmddyy6.");
        x7 = putn(d, "yymmn.");
        x8 = putn(d, "yymmddn8.");
    run;

    proc contents data=date out2=dd;
    run;

    proc print data=dd;
    run;

The output containing types of variables is as below.

|Alphabetic List of Variables and Attributes||||
|:-------------------------------------------:|::|::|::|
|#|Variable|Type|Len|
|1|d|Num|8|
|2|x1|Char|200|
|3|x2|Char|200|
|4|x3|Char|200|
|5|x4|Char|200|
|6|x5|Char|200|
|7|x6|Char|200|
|8|x7|Char|200|
|9|x8|Char|200|

From the results above we can see that
when converting a numeric value to format `date9.`, `date7.`, `yymmdd10.`, `yymmdd8.`, `yymmdd6.`, `mmddyy6.`, `yymmn.` and `yymmddn8.`
using the function putn, 
the returned type is always character.

### Convert Between Numeric and Character Values

Please refer to the input and put post.
