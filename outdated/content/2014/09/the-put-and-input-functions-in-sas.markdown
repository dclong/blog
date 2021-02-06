UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-08-28 17:11:56
Author: Ben Chuanlong Du
Slug: the put and input functions in sas
Title: The PUT/INPUT Functions in SAS
Category: Computer Science
Tags: programming, SAS, put, input, putn, putc, inputn, inputc

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**


## The put/input Functions 
1. The `put` function is similar to the `putn` function. 
`$` is not required in the format of `put` and the format must not be quoted.
`$` is not required in the format of `putn` either,
however, the format for `putn` must be quoted. 
It is easier to understand that `$` is not required for the format of `put` or `putn`.
Both of them return character values, 
so there is no necessary to indicate that the output is character 
by using `$` in the format.

2. The function `putn` converts a numeric value to a string value.
Though you can pass a string value 
(which will be implicitly converted to a numeric value) to the function `putn`,
you should never do this.
Since the return value of `putn` is always character,
you should not put dollar signs in formats.
That is you should use $w$. (or $w.d$) instead of \$$w$. (or \$$w.d$)
and char$w$. (or char$w$.d) instead of \$char$w$. (or char$w$.$d$),
where $w$ and $d$ are integers.


3. The function `putc` format a character (as a character value).
You have to create formats using the procedure format.
See the example below.
Even if it seems that you format the variable word to be numbers,
it is actually a character variable.

        proc format;
            value typefmt 1='$groupx' 2='$groupy' 3='$groupz';
            value $groupx 'positive'=1 'negative'=2 'neutral'=3;
            value $groupy 'positive'=10 'negative'=20 'neutral'=30;
            value $groupz 'positive'=100 'negative'=200 'neutral'=3000;
        run;

        data answers;
            length word $ 8;
            input type response $;
            respfmt = put(type, typefmt.);
            word = putc(response, respfmt);
            datalines;
            1 positive
            1 negative
            1 neutral
            2 positive
            2 negative
            2 neutral
            3 positive
            3 negative
            3 neutral
        ;

3. The tricky thing is that when you functions in macro, 
then the return does not matter,
as everything is text to macro. 

3. You should not use `%put` in a data step, 
instead you should use `put`.


2. You can use the function `input` 
to change a character variable to a numeic one when applicable.
In the contrary, 
you can use the function `put` to change a numeric variable to a character one.

        data char;
            input string :$8. date :$6.;
            numeric = input(string, 8.);
            sasdate = input(date, mmddyy6.);
            format sasdate mmddyy10.; 
            datalines;
            1234.56 031704
            3920 123104
            ;
        run;

|Expression|Output|Expression|Output|
|:----------:|:------:|:----------:|:------:|
|putn(12345, "2.");|**|putn(12345, "2.2");|**|
|putn(12345, "3.");|1E4|putn(12345, "3.2");|1E4|
|putn(12345, "4.");|12E3|putn(12345, "4.2");|12E3|
|putn(12345, "5.");|12345|putn(12345, "5.2");|12345|
|putn(12345, "6.");|12345|putn(12345, "6.2");|12345|
|putn(12345, "7.");|12345|putn(12345, "7.2");|12345.0|
|putn(12345, "8.");|12346|putn(12345, "8.2");|12345.00|
|putn(12345, "9.");|12347|putn(12345, "9.2");|12345.00|
|putn(12345, "z2.");|**|putn(12345, "z2.2");|**|
|putn(12345, "z3.");|1E4|putn(12345, "z3.2");|1E4|
|putn(12345, "z4.");|12E3|putn(12345, "z4.2");|12E3|
|putn(12345, "z5.");|12345|putn(12345, "z5.2");|12345|
|putn(12345, "z6.");|012345|putn(12345, "z6.2");|012345|
|putn(12345, "z7.");|0012345|putn(12345, "z7.2");|12345.0|
|putn(12345, "z8.");|00012345|putn(12345, "z8.2");|12345.00|
|putn(12345, "z9.");|000012345|putn(12345, "z9.2");|012345.00|
|putn(12345, "comma2.");|**|putn(12345, "comma2.2");|**|
|putn(12345, "comma3.");|1E4|putn(12345, "comma3.2");|1E4|
|putn(12345, "comma4.");|12E3|putn(12345, "comma4.2");|12E3|
|putn(12345, "comma5.");|12345|putn(12345, "comma5.2");|12345|
|putn(12345, "comma6.");|12,345|putn(12345, "comma6.2");|12345|
|putn(12345, "comma7.");|12,345|putn(12345, "comma7.2");|12345.0|
|putn(12345, "comma8.");|12,346|putn(12345, "comma8.2");|12345.00|
|putn(12345, "comma9.");|12,347|putn(12345, "comma9.2");|12,345.00|
|putn(12345, "dollar2.");|**|putn(12345, "dollar2.2");|**|
|putn(12345, "dollar3.");|1E4|putn(12345, "dollar3.2");|1E4|
|putn(12345, "dollar4.");|12E3|putn(12345, "dollar4.2");|12E3|
|putn(12345, "dollar5.");|12345|putn(12345, "dollar5.2");|12345|
|putn(12345, "dollar6.");|$12345|putn(12345, "dollar6.2");|12345|
|putn(12345, "dollar7.");|$12,345|putn(12345, "dollar7.2");|12345.0|
|putn(12345, "dollar8.");|$12,345|putn(12345, "dollar8.2");|12345.00|
|putn(12345, "dollar9.");|$12,346|putn(12345, "dollar9.2");|$12345.00|
|putn(12345, "dollar10.");|$12,347|putn(12345, "dollar10.2");|$12,345.00|
|putn(12345, "dollar11.");|$12,348|putn(12345, "dollar11.2");|$12,345.00|
