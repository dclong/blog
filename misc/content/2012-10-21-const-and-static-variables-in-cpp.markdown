UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-03-25 00:44:03
Slug: const-and-static-variables-in-cpp
Author: Ben Chuanlong Du
Title: Const and Static Variables in C++
Category: Computer Science
Tags: programming, C++, static, const

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Const Variables

but you can initialize a `static constexpr` variable inside the defintion of a class.

5. `constexpr` means that the corresponding value can be dertermined at compile time. 

## Static Variables 

4. You cannot initialize a `static` member variable of class 
inside the definition of the class 
and you'd better not initialize it in a header file,
instead, 
you should initialize a `static` variable in the source file. 
This is because if a `static` variable is initialized in a header file 
and the header file is included multiples times,
the code cannot be compiled.

6. Java has the concept of static blocks while there is no such concept in C++. 
However, by calling a helper function/method (with code intended to be static) in 
a static statement you can achieve similar effect. 
You can also use lambda functions in a static statement to initialize complex objects such as vectors and so on.
For example you can use the following code to statically initialize an integer vector to be 0 to 10 (exclusive). 
```C++
static const vector<int> x = [](){
    vector<int> x;
    for(int i=0; i<n; ++i)
        x.push_back(i);
    return x;
}();
```
4. Static variables can be very useful sometimes, 
however, 
defining static variables inside non-static methods is potentially dangerous.
This is because these static variables are intialized once per program not once per instance,
so that every instances of the class shares the same copy of the variable. 
General speaking, 
it is recommended that you avoid using static variables unless absolutely necessary.
And when you do have to use static variables,
be careful as they are "global".

5. Static variables are sometimes used in recursive functions/methods as a way to improve performance. 
In these situations, you can separate the recursive function with static variables into 2 functions/methods.
The first one defines a local object and calls a second recursive function/method which takes a reference argument. Give an example here ...

