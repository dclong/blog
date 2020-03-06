UUID: 4fa64834-89aa-4091-bba3-2e43834223d3
Status: published
Date: 2015-05-17 18:57:48
Author: Ben Chuanlong Du
Slug: number-of-observations-in-a-sas-dataset
Title: Number of Observations in a SAS Dataset
Category: Computer Science
Tags: programming, SAS, observation, number, dataset

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

```SAS
proc sql;
    select count(*) from lib.dataset;
run;
```

Proc sql is not efficient when we have large dataset. 
Though using ATTRN is good method but this can accomplish within base sas, 
here is the efficient solution that can give number of obs of even billions of rows just by reading one row:
```SAS
data DS1;
    set DS nobs=i;
    if _N_ =2 then stop;
    No_of_obs=i;
run;
```
```SAS
data _null_;
    set yourdataset nobs=number;
    put number= ;
    stop;
run;
```

