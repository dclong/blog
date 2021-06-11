UUID: a57587d8-9b0b-4c74-b5f3-f1bcd2aa7d4f
Status: published
Date: 2018-01-01 16:15:21
Author: Ben Chuanlong Du
Slug: select-columns-from-structured-text-files
Title: Select Columns from Structured Text Files
Category: Computer Science
Tags: programming, Python, pandas, SQL, awk, cut, text file, data manipulation, column, field
Modified: 2018-01-01 16:15:21

## Python pandas

My first choice is pandas in Python. 
However, 
below are some tools for quick and dirty solutions.

## [q](https://github.com/harelba/q) 
```sh
q -t -H 'select c1, c3 from file.txt'
```

## cut
```sh
cut -d\t -f1,3 file.txt
```

## awk
```sh
awk -F'\t' '{print $1 "\t" $3}' file.tsv 
```
Note: neither `cut` nor `awk` honors escaped characters.
For working on complicated structured text files, 
pandas in Python is a much better solution.