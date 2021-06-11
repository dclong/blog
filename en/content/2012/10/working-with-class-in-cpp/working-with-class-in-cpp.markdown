UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2012-10-05 10:56:31
Slug: working-with-class-in-cpp
Author: Ben Chuanlong Du
Title: Working with Class in C++
Category: Computer Science
Tags: C++, destructor, programming, inheritance, override, class, hidding, constructor
Modified: 2015-08-05 10:56:31


Illustrative examples for the following discussions can be found 
[here](https://github.com/dclong/cearn/tree/master/class).

1. It is suggested that you also provide a default constructor 
if you ever provide a user-defined constructor when writing a C++ class.

2. If you want to allow deleting a derived class from a pointer of the base class,
you have to make the destructor of the base class `public` and `virtual` 
even if it does nothing. 
If you want to prevent deleting a derived class from a pointer of the base class, 
make the descturctor of the base class `protected` and `virtual`.

3. If you derive a class from a base class, 
the destructor of the base class is called automatically 
so that you do not have to call it manually.

2. If a derived class `D` has a method with the name `fun`, 
then all non-virtual methods with the name `fun` (no matter what signature they have) in its 
base class `B` are `hidden` by the method `fun` in `D`.
Suppose `d` and `b` are instances of the class `D` and `B` respectively,
and you invoke the method `fun` throught these two instances, 
then everything works OK (in the sense that the `right` method is invoked).
However, this is different from `overridding`.
The problem is that `hidden` does not support polymorphism. 
If you have a pointer of the base class `B` pointing to an instance of the 
derived class `D`, and you invoke the method via the pointer, 
then `fun` of the base class `B` will be called. 
To support polymophism, you have to `override` the method `fun` in the base class `B`.
To do this, you have to mark `fun` as virtual in the base class. 
To help the compiler (and also make your code more readable), 
you can use `override` after the signature of method explicitly.
[Here](https://github.com/dclong/cearn/tree/master/class/inheritance) is 
an example illustrating problems discussed above. 

2. Overriding method must have the same return type as the overrided method.
(not sure whether this is required in Java)

3. If you write your own version constructor for a class, 
you'd better also provide the copy/move constructor and assignment operator. 

4. You'd better not use lvalue references in a class that point to an object outside the class.
A better way is to pass the object by lvalue reference to methods that need it.
If you ever decide to use a lvalue reference in a class that point to an object outside the class, 
you must initialize it in the initialization list of a constructor. 
This is because when you initialize a lvalue reference, 
you must point it to a valide object. 

5. Generally speaking, member variables should not be declared as public,
unless they are `static constant`. 
Also you should not declare member variables as `protected` unless 
you are sure that the derived classes want to access these member variables directly. 
If you define a proteced member `m` in a base class `B`, 
a derived class `D` can access and modify (if `m` is a data member) `m` in its own class or throught its own instances
but not throught other arbitrary object.
For example, if `b` is an object of the base class `B`, 
you cannot access or modify `b.m` directly in the definition of the derived class `D`.


6. It is suggested that you provide a `to_string` method, 
rather than overridding the `<<` operator. 

7. You'd better not use overloading and default parameters at the same time. 
Because this might make compiler fail to find the right version of function/method to call. 
Generally speaking, overloading is more powerful and thus prefereed.

8. Inheritance works with template class, 
i.e., you can derive class from template classes. 

9. A `swap` method can make the implementation of copy and move structor unified and thus more conveneint. 
It is suggested that you make the `swap` function `public` (at least `protected`) if you provide one.

10. If a class have many variables to be initialized, 
you can think of intializing non-critical variables in the definition 
of the class and provide public method to access and modify them. 
This make it easier to implement constructors. 

11. Always mark a method as `const` if it does not change the state of the object.

12. It is suggested that you intialize member variables in the constructor initializeing list 
(after `:` before `{`).
Surely you can achieve the same by assigning values to member variables in the body of constructors, 
but in this way these member variables are first initialized to default values and then assigned values,
which is not as efficient.

## Virtuality

The following are some guidelines for virtuality from Herb Sutter.
The original article can be found [here](http://www.gotw.ca/publications/mill18.htm).

13. Prefer to make interfaces nonvirtual, using Template Method.

14. Prefer to make virtual functions private.

15. Only if derived classes need to invoke the base implementation of a virtual function, make the virtual function protected.

16. A base class destructor should be either public and virtual, or protected and nonvirtual.

A few points to add:

1. A virtual method can be overridden by a derived class even if it is private.

2. A class without a public destructor cannot be used by itself. 
It servers as a base class only. 

