UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-03-13 10:53:45
Slug: cpp-common-mistakes-and-debug
Author: Ben Chuanlong Du
Title: Common Mistakes in C++ Code and Ways to Debug
Category: Computer Science
Tags: debug, C++, mistake, programming, trap, bug, error


## Debugging

1. gdb is a excellent command tool for debugging C/C++ code. 

## Syntax Mistakes

2. Missing "}". 
When this happens, 
you usually get lots of error message when you compile your code. 
And these error messages are often hard to understand and seems not related to your code. 

3. Missing template arguments. 
This is relative easy to debug. 
The compiler will usually give clear enough error message. 

7. Using member types of template types without the `typename` prefix. 
For example, 
instead of 

        template<class InputIt, class set<InputIt::value_type>> void f(...){
            ...
        } 

it should be 

        template<class InputIt, class set<typename InputIt::value_type>> void f(...){
            ...
        }

The g++ compiler is usually smart enough to detect a missing `typename` and give you the right instruction
on how to fix the code. 

8. Accessing members in a template base class without using `this` pointer.
The compiler will tell you that these members are not found. 

## Logical Mistakes

6. Abuse of `auto`. 
Tough `auto` it a lot more convenient to work with template code, 
it is dangerous if an expression corresponds to several different types. 
For example, 
if you use 

        auto x = "abc";

then `x` is of type `const char *` not `std::string`. 

4. Passing invalid iterators to functions/methods that operate on containers.
This usually result in segmentation fault. 
For example, 
if you use the `erase` method of a vector `x` (of length 10) to erase a range of elements from it,
the second iterator must be no "smaller" than the first iterator.
The code 

        x.erase(x.begin()+1, x.begin());

will result in an error message of segmentation fault when you compile it.

5. Forgeting to return a value for a non-void function/method. 
This usually results in segmentation fault.

## Compile Option Mistakes

5. Forgetting the `-lpthread` option when compile code which uses the `<thread>` header.
The compiler usually gives the following error message.

        terminate called after throwing an instance of 'std::system_error'
          what():  Unknown error 4294967295
        Aborted




