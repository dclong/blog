UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Template Meta Programming
Date: 2012-10-21 00:00:00
Tags: overload, programming, TMP, specialization, C++, template
Category: Computer Science
Slug: template-meta-programming
Author: Ben Chuanlong Du
Modified: 2012-10-21 00:00:00

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


Illustrative examples for the following discussions can be found 
[here](https://github.com/dclong/cearn/tree/master/template).

2. Do not use templated generic function/method unless necessary. 
Templated generic function are more useful generally speaking.
However, templated function/method are inconvenient to use sometimes,
and they are often error prone.
Always keep in mind the first programming rule "KISS" (keep it simple stupid).

0. A good design is essential in template meta programming. 

1. When you write templated class/function/method, 
it is suggested that you use as fewer template arguments as possible. 
Because it is often much harder and requires much more work to specialize a 
templated class/function/method with more template arguments. 
By using templated methods, one can often reduced the number of arguments 
required by a template class. 

1. When you call a template function,
the compile try to find the right version to call.
If a template function does not take any argument,
then there is no way for the compiler to figure out the right version from argument (as there is no argument)
So in this case, 
you must supply the template argument manually.
If a template argument is supply manually,
then the argument passed to the template function are
casted to the right type (specified by the template argument) if necessary.

3. If a type depends on a template argument, 
then you have to use `typename` before the type to let the compiler 
know that it is a template type. (This is not right ..., sometimes you need it sometimes not ...)

5. Whenever you refer to a template class, 
you must specify the template arguemnts. 
If all template arguments have default values, 
then they can omitted, 
however, you still have to use `<>` after the name of the class
to let the compiler know that it is a template class.
Forgetting template arguments is a common mistake when using template classes. 
When you implemente a template method outside the definition of its class,
you must start with `template<...> `.
This is because the template arguments of the template class is only in effect
inside the scope of the class. 

6. A specialization of a template class does not have access to members in the 
general version of the class if these members are not defined in the specialized class.
That is when you specialize a class, 
what you define in the specialized class is what is available to it.
Different specializations of a template class usually have members with same names. 
This make it convenient to write template functions which can 
handle different versions of the template class. 

7. Template functions/methods can only be "full" specialized. 
That is when you specialize a template function/method, 
you must specialize all template arguments. 
If a template method is inside a template class, 
then you must first specialize the template class so that
you can specialize the template method. 
On the contrary, you can specialize a class without specialize 
its template methods. 
"Partial" specialized member functions are achieved through specialization of class.
Relative to the specialized class, 
the "partial" specialized member function is still full specialized. 

4. The implementations of specializations of a template method must be outside 
the definition of the class. 
Also the orer of specialization of template functions/methods
matters if one depends on another.
This is similar to the concept that the order of functions matters if one depends 
on another.

9. Except types, you can also use values that are essentially integers 
(e.g., values of long, int, char, bool and so on) as template arguments.
However, you cannot use values that are essentially float point types 
(e.g., values of float, double and so on) as template arguments. 
For example, `std::get<2>` takes an integer as template argument. 

10. Specializing a template class is often tedious. 
There are some ways to avoid specializing template classes. 
	1. Avoid specializing template methods in template classes unless the template class has only one argument 
	(in this case you can full specialize template methods), 
	because specializing a template method in a template class often 
	requires specialization of the template class. 
	Instead, a better way is to use overloaded methods. 
	Some examples using this trick can be found 
	[here](https://github.com/dclong/cearn/tree/master/template/overload-vs-specialization).
	2. If different versions of a template class requires different temporary variables, 
	it is often good idea to group these temporary variables into a struct and specialize 
	the small struct instead of the template class.

11. Functions operate on containers in STL often take iterators as arguments,
which is for the concern of writing more generic and easier-maintain code. 
However, this make it slightly inconvenient to use these functions and 
make the code insecure.  
When you write your own functions/methods that operate on containers, 
keep them simple and use containers as arguments unless generic is necessary. 

12. If you want to member types of a template type, add `typename` before it. 
For example, `template<class InputIt, class set<InputIt::value_type>> void f(...){...}` won't compile, 
but `template<class InputIt, class set<typename InputIt::value_type>> void f(...){...}` is OK.

13. When inheritating a template base class, 
protected members in the base class is not directly available.
You have to use them by `this` pointer. 

14. A template method cannot be virtual. 
Template is sort of static polymorphism while virtual is sort of dynamic polymorphism.
They cannot be mixed together. 



