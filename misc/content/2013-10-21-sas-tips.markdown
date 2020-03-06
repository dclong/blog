Status: published
Author: Ben Chuanlong Du
Title: Tips on SAS
Date: 2019-05-10 19:13:40
Slug: sas-tips
Category: Computer Science
Tags: tips, SAS, programming

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
1. SAS on Linux recognize `~` as the home directory of users.

2. good to use a profile (containing database use and password, etc.) and %include it ...
    e.g., .sas_profile

```SAS
%include "~/.sas_profile";
```

## Library

1. There are at least two ways to get the path of the temporary `work` library.
    The first way is to right click on the `work` library
    and choose `Property ...`.
    The second way is to run the following code.

        %put %sysfunc(getoption(work));

    However, 
    the path returned by these 2 ways might not be correct (which is really annoying).
    If you want to keep datasets in the "work" library,
    you can copy it to another permanent library.
    To do this, 

        1. select datasets in the "work" library,
        2. right click and select copy
        3. right click on the permanent library
        4. choose paste.

    Or you can use the `datasets` procedure directly.

        proc datasets library=source;
           copy out=dest;
        run;


6. Do not use the "work" library to save important datasets.
    Always use a (permanent) library.

2. SAS is case-insensitive. 
    It does not matter whether you use upper or lower case 
    for keywords, functions, data set names, etc. in SAS.
    However, 
    strings/characters are case-sensitive. 
    For example, 
    `"good"` and `"GOOD"` are different as characters. 
    This matters when your SAS code relies on string comparisons.
    A file path is case-insensitive in Windows but case-sensitive in Linux,  
    so a file path in SAS running on a Windows server is case-insensitive 
    but case-sensitive in SAS running on a Linux server.
    A tricky situation where case matters is 
    when a macro variable is embedded in double quotes 
    to be used it as a string value.


## procedures

1. metalib (for user name, password information and so on)
    LIBNAME CRE_DATA BASE "/var/userdata/CPRA/Users/ub66536”
    you have additional key word base 
    (this fixes a SAS stored process problem, 
    if you cannot run a stored process, maybe permission)

2. lag and dif functions very useful ...
    can we combine lag and diff? yes
    lag does not work on variables that don't exist in the table
    so you cannot use lag on new variables
    instead, you should use retain

6. termstr, according to files created on different operating systems ...
    use different termstr 


## Other tips

1. dm statement is the display manager ...

5. It is very slow to display results in HTML format when there are massive results. 
    Instead of using the prin procedure, it might be much faster to just rerun the code. 

1. The `pwencode` procedure encodes password 
    and let you use it in place of plaintext passwords in SAS programs 
    that access relational database management systems (RDBSMs) and various servers.

## Options

6. The global key `options` in SAS has an alias `option`. 
    However, it is suggested that you always use `options` instead of `option` 
    when setting SAS system options.

        sas proc sql stimer option;
        options macrogen symbolgen;
        option mprint symbolgen;


## Syntax

1. be careful when you copy sas code from a non-text editor (e.g., MS Word).
    It might screw up special symbols, such as the double quotes,
    which results in syntax error.

4. SAS has many pre-mature syntax sugars. For example, 

        data _null_;
            x = intnx('week', '17oct03'd, 6);
            put x= date9.;
        run;

    However, 
    it is suggested that you use the following way instead 
    as it is more consistent with other programming languages.

        data _null_;
            x = intnx('week', '17oct03'd, 6);
            put 'x = ' x date9.;
        run;

1. You can use l <= x <= u conditions in a SAS where statement,
    which is more convenient.
    We can also do this in python.

11. The keyword descending in the sort procedure must be before the variable it describes in proc sort.

### Naming

1. Names of engines, filerefs, librefs and passwords can be at most 8 characters;
    names of call routines, functions and procedures can be at most 16 characters;
    all other variable names can have at least 28 characters.

3. You can use _SomeVar as macro variable names.
    It seems that some people like to use this naming convention.
    I think this is to avoid name confliction.
    To avoid name confliction, 
    a good way is to use _ followed by a sequence of random digits (e.g., _2893478219903).


## Random

1. ranuni, call ranuni, unifrom, call randgen
    use a negative seed to use time as seed,
    which is recommended

4. `&&x&i.`, `&&x.&i.` 
    `.` is not makeing things clear, from this view, you know which is right!

## branch
1. only the first statment following an if ... then ... clause is run.
    If you want to run run multiple statements in a if ... then ... branch,
    you have to include them in a do ... end block.


## References

- [CFA SAS FRM Statistics Finance](http://duanzy.blogspot.com/)


http://www.jiangtanghu.com/blog/2012/10/16/incorporate-sasiml-to-base-sas/

http://support.sas.com/documentation/cdl/en/imlug/64248/HTML/default/viewer.htm#imlug_procs_sect005.htm
