UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-03-17 18:35:52
Author: Ben Chuanlong Du
Slug: rounding-related-functions-in-sas
Title: Rounding Related Functions in SAS
Category: Computer Science
Tags: programming, SAS, rounding, 
Modified: 2015-05-17 18:35:52

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

1. To avoid numerical issues,
you should use the ceil function instead of the ceilz function
for rounding up generally speaking.


2. Notice that the round function in SAS rounds away from zero to break ties (i.e., at x.5). 
```SAS
data _null_;
	x1 = round(1.5);
	put x1;
	x2 = round(2.5);
	put x2;
	x3 = round(-1.5);
	put x3;
	x4 = round(-2.5);
	put x4;
run;
```

Truncation Functions
CEIL
returns the smallest integer  the argument
CEILZ
returns the smallest integer that is greater than or equal to the argument, using zero fuzzing
FLOOR
returns the largest integer  the argument
FLOORZ
returns the largest integer that is less than or equal to the argument, using zero fuzzing
FUZZ
returns the nearest integer if the argument is within 1E-12
INT
returns the integer portion of a value
INTZ
returns the integer portion of the argument, using zero fuzzing
MODZ
returns the remainder from the division of the first argument by the second argument, using zero fuzzing
ROUND
rounds a value to the nearest round-off unit
ROUNDE
rounds the first argument to the nearest multiple of the second argument, and returns an even multiple when the first argument is halfway between the two nearest multiples
ROUNDZ
rounds the first argument to the nearest multiple of the second argument, with zero fuzzing
TRUNC
returns a truncated numeric value of a specified length
