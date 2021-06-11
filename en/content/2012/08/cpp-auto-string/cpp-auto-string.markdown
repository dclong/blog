UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: String in C++11
Date: 2012-08-20 00:00:00
Tags: auto, iteration, programming, C/C++, string, loop, char
Category: Computer Science
Slug: cpp-auto-string
Author: Ben Chuanlong Du
Modified: 2012-08-20 00:00:00

1. `auto s = "abcd"` creats `const char *` not string, so use `auto` with caution. 

2. Since a string in C++ is an array of chars, 
you can operate it like an array. 
For example, you can use range-based for loop and so on.

3. It is recommended that you use `std::string` in function which are not intended to be 
interfaces, and you use `const char *` as parameters of function that are intended to be 
interfaces (e.g., compiled as shared library and so on).

4. You can use `==` to compare whether the content of two `std::string` are the same,
but you cannot use `==` to compare the content of `const char *`.
