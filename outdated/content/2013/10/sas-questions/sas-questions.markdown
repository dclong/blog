UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Questions About SAS
Date: 2016-07-13 22:55:14
Slug: sas-questions
Category: Computer Science
Tags: questions, programming, SAS
Modified: 2016-07-13 22:55:14

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

0. include... can i use relative path?

1. Actually, I think it is good idea to always quote data 
when exporting data to CSV format.
But how do you read in quoted data in SAS? 

9. easy way to make design matrix in SAS?

3. ssp, prompts as code? is it possible?

3. SAS hash is interesting, sounds like something you should learn about

5. how to go back to the last position of cursor?

1. check procedures freq, tabular, report

## Ask 

1. Is there any restriction on th number of macro variable 
that we can use?

8. When defining a function using the procedure fcmp,
can we use a data set as argument? 
I don't think so.

3. it is said that %sysevalf is not very accurate, 
and you should do calculation in a null data step.
Is that true? 
Check on this.


6. it seems that "return" a value from a SAS macro function is really tricky?
How can I do it in a robus way? 
you should never try to do this. 
A much better way is to create a macro variable or dataset containing the results 
and use the macro variable or dataset instead.

2. SAS option compress = yes; 
I don't think it helps on downloading data over internet from databases 
such as Teradata. Ask expert's opinion on this!!!

4. can we use filename shortcut in libname?

7. Is there an easy way to get the total of a column 
which can be used in a data step?
What I'm looking for is a function which takes a data set 
and a variable name as input and gives the total of the variable.

## SAS Stored Process

2. most convenient way to backup/migrate sas stored process?

## SAS SQL

5. it seems to me that proc sql cannot cast data?
you have to use input/put instead.



## SAS Enterprise Guide

    does SAS Enterprise Guide support debugging?
    How to quickly run a procedure in SEG?



is it possible to define a constant macro variable?

convenient way to read content of a file and put it into a macro?

better to define global macro variables at the beginning or when needed?


## data type
1. when implicitly convert a character to number, what informat is used?
