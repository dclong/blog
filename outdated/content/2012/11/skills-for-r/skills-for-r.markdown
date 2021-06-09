UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-05-14 21:59:32
Author: Ben Chuanlong Du
Slug: skills-for-r
Title: Skills for R
Category: Programming
Tags: R, skills, programming, CRAN


1. Unlike C/C++, Java and SAS, 
you do not have semicolon to indicate the end of a command, 
but you can do this if you like. 
It is helpful if you have to write multiple commands on a line.

2. R support command/terminal mode, 
and if you open R in a command/terminal window, 
the working directory of R will be the working directory of the command/terminal window. 
For some GUI for R, 
you can only use a single application, 
e.g. you cannot open two Rstudio at the same time. 
But sometimes, 
you might want to open more than one R applications in different directories. 
To do this, 
you can use the command/terminal mode.

3. When you do not know how use a function, 
you can always type a question mark 
before the function name to open the help document of the function. 
For example, 
if you do not know how to use `sum`, 
you can type in `?sum` in R console to open the help document for `sum`.
Sometimes, 
you might just want see what arguments a function have,
instead of opening the help document. 
In this case, 
you can use `args` which display the declaration of a function. 
It is quite often that you want to use a function in R, 
but you cannot remember the name of the function. 
If you still know part of the function name, 
you can type in `??partial_name` in R console, 
then R will try to match it with all possible functions using regular expression.

4. Sometimes, 
you might want to hide an object 
(i.e. do not display the object when using the command `ls()`) in the R workspace, 
for example if you write a package
which relies on some global variables or some functions that should never by renamed. 
To do this, 
you can give a name to the object starting with a dot. 
For example there are some functions such as `.jinit`, `.jcall` and so on in R `rJava`, 
but you cannot see them by use `ls()`. 
If you do want to display all objects including these that start with a dot in R workspace, 
you can use `ls(all.names=TRUE)`.

5. By default, 
numerical variables in R are double values 
even you even they do not have decimal digits. 
To use data type of integer, 
you can put an `L` after integers. 
For example to assign a integer 5 to a variable `aInt`, 
you can use `aInt = 5L`.

6. `comment` can be use to set or query `comment` of an object in R.

7. `with` allows you evaluate an expression 
inside a data environment (usually a data frame), 
so you do not have to attach the data into R workspace 
(Attaching data into R workspace might mark other variables with the same names, 
so it is encouraged to do so.). 
within transform 

8. `class` gets/sets the class of a R object.

9. `attributes` and `attr` can get and set attributes of objects, 
e.g.  it can list names of objects. 
The difference between them is that `attributes` can set the attributes of a null object.

10. `str` shows the structure of an arbitrary R object. 
For example, 
if you have a large data frame `df` you can use `str(df)` to show its structure, 
so that you know what columes (type of data and names) it has.

11. The `ESC` hot key halts current unfinished command, 
which is helpful when you make typo in a command 
(especially when you miss a single/double quotation mark).

12. `Rprof` enables profiling an R is execution, 
which helps you write efficient R code.

13. If you want to run some code 
without writing any intermediate result into the workspace, 
you can put the code into `local` surrounded by curly braces. 
However, 
you must use `-\>` or `<-` instead of `=` in the code. 
Note that you can use semicolon to separate different commands.

14. `exists` checks whether a R object with a given name has been defined. 
For example,
```R
> exists("aNon_Exist_Object")
[1] FALSE
```
`missing` checks whether an argument of a function has been passed a value or not. 
It can only be used inside a function to help check availability of arguments.

15. You can use `shell("shutdown/s")` (in Windows) 
to shutdown the computer after R has finished computing.

16. When write a user-defined function, 
you'd better return a comprehensive result 
which contains not only the final outcomes 
but also other information such as parameters used in the computation.
This gives you the ability to work on a project in the long term,
especially when the names of variables do not give you much information 
about parameters used in computation 
(typical they do not because otherwise they will be long).


