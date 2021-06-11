UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-01-17 18:47:56
Author: Ben Chuanlong Du
Slug: sas-loop
Title: SAS Loop
Category: Computer Science
Tags: programming, SAS, loop
Modified: 2015-05-17 18:47:56

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

```SAS
y = 0;
do i = 1 to 10 by 2;
   y = y + i;
end;

count = 1;
do while(count<5);
   count = count+1;
end;

count = 1;
do until(count>5);
   count = count+1;
end;
```

```SAS
data _null_;
    do x="a", "b", "c";
        put x;
    end;
run;
```

comma cannot be omitted.


However, 
you cannot do this directly in macro loops.
A way to close assembly this to use the trick of `%scan`.

```SAS
%let months = 200201 200202 200203;
%macro f;
	%local i m;
	%let i = 1;
	%let m = %scan(&months, &i);
	%do %while(&m ^= );
		%put &m;
		%let i = %eval(&i + 1);
		%let m = %scan(&months, &i);
	%end;
%mend;
%f
```
