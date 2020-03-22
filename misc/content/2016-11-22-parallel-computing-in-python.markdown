Status: published
Date: 2020-03-21 13:13:26
Author: Ben Chuanlong Du
Slug: python-concurrency-parallel-computing
Title: Concurrency and Parallel Computing in Python
Category: Computer Science
Tags: programming, Python, parallel computing, multithreading, multiprocess, HPC, high performance computing

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


The GIL is controversial because it prevents multithreaded CPython programs from taking full advantage of multiprocessor systems in certain situations. Note that potentially blocking or long-running operations, such as I/O, image processing, and NumPy number crunching, happen outside the GIL. Therefore it is only in multithreaded programs that spend a lot of time inside the GIL, interpreting CPython bytecode, that the GIL becomes a bottleneck.


1. Due to the GIL, 
    multithreaded CPython (which is the Python distribution that most people use) programs 
    cannot take full advantage of multiprocessor systems in some situations.
    Keep a few things in mind when you write multithreaded code in CPython.

    - In the same Python interpreter process, 
        **only 1 Python thread runs at a time** while others sleep or await (I/O, networking, etc.).
    - Things happening outside the GIL (I/O, network, properly handled 3rd-party code such as C, Fotran, C++, Java, Rust, etc.),
        do not suffer performance downgrade from the GIL.
    - Combining the above 2 facts, 
        multithreading in Python might or might not increase the speed of your program.
        If all your code runs in the CPython interpreter 
        (e.g., your code is pure Python and doesn't call 3rd-party code), 
        having multithreading only slows download your program.
        Multithreading helps if some long-running tasks (I/O, networking, 3rd-party code) happen outside the GIL.
    - A GUI application needs multithreading to be more responsive.
        If you develop a GUI application in Python,
        it is best to move long-runing tasks to 3rd party code
        and calling it from a separate Python thread (rather than the GUI thread)
        so that it won't freeze your GUI.
        (As a matter of fact, 
        the strength of Python is to act a s glue-language 
        which binds native code and provide easy to use APIs.)
    - If multiple CPython threads share data and at least one of them write the data,
        **you still need to lock the data before writing** (no need to lock if the thread read data only)
        even if CPython has GIL.
        To avoid slowing down your program,
        **limit locking to the minimum scope**.

2. Multiprocessing has much higher overhead than multithreading.
    It is rather inconvenient to share data among different processes.
    It is suggested that you only use multiprocessing for CPU intensive tasks 
    where communication among tasks is minimum.

## References

[Python Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock)

[python 线程，GIL 和 ctypes](http://zhuoqiang.me/python-thread-gil-and-ctypes.html)

https://docs.python.org/3/library/multiprocessing.html?highlight=process

[A Jesse Jiryu Davis Grok the GIL Write Fast And Thread Safe Python PyCon 2017](https://www.youtube.com/watch?v=7SSYhuk5hmc)

[Grok the GIL: How to write fast and thread-safe Python](https://opensource.com/article/17/4/grok-gil)

https://xph.us/2009/12/10/asynchronous-programming-in-python.html

