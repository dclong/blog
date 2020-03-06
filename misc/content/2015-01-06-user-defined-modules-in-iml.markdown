UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-03-13 14:49:32
Author: Ben Chuanlong Du
Slug: user-defined-modules-in-iml
Title: User-defined Modules in IML
Category: Computer Science
Tags: programming, SAS, IML, function, module, user-defined

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. There are in general 2 types of modules. 
Modules with or without arguments.
A module without arguments CANNOT return values.
A module with arguments can return values,
and it is called a function module if it returns values.
<@TODO: use a picture or a math formula to illustrate this, and also search path ...>
Variables defined in a module without arguments are GLOBAL
while variables defined in a module with arguments are local to the module.
It is recommended that you avoid using modules without arguments.
If your module does not need any argument,
you can add a fake argument (never use by the module) just to make your code more modulized.
Notice that you cannot define a function module with the same name as a built-in module 
as it will be hidden by the built-in module.
For a module that does not return values,
you can invoke it with either `run` or `call`.
The following is an illustration.
```SAS
	proc iml;
	start f(x);
		x = 1
	finish f;
	start g;
	finish;
	run f;
	call g;
	quit;
```
When `run` is used use-defined functions are searched before built-in modules
while `call` is used built-in functions are searched before user-defined modules.
It is suggested that you always use `run` to invoke a module that does not return values.


3. If a module has a dependency (user-defined module) that is not intend for users (but rather pure helper modules), 
put into an IML procedure and store it using `store module_name;`.
Otherwise, put the definition of the module into a plain text file (you can use .sas as the file extension). 
This way keeps good balance between easy access and code encapsulation.


4. In SAS 9.3, 
you cannot define function modules with default or optional arguments in the IML procedure.
However, 
this is supported starting from SAS IML 12.1 (IML has an independent version number).

