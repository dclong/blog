UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Lvalue Reference and Rvalue Reference
Date: 2015-01-15 02:17:12
Tags: C/C++, reference, programming
Category: Computer Science
Slug: lvalue-rvalue-reference
Author: Ben Chuanlong Du

<img src="http://dclong.github.io/media/cpp/left-right.jpg" height="180" width="200" align="right"/>

## Difference betwen Lvalue and Rvalue Reference

1. Lvalue and Rvalue are terrible names. 
They are due to historical reasonal but people stuck with these names.

2. A lvalue reference has a name while a rvalue reference has no name, in other words, 
a lvalue reference is persistent while a rvalue reference is temporary.
Let `f(vector<int> && x)` be a function/method (can be a constructor) 
which takes a rvalue reference as argument.
It is common to misunderstand `x` as a rvalue reference. 
When a rvalue reference/temporary object is passed to `f`, 
it is moved to `x`,
however, `x` itself is not a rvalue reference/temporary object because it has a name.
`&&` only means that it is OK to move `x`, but does not mean that `x` is a rvalue reference/temporary object.
And at the place where you intend to move `x`, 
you must use `std::move` manually to move it, 
otherwise, it get copied. 
Values return by functions/methods and expression are temporary values, 
so you do have to use `std::move` to move them when you pass them 
to functions/emthods that take a rvalue reference as argument.

3. You can take the address of a lvalue reference but you cannot take the address of a rvalue reference. 

4. When you apply `std::move` on a primitive type variable (double, int and so on), 
it is usually lefted unchanged. 
This means that copy is usually the fastest way to implement
move on primitive types, but it is not guaranteed that copy is 
always used (different compiler might have different implementation on this). 
After being moved a variable still have a valid but unspecified value.
So do not use the value in a moved variable until you given it a new known value.  

5. A lvalue referece cannot be moved. 
The reason is that such operation is not necessary. 
To move the object that the lvalue reference points to, 
one can move the object directly.

2. You cannot use a vecotor (similar for other containers) of lvalue references,
because lvalue references have to be initialized to point to valid objects when they are created. 
An alternative way is to use vector of pointers/iterators instead. 

1. Always use `const` lvalue reference, unless you intend to change the referenced object. 

## How to Use Rvalue Reference

1. Do not write && to return type of a function,
and there is no need to return a local variable using `std::move`.
When return a local variable, it is automatically move in C++11. 
However, if the local variable is static, then it is not moved as expected.

2. When you copy content of an argument in a function, 
overload it with rvalue reference and move the content.

3. When you write a class with the copy constructor and the assignment operator, 
write also the move constructor and the move assignment operator.


