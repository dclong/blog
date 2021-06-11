UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: General Tips for MATLAB
Date: 2012-12-08 10:35:47
Tags: tips, skills, programming, MATLAB
Category: Computer Science
Slug: general-tips-for-MATLAB
Author: Ben Chuanlong Du
Modified: 2014-09-08 10:35:47


## Skills

1. MATLAB support profiling running time of code, 
so that you what to work on to optimize your code.s

1. It is expensive to allocate a new block of memory (not only in MATLAB
but also in other programming laguages), 
so you should avoid allocating new blocks of memory all the time. 
It is better to allocate a big block of memory once and forever 
if you know the actually size of memory that you have to use 
(e.g. usually you know the size of arrays and matrices that you are going to use) 
than to allocate small blocks of memory many times. 
If it is impossible to avoid allocating new blocks of memory, 
it is better to allocate a bigger memory than needed each time. 
In this way, you waste space but might save much time.

2. You can use block `try ... catch ... end` to handle code that might throw exception in MATLAB. 
You should be aware of the importance of handling exception. 
In many cases you just cannot afford to stop running code, 
for example the program written for a rocket should not stop running when exception happens. 
Even for statistician, 
it is very important to handle exceptions. 
For example, if you run a code which might takes 2 month, 
but your code throws out an exception after running a month. 
Do you want the program to the stop running after half the the long task has been done? 
So a better ways is always handle any exceptions that throws out. 
Some exceptions might result from hardware (e.g. no enough disk space). 
In this case, 
you can let your code notify you (e.g. via email or text message) 
and then wait for you fix the problem and then continue running.

3. Sometimes you might want to write a user-defined function 
with variable (even unknown) number of arguments. 
There are some functions helpful for this in MATLAB. 
`nargin` and `nargout` returns the number of input variables and output variables; 
`nargcheck` and `nargoutchk` validate number of input and output arguments respectively; 
`varargin` and `varargout` stand for input and output argument lists respectively.

4. break, return goto and error

5. By default, MATLAB use "short" format to display out, 
which uses only four decimal digits for numbers. 
To change the display format, you can use `format`. 
For example, you can use `format('longG')` to make MATLAB give more readable outputs.

6. You can execute system command by invoke `system`, 
which is similar to R. 
For example, 
to shutdown computer 1 hour after computing in MATLAB is done in Windows operating system, 
you can add `shutdown('shutdown/s /t 3600')` at the end of your code 
or just type it into the console while the code is running. 
Similarly, 
you can invoke `dos` to run dos command and `perl` to execute perl script.

7. You can use `computer` to get information about the computer on which MATLAB is running.

## Programming

0. MATLAB supports boolean variables. 
(I somehow have an impression that MATLAB does not support variables 
and one must use 1 or 0 instead. 
I am not sure whether boolean variables are introduced in newer versions of MATLAB or not.)
A boolean variable has 3 possible values: `true`, `false` and `unknown` 
(more programming languages are supporting ternary boolean variables).
You have to be very careful about the `unknown` value.
It can be error-prone sometimes.
Logical comparisons can be assigned to (boolean) variables directly. 
Numerical values are casted to boolean values when needed.

1. The syntax of MATLAB is kind of a mix of `Visual Basic` and `C`. 

2. 
        function [y1, y2, y3] = f(arg1, arg2, arg3, arg4)
            statements
defines a function named `f` in MATLAB. 
To get all 3 return values of `f`, 
you must call it in the form of `[rv1, rv2, rv3] = f(arg1, arg2, arg3, arg4);`;
to get the first 2 return values of `f`, 
you call it in the form of `[rv1, rv2] = f(arg1, arg2, arg3, arg4);`, so on and so forth.
Notice that you cannot use a vector with length `k` to extract the first `k` return values of `f`. 
The reason is that the types of return values are unkown and can be of any types. 
The tricky part is that when you extract the return values of `f` using a vector of length `k`,
it is possible that no error or warning message is displayed. 
The first return value of `f` is assigned to the vector or all elements of the vector
(if it is an slicing of an array).

3. The first function defined in a m-file is the main function 
and will be called when the m-file is called.
All subsequent functions in the m-file can only be called by the main function.
It is recommended that you named a m-file after the main function.

2. There are two types of objects in MATLAB: value object and handle object. 
A value object behaves like being passed by value 
while a handle object is passed by reference. 
By default objects (matrix, array and so on) in MATLAB are value objects. 
However, even if a value object behaves like being passed by value, 
if it is not modify inside a function when passed to the function, 
no copy will be made into the workspace of the function. 
This system is so called copy-on-write, 
which might save much memory if the matrices or arrays passed are huge. 
The famous statistical software R will always make a copy of a argument 
if it is passed by value.

3. MATLAB does not check the passing of parameters to functions. 
Whether the parameters passed to a function are illegal can only be decide at run time, 
which is the way that most interpret language use.
If your code takes lots of time to be run (e.g. a big simulation),
you'd better first downgrade the complexity of the problem and run a test code, 
otherwise you might find that there is in your code after you have run your code for a long time.

4. By default, 
variables appear in a user-defined function 
and variables in the workspace are local variable, 
which means that you cannot use variables from the workspace in a user-defined function
nor can you use variables from a user-defined function in the workspace. 
To make a variable global, 
you can use command `global`, e.g. to make variable `x` global you can use `global x;`. 
If a variable is global, 
you can use it everywhere if you have made the necessary declaration 
(e.g. you have to declare that a variable is global in a user-defined function, 
if you want to use it as global.), 
and its value will be the same everywhere 
(This is because no matter where you use it, 
it points to the same place in the memory).

5. To run a bunch of code, you can put the code into a M file or you can define a function. 
Sometimes, 
there are a few of small pieces of code that you use a lot 
but they are too short and will be used only in a single work 
that you hesitate to write them into M files or to write them as functions. 
What you can do is to define them as inline functions or function handles. 
Inline functions work only for very simple functions. 
Every symbol appear in a inline function string is treated as a variable, 
so you cannot pass data into a inline function except for constants. 
Function handle is more flexible way to deal with this situation. 
You can use any object in the workspace in a function handle. 
What's more, a function handle cannot be changed after it is defined. 
For example, if a function handle uses an object in the workspace, 
it remains the same even if you change the object or remove it from the workspace, 
which is usually what we expect. 
So generally speaking function handles are more flexible 
and useful than inline functions, 
but surely it is slower than inline functions. 
Function handles are usually used to wrap existing functions for convenient use. 
For example, 
in statistics data is usually passed to a likelihood function as a parameter 
because global variable is generally not a good idea. 
When you optimize a likelihood function, 
you do not want to optimize over the data parameter. 
To handle this situation, please refer to section `optimization`.

6. `eval` evaluate string containing MATLAB expressions.

6. The passing of a function as an argument of another function 
is achieved through function handle in MATLAB. 
To get the function handle of an existing function (not a function handle), 
you can simply add a prefix `@` to it.

