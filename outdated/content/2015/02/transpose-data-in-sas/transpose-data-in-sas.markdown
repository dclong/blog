UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-08-26 22:09:17
Author: Ben Chuanlong Du
Slug: transpose-data-in-sas
Title: Transpose Data in SAS
Category: Computer Science
Tags: programming, SAS, data manipulation, transpose
Modified: 2015-08-26 22:09:17

You can use the transpose procedure to tranpose a fat/thin data to a thin/fat data in SAS.
For example, 
suppose we have a data set s1 in SAS.

```SAS
data s1; 
    input famid faminc96 faminc97 faminc98 spend96 spend97 spend98 ; 
    datalines; 
1 40000 40500 41000 38000 39000 40000 
2 45000 45400 45800 42000 43000 44000 
3 75000 76000 77000 70000 71000 72000 
; 
run;
```
You can transpose the fat data set to a thin one using the transpose procedure.

```SAS
proc transpose data=s1 out=s2 (rename=(_name_=year)) prefix=x;
    by famid;
    var faminc96-faminc98;
run;
```
This gives you the following data set.

|famid|year|x1|
|:-----:|:----:|:----:|
|1|faminc96|40000|
|1|faminc97|40500|
|1|faminc98|41000|
|2|faminc96|45000|
|2|faminc97|45400|
|2|faminc98|45800|
|3|faminc96|75000|
|3|faminc97|76000|
|3|faminc98|77000|

You can transpose this thin data back to a fat one. 
```SAS
proc transpose data=s2 out=s3 (drop=_name_);
    by famid ;
	id year;
run;
```
The following are a few tips.

1. The `id` statement specifies one or more variables in the input data set 
whose formatted values name the transposed variables in the output data set.

2. The `var` statement specified variables in the input data set to be transposed. 

3. The `by` statement defines groups and the transpose will be done in each `by` group.
