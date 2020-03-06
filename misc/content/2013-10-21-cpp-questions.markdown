Status: published
Author: Ben Chuanlong Du
Date: 2019-12-24 11:04:24
Slug: cpp-questions
Title: Some Questions About C++
Category: Computer Science
Tags: questions, C++, programming

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
1. in C++, vector is the fastest, is the same for Java and other programming languages, 
    I think the concept of cache applies, but what about deep copy, etc.?

2. what's the difference between a vector of pointers and a vector of objects?
    if class object, how does it store them in memory ...? 
    does it save address or reference? and all objects (all contents) continus? 

1. when does one have to provide copy/move constructors and operator=?

3. different ways to pass a function/functor as argument? 
    It seems that to me that there are many diffrent ways. 
    For example, one can use function pointers,
    functional argument, or use template ...

    in the standard library, the template way is used a lot.
    which of them is recommended? 

    My opinion:
    function pointer is more C style,
    functon object is C++ style and cleaner. 
    Both of them requires you to specify the signature of the function.
    However, template is more flexible which doesn't require you to specify the signature. 

5. about "{}" initializing list? what's wrong? Do I misunderstand it?
    Just avoid using "auto" together with "{}".

6. multiple std::tolower function, how to resolve overload problem when using it as a function in algorithm functions?

7. what's the difference between std::min and std::fmin? 
    std::min is more general
    std::fmin is specifically for floating point numbers

8. the static_cast from integer/double to unsigned integer is very tricky. 
    be sure you understand how it works. -2 will be casted to a large number. 
    I think some bits are discarded ...

9. it seems to me that when using integers, 
    it's easy to get an overflow bug, especially when you use unsigned integers ...
    see whether there's a good practice to avoid this.

10. what happens if you use a reference to a reference? do we get a rvalue reference or what?

11. a question about boost::graph, vertex iterator and other iterator, sorted or not?

12. what happens if the arguments of make_pair is rvalues and a value 
    also does it get ...

13. when is recursive definition possible? in your HMM case, it seems that the components must be separated ...
    because it relies on defintion of ... and thus cannot be put into the definition ...

14. can we use g++ with libc++?
    g++ -nostdlib -lc++ -lc++abi -std=c++11 -o plop /usr/lib/x86_64-linux-gnu/crt1.o /usr/lib/x86_64-linux-gnu/crti.o foo.cpp /usr/lib/x86_64-linux-gnu/crtn.o -isystem/usr/include/c++/v1 -lc -lgcc_s

15. why C/C++ library offeres only shared memory model?

## Template Meta Programming

16. can a template class be defined in a non-template class?

1. how to define a hash function for a user defined class?

## File System

1. how to get the current working directory?
