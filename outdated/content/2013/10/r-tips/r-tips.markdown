Status: published
Author: Ben Chuanlong Du
Title: Tips on R
Date: 2013-10-29 17:08:42
Slug: r-tips
Category: Programming
Tags: tips, programming, CRAN, R
Modified: 2020-02-29 17:08:42

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. commandArgs extract command line arguments when R seesion was invoked. 
 
16. if performance is not critical, 
    then it is a good idea to always check the type of parameters. 
    Be flexible causes too many problems, 
    e.g., you problem of boolean and integer, 
    you thought they are equivalent, but actually not becuase there are revoke functions 
    which replies on boolean input. 
    integer input doesn't make the code throw any error, but the result is not right ...

17. some constants: letters LETTERS, month.name, month.abb, for more see base::Constants

18. auto complete in window works, 
    however, be careful with file names, if file name is in big letters, 
    you must use big letters in order for auto complete to work, i.e. type exactly as you see the files 

21. in the situation where data format is not necessarily consistent, 
    it is very good idea to pass names of columns that you need as parameters.

24. if both character and numeric are OK, prefer to use numerc as it's more convenient


## Debugging

1. You can the debug a function using the function `debug`. 
    For example, 
    you can use the following command to debug a function named `f`.

        :::r
        debug(f)

    During debugging,
    you can type `Q` to quit the process.
    For this reason, 
    you'd better not use `Q` as a variable name in user-defined functions.
    The the function `f` is no longer debugged once you source in its code again.
    You can also undebug it manually be the following command.

        :::r
        undebug(f)

## Other

1. R uses a copy-on-write technic which is similar to what MATLAB does.

2. Function `fix` can be used to fix object in R, 
    which can be very convenient.

25. Sometimes, 
    you want to check the source code of a function in R. 
    To do this, 
    you can just type in the name of the function in R. 
    However, 
    for functions which call interfaces written by C/C++ or Fortran this does not work. 
    You must download the source code of the corresponding R package, 
    and check the code there. 
    However, 
    for functions written in S3 method, 
    you can use function `getS3method` to check the source code.

29. `getAnywhere` can show you code of functions that are written s3 or
    s4 method.

33. S3method object uses `$` while s4method object uses `@` to extract
    elements. You can use `str` to see the structure of both of the two
    types of objects. And which symbol to use will be indicated in the
    output.

1. Always save R workspaces for important projects. 
    You might need intermediate results in the work space later
    or you might need to debug the code.
    The saved R workspaces will make things easier for you.
    Sometimes you have to (automatically) run the a same script many time (with different arguments)
    and it is possible to save workspaces for all of them due to disk limit.
    You can save all workspace to the same file so that the old workspace is overwriten by the new one.
    This way you do not consume too much space but still keep a workspace in case you need it.

2. make code robust and avoid using functions/packages that your are not familiar about, 
    if you do want to use them, read the help doc first, make sure you understand how it works!!!

3. it is suggested that you use R in Linux as much as possible. 
    First, R intrinsically has a bloody of Linux and thus some functions are best supported in Linux.
    Second, the IT services are often deployed on Linux so if you get a file from a service it is likely to be in Linux format.
    Finally, Linux has good support of Windows format while the opposite is not true. 
    Reading a Windows formatted file on Linux has no problem while reading a Linux format file on Windows can have problems.
