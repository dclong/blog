UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-05-30 14:20:50
Author: Ben Chuanlong Du
Slug: import-export-data-sas
Title: Import/Export Data to/from SAS
Category: Computer Science
Tags: programming, SAS, import, procedure, Excel


## Import Data to SAS

1. The `IMPORT` procedure is based on the `DATA` step.
When you run an `IMPORT` procedure, 
the unlying data step code is printed into the log.
Sometimes the `IMPORT` procedure does a little bit extra work 
to automatically decide the most possible format you want (especially when you have date related data).
If it is not what you want, 
you can copy and paste the `DATA` step code 
generated in the log and modify it where necessary.

1. You'd better use SAS valid names for sheet names and column names in each sheet. 
This saves you trouble when importing data.

2. You can also use the data step to read a text/CSV file,
however, 
the `IMPORT` procedure is preferred over the data step for reading files
as you can read in variable names from the file instead of specifying them manually 
(as you would do in a data step).

3. It is suggested that you use CSV files whenever possible
as it is easier to modify a text file than a binary file (especially on a Linux server).
Also, you have better control over a CSV file compared to, e.g., an Excel file 
when using `proc import`.
You should avoid using other general format text file 
as it might take you or others extra effort to figure out the exact format of the file.

4. A common problem with the `IMPORT` procedure is that 
if you work on SAS server and import an Excel or CSV file created on Windows, 
the last column will always be character.
This is due to different termination of line used on Linux and Windows. 
I always upload data files using rsync/scp via command line, 
and never encounter the problem when importing an Excel file.
I do observe the problem on CSV (and other text files). 
A solution is to simply convert the CSV (or text) files  
from Windows format to Linux format using the command `dos2unix`.
Or you can manually import the CSV/Excel file into SAS using "File -> Import Data".
Another "dirty" solution is to append a "junk" column as the last column in the CSV (or text) file. 

5. A trick problem that might happen when you import data using `proc import` 
is that text might get truncated if it is too long.
A way to resolve the issue is to add the option `guessingRows=n;`,
where `n` is a large enough number (e.g., the number of rows in the data set).







The following SAS code reads in the sheet named "Hist_Macro" 
from the Excel file "data.xlsx"
using the `IMPORT` procedure.
The option replace overwrites the data set macro if it already exists.
Notice that you have to end the `IMPORT` statement (semicolon after replace) 
before you use other statement (sheet, getNames, etc.).
The getNames statement controls whether the first row in the range is read in as column names.
If Yes, the first row in the range is read in as column name, vice versa.
The default is to read in the first row (of a sheet/range) as column names.
The dataRow statement controls from which row the data is read in.
The default is to read in data from the first row of a sheet.
This option is overwritten if the range statement is used.
The statement `guessingRows=100` asks the `IMPORT` procedure 
to scans the first 100 rows in the input file 
to determine the appropriate data type and length of columns.

```SAS
proc import out=macro
    datafile="~/projects/data.xlsx" 
    dbms=xlsx 
    replace
    ; 
    sheet="Hist_Macro";
    getNames=Y;
    dataRow=5;
    guessingRows=100;
run;
```

The following SAS code reads in data from the range A35:B40 
of the sheet "Hist_Macro" of the Excel file "data.xlsx". 

```SAS
proc import out=s1
    dataFile="~/projects/data.xlsx" 
    dbms=xlsx
    replace
    ;
    range="Hist_Macro$A35:B40";
    getNames=N;
run;
```

You can also use the IMPORT procedure to read a CSV file 
(A CSV file is a text file with data fields seprated by commas).
or a general text file. 

```SAS
proc import out=shoes
    dataFile="~/test.csv"
    dbms=csv
    replace
    ;
    getNames=no;
    dataRow=5;
run;
```

```SAS
proc import out=class
    dataFile='~/tab.txt'
    dbms=dlm
    replace
    ;
    delimiter='09'x;
    getNames=Y;
    dataRow=5;
run;
```

## Export Data from SAS

1. When SAS export data to csv, missing values are left as blank.
SAS automatically decide whether quoting is needed.
When there is ambiguition (e.g., a string contains comma), 
then SAS automatically quote data when exporting to CSV. 

```SAS
proc export data=dataset (where=(conditions))
    outfile="file_path"
    dbms= csv
    replace;
run;
```
