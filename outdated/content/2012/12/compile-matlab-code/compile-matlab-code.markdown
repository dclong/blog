UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Compile MATLAB Code
Date: 2015-06-07 23:48:09
Tags: compile, compiler, programming, MATLAB
Category: Computer Science
Slug: compile-matlab-code
Author: Ben Chuanlong Du
Modified: 2015-06-07 23:48:09


1. MATLAB code can be compile to C/C++ code or stand alone applications. 
Usually you can run the stand-alone application in Windows system directly, 
but for Linux system it is a little headachy. 
The stand-alone application usually takes less than 50% of the time 
that the original MATLAB code takes to run.
This depend on different situations. 
It can happen that the stand-alone application runs slower than the original MATLAB code.

2. To compile MATLAB code to c code, 
you can use `mcc -mc mainfn sub1fn sub2fn`, 
and to produce an stand alone executable file from c files,
you can use `mbuild mainfun sub1fn sub2fn`.

3. To compile MATLAB code to c++ code 
and to create a corresponding stand-alone executable file 
you can use `mcc -p mainfn sub1fn sub2fn`. 
To compile MATLAB code that contains Handle Graphics functions into C++ 
and to create a corresponding stand-alone executable file, 
you can use `mcc -B sglcppp mainfn sub1fn sub2fn`.

4. To compile MATLAB code to c and to create corresponding stand-alone executable file, 
you can use `mcc -m mainfn sub1fn sub2fn`. 
To compile MATLAB code that contains Handle Graphics functions into c 
and to crate a corresponding stan-alone executable file, 
you can use `mcc -B sgl mainfn sub1fn sub2fn`.

5. If you use parallel computing, 
you will not be able to run the compiled application (at least before version 2010b) 
unless you have MATLAB Distributed Computing Server (MDCS) available on a computer cluster. 
If you have access to a MDCS, 
there is little necessary for you to compile your MATLAB parallel code to a stand-alone application, 
so just do not bother to compile your MATLAB parallel code.

