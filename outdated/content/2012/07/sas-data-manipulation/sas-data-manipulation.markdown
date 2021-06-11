UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2012-07-02 12:40:28
Slug: sas-data-manipulation
Author: Ben Chuanlong Du
Title: Manipulate Data in SAS
Category: Computer Science
Tags: programming, SAS, SQL, data step, data manipulation
Modified: 2015-08-02 12:40:28

<img src="http://dclong.github.io/media/sas/sas.jpg" height="200" width="240" align="right"/>

## Data Manipulation

3. Create a user library if you want your SAS data sets to persist.
For example,
the following code creates a library named `lib` 
which points to the directory `~/sas/lib`,
and creates a data set named `s1` in this library in the data step.

        libname lib "~/sas/lib";
        data lib.s1;
            ...
        run;
The data set `s1` will persist after you quit SAS,
and you can still access it next time you use SAS.
Surely you have to define a library (e.g., `lib`) pointing the diretory `~/sas/lib` again,
and use the library to reference the data set `s1` (e.g., `lib.s1`). 

2. You can specify several different directories as a single library in SAS. 
For example,
the following code creates a library named `mlib` pointing to 
a previously created library `lib` and 
directories `~/sas/lib2` and `~/sas/lib3`.

        libname mlib (lib, "~/sas/lib2", "~/sas/lib3");
        ...
This is convenient if you previous created SAS data sets in different directories
and want to use all of them without moving these data sets.
Note that when you create data sets in `mlib`, 
SAS will use these directories/libraries in the order you specified.
That is SAS will put the data set into `lib` if there's space,
otherwise it looks for the next directory with enough space.

4. You can use create shortcuts for files in SAS.
For example,
the following code creates a file shortcut `f` pointing to a local file,
and use it in data step.

        filename f "~/sas/examples/data/fake1.txt"
        data s1;
            infile f;
            ...
        run;
To point a file online, 
you can the following code.

        filename f url "http://dclong.github.io/fake1.txt"
        data s1;
            infile f;
            ...
        run;
This allows you to read files online in SAS.
You can also create a a file shortcut point to a directory. 
For example, the following is equivalent code to the first example.

        file f "~/sas/examples/data/";
        data s1;
            infile f(fake1.txt);
            ...
        run;
This is convenient if you have to read in many files from the same directory.


4. When a matrix has many columns (variables), 
it is not very convenient to specify variables to read in 
(if you want to read in almost all of them). 
A good alternative is to read in all numeric/character columns into IML procedure i
and then drop unnecessary columns.


3. You can use proc import or proc access to read data from different
kinds of files and this enable us to read data without specify
variable names.

There are two popular ways to manipulate data sets in SAS, 
the data step and the SQL procedure. 
The data step is often used to read in data. 
It can also perform some simple data manipulation jobs, 
for example, selecting variables and merge data sets. 
The SQL procedure is an advanced way for 
manipulating data sets. 
Besides these two ways, 
there are also other SAS procedures for manipulating data sets. 
For example, the `transpose` procedure can transpose a data set. 
Almost all SAS procedures can filter observations and variables before using a data set. 
For example, you can use `where` statement to filter observations, 
and you can use `keep` and `drop` after `data=data_set_name` 
to select variables in the input and output data set. 
In many SAS procedures, you can use the `var` statment to declare the variable(s) to work on.

1. You must sort data sets first before you merge them together.

5. All temporary variables are kept in the data set by default in the data step. 
If not overwritten, 
the next value (value in next observation) of a variable is its value in last observation. 

6. You can use `set` in a data step 
to combine data both vertically (by row) and horizontally (by column).
When combining two data sets d1 and d2 vertically (using set d1 d2;),
records are combined by column names,
i.e., columns with the same name are concatenated.
For a column in d1/d2 but not in d2/d1,
it is recorded as missing.
For example,
suppose we have data set d1 

|x1|x2|
|:-:|:-:|
|1|2|
|100|200|

and d2

|x1|x3|x4|
|:--:|:--:|:--:|
|1000|3|4|
|-1000|300|400|

        data d3;
            set d1 d2;
        run;

returns

|x1|x2|x3|x4|
|:--:|:--:|:--:|:--:|
|1|2|.|.|
|100|200|.|.|
|1000|.|3|4|
|-1000|.|300|400|

When combining two data sets horizontally,
columns in the first data sets are overwritten
if they also exists in the second data set.
For example,

        data d4;
            set d1;
            set d2;
        run;

returns

|x1|x2|x3|x4|
|:--:|:--:|:--:|:--:|
|1000|2|3|4|
|-1000|200|300|400|

However,
columns that appear in both datasets (d1 and d2) must have the same data type 
(either numeric or character).

6. `merge` to combine data horizontally (by column) in a data step. 

7. The `return` statement in the data step tell SAS 
that the reading/manipulation of current observation is done 
and it should continues to read/manipulate the next observation.

8. You can use variables in the data step without initialize them. 
The default value for numerical variables is 0,
and the default value for character variables is the empty string. 

9. When we read in data in data step we can treat "txt" file as "dat" file sometimes, 
which means that we can use file extension "dat".
(actually, I don't file extension matters)

10. PROC SQL is a very powerful procedure to deal with data set, 
but still data step have some advantages over SQL procedure.

11. When we print out a data set, 
the label(s) we have defined in data step will not appear in the output 
unless we define lable(s) again in print procedure. 
However if we use PROC SQL to get a report of the data set, 
the label(s) will appear in the output.

12. You often use statement `filename` to make shortcut, 
so that we can read in data easily either from a website or a local disk. 
You often define a shortcut as the whole path of a file. 
Actually, we can just specify part of the path as the shortcut.

13. Sometime times problems might occur when we read data into SAS from a file. 
This might be because that there are too many columns in a row. 
You use option `lrecl=n` to change the configuration. 
However the biggest value for `lrecl` is 32767, 
which means that there cannot be unlimited columns in a row.

14. The `if` statment for extracting a sub set from a data set
can be substituted by `where` statement 
given that you only keep the condition in the `if` statement.

2. lag and dif functions very useful ...
can we combine lag and diff? yes
lag doesn't work on variables that don't exist in the table
so you cannot use lag on new variables
instead, you should use retain
a friend of me asked a good question about lag, opposite, doesn't exists, 
between read in data line by line ....
such a function requires second scan ...

However, a lagged variable in the data step cannot be used by itself.
That is y = f(lag_y) will not work as you expected.
If lag1, you can use reatain. otherwise, it is very hard to do in SAS. 
see the example on another post ...

3. scan ... similar to split in other programming languages


6. It is recommended to use x1 x2 and so on as variable names in the data step. 
this makes manipulating data much easier.


6. termstr, according to files created on different operating systems ...
use different termstr

3. `goto` (or `go to`) is supported in SAS.

1. You can use "||" or "!!" to concatenate characters horizontally and "//" 
to concatenate matrices vertically.

2. Using multiple `input` statement in a data step allows you
to read a single record from multiple lines
and the double trailing at sign (`@@`) allows you to read in data in flexible way

1. In many procedures, 
you can filter data that you want to work on in parentheses following the dataset name.
For example, 
you can use the following code to print out the first 10 observations/rows/records of the data set `fit`.
        proc print data = fit (obs = 10);
            title 'Data set "fit".'
        run;

2. In a data step, 
you can overwrite an existing data set  
even if it is used in the data step.

        data d1;
            set d1;
            set d2;
        run;

3. If you do not specify an output data set in the sort proc,
the original data set will be overwritten by the result (sorted data set).

4. Unlike many other programming languages,
SAS math functions cannot handle singular point,
e.g., log(0) is invalid in SAS.

6. it is recommended to use x1 x2 and so on as variable names in the data step. this makes manipulating data much easier.

2. In the data step, 
you can assign values to a variable multiple times 
and the last assigned value will be kept.
However, 
tricky things can happen if you do this.
Please refer to the post about confusing string in sas.


3. When using datalines in a sas data step, tab (instead of space) can causes troubles. 
There might be options to get rid of the problem, but I forget which option to use ...

4. The datasets procedure is recommended for copying, deleting and renaming datasets, etc.
