Status: published
Author: Ben Chuanlong Du
Date: 2020-03-03 11:00:37
Slug: tips-gcc-compiler
Title: Tips on C++ Compilers
Category: Computer Science
Tags: C++, programming, GCC, thread, compiler, link

## GCC
1. User option `-lpthread` to link the thread library when your code use the thread library. 
If you do not use, the option `-lpthread`, you can probably compile your coe without any 
error or warning, but you will probably get the following error when you run the code.

        terminate called after throwing an instance of 'std::system_error'
          what():  Operation not permitted
          Aborted


2. User option `-std=c++0x` to compile C++11 code. 

3. Some thumb rules for compiler optimization:
    - when you need to debug, use the option `-O0` 
    (and the option `-g` to generate debugging symbols.)

    - when you are preparing to ship it, 
    use the option `-O2`.

    - when you really care about performance (e.g., for use on Gentoo), 
    use the option `-O3`. 
    However, this is not always safe. 

    - when you need to put it on an embedded system, use `-Os` 
    (optimize for size, not for efficiency.)

4. use to `-D` to predefine macros

## Clang

1. use `libc++` instead `libstdc++`
