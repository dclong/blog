UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-01-13 13:14:35
Author: Ben Chuanlong Du
Slug: pass-array-r-other-language
Title: Compare R with Other Languages on Data Manipulation
Category: Computer Science
Tags: Python, C++, programming, statistics, Java, string, data frame, R, OOP, MATLAB, CRAN

<img src="http://dclong.github.io/media/r/r.png" height="200" width="240" align="right"/>
Here I compare R with other languages such as C/C++, Java, MATLAB, Python and so
on data manipulation. I list a few advantages and disadvantages of R on data
manipulation compared with other programming languages. 

Generally speaking, it is very convenient to manipulate data in R. Using function
`read.table` (and other derived functions), you can read numerical and
character data into a data frame from a text file at the same time. Though other
programming languages can do this too, most of them are not as simple and convenient
as R. For example, you can read in a table in MATLAB using function `dlmread`,
but the data has to be of the same type. Function `xlsread` in MATLAB can read
numerical and character values at the same type, but as its name indicates, it
relies on the Microsoft Excel software. What is more, `xlsread` read data into a
cell which does not have row names and column names attributes. The first row of
the data (usually stands for the headers) is read into the cell as the first row
of data. This is inconvenient. 
A matrix and data frame in R can have both column names and row names.
They make extracting and recording data very convenient in R.
MATLAB is close to R in the sense that its matrix data structure is comparable
to the matrix data structure in R, and its structure array data structure is
comparable to the data frame data structure in R. However, you can only extract
rows from a structure array but not columns. The cell data structure in MATLAB
is another data structure that is comparable to the data frame data structre in
R, however, as I mentioned before it doesn't have row names and column names
attributes. All these things make it a hessle to work on data with different
types at the same time in MATLAB. 

Python has some libraries (e.g., pandas and pydataframe) that offer similar
object as data frame in R and similar functions as `read.table` and
`write.table` (and their derived functions) in R. One advatange of Python over R
is that it has better support of object oriented programming than R. Working on
vector alike object in python is more convenient than in R many times. For example, you can
easily insert an element into a list in Python with the `insert` method while in
R you have to extract parts of a vector/list and then recombine them with the
elements you want to insert. 

Support of string in C awful. Java has a better support of string, however, I
don't know whether there are libraries offering convenient ways to read and write data like 
`read.table` and `write.table` in R. Honestly speaking, I doubt. What's more,
compiled langugaes are not as convenient as script languages to explore data.

Given these things discussed above, Python and R
are good choices if you have to deal with both numerical and character data at the same time.

