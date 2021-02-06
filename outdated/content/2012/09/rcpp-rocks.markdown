UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2014-08-16 19:26:30
Slug: rcpp-rocks
Author: Ben Chuanlong Du
Title: Rcpp Rocks
Category: Computer Science
Tags: C++, list, programming, HPC, Rcpp, R, RcppArmadillo, Armadillo, rock


Please see [here](https://bitbucket.org/dclong/r-learn/src/) 
for some simple examples for learning Rcpp and related packages.

## Tips

1. Though you can overload functions in a Rcpp module,
it causes problems when you export these overloaded functions.
This is because currently Rcpp cannot distinguish them when exporting them.
It is suggested that you do not overload functions that are to be exported.

2. The `Module` function in the "Rcpp" package 
might fail to load modules even if the C++ code is compiled successfully.
If this happens, 
you can try the option `mustStart = TRUE`.
It is suggested that you always use this option when you use the `Module` function.

3. Do not import the namespace `std` when using Rcpp. 
This causes name conflicts. 
It is also suggested that 
you always prefix functions with their namespace (even for Rcpp functions),
otherwise it is very error-prone.
For example, 
if you want to use the `std::abs` function 
but you forget the namespace (`std::`) prefix, 
the `Rcpp::abs` will be used instead. 
Your code will probably compile without any error message,
but the results won't be right. 
This kind of bug is very trick.
You'd better avoid it at the first place.

4. The following operations might cause segmentation fault and 
thus forces R to quit.

        - Calling C++ functions with wrong number of parameters.

        - Unhandled exceptions (e.g., out of bound).

        - Use Rcpp module from previous save R workspace without compiling C++ code again. 

These operations are very dangerous, 
because you lose unsaved data in the R workspace when R is forced to quit. 
So you have to be very careful when you use C++ functions. 
It is recommended that you handle exceptions in C++ code. 
If you do not know how to handle exceptions in C++ code,
a safer way but a little tedious way is to always call C++ functions using the `try` function in R.

5. In C++, 
methods for accessing elements of containers usually have both bound-checking 
and no-bound-checking versions. 
You should be aware that the no-bound-checking versions are more dangerous,
because your code might continue to run without any warning message after things to wrong.

1. Passing data between R and C++ is made easy. 
You can pass vectors, matrices and lists 
between R and C++ directly with the help of Rcpp. 
Rcpp takes care of the data converting automatically.
When you use the "RcppArmadillo" package, 
the converting between R objects and "Armadillo" matrices is also done automatically.

2. A list in R (and thus in Rcpp) is essentially a generic vector. 
You must know the structure of the list in order to work on it in Rcpp.
Each element of a `List` in Rcpp is of type `SEXP`. 
You have to first convert it to an Rcpp object 
and then work on it.

3. You can use reference of List in Rcpp, 
but a const reference of List is not allowed. 
Also though you can make a const reference of elements of a List,
I think it is misleading. 
Because a cast is usually need, 
I think a copy is often made. 
It is always good practice to transform a List object 
to a more type-strict data structure in C++ before you operate on it. 

3. A vector in Rcpp can have names and you access an element by its name. 
However, 
different from R, 
error happens if you access element using a non-existing name. 
To avoid this, 
you can first use the `containsElementNamed` method 
of the Vector class to query whether an element 
with a specified name exists. 
Note that the `containsElementNamed` method accepts `const char *` as argument
not `std::string`. 
However, 
you can use the `c_str` method to convert std::string to `const char *`.

4. There is no data structure in R corresponding to `std::set` in C++. 
So when you `wrap` a set to an R object, 
it becomes an array/vector in R.
If you want to convert, 
say, 
a vector in R to a `std::set` in C++,
you have to first convert the vector in R 
to `std::vector` or `Rcpp::NumericVector` 
and then insert the vector into the set.

4. It is not convenient to get and operate on the names of a vector in Rcpp,
but you can pass the names of a vector/list to Rcpp as a vector from R. 

5. You can use access R functions (in installed packages) easily in C++ code via Rcpp.
However, 
Rcpp is for extending R via C++, 
i.e., you have to come back to R. 
Trying to compile C++ code using Rcpp to and run binary code usually cause segmentation fault. 

5. You can pass R functions (including user-defined functions) to Rcpp as Function objects, 
which is really convenient. 
The following is a silly illustration example. 

        code = 'Function f(fun);
        SEXP x = f();
        int y = as<int>(x);
        return wrap(y+1);'
        rwrap = cxxfunction(signature(fun="function"),code,plugin="Rcpp")

6. C++11 support is still experimental in most C++ compilers. 
To enable the support of C++11 in g++, you can add the option `-std=c++0x` 
or `-std=c++11` (depending on the version of the compiler). 
In Rcpp, support of C++11 can be done throught the `settings` option 
of the `cxxfunction`. The following is an illustration example.  

        code = 'std::vector<int> v{1,2,3};
        return wrap(v);'
        settings=getPlugin("Rcpp")
        settings$env$PKG_CXXFLAGS=paste('-std=c++0x ',settings$env$PKG_CXXFLAGS)
        fcpp11 = cxxfunction(body=code,includes="#include <vector>",settings=settings)

9. To link libraries, 
you have to add options to the `settings` argument of `cxxfunction`.
The following is an example of linking the GSL library. 

        code = '
        int n(as<int>(r_n));
        double p(as<double>(r_p));
        std::vector<double> x(n);
        ralpha_wrapper(x.begin(), x.end(), p);
        return wrap(x);
        '
        includes = readText('beta.cpp')
        settings=getPlugin("Rcpp")
        settings$env$PKG_LIBS = paste('-lgsl -lgslcblas ', settings$env$PKG_LIBS)
        settings$env$PKG_CXXFLAGS=paste('-std=c++0x ',settings$env$PKG_CXXFLAGS)
        ralpha = cxxfunction(signature(r_n="integer", r_p="double"), 
                        body=code, includes=includes, settings=settings)

## Traps

1. Missing namespace prefix when calling functions that present in different namespaces.
For example,
if you want to use `std::abs` but forget the namespace prefix (`std::`),
the function `Rcpp::abs` will be used.
This is a very tricky bug.

2. Forget to synchronize the state of random number generators 
used in Rcpp with the one used in R. 
In this situation, 
random number generating functions in Rcpp always generate the same number. 
If you use random number generating functions in Rcpp but always get the same result, 
it's probably that you forget to synchronize the state of random number generators.
A simple way to synchronize the state of random number generators in Rcpp is to 
define a object of `RNGScope` before you call random number generating functions.
For example,
you can put the statement `RNGScope scope;` in the function/block that you have to call 
random number generating functions.
