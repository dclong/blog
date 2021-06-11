UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2009-11-02 12:05:07
Author: Ben Chuanlong Du
Slug: general-tips-for-sas
Title: General Tips for SAS
Category: Computer Science
Tags: character, programming, SAS, procedure, data step, tip
Modified: 2015-08-02 12:05:07


**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement. 
**

1. Do not go crazy in encapsulating/reusing code in SAS.
SAS is too stupid on this.

2. `proc univariate` only works on numerical variables.
You can use `proc freq` or `proc sql` to summary statistics of character variables.


2. sometimes, you need to use plain password to access some database (due to stupid steup ...)
one way to make things a little bit secure is to define you username 
and password as macros in a sas file 
and put them into your home directory 
and do not any other people read access ...

7. You can run `dm 'clear log';` to clear log information.

1. There are two kinds of modules in SAS.
One is data step, 
the other is procedure.
The data steps read in, create and modify data sets.
The procedures are mainly used to analyze data sets and display results.
However, 
procedures can also manipulate data, 
e.g., the `SQL`, `SORT`, `TRANSPOSE` procedures and so on.
Every procedure in SAS has tons of options 
that help you accomplish different tasks. 

3. There are 2 ways (`*...;` and `/*...*/`) to make comment in SAS. 
It is recommended that you always use the `/*...*/` comment style.
The reason is that `*...;` might cause problems in user-defined macro functions.

4. In SAS, 
a key word can have different means in different context. 
For example, 
a key word can be an option, 
a function or a procedure. 

3. SAS is a very stupid language. 
It is very annoying in the sense 
that the identical code might not work in a different environment.
And even if it works, 
it might give you different results.
For example,

        data test;
            x=intnx('week', '17oct03'd, 6);
            put x date9.;
        run;

prints `16032` while

    data _null_;
        x=intnx('week', '17oct03'd, 6);
        put x date9.;
    run;

prints `23NOV2003` in the log 
(Note that you should not put `date9.` in single/double quotations. 
Please refer to Confusing string in SAS for more on this).


2. The `_null_` date step is good environment for testing SAS code.
Neither macro (outside data steps or procedures) 
nor the `IML` procedure is as convenient.

4. The `intnx` function returns the SAS date value 
for the **beginning** date, time, 
or datetime value of the interval that you specify in the start-from argument. 
For example, 
`intnx('month', '08aug2013'd, 0);` 
returns a value that represent Aug 1, 2013.
To convert the SAS date value to a calendar date, 
use any valid SAS date format (such as the `date9.` format).
The following example shows 
how to determine the date of the start of the week 
that is six weeks from the week of October 17, 2003.

        x=intnx('week', '17oct03'd, 6);
        put x date9.;

5. Every SAS command must be ended with a semicolon (`;`).
If you miss a semicolon in SAS,
code following might turn red in SAS enhanced editor.
And you will get wild error messages if you run the code.

1. Most procedures in SAS take data sets 
(with rows stand for observations and columns stand for variables) as input. 
However, 
some procedures also accept other special types of data (e.g., covariance matrix) as input.
When you want to use a special type of data as input, 
you must explicit specify its type (use `type=data_type`).  

2. It is suggested that you keep variable names in SAS short 
(best not to exceed 8 characters),
because you cannot use names with more than 8 characters in some situations,  
e.g., when you create shortcut using `filename` 
(not sure whether this has been changed in new versions of SAS).

## Output

5. It is very slow to display results in HTML format 
when there are massive results. 
Instead of using the `print` procedure, 
it might be much faster to just rerun the code. 

## Linear Models
3. Prefer nested than distinct (many) levels,
for example, instead of 1-9, 
prefer 1-3 inside another factor of 3 levels. 
This is a performance concern. 

2. Prefer numerical values to character values: 
first, character variables has a default length of 8 which is usually too short
while numerical values are 64 bits. 
Second, the `IML` procedure accepts matrices only, 
so you cannot mix numeric and character values in the `IML` procedure.

2. You can use the `SetInit` procedure (see code below) 
to list SAS expiration date, licensed components, etc.

        proc setinit;
        run;

10. You can include a SAS file using the `%include` macro.
To include a single file, 
use `%include path_to_file;`.
You can also include multiple SAS files at a time using the following statement

        %include mylib("c1.sas", "c2.txt");

where `mylib` is SAS library.
You can ignore the extention and quotations marks for "c1.sas" 
as it has an SAS file extension. 
However,
it is recommended that you always use quotation marks and full file names.
You can also include an SAS file interactively using `%include *;`.

2. A `filename` shortcut points to a location on the machine that runs SAS.
For example, 
if you run SAS on a server using SAS Enterprise Guide, 
a `filename` shortcut should point to a location 
on the server not a location on your local computer.

3. The maximum length for numeric variables is 8. 
SAS has only 2 types of data: numeric and character.
The SQL procedure supports more numeric data types,
but they are just alias to numeric (type).
