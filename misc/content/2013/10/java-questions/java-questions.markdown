UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Questions About Java
Date: 2013-10-12 23:44:08
Slug: java-questions
Category: Computer Science
Tags: questions, Java, programming
Modified: 2021-04-12 23:44:08

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 

1. is possible to define abstract static method? i.e., 
the method doesn't depend on any instance variables but subclasses have different implementations

2. for a void method, we can also make it return values. 
Sometimes it can be more convenient to have it return value. 
Generally speaking what's the advantage of void methods? faster?

3. how can I make a copy of the subclass which implements an abstract class?

4. if a getter method doesn't return a deep copy of an object, 
then there's no advantage over making it protected, right?

5. if a class don't have any instant variables, 
what's the advantage of making it a static class？Create a new object is expensive? 
But how expensive it is for simple classes that only have static members? 
I guess for classes that have both static and non-static method, 
reference by class name is preferred. But ...

6. if a instance variable (need not to be initialized manually) is affected by multiple instance varibles, 
what the best way to update them? 
I currently use a single method to update them all to avoid possible issues, but it's less convenient, and confusing. 	

7. if you write a generic class, for example MyClass<T>, how do you make a defensive copy in the constructor?

8. java ArrayList<ArrayList<DataPoint>>, 
if i remove an elment of the list, but the element of the elment (also a list) is still in use, will there be memory leak?

## input and output 

1. good way for random access file?	


1. # concurrency

1. johnson told me that we have to protect shared data even if we sum a bunch of values together, because of thread local cache, 
if this is the case, how can we avoid using lock? there are some algorithms that are thread safe without lock ...

3. atomic seems to be more tight than volatie. I think atomic can replace volatile if you do not consider performace, while volatitle can not replace atomic. Atomic is for interaction between threads ...

4. about mutex, if an object has two fields that are shared, thought they are independent, 
still only once thread can access the object no matter which filed it access ...
This is not true, you can use multiple mutex, so that these two fields can be access by 
different threads if that's safe.

5. difference between lock and readwirtelock, 
the former allows only thread to access the shared resource while the latter allows multiple to read or exclusive to write.


## other

1. the working directory of java class seems to be the directory where you run the command. 

1. how to get the directory where the java application is? there seems to be some solution online

2. how to patch files into jars so that they can always be found and used in java program?


## exception

1. when to handle exception is a big problem ...

# lambda 

1. lambda function in java? 
currently we cannot pass method as argument to another method. 
Interface for comparing is OK but not flexible, 
if generics functions e.g., sort take lambda function, then it's more comveneint.

# exception

1. when to handle exception is a big problem ...

# class and object

1. is possible to define abstract static method? i.e., 
the method doesn't depend on any instance variables but subclasses have different implementations

2. for a void method, we can also make it return values. 
Sometimes it can be more convenient to have it return value. 
Generally speaking what's the advantage of void methods? faster?

3. how can I make a copy of the subclass which implements an abstract class?

4. if a getter method doesn't return a deep copy of an object, 
then there's no advantage over making it protected, right?

5. if a class don't have any instant variables, 
what's the advantage of making it a static class？Create a new object is expensive? 
But how expensive it is for simple classes that only have static members? 
I guess for classes that have both static and non-static method, 
reference by class name is preferred. But ...

6. if a instance variable (need not to be initialized manually) is affected by multiple instance varibles, 
what the best way to update them? 
I currently use a single method to update them all to avoid possible issues, but it's less convenient, and confusing.   

7. if you write a generic class, for example MyClass<T>, how do you make a defensive copy in the constructor?

8. java ArrayList<ArrayList<DataPoint>>, 
if i remove an elment of the list, but the element of the elment (also a list) is still in use, will there be memory leak?

1. Java container resize, how to make sure the length of array won't overflow?
