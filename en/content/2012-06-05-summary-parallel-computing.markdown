Status: published
Title: Parallel Computing in Different Programming Languages
Date: 2019-12-19 09:41:32
Slug: summary-parallel-computing
Author: Ben Chuanlong Du
Category: Computer Science
Tags: Mathematica, lock, programming, C/C++, thread, Java, HPC, parallel, R, concurrency, mutex, GPU Computing, high performance computing

There many different ways for parallel computing. 
This article focus on multithreading computing.
Generally speaking, commercial softwares have very good support for parallel computing. 
For example, Mathematica, MATLAB and Revolution R all have solid support for parallel computing. 
Mathematica and MATLAB also have good support for GPU computing. 

## Python
Multithreading does not speed up computation in Python due to GIL. 
An alternative way use multiprocessing (using the `multiprocessing` library) in Python.
This is contrarary to most other programming languages which encourages multithreading rather than multiprocessing 
as processes are much heavier than thread and communication among processes are harder than communications among threads.
Despite this, `multiprocess.Pool.map` makes parallel computing real easy in Python.

## [Parallel Computing in Bash](http://www.legendu.net/misc/blog/parallel-computing-in-bash/)

## Mathematica
In Mathematica,  
there are a bunch of functions starting with "Parallel" 
(e.g., `ParallelTable`, `ParallelSubmit`, etc) for the purpose of parallel computing. 
If I remember correctly, 
one has to distribute a user-defined function to kernels manually before you can use it for parallel computing in Mathmatica 7 and earlier. 
In Mathematica 8+, 
user-defined functions are automatically distributed to kernels 
so that you can use your own function for parallel computing directly, 
which is very convenient. 
Actually, 
Mathematica is the most convenient one to do parallel computing among all programming languages mentioned in this post, 
but at the cost of effciency of parallel computing. 
Mathematica is famous for its intellegency but also nutorious (at least I think so) for running slow. 
It is the most smart but also the slowest programming languages among all programming languages 
that I have ever used (not just these mentioned in this post). 
It is probably safe to say that Mathematica is the slowest programming language. 
The more convenient a language is, the slower it is generally speaking. 
It is hard to get both. 
A way to improve the speed of Mathematica code is 
to compile the code to C code or some other code that is more efficient to run. 
I will not go deeply into this since it is not the main purpose of this post.

## MATLAB
There are several ways to do parallel computing in MATLAB. 
The one I know (and is probably the easiest way) is to use `parfor` instead of `for` in loops. 
If there is only 1 thread, 
`parfor` works in serial. 
To better use `parfor` for parallel computing, 
you have to learn some concept about different kinds of variables, 
e.g., slicing variables, reduced variables, etc.
Understanding these concept helps you write better parallel code, 
and it help debugging if your code does not work. 
To let `parfor` use multiple threads, 
you must open the matlabpool manually. 
For example, 
to use the local host for parallel computing, 
you use the following command to initilize a pool with 8 workers 
(I assume the computer has 8 cores). 
```MATLAB
matlabpool open local 8
```
`parfor` in MATLAB works like a charm most of the time. 
Consider the fact that MATLAB code is very fast compared to other scripting languages, 
it is a good choice for heavy numeric computing.  
However, 
for some reason I am not sure about (probably bug in MATLAB interpreter), 
sometimes even very simple parallel code does not work. 
If this is happens, 
it is usually not easy to get if fixed. What you try is to change reduced variables to a slicing variable, 
and operate on the slicing variable after parallel computing. 
Another annoying thing I met when doing parallel computing in MATLAB was that 
sometimes the exactly same code did not work on another machine with the same version of MATLAB. 
I was not sure what caused the problem, 
but I found that it was related to functions end with `rnd` 
(random number generating functions) I used in the code. 
There are some old version functions starting with `rand` for generating random numbers, 
which are more robust and always works well in parallel computing.

## R
R (not talking about Revolution R) has many packages for parallel computing.
Actually there are too many and thus make people confused about where to get started. 
Fortunately, the company of Revolution R contributed some packages to CRAN to make parallel computing in R unified. 
It is similar to `parfor` in MATLAB. 
You use `foreach` together with `%dopar%` to do parallel computing. 
To do this, 
you must first register a backend for it. 
The following simple example does parallel computing using package "doMC" as the backend of `foreach`.
```R
library(doMC)
library(foreach)
registerDoMC(8)
n = 10000
j=foreach(i=1:n) %dopar% {
    for(j in 1:10000){
        1000 %% 31
    }
}  
```
You can use package "snow" as the backend if you have access to a cluster.
In R, 
you do not have to worry about different kind of variables. 
Variables outside the `foreach` loop are shared among threads, 
and `foreach` returns a list of results corresponding to each iteration. 
Surely access variables outside the `foreach` loop
make the parallel compting less efficient. 
A better way is to let `foreach` return a list of results and then operate on the list. 
Sometimes, 
when you do parallel computing in R, 
the program does not speedup as you expect. 
This is probably because some functions you used has already been implemented in parallel. 
Notice that `foreach` is not just for parallel computing. 
Even if you do serial computing, you can still use `foreach` with `%dopar%` replaced by `%do%`. 
It is usually faster than the `for` loop.

## Java & C++
Both Java and C/C++ support multithreading directly. 
The concept of multithreading computing in these two languages are similar. 
You have to create multiple threads, 
and let each of them run part of the job.
Java has a better support for multithreading in the sense that its standard library supports thread pool. 
There is still no directly support of thread pool in C++11. 
You have to non-standard libraries for this purpose. 
For scientific computing (e.g. statistical simulations), 
it is usually every easy to partition the work by yourself 
and assign them to different threads so that a thread pool is not essential.
For example, 
if you want to do a simulation of 1000 runs, you can create `k` threads, 
assign the first `1000/k` runs to the first threads, 
assgin the second `1000/k` runs to the second threads, 
and so on and so forth.
To share data between different threads, 
usually you have to lock and unlock shared resources. 
In Java, 
this can be done through `ReentrantLock` class or `synchronized` methods.
In C/C++ this can be done through `mutex`. 
Details about multithreading computing in these two languages is beyond the scope of this post. 
For more information about multithreading in Java, 
you can refer to the book `Big Java` which is really easy to follow, 
and "C++ Concurrency in Action" is a good book about multithreading for C++. 


Finally, 
I want to mention that not all computing job is suitable for parallel computing. 
The more comminication threads has to make, 
the more dependent the jobs are, the less efficient the parallel computing is. 
In statistical simulations, 
random numbers are usually generated in serial 
(though there are parallel algorithm for random number generating, the popular RNGs are usually serial). 
If a simulation is mostly about generating random numbers, 
it is probably non-benefitial to do parallel computing.
