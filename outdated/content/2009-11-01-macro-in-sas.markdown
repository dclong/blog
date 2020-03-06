UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Macro in SAS
Date: 2015-08-28 16:43:05
Tags: dot, SAS, macro, branch, programming
Category: Computer Science
Slug: macro-in-sas
Author: Ben Chuanlong Du

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

[Here](https://bitbucket.org/dclong/sas_learn/src/) are some examples for SAS macro.

http://www.devenezia.com/downloads/sas/macros/?m=array

1. for macros, passing in a data set and operate on the data set sounds like a better way to do 
rather than passing plain text especially when there are lots of things to pass to a macro function 
and better to write outputs into datasets or macro variables rather than doing text substitute.

4. When you select values into macro variables using a sql procedure in a macro function, 
the macro varibles created are local to the macro function.

1. avoid return a value from macro, this gives you more trouble than convenience, 
just assign the value to macro or write results into a data set ...

1. Macros are substituted with their definition before SAS code is run,
which is similar to macros in other programming languages such as C/C++.
The essence of macro is text substitution.
Macro (text substitution) in SAS is tricky and error prone. 
It is suggested that you do not overuse user-defined macros in SAS.

2. Macro variable values have a maximum length of 65,534 characters. 

8. Arguments of a macro are local to the macro.
However, passing macro variable name can sort give you a taste of passing by reference.

9. It is recommended that 
you define macro variables as local in user-defined macro functions using `%local`,
especially if you use simple short macro variable names such as `i`, `n`, etc. 
Otherwise, you will end up using GLOBAL macro variables which is error-prone.

1. Do not define macro variables starting with "sys", 
otherwise, 
you confuse yours with system's macro variables.

2. Macro variable in the smallest scope is used if not defined.

## Important and Useful Macro Variables

1. &sysuserid

2. sysver: SAS version

1. %symexists

9. You can use command `%put _ALL_;` to show all macro variables in SAS log.
In addition to `_ALL_` you could use any of the following.
    
        - `_USER_` to list only user defined macro variables;
            
        - `_AUTOMATIC_` to list those defined by the SAS system;
                    
        - `_GLOBAL_` to list all session wide macro variables (global symbol table);
                    
        - `_LOCAL_` to list those macro variables local to the executing macro. 

2. Macros in double quotation marks are expanded 
while macros in single quotation marks are not expnaded.
For example,

        %let m = "Hello, ";
        title "&mWorld!";
generates `Hello, World!` while

        %let m = "Hello, ";
        title '&mWorld!';
generates `&mWorld!`.
This is similar to the behavior of Bash variables in strings.

2. Be careful when you use macro in SAS especially when you deal with `%if`. 
My suggestion is that avoid using `%if` if you can. 
You can use `%select` instead. 
If you have to use `%if`, 
you must be aware that the macro is expanded before it is run,
i.e. there is no branching going on when running the code. 
(Confused, I think %select will have same problem here,
put the probelamtic example here ...)

3. You can use dot (".") to connect a macro variable and usual characters. 
For example,

        %let i = 1;
        data set.&i;
        ...
is expanded to 

        data set1;
        ...
before running.

&&ms&i. cannot use &&ms.&i. the reason is that ms is not a macro.
there's good reason to end macros with ., becuase database.table ... actually, wait, try only one dot instead ...



1. `%sysfunc` execute SAS or user-defined functions. 
You must embed every expression 
envolving SAS or user-defined functions (not pure macros) in a %sysfunc statement.
For example,

2. `%eval` is similar to `%sysfunc` for only for simple arithmatic calculations in macro environment.

3. You can show SAS version information by running `%put _automatic_;`

4. `%sysuserid` represent the user id of the current SAS process. 
It is similar to the `whoami` command in Linux 
(of course `whoami` is a command not a environment variable, macro equivalent).

5. It is suggested that you always use dot after macro variables.

6. `%array` is a useful (non-built-in) macro for creating macro arrays quickly.
And `%do_over` (non-built-in) can be used to iterate through macro arrays.

12. It is not very convenient to use %do_over to apply a macro 
with multiple arguments to an array.
It is recommended that you use the `%do` loop manually 
inside a temorary macro. 

7. `%if`, `%do ... %end`, etc. can only be used in a SAS macro.

9. There is no concept of annonymous macro functions in SAS.

13. The option `phrase` in the `%do_over` macro cannot contain commas.

1. You can use the macro `%SYMDEL macro-variables(s);` to delete macro variables.
To delete all, e.g.,  global macro variables, 
you can use the the following code.

        data gmv ( keep = name ) ;
            set sashelp.vmacro ;
            where scope = 'GLOBAL' ;
        run ;

        data _null_ ;
            set gmv ;
            call symdel(name) ;
        run ;

1. The function `symget` gets the value of a macro variable 
into a variable in a data step.
It is similar to the function `getenv` in R 
and `os.getenv` in Python.

2. `symput` puts the value of a variable in a data step 
into a macro variable.
`symput` can also export a variable (inside a data step) to a local macro variable
inside a user-defined macro function.
It is ugly and error-prone to manipulate macro variables directly,
thus it is suggested that you define and manipulate (regular) variables 
in a `_null_` data step,
and exported (regular) variables to macro variables using `symput` when needed.

3. The macro `%sysget` function gets the value 
of the specified operating environment variable.
It is similar to the function `getenv` in R and `os.getenv` in Python.

4. You can nest definitions of macros,
however, 
it is suggested that you never do this
as it is very inefficient to do so.

5. When a macro functions takes no argument,
you can omit the parentheses in the definition 
and when you call it.

6. Be careful about the restriction of length of macro variables.
This can cause problems when you concatenate a input macro variable and a string
to create a new macro variable name.

7. Generally speaking, 
you do not want to overwrite a macro variable with a value that has a different meaning.
This is the same in many other programming languages (unless for serious performance concerning).
A rule of thumb in scripting language programming is not to change type of variables.

1. Macro variables and data sets (essentially files) are 2 ways 
for procedures in SAS to communicate with each other.

2. There is no limit on the maximum number of macro variables
that can be used in a SAS program besides memory limit.
However, the SAS symbol table exhibits a quadratic behavior,
which means that there is a performance issue 
when too many SAS macro variables are created.

3. SAS macro functions support 2 types of arguments,
positional arguments and keyword arguments.
A keyword argument has a default value,
which makes it similar to a default argument in other programming languages.
The difference is that a keyword argument in a SAS macro function 
can only be resolved relying on keyword not by its positions.
That is when you want to use a different value 
rather than the default value for a keyword argument, 
you must pass the keyword argument with the `keyword_argument = value` style.
When you define or call a macro function,
all positional arguments must preceede keyword arguments.

2. Pay attention to (implicitly created) macro variables.
Generally speaking,
you don't want to create global macro variables in your macro 
(especially, i, j, n, etc.).
And generally speaking, 
you don't want to use a use-defined macro function
which creates global macro variables.

3. The `%eval` function evaluates expressions using integer arithmetic 
while the `%sysevalf` function evaluates expressions using floating point arithmetic.

5. Whenever you use a non-macro function 
in an open macro statement 
(i.e., macro statement outside a data step or procedure),
you have to embed it in a `%sysfunc` call. 
For example, 
you cannot use

        %let run_date = intnx(month, &init_date., 0, M);

but instead you should use

    %let RUN_DATE = %sysfunc(intnx(month, &INITL_DATE., 0, M));

If there are multi-levels of nested non-macro functions in an open macro statement,
you have to embed each level of non-macro functions in a `%sysfun` call.
An illustrative example is given below.

    %let m2 = %sysfunc(putn(%sysfunc(intnx(month, &run_date., -1., E)), date9.));


1. Macro variables and data sets (essentially files) are 2 ways 
for procedures in SAS to communicate with each other.

12. `mlogic` specifies that the macro processor should traces its execution,
which is helpful for debugging.
`nomlogic` disables tracing of macro processor. 

1. Non-macro functions and call routines can only be used 
in a data step or procedure.
If you want to use it in a macro,
you have to embed it in the macro function `%sysfunc`.

4. When you develop a macro,
you should do a clean-up by default.
And give user the option to keep temporary files for debugging purposes.

5. Be a little bit flexible on these commonly used macro function argument values 
(e.g., Yes/No).
Generally speaking,
it is good to allow case-insensitive inputs. 
You should think about how to make your code more robust (tolerrent to user input).
And terminate program when user type in invalid argument values.

8. In my mind, 
macro variables (outside the definition of a macro) 
should be only for sharing and passing values among procedures.
We should do things as much as possible in a `_null_` data step 
and then expose necessary macro variables to other procedures.


1. it is suggested that you always end a macro variable with ".",
i.e., use `&x.` instead of `&x`

2. I think keyword arguments for macro functions are cleaer ...

