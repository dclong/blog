UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2016-07-09 18:20:45
Slug: io-in-r
Author: Ben Chuanlong Du
Title: Input and Output in R
Category: Programming
Tags: R, IO, programming, CRAN

## read.table, read.csv, read.delim, etc.
1. It is suggested that you use `read.csv`/`read.delim` and avoid using `read.table`.
This is because that the `comment.char` is off for `read.csv`/`read.delim` and on for `read.table` by default. 
My experience is that data seldom has comments in them 
and people are usually not aware that `comment.char` is on for `read.table` by default. 
When there are "comment chararacters" in data which are not intended to be comment characters,
you screw up if you read data using `read.table` and forget to turn off comment using `comment.char = ''`. 

2. By default, 
lines starting with `#` are treated as comment lines 
and thus are ignored when reading data using `read.table`, etc.
If a line is not a comment line, 
avoid starting it with `#`. 
Or you can specify a different comment character 
(e.g., `$` using option `comment.char = "$"`).

3. It is suggested that you always use `stringsAsFactors = FALSE` 
when constructing a data frame (data.frame, as.data.frame, read.table, read.csv, etc.).
Factors causes more troubles than conveniences. 
If you do need factors (for building models),
just manual convert columns to factors.

1. If a data row have an extra column/field (e.g., due to missing quotes in CSV format),
R will not throw error but instead treats the data to have a row names column. 
This results in shifted columns in some (shorter) rows. 
You can examining the format of a data file 
using the function `count.fields` 
which counts the number of fields in each line.

1. `read.csv` for standard CSV files while `read.csv2` is for European CSV format. 

## write.table, write.csv, write.delim, etc.

1. It is suggested that you write data frames into CSV format.
CSV format has a clear definition. 
If you tell people that a file is in CSV format,
they know how to read it. 
But if you tell people that a file is in a general delimited format,
people have to ask about what the delimiter is 
and whether fields are quoted, etc.

1. The function`write.table` writes a data frame or a matrix into a file. 
Note that it can also append data into a file. 
```R
x = matrix(1:24, nrow = 6)
colnames(x) = paste0("x", 1:4)
write.table(x, 'out.txt')
x[, ] = 0
write.table(x, 'out.txt', append = T, col.names = F)
```

3. By default `write.table` output missing values as character NA (`na = "NA"`). 
It is suggested that you output missing values as empty strings (na = "") as it is more portable. 
Other programming languages do not recognize character `NA's` as missing values. 

2. Always quote fields when you write data into CSV format.

0. `row.names` have different means in `read.table` and `write.table`.
`row.names` is a logical variable indicating 
whether you want to output row names or not in `write.table`,
however, it is not a logical variable indicating whether there is a row names in the data.
It is much more complicated. 
Please refer to the R help doc for detailed explanation.

1. It is suggested that you never write row names into files. 
If row names contains useful informtion, 
write row names into file as a column/field.
The reason is that row names causes troubles in IO. 
On one hand,
it is not convenient to read in a file 
with row names into other programming language. 
On another hand,
row names causes side effect in R too.

## MS Excel
<http://www.thertrader.com/2014/02/11/a-million-ways-to-connect-r-and-excel/>
It is suggested that you avoid using Excel as input/ouput data format. 
CSV is a better alternative.
However, 
if you do have to use Excel as input/output data format,
read the following tips.

1. There are lots of ways to read data from and write data into Excel documents. 
For example, 
packages `xlsReadWrite`, `xlsx`, `RODBC` 
(and many more) all offers ways to import data from and export data to Excel documents. 
`xlsx` (which offers `read.xlsx` and `write.xlsx`) is good package for dealing with Excel spreadsheet.
`RODBC` is a universal way to deal with all kinds of databases 
(not just Excel spreadsheet). 

2. It is usually very slow to read in (or write to) a large Excel spreadsheet.
It is suggested that you convert large Excel spreadsheets to CSV files first 
and then read in them.
Also, write data into CSV files instead of Excel spreadsheet.
However, 
be careful that the stupid Excel might loss information when converting to CSV format.
Generally speaking, 
this happens when there are very long numbers.

3. Excel might scilently format opened CSV (or imported text) files. 
Generally speaking,
this happens when there are very long numbers in the text file.
Be careful not to introduce undesired changed. 
If you just open a CSV file to view it and do not want change its content, 
then just discard any changes Excel has made. 
If you indeed want to change CSV file in Excel, 
keep your fingers cross. 

## Binary Data

1. The function `readBin` reads in binary data 
and the function `writeBin` writes binary data into files. 
Both of the two functions have limits on the size of data that they can deal at a time. 
For large binary data, 
you have to use `readBin/writeBin` multiple times to read/write them from/to files.
`readBin` and `writeBin` are compatible with `fwrite` and `fread` in MATLAB. 
`fread` and `fwrite` are C style functions, ... (to be checked for compatible with c/c++). 
However, `readBin` and `writeBin` is not compatible with 
Java classes `DataOutputStream` and `DataInputStream`. 
To read binary data written using `DataOutputStream` from Java, 
you can call Java code for reading binary data using `rJava` in R; 
to write binary data that is recognized by `DataInputStream` in Java, 
you can call Java code for writing binary data using `rJava` in R.

## Misc
1. All most all input/output functions in R support reading data 
from all kinds of source including files, console, clipboard and website.
For example, 
if you have copied a block of data from an Excel document, 
you can read it into R using the following command.
```R
x = read.table('clipboard', sep = '\t')
```
This is good and quick way to import part of the data from a Excel document into in R. 
You do not have to worry about formula in cells. 
When you read data from Excel, values (instead formulas) are read in.
If the data is on a website, 
you can just pass the URL to `read.table` (or `read.delim`, `read.csv`, etc.) to read it.

3. `print` prints an R object to the R console 
and `cat` can print multiple objects to the R console, clipboard or files. 
There is some difference between the outputs generated by these two functions.
Generally speaking, 
if you want to see the content of an object in R scenario 
(keep special characters as they are), 
you want to use `print`; 
if you want to see the content in human readable format
(special characters are translated), 
you want to use function `cat`.
I have to mention that `cat` doesn't work for all types of R objects 
(e.g. objects of `xtable`).

4. The function `scan` is extremely powerful and flexible. 
You can skip first `k` lines using the option `skip = k`.
For example, 
the following command skips the first 5 lines.
```R
scan(what = double(), skip = 5)
```
You can skip lines starting with special characters using the option `comment.char`.
For example, 
the following command skips lines starting with "#".
```R
scan(what = double(), comment.char = "#")
```
You can decide which special strings are treated as missing values using the option `na.string`.
For example,
the following command treats "NA" as missing values.
```R
scan(what = double(), na.string = "NA")
```
You can limit the number of data values/lines to be read in, etc.
Many input functions in R are based on the function `scan`, 
for example, `read.table`.
These functions inherits the powerfulness and flexibility of `scan`. 
`scan` is also helpful for interactive programming. 
For example, you can read a string into the variable `input` using the following commmand.
```R
scan(what = character(), n = 1) -> input  
```
However, `scan` is used to read in a vector, 
so the data to be read in *at the same time* must be of the same type. 


