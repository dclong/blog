UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2014-09-17 18:49:20
Author: Ben Chuanlong Du
Slug: date utilities in sas
Title: Date Utilities in SAS
Category: Computer Science
Tags: programming, SAS, date
Modified: 2015-05-17 18:49:20

### Convert a Date to a String of the Format "YYYYMMDD"

    data _null_;
        x = put("23Aug2014"d, yymmddn8.);
        put x date9.;
    run;

or

    data _null_;
        x = putn("23Aug2014"d, "yymmddn8.");
        put x date9.;
    run;

Both of the 2 data steps print "20140823".
The following is a comprehensive list of expressions 
(that can be used in data steps and procedures)
to convert dates into strings with given formats. 
Let `d` be a numeric variable with the value 19958 
(which represent Aug 23, 2014 in SAS).

|Expression 1|Expression 2|Return Value|Return Type|
|:------------:|:------------:|:------------:|:-----------:|
|put(d, date9.)|putn(d, "date9.")|23Aug2014|Character|
|put(d, date7.)|putn(d, "date7.")|23Aug14|Character|
|put(d, yymmdd10.)|putn(d, "yymmdd10.")|2014/08/23|Character|
|put(d, mmddyy10.)|putn(d, "mmddyy10.")|08/23/2014|Character|
|put(d, ddmmyy10.)|putn(d, "ddmmyy10.")|23/08/2014|Character|
|put(d, yymmdd8.)|putn(d, "yymmdd8.")|14/08/23|Character|
|put(d, yymmddn8.)|putn(d, "yymmddn8.")|20140823|Character|
|put(d, mmddyy8.)|putn(d, "mmddyy8.")|08/23/14|Character|
|put(d, mmddyyn8.)|putn(d, "mmddyyn8.")|08232014|Character|
|put(d, ddmmyy8.)|putn(d, "ddmmyy8.")|23/08/14|Character|
|put(d, ddmmyyn8.)|putn(d, "ddmmyyn8.")|23082014|Character|
|put(d, yymmdd6.)|putn(d, "yymmdd6.")|140823|Character|
|put(d, yymmddn6.)|putn(d, "yymmddn6.")|140823|Character|
|put(d, mmddyy6.)|putn(d, "mmddyy6.")|082314|Character|
|put(d, mmddyyn6.)|putn(d, "mmddyyn6.")|082314|Character|
|put(d, ddmmyy6.)|putn(d, "ddmmyy6.")|230814|Character|
|put(d, ddmmyyn6.)|putn(d, "ddmmyyn6.")|230814|Character|
|put(d, yymm.)|putn(d, "yymm.")|2014M08|Character|
|put(d, yymmn.)|putn(d, "yymmn.")|201408|Character|
|put(d, mmyy.)|putn(d, "mmyy.")|08M2014|Character|
|put(d, mmyyn.)|putn(d, "mmyyn.")|092014|Character|

A convenient way is to wrap these formats 
into functions with (better) meaningful names in the fcmp procedure for use.

### Convert a string of the format "YYYYMMDD" to a Date

    data _null_;
        x = input("20140823", yymmdd8.);
        put x date9.;
    run;

or

    data _null_;
        x = inputn("20140823", "yymmdd8.");
        put x date9.;
    run;

Both of the 2 data steps print "23AUG2014",
which menas that the string has been converted to a date successfully.
The following is a comprehensive list of expressions
(that can be used in data steps and procedures)
to convert strings with valid formats into dates.

|Expression 1|Expression 2|Return Value|Return Type|
|:------------:|:------------:|:------------:|:-----------:|
|input("23Aug2014", date9.)|inputn("23Aug2014", "date9.")|19958|Numeric|
|input("23Aug14", date7.)|inputn("23Aug14", "date7.")|19958|Numeric|
|input("2014/08/23", yymmdd10.)|inputn("2014/08/23", "yymmdd10.")|19958|Numeric|
|input("08/23/2014", mmddyy10.)|inputn("08/23/2014", "mmddyy10.")|19958|Numeric|
|input("23/08/2014", ddmmyy10.)|inputn("23/08/2014", "ddmmyy10.")|19958|Numeric|
|input("20140823", yymmdd8.)|inputn("20140823", "yymmdd8.")|19958|Numeric|
|input("14/08/23", yymmdd8.)|inputn("14/08/23", "yymmdd8.")|19958|Numeric|
|input("08/23/14", mmddyy8.)|inputn("08/23/14", "mmddyy8.")|19958|Numeric|
|input("23/08/14", ddmmyy8.)|inputn("23/08/14", "ddmmyy8.")|19958|Numeric|
|input("140823", yymmdd6.)|inputn("140823", "yymmdd6.")|19958|Numeric|
|input("082314", mmddyy6.)|inputn("082314", "mmddyy6.")|19958|Numeric|
|input("230814", ddmmyy6.)|inputn("230814", "ddmmyy6.")|19958|Numeric|

Notice that several interesting things I'd like to point out here.

1. For converting a string to date, 
all numeric informats 
(yymmddn8., mmddyyn8., ddmmyyn8., yymmddn6., mmddyyn6., ddmmyyn6., yymmn. and mmyyn.)
and incomplete informats (yymm. and mmyy.) are invalid.

2. Both "20140823" and "14/08/23" use the informat `yymmdd8.`
when converting to dates.

3. The informat names must NOT be quoted if you use the function `input`,
while they must be quoted if you use the function `inputn` or `inputc`.
The underlying difference is that `input` takes a compile-time informat,
so there is no need to quote the informat and it is fixed.
The function `inputn/inputc` takes a run-time informat,
so you must quote the informat and it can be changed based on different contexts.

2. The function `inputn` converts a character value to a numeric one;
takes numeric informat
the function `inputc` converts a character value to a character value;
takes character informat
the function `input` converts a character value to a character/numeric one.
character/numeric informat

3. SAS implicitly convert between numeric and character values ...

### Create a Date From Year, Month and Day

    data _null_;
        x = mdy(8, 23, 2014);
        put x date9.;
    run;

### Extract Year, Month or Day from a Date

    data _null_;
        date = mdy(8, 23, 2014);
        y = year(date);
        m = month(date);
        d = day(date);
        put date date9.;
        put y;
        put m;
        put d;
    run;

Notice that all the 3 functions `year`, `month` and `day` return numeric values.

### Arithmatic Operations on Date

1. last day of the month in a given date
```SAS
    d = intnx('month', d, 0, 'e');
```

## convert between data and datetime
```SAS
data _null_;
    d = '29FEB1984'd;
    put d date.;
    /* convert date to DateTime */
    dt = dhms(d,0,0,0);
    put dt datetime.;
    /* extract date from DateTime */
    d = datepart(dt);
    put d date.;
run;
```
