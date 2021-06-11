Status: published
Date: 2015-08-28 17:02:54
Author: Ben Chuanlong Du
Slug: missing-values-in-sas
Title: Missing Values in SAS
Category: Computer Science
Tags: programming, SAS, missing values, null, white space
Modified: 2015-08-28 17:02:54

1. SAS uses a dot (`.`) to stand for a numeric missing value 
    and any number (can be 0 which correspond to the blank string `""`) 
    of white spaces (e.g., `"  "`) for character missing value. 
    (This also means that you cannot save pure white spaces in SAS.) 
    However, 
    when you enter values after `datalines` in the data step,
    you always use dots (not a blank/space) to stand for missing values 
    (no matter a variable is numeric or character). 
    You can use `where v is null` or `where v is missing` 
    to check whether the variable `v` is null/missing.
    Here `null` and `missing` have the same meaning. 
    However, 
    both of `is null` and `is missing` can only be used 
    in the `where` clause (in any procedure) and the `on` clause (in the SQL procedure).
    In other logical comparisons (e.g., if), 
    you have to use `v = .` or `v = " "` 
    according to whether `v` is a numeric variable or a character variable.
    In Teradata SQL, 
    `null` means missing value and you can use `null` (and only `null`) 
    for both numeric and character variables and in any logical comparisons. 
    When SAS displays missing values, 
    a numerical missing value is displayed as a dot 
    and a character missing value is displayed as a blank/space.
    When Teradata SQL Assistant displays query results, 
    `null` values are indicated by `?`.
    It is suggested that you always `is null` 
    instead of `is missing` or `v = .` or `v = " "` in `where` clauses in SAS. 
    This makes your SAS SQL code more portable.

6. In the IML procedure (seems also true for data step?) missing values 
    and white space (no matter how many) all have length 1,
    which is ridiculous.
    You have to be very careful when you work with string in `proc iml`.

7. SAS treats the numeric missing value (`.`) as the smallest numerical value.
    When you check whether a numeric value is negative, 
    you have to first get rid of missing values. 

7. Most functions (e.g., `sum`, `min`, `max`, etc.) in SAS ignores missing values
    instead of propagate missing values. 
    This is a little bit crazy as propagating missing values sounds more reasonable.
    You'd better filtering out missing values (if any) before you do calculations.

8. `input("", 8.)` returns `.` (numeric missing value) 
    while `put(., 3.)` returns `"."` instead of `""` (character missing value).
    The inconsistent is annoying.

## Questions 

4. Numeric missing value (`.`) affects functions such as `lag` and `dif`

5. the missing(.) function is strange, check it, and I think it should replaced by `x is missing` or `x is null` ...
