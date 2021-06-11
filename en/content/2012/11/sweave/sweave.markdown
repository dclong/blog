UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Sweave
Date: 2012-11-13 00:05:31
Tags: LaTeX, programming, Sweave
Category: Computer Science
Slug: sweave
Author: Ben Chuanlong Du
Modified: 2016-07-13 00:05:31


1. Do not use sweave unless you are sure that you have run to the same
code again and again on different data sets, and you want the report
to be generate automatically each time.

2. You must start `<<...>>` at the beginning a line.

3. If you want to do simulation, you'd better set a seed for the random
number generator (RNG). In this way, you can reproduce your simulation
and the running result of the R code will always be the same. Sometime,
the result of R code will different every time you run it. For example,
if you want to test the speed of some algorithms, the time needed for
each algorithm will be different each time you run the code even if you
use the computer and use a same seed for RNG (if simulation used). For
this kind of output, you'd better not use Sweave. A better way is to
write the auto-write the result into a tex document, and then include
the file in your main tex file. In this way, you can still redo old work
easily but without worrying out having different outputs every time.
