Status: published
Date: 2020-01-02 12:01:27
Author: Benjamin Du
Slug: memory-in-jvm
Title: Memory in JVM
Category: Computer Science
Tags: programming, JVM, memory, stack, heap, off-heap

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Stack, heap and off-heap are all memory that stored in a computer's RAM.

## Stack

Stack is used for static memory allocation.
Variables allocated on the stack are stored directly to the memory 
and access to this memory is very fast, 
and it's allocation is dealt with when the program is compiled. 
When a function or a method calls another function which in turns calls another function etc., 
the execution of all those functions remains suspended 
until the very last function returns its value. The stack is always reserved in a LIFO order, 
the most recently reserved block is always the next block to be freed. 
This makes it really simple to keep track of the stack, 
freeing a block from the stack is nothing more than adjusting one pointer.



## Heap

Heap is used for dynamic memory allocation.
Variables allocated on the heap have their memory allocated at run time and accessing this memory is a bit slower, 
but the heap size is only limited by the size of virtual memory. 
Element of the heap have no dependencies with each other and can always be accessed randomly at any time. 
You can allocate a block at any time and free it at any time. 
This makes it much more complex to keep track of which parts of the heap are allocated or free at any given time.



You can use the stack if you know exactly how much data you need to allocate before compile time and it is not too big. You can use heap if you don't know exactly how much data you will need at runtime or if you need to allocate a lot of data.

In a multi-threaded situation each thread will have its own completely independent stack but they will share the heap. Stack is thread specific and Heap is application specific. The stack is important to consider in exception handling and thread executions.


## Off-heap

EHCache's off-heap storage takes your regular object off the heap, serializes it, and stores it as bytes in a chunk of memory that EHCache manages. It's like storing it to disk but it's still in RAM. The objects are not directly usable in this state, they have to be deserialized first. Also not subject to garbage collection.


## References

https://stackoverflow.com/questions/6091615/difference-between-on-heap-and-off-heap
