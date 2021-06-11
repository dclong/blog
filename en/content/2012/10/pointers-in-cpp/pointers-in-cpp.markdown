UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Pointers in C++
Date: 2012-10-21 00:00:00
Tags: C++, programming, pointer
Category: Computer Science
Slug: pointers-in-cpp
Author: Ben Chuanlong Du
Modified: 2012-10-21 00:00:00


## Pointers

0. No pointer, no polymorphism.

1. C/C++ is notorious for raw pointers. 
While pointers can boost up the speed of programs, 
it invites a trillion chances for making mistakes. 
You should avoid using raw pointers, 
instead, 
consider using `unique_ptr`, `shared_ptr` and `weak_ptr`.
They are almost as efficient as raw pointers but much safer to use. 

1. If `p` is a dynamically allocated array, 
you have to use `delete[] p` to delete it when it is no longer required. 

2. `auto_ptr` objects cannot be stored in STL containers, 
because they are not copy-construable or assignable.


