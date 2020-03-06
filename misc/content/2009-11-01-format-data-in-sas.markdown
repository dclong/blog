UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-05-17 18:52:19
Slug: format-data-in-sas
Author: Ben Chuanlong Du
Title: Formatting Data in SAS
Category: Computer Science
Tags: SAS, formatting data, programming, label

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Data Formatting

1. To add labels to a variable, 
You can use the statement `label` to add labels to a variable in SAS.
And it doesn't matter whether you use the quotation marks for the label string or not.


3. The `label` statement in SAS is somehow similar to the `format` procedure. 
The difference is that `label` explains the name of variables while 
`format` explains the value of variables. 


2. To quickly remove all labels 
```SAS
proc datasets library=mylib nolist;
    modify mydataset;
    attrib _all_ label='';
quit;
```

4. There are times in SAS when you simply want to remove all the formats from a dataset. 
This can be done in one line in a data step.
```SAS
data unformatted;
    set formatted;
    format _all_;
run;
```
