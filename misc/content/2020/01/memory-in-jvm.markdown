Status: published
Date: 2021-03-23 17:25:59
Author: Benjamin Du
Slug: memory-in-jvm
Title: Memory in JVM
Category: Computer Science
Tags: programming, JVM, memory, stack, heap, off-heap

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Stack, heap and off-heap are all memory that stored in a computer's RAM.

## Stack

Stack is used for static memory allocation.
Variables allocated on the stack are stored directly to the memory 
and access to this memory is very fast.
When a function or a method calls another function which in turns calls another function etc., 
the execution of all those functions remains suspended 
until the very last function returns its value. 
The stack is always reserved in a LIFO order, 
the most recently reserved block is always the next block to be freed. 
Stack memory is collected automatically when the execution path reaches the end of the scope.


## Heap

Heap is used for dynamic memory allocation.
It is another named for "managed memory" and is subject to garbage collection.
Variables allocated on the heap have their memory allocated at run time and accessing this memory is a bit slower, 
but the heap size is only limited by the size of virtual memory. 
Element of the heap have no dependencies with each other and can always be accessed randomly at any time. 
You can allocate a block at any time and free it at any time. 
This makes it much more complex to keep track of which parts of the heap are allocated or free at any given time.


You can use the stack if you know exactly how much data you need to allocate 
before compile time and it is not too big. 
You can use heap if you don't know exactly how much data you will need at runtime or if you need to allocate a lot of data.


In a multi-threaded situation each thread will have its own completely independent stack 
but they will share the heap. 
Stack is thread specific and Heap is application specific. 
The stack is important to consider in exception handling and thread executions.

## Off-heap

EHCache's off-heap storage takes your regular object off the heap, serializes it, and stores it as bytes in a chunk of memory that EHCache manages. 
It's like storing it to disk but it's still in RAM. 
The objects are not directly usable in this state, they have to be deserialized first. Also not subject to garbage collection.

Off-heap memory is leveraged in JVM to avoid GC.
For example,
Off-heap memory is leveraged by Spark Tungsten to boost efficiency.
However, 
off-heap is tricky.
First,
use of off-heap memory increases CPU usage because of the extra translation from bytes of arrays into expected JVM object. 
Second, 
even though we manage to store JVM objects off-heap, 
when they're read back to be used in the program, 
they can be allocated on-heap. 
Thus, there will be the need to garbage collect them. 
Therefore, 
it makes sense to use off-heap for things that do not need to serialize back the data from the bytes array.

## Tune JVM 

java -XX:+PrintFlagsFinal -version

java -XX:MaxDirectMemorySize=8g (an example of off-heap memory)

[JVM Tuning](https://docs.gigaspaces.com/latest/production/production-jvm-tuning.html)
has a very explanation on the use of memory in JVM.


## References

[Decoding Memory in Spark — Parameters that are often confused](https://medium.com/walmartglobaltech/decoding-memory-in-spark-parameters-that-are-often-confused-c11be7488a24)

[Apache Spark and off-heap memory](https://www.waitingforcode.com/apache-spark/apache-spark-off-heap-memory/read#off-heap_memory_and_Project_Tungsten)

https://stackoverflow.com/questions/6091615/difference-between-on-heap-and-off-heap

https://stackoverflow.com/questions/3773775/default-for-xxmaxdirectmemorysize

[-XX:MaxDirectMemorySize](https://www.eclipse.org/openj9/docs/xxmaxdirectmemorysize/)

[JVM Tuning](https://docs.gigaspaces.com/latest/production/production-jvm-tuning.html)