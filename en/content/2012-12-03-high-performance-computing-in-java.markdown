UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-02-20 10:52:13
Slug: high-performance-computing-in-java
Author: Ben Chuanlong Du
Title: High Performance Computing in Java
Category: Computer Science
Tags: programming, thread, Java, HPC, parallel, concurrency, high performance computing

## Efficient Computing

1. Avoid resizing arrays and ArrayLists if the alternative does not cost
too much memory.

2. Avoid creating unnecessary objects if possible.

## Parallel Computing

1. After you open a pool, the threads in the pool might still exist and
run outside the scope (the method in which the pool is created). To
ensure that the pool is destroyed before the end of its scope
(before the program leaves the method in which the pool is created),
you must wait for termination of pool manually. Notice that some
other packages in java or some other languages might have
implemented thread pool differently, but generaly speaking, what
java does is the nature way. Depends on what you want to do, you
must decide whether to manually wait for termination of the pool
carefully.

2. Not all parallel code runs faster than serial code while parallel
code is almost surely much hard to develop, so you have to think
about your problem and decide whether it is worth writing parallel
code to solve your problem. Usually the process of generating random
numbers cannot be parallelized, so if the process of generating
random numbers is the bottleneck, it is no use to do parallel
computing.

3. Remember to use defensive copy for constructors and methods of
classes that implement `Runnable`, except for these variables
through which threads communicate.

4. `Runtime` in Java can help to find the number of processors that a
computer have. Notice that every Java application has a single
instance of class Runtime that allows the application to interface
with the environment in which the application is running. The
current runtime can be obtained from the `getRuntime` method.

5. Never use more threads than the number of processor of the machine
on which the Java application will be run on. With the help of
`Runtime` we can write universal code for parallel computing.

6. You should always synchronize shared objects among different threads
because of delay effect in parallel computing. If we can make
different threads independent, we'd do it because this not only make
the code easy and run faster.

7. You should use thread pool to avoid the cost of creating new thread
if there are many different parts in parallel computing.

