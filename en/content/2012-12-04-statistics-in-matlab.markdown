UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: MATLAB for Statisticians
Date: 2012-12-04 00:00:00
Tags: statistics, programming, MATLAB
Category: Computer Science
Slug: statistics-in-MATLAB
Author: Ben Chuanlong Du


1. There are generally two ways to generate uniform and normal random numbers in MATLAB. 
One ways is to use [functions] `randn` (for standard normal distribution) 
and `rand` (for standard uniform distribution). 
The other way is to use [functions] `unirnd` and `normrnd` 
(there are also functions end with "rnd" for generating random numbers from other distributions). 
The difference between these two different kinds of functions is that 
the first group of functions generate only "standard" distributions 
while the second group of functions generate distribution with any parameters. 
So the group of functions end with "rnd" is recommended to use.
In old versions (2010a and earlier) of MATLAB, 
these random number generating functions end with "rnd" might cause problems 
in parallel computing. 
Then you want to use these two basic functions `rand` and `randn`, 
and use all kinds of technics to generate random variables you want.

2. `randsample` generates a random sample 
from a given collection of data with or without replacement. 
It also support weighted sampling with replacement, 
but does not support weighted sampling without replacement. 
There is another very similar but more powerful function called `datasample` 
which support weighted sampling (both with and without replacement). 
Note that both these two functions can generate random permutations 
which was frequently done using `randperm` in MATLAB of older versions. 
For old versions (before 2011b) of MATLAB, 
you can use `randi` to generate random indexes 
and extract corresponding elements of arrays.

3. When MATLAB starts, 
it set the random number generator to the default one 
and set the seed to be the default seed. 
So if you run a simulation, 
reboot MATLAB and run the same simulation, 
you will get the same results.

4. `tabular` counts the frequency of observations.

5. `iqr` calculates the interquartile range of given data.
There is a similar function called `IQR` in R.
