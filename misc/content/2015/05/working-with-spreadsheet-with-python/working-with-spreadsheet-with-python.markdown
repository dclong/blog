Status: published
Date: 2015-05-09 08:43:45
Author: Ben Chuanlong Du
Slug: working-with-spreadsheet-with-python
Title: Working With Spreadsheet with Python
Category: Computer Science
Tags: programming, Python, Spreadsheet, Excel, pandas, xlsxwriter
Modified: 2020-12-09 08:43:45

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## pandas

If you just want to read an Excel spreadsheet to a pandas DataFrame 
or write a pandas DataFrame to an Excel file, 
it is best to use the pandas library directly.

## [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl)

[openpyxl](https://foss.heptapod.net/openpyxl/openpyxl)
is the underlying library that pandas leverages for reading/writing Excel files.

## [xlsxwriter](https://github.com/jmcnamara/XlsxWriter)
[xlsxwriter](https://github.com/jmcnamara/XlsxWriter)
is a Python module for writing files in the Excel 2007+ XLSX file format.
XlsxWriter is designed only as a file writer. 
It cannot read or modify an existing Excel file.
However,
if an Excel file is created from data (understandable by Python),
you can create a new Excel file from the same data to overwrite the existing one. 
This sort of gives you a flavor of updating an existing Excel file.

## [xlwings](https://www.xlwings.org/)
xlwings is a commerical software but has a opensource community edition. 
It requires an installation of Excel and therefore only works on Windows and macOS. 
Note that macOS currently does not support UDFs.

## References 

https://xlsxwriter.readthedocs.io/

https://xlsxwriter.readthedocs.io/faq.html

https://xlsxwriter.readthedocs.io/examples.html

https://github.com/xlwings/xlwings