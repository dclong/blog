UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-07-13 22:10:28
Slug: some-tricky-problems-in-java
Author: Ben Chuanlong Du
Category: Computer Science
Title: Some Tricky Problems in Java
Tags: tricky, Java, programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Confusion Clarification

1. You cannot define an abstract static method. 
This is because "abstract" means that no functionality is implemented 
while "static" means that functionality exists even there is no object. 
The two conflict in concept.

2. Currently there is no way to make subclass level access 
but no package level access in Java.

## Tricky Problems

1. If there is broken references (e.g. a imported jar file has been
deleted or moved to another place), eclipse cannot build proejects.
When you run code, you will probably get error message that some class
does not exist.

2. The `hasNextInt()` method of `Scanner` class test whether the next
parsed word is integer or not. Even if there is integer in the string
the method returns `false` if it is not the first parsed word.

3. When a `double` number is casted to an `integer`, only the integer
part is kept, i.e. the number will be rounded towards 0. When we use
method `Math.round()`, we get the same result. However, the first
method is preferred, though it uses cast. Usually this kind of type
cast is very fast.

4. There is no power operator in Java, instead, method `Math.power`
should be used. If you want the square or cubic of a number [] `x`,
you can use `x * x` or `x * x * x`, 
which is faster than invoking the `Math.power`.

5. In Java (and also C++), you can access the instance variables of
objects with the same class in the definition of a class.

6. When a return a result in method using key word `return`, the
parentheses are not required.

7. Unlike C/C++, we can only give `if` statement a boolean expression
in Java, which means that `if(x=2)` (which works in C/C++) will not
work in Java.

8. In C/C++, we can convert integer values to boolean values, vice
versa. While in Java, we cannot do this.

9. To quit a program when error occurs in Java, we can use
`System.err.println()`. This will print out the error message and
then quit the running program. !!!!!!!!!!!It will not stop running,
just print error message.

10. We can not call a non-static method inside a static method. So all
methods in the class which contains function `main` (the start place
of all code) should be static. Similarly all instance variable in
this kind of classes must be static and (usually final).

11. Be careful when you use `switch` in Java. Do not forget to add code
`break;` at the end of each branch.

12. Do not use `==` to check whether two objects are equal or not,
instead, use method `equals`.

13. By default, the elements of an array of objects in Java have value
null. So we must either instantiate the elements or point them to
objects with the same type.

14. The index of `arrays` in Java must start from 0, however, it does not
have to be a regular array, i.e. the elements of the array do not
have to have the same length.

15. We know that many programming languages use lazy evaluation to
evaluate boolean expressions. However, sometimes we might want to
evaluate all conditions of an expression, which is mainly for side
effect and parallelism maintain concern.

16. In java, `"\r"` stands for return (i.e. put the cursor to the first
column) and `"\n"` stand for new line, which is different from some
programming languages. For example, some programming language use
`"\n"` to stand for return and new line.

17. When overriding an existing method in a class, you must provide
different arguments for the overriding method. This is because the
name of a method and the number and type of arguments is how Java
can distinguish different methods. Notice that before executing a
method, Java does not know the type of return result, which means
that the return type of methods is not used to distinguish different
methods. For this reason, we cannot define two methods with the same
name and the same number and type of arguments with different return
types. And when we overwrite a method in a super class, we must keep
the same return type or a return type that is compatible with the
return type of the corresponding method in the super class.

18. There can be both public and static method in a class in Java. To
call a public class, you must invoke a public method through an
object of the class; to call a static method, you can either invoke
it through an object of the class or we can invoke it using the name
of the class, however, the latter way is prefer for invoking a
static method, because it does not have to create a new object.

19. When you invoke the constructor of a super class in a sub class, it
must be the first line in the constructor of the sub class.

20. You can only extend a subclass from only one super class in Java
while you can implement class from more than one interface in Java.

21. `Cast` has lower priority than `.` in Java, which means that you
have to use two pairs[^2] of parentheses when you want to first cast
an object and then invoke some method of the casted object.

22. After reading or writing a file in Java, you have to close it in
order for Java to release the resource. If you use `Scanner` to read
a file, you should also close it after reading. But if you use
`Scanner` to read data from other place, e.g. a string or
`System.in`, then you do not have to close it.

23. If a sub class extends from a super class which implements an
interface, then the sub class implements the interface
automatically.

24. For parameter (some type) of generic types, we cannot use primitive
types.

25. For a state that is unique to an object of a class, you want to use
key word new to create an object for the state (if the state is a
not a primitive type). For a state that is shared among all objects
of a class (e.g. random number generators in a class usually should
be shared among all its object), never use key word new to create an
object for the state. Just point it to an object passed as argument
of the constructor of the class.

26. For statistical simulations involving generating random numbers,
you'd better use a single base random number generator (RNG) for
generating random numbers. To do this in Java, you just need to
create a single random number generator and pass it by reference
(which is the default way) to objects that require a RNG. Also to
make your work repeatable, you'd better set seed(s) for your
simulations.

27. String and Enum are immutable classes in Java ....

28. Be careful if an object is initialized based on another object of
the type, i.e. when some object is passed to the constructor for
initializing an object of the class. Be aware about whether you want
the state object to be shared or not.

29. For an object whose states might be changed by itself (i.e. states
can be changed by some other methods (either public or private)
rather than its setters), you'd better make it immutable. Generally
speaking, you do not have track of the inner states of this object,
and thus you might mis-predict its inner states. If you allow setter
methods to mutate the object, it can happen that you think you have
changed the states of the object to these you expect, but rather
they are not.

