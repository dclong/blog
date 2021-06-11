UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2010-11-10 01:23:25
Slug: functions-and-calls-in-r
Author: Ben Chuanlong Du
Title: Functions and Calls in R
Category: Programming
Tags: R, function, programming, call, CRAN
Modified: 2016-12-10 01:23:25

1. `"["` is a function in R.
It takes elements from a container (vector, matrix, list, etc.)
For example, suppose `lv` is a list of vectors.
The following code takes the first element of each vector in `lv`.
    
        lapply(l, "[", 1)

    In this way,
    you do not have to define a function to get the element of a vector by yourself.

        get_1st_elem = function(x) {
            x[1]
        }

2. You can assign value to an R object by its name (in string) using the function `assign`.

        > assign("x", 1)
        > x
        [1] 1

    You can get the value (i.e., deep copy not reference) of an R object
    (for general expression, use `eval` with `deparse`)
    by its name (string) using the function `get`.

        > get("x")
        [1] 1

        > get("as.character")
        function (x, ...)  .Primitive("as.character")

        > get(paste("as.", "character", sep = ""))(1)
        [1] "1"

    On the contratry,
    you can use the function `substitute` or `quote` to get the name (string) of an object,

        > deparse(substitute(ftree_0_4_0_0.5_100))
        [1] "ftree_0_4_0_0.5_100"
        > as.character(substitute(ftree_0_4_0_0.5_100))
        [1] "ftree_0_4_0_0.5_100"
        > as.character(quote(ftree_0_4_0_0.5_100))

    The function `dclong.fs::sym2str` is an interesting one
    which tries to be smart to convert an R object to the right string.
    Note that `get` only works on object names not string containing general expressions.
    To evaluate a string containing an R expression,
    you have to first parse it using the function `parse`
    and then evaluate it using the function `eval`.

        eval(parse(text = "x + 1"))

2. There are several ways to create function calls without executing it.
The first way is to use `call` by passing the name of a function
and corresponding parameters to it.

        > eval(rnorm.call)
        [1]  0.7618801 -1.2722733  1.1521628
    
    The second way is to create a list containing a function,
    and parameters to be passed to the function,
    and then set the mode of the list to `'call'` or coerce it to a call using `as.call`.

        list(rnorm, n = 4, mean = 3) -> call.rnorm
        mode(call.rnorm) = 'call'
        eval(call.rnorm)
        [1] 3.842330 3.027134 3.515679 2.346022

    The last way is to use the function `parse` to parse expressions (string).

        expr = parse(text = "rnorm(3)")
        eval(expr)

    This is useful when you want delayed evaluation or flexible calls.
    Though you can make a function flexible using dots arguments ("..."),
    you can use only one dots arguments,
    and all arguments in the dots arguments must be pass to one function.
    Using list with mode `'call'` and `eval`,
    you can make a user-defined function accept list as argument,
    which contains arguments to be passed to a call in the user-defined function.
    In this way,
    the list argument containing arguments to be passed to a call is comparable to the dots argument.
    The advantage of list argument over the dots argument is that
    you can use more than multiple list arguments containing arguments
    to be passed to different calls in a user-defined function,
    thus it is even more flexible.
    Another smart use of call and `eval` is to apply a function over a list of argument.
    For example,
    if you want to convert a list (of vectors/matrices) to a matrix,
    you can use the following code.

        # create a list with elements being 2 * 2 matrices
        x = list(
          a = matrix(0, 2, 2),
          b = matrix(1, 2, 2),
          c = matrix(2, 2, 2)
        )

        eval(as.call(c(rbind, x)))
           [,1] [,2]
        [1,]    0    0
        [2,]    0    0
        [3,]    1    1
        [4,]    1    1
        [5,]    2    2
        [6,]    2    2
        [7,]    3    3
        [8,]    3    3

    There is another R `do.call` which performs the above operations at once,
    i.e., it constructs and executes a function call from a name or a function
    and a list of arguments to be passed to it.
    The following is another example of converting a list (of vectors/matrices) to a matrix.

        do.call(cbind, list(
          matrix(0, 2, 2),
          matrix(1, 2, 2)
        ))
        [,1] [,2] [,3] [,4]
        [1,]    0    0    1    1
        [2,]    0    0    1    1

    In `data-structures`,
    you learned that there is a `sapply` which can apply a function over a list.
    The difference between `do.call` and `sapply` is that  
    `do.call` takes the whole list as an argument and returns only one result
    while  `sapply` takes each element of the list as argument and returns a list of results
    (Sometimes, theses results are reformed to a simpler data structure,
    e.g. a vector or a matrix.).

3. To check whether an object is a call, you can use `is.call`.

4. You can refer to missing arguments in user-defined functions.
R will not complain until these missing arguments are really required.
For example consider the following silly function.

        foo = function(x, y) {
          if (x > 0) {
              return("...")
          }
          return(foo(x = 1, y = y))
        }
        > foo(-1)
        [1] "..."

    Notice that `foo(-1)` calls `foo(x = 1, y = y)`.
    You might think that this is not valid because the argument `y` is missing,
    however,
    R does not complain about it because the argument `y` is never used.

17. Function `try` allows us to handle error-recovery,
which is similar to `try-catch-end try` in vb.net.
If you this function,
R does not stop executing code when error is detected,
rather you can decide what to do when error happens.

13. We can use function `switch` to write branch statement in R,
however this function is not very friendly.

14. We can use command `stop` to stop executing a function in R,
however it will print error message at the same time.
And what's more,
no values can be returned.
To avoid printing error messages or to return values when exiting a function,
we can use function `return`.
Even if a function do not return anything,
we can pass it as a argument to `return`,
and absolutely nothing will be return in this case.
This can be help if we do not want anything to be return in a user-defined function.
Notice that you can use return as a statement (i.e. put it on a single line),
but it has no effect.

12. You can use the names of build-in functions in R as parameter in self-defined functions.
To avoid confusion,
we can we use name space such as `base::matrix` instead of `matrix`.

11. You can define overloaded functions and functions with uncertain number of variables (using `...`).

5. We can define a function inside another function in R.
This can be helpful when we want to define some function that never be used again.

19. You can define sub functions in a function, which is very convenient.
For example,
sometimes you want to call another function inside a function.
However,
the function that you want to call is different every time
and you even do not how to define it before you get intermediate results,
i.e. the function that you want to call does not just differ in the form of arguments.
To achieve this,
you can use the strategy of defining sub functions inside a function.

20. Some functions in R require a function as argument.
To pass value to the argument,
you can directly give the define of a function instead of writing a function first
and then pass the name of the defined function to the argument.
This can be very convenient sometime,
e.g. when you use function `apply`,
the function that you want to call is not define in R yet very simple,
then you can use the strategy of passing definition to argument.

21. In R the arguments passed to a function can be changed,
e.g. if x is a argument a function,
then you can assign a new value to x.
Notice that in some other languages,
the arguments passed to a function cannot be changed, e.g. Mathematica.

22. For most functions in R,
you can just type in their names in R GUI to get their source code;
for functions written in S3,
you can use function `getS3method` to get their source code;
for other functions written in C or Fortran,
you have to download the source code of R in order to find the source code of these functions.

28. For a R function which accepts the dots argument (...),
you can pass basically any argument to it including dots itself.
So if you want to pass all stuff in a dots argument to a function,
you do not have to parse it.

3. Usually built-in R functions have many arguments
and because R use partial matches to pass arguments to functions,
you might never get a warning message
if you use some argument that actually does not exist.
If this happens when you use a function directly,
it is possible for you to find this subtle mistake.
However, if you make this kind of mistakes in a user-defined function,
then it can be a very tricky bug.
So it is recommended that you always check the arguments of functions
that you are not very familiar with before you use it.
When you come across some tricky bugs,
you might want to check whether it is resulted from miss-passed argument(s) or not.

9. R uses buffer to store the output and then print it when the buffer is full.
In order to print the information immediately you can use function `flush.console`
after you use function `cat` to print out information.

16. It is suggested that you always use `{}` when use branches and loops in R.

16. An R object exists ever since it is defined
until the end of its current evaluation environment.
So unlike C++ and Java in which an object defined in a block is only in effect in that block,
an object in R defined in a block will still be in effect outside the block.

18. Function `with` allows us to evaluate expressions in a data environment,
so it's convenient to use it to work with data frames.

24. You can use `T` to stand for `TRUE` and `F` stand for `FALSE` when you write code in R,
but you'd better use `TRUE` and `FALSE`
when you write user-defined functions
because `T` and `F` are actually global variables that are defined as `TRUE` and `FALSE`
while `TRUE` and `FALSE` are constant in R.

26. The function`missing` tests whether a value has been specified as an argument for a function,
so it can be used write very robust functions and functions with flexible number of arguments.

27. Some functions in R can only be use when R is run in interactive mode.
If you want your code to run flawlessly in any mode,
you can use `interactive` to check whether R is run in interactive mode or command mode,
and modify your code correspondingly.
Notice that when compiling an R package (commands such as `R CMD build` are used),
R is run in command mode.
As the reason mentioned before,
some of your examples might not run correctly,
which can make your package fail to pass the test.
A simply tricky is to include your code in block `if (interactive()) { ... }`,
so that it will not run when the package is compiled
while it runs perfectly when copied and pasted in R GUI.

31. `pmatch` performs partial string matching. If a function takes a
string argument, you can incorporate partial matching technic so
that the users can use partial values for the string argument. This
can make it a better experience for users to use the function.

30. Usually a `for` loop is more convenient than a `while` loop in all
kinds of programing languages. However, a `for` loop in R requires a
vector specifying the loop range. Sometimes it's not very convenient
to construct a general purpose vector for a loop, e.g. if a loop
starts from `loopStart` and ends at `loopEnd` with a step `loopStep`
but `loopEnd` is not always greater than `loopStart`, then it's
clumsy to use `loop`. In this kind of situations, you can use a
`while` loop instead.

34. The vector in a for loop is calculated once and stored.
So it will not take more time if you put an expression
which generate the needed vector in for loop.
What is more,
if you use an existing vector,
the for loop will not be affected even if you change the original vector.
(How about while loop? I think it is the same.
In one word,
the conditions is determined before the loop and cannot be changed in the loop.
It is the same in MATLAB, but different in Java.)

35. `addTaskCallback` registers an R function that is to be called
each time a top-level task is completed.
`removeTaskCallback` and `taskCallbackManager` are also very useful functions.
