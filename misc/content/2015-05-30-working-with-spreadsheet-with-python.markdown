Status: published
Date: 2020-08-03 09:17:08
Author: Ben Chuanlong Du
Slug: working-with-spreadsheet-with-python
Title: Working With Spreadsheet with Python
Category: Computer Science
Tags: programming, Python, Spreadsheet, Excel, pandas, xlsxwriter

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

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