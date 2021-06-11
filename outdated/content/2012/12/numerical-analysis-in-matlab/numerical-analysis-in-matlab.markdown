UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Numerical Analysis in MATLAB
Date: 2012-12-04 00:00:00
Tags: programming, MATLAB
Category: Computer Science
Slug: numerical-analysis-in-MATLAB
Author: Ben Chuanlong Du
Modified: 2012-12-04 00:00:00


1. `fmincon` finds minimum of constrained nonlinear multivariate function.
`fminunc` finds minimum of unconstrained nonlinear multivariate function.
`fgoalattain` solves multiobjective goal attainment problems; 
`fminimax` solves minimax constraint problems.

2. When you use one of these functions mentioned above to do optimizations, 
you might want to pass extra parameters to the objective function. 
You can do this directly in R, 
however, 
you have to this indirectly in MATLAB. 
To pass extra parameters to the objective function, 
there are 3 different ways: anonymous function, nested function and global variable. 
I think anonymous function is the best an most nature way to do it. 
Suppose you have defined an objective function `myObjFun(x,a,b,c)`, 
and you want to do optimization for given `a`, `b` and `c`. 
You can first specify values for `a`, `b` and `c`, 
define a function handle `f=@(x)myObjFun(x,a,b,c)`, 
and then optimize function handle `f`.

3. `quadl` can be used to numerically calculate integrals. 
To calculate integrals symbolically, 
you can use `int`.

