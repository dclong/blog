UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-07-06 21:25:28
Slug: filesystem-in-r
Author: Ben Chuanlong Du
Title: Filesystem in R
Category: Programming
Tags: R, filesystem, programming, CRAN, file system
Modified: 2016-07-06 21:25:28

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**


1. `dirname` returns the parent folder of a file or directory, 
and `basename` return the name (without the parent folder) of the file or directory.

2. Function `file.path` joins path components into one path. 
It works similar to `paste` which concatenates strings to a single one, 
but it is platform independent.
The following code get the full path of the file `1.txt` in the current working directory.
```R
file.path(getwd(), '1.txt')
```
`file.path` does not handle the leading/trailing forward/backword slash(es) well,
but this does not matter as the result is still a valid Linux-style path.
```R
> file.path('C:/Study/','1.txt')
[1] "C:/Study//1.txt"
```
The author of this blog has a package named `dclong.fs`
which contains a function `join_path` 
that can handle leading/trailing forward/backword slash(es) nicely.

4. There are many useful functions in R 
which provide low-level interface to the computer's file and directory system, 
e.g., `file.create`, `file.exists` and `dir.create` and so on. 
If a function for manipulating directories is missing, 
it is probably the same as the function for manipulating files, 
e.g. function `file.rename` can also be used to rename a directory.

5. `file.info` returns the information of files and directories. 
The "isdir" column of the resulting data frame indicates whether a path stands for a file or a directory. 
For example,
```R
> file.info('.')
  size isdir mode               mtime               ctime
.    0  TRUE  777 2011-11-07 22:26:38 2011-10-20 17:14:41
                atime exe
. 2011-11-07 22:33:37  no
```
Notice that `file\_test` can also be used to check whether a path is a file or a directory. 
For example,
```R
> file_test('-f',".")
[1] FALSE
```
6. Often times, one need to use temporary files. `tempfile` returns a
vector of character strings which can be used as names for temporary
files. By default the temporary file is created in a temporary
directory returned by `tempdir`. For example (the following results
is platform dependent),
```R
> tempdir()
[1] "C:\\Users\\adu\\AppData\\Local\\Temp\\Rtmp55KGaO"
> tempfile('output.txt')
[1] "C:\\Users\\adu\\AppData\\Local
\\Temp\\Rtmp55KGaO\\output.txt122935c"
```

## Excel

1. Write hyper link into excel (using `write.xlsx`) does not work well. 
One workaround is to write the same content into a CSV file (using write.csv).
The hyper links work when you open the CSV file in Excel.
You can then save an Excel copy if really want a Excel spreadsheet.
