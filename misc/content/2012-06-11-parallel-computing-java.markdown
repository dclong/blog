Status: published
Title: Parallel Computing in Java
Date: 2020-03-25 18:35:06
Tags: lock, programming, thread, race condition, Java, HPC, parallel, concurrency, mutex
Category: Computer Science
Slug: parallel-computing-java
Author: Ben Chuanlong Du

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


<img src="http://dclong.github.io/media/java/multithreading.png" height="200" width="240" align="right"/>

The following are a few tips for multithreading parallel computing in Java.

1. Instance fields, 
    static fields and elements of arrays are stored in heap memory and thus can be shared between different threads. 
    Local variables and parameter variables are never shared between threads.

2. If race condition happens (read and write to the same shared variable by different threads), 
    you must protect the shared resource (object), which can be done through synchronized method, 
    locking/unlocking or atomic variables. 
    When a thread excecute a synchronized method or block, 
    it requires a mutex (mutual exclusion) of the object. 
    This does not prevent all other threads from accessing the object 
    but only these threads who also require mutex of the same object. 
    If the object has public fileds and other unsynchronized methos,
    other threads can still access these fileds or methods at the same time.
    This means that nothing is acutally locked when you use synchronized method or locking/unlocking.
    The locking/unlocking is a conceptual thing that happens via programmer discipline: 
    basically if you make a method synchronized to prevent a read/write conflict on a variable, 
    then you have to ensure that **every** access to that variable is throught a synchronized method/block of the same object. 
    That forces every threads to acquire mutex of the object and ensures mutual exclusion. 
    The misunderstanding about locking/unlocking leads to buggy code which try to protect shared
    object using synchronized method/block outside it. 
    If a synchronized method/block is used to protect shared object, 
    it must be inside the object.

3. Elements of arrays are independent variables and thus no synchronization 
    is needed if different threads access elements with different indices. 
    Similar rule applies to different instance variables of an object.
    However, false sharing can happen if two threads access variables that are 
    stored close in the memory (more accurate, in a same cache line). 
    Though false sharing does not make your parallel code invalid, 
    it downgrade the efficiency of the code. 
    The following are some strategies to allievate false sharing.
        - If you let different threads to access different elements of an array, 
        you can cut the array into non-interleaving parts 
        (e.g., `0-(k-1)` and `k-(n-1)`) and let different threads work on different pieces. 
        Or you can use thread-local copies of the array. 
        This does not kill falsing sharing. 
        The essential way to avoid falsing sharing is to avoid different threads accessing a same cache line. 
        To avoid false sharing completely, you can separate parts of the array (to be 
        accessed by diffrent threads) using dummy elements. 
        A general rule is to make the sepration segment twice the size of cache line 
        (which is usually 64 bytes).

        - You can use future object to return results from threads.

        - You can align varialbes at the beginning of cache lines.  
        While this is supported in C/C++, it is not well supported in Java.

4. The `join` method of threads and the `awaitTermination` method of thread pool (if return true)
    guarantees happen-before relationship between threads. 
    In other words, 
    if you call the join method of a thread, then the changed made by the threads 
    is seenable by the code after the `join` method. 
    This is also true for the method `awaitTermination` given that it returns `true`. 
    A thread pool cannot be reused after shutdown. 
    To reuse a thread pool, 
    you need to use ExectorCompletionService. 
    ExectorCompletionService handles synchronization for you automatically
    to place future objects on to a (synchronized) queue for access.

2. If no barrie (join of threads, termination of thread pool) is set, the order of execuation of thread is underterminant. 

4. You have to call the `signal` or the `signallAll` method in some thread if you every called
    the `await` method in another thread. There is no need to call these two notifying methods
    if you never called the `await` method in a thread. 

5. When doing multithreading parallel computing, there is no benefit to use
    more thread than the number of available cores on the computer on which the
    code is to be run. You can use the following code the get the number of available
    cores on a computer.  

        :::java
        int coresNumber = Runtime.getRuntime().availableProcessors();

6. Using the future class, you can return results from threads. 
    The advantage of using future class is that you do not have to
    destroy threads or thread pool to retrieve result. 
    The threads/thread pool created are/is resuable.  

7. When you create an object of Runnable or Callable and pass it to a thread or submit 
    it to a thread pool, it is better to make deep copies of arguments passed to the 
    constructor of the object. There are two reasons for this. First, shallow copy
    makes the object shared and might result in race condition. Second, the object
    might be destroied while the threads which require the object are still running. 

    The following is a Java method which create a thread pool of fixed number of threads, 
    add tasks into the pool, shutdown the pool and wait for all jobs to be finished.  

        :::java
        public void parSimulateIndependent(String outputFile,int maxNumberOfThreads) throws IOException{
            //initialize output, must do it here to avoid possible issues
            output = new SPTOutput[numberOfSimulations][];
            //thread pool
            ExecutorService pool = Executors.newFixedThreadPool(maxNumberOfThreads);
            for(int simulationIndex=0; simulationIndex<numberOfSimulations; ++simulationIndex){
                generateIndependentData();
                //writeData(simulationIndex);
                generateRandomIndexOfCombinations();
                pool.execute(new SPTsRunnable(combinations,data,randomIndexOfCombinations, sizeOfFirstGroup,sequentialTerminationCriteria,output,simulationIndex));
            }
            pool.shutdown();
            while(!pool.isTerminated()){
                try {
                    pool.awaitTermination(1000, TimeUnit.SECONDS);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                    System.out.println("Some thread in the pool was interrupted.");
                }
            }
        }

    Below is another example which distribute jobs to threads manually.

        :::java
        private static void runJobs(int threadsNumber) {
            Thread[] t = new Thread[threadsNumber];
            int each = array.length / threadsNumber;
            int eachPlusOne = each + 1;
            int extra = array.length - threadsNumber * each;
            int startIndex = 0;
            int endIndex;
            for (int i = 0; i < extra; ++i) {
                endIndex = startIndex + eachPlusOne;
                t[i] = new Thread(new SetElementRunnable(array, startIndex, endIndex));
                t[i].start();
                startIndex = endIndex;
            }
            for (int i = extra; i < threadsNumber; ++i) {
                endIndex = startIndex + each;
                t[i] = new Thread(new SetElementRunnable(array, startIndex, endIndex));
                t[i].start();
                startIndex = endIndex;
            }
            for (int i = threadsNumber - 1; i >= 0; --i) {
                try {
                    t[i].join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                    System.out.println("Thread " + i + " was interrupted.");
                }
            }
        }

    And the run method of the SetElementRunnable class is given below.

        :::java
        public void run(){
            for(int index=startIndex; index<endIndex; ++index){
                for(int i=0; i<1000000000; ++i){
                    for(int j=0; j<100000000; ++j){
                        Math.sqrt(i*j-0.5);
                    }
                }
                array[index] = 0;
            }
        }

    Notice that different threads acess different elements of a shared array, 
    so no synchronization is need. 
    Another lock-free approach is to use atomic variables (operations to the variable is atomic). 
    The following example sums integers in parallel using the AtomicInteger class.

        :::java
        public class TestSumRunnable {
            public static void main(String[] args) {
                for (int step = 0; step < 10000; ++step) {
                    AtomicInteger sum = new AtomicInteger(0);
                    int coresNumber = Runtime.getRuntime().availableProcessors();
                    ExecutorService pool = Executors.newFixedThreadPool(coresNumber);
                    for (int i = 0; i < 1000; ++i) {
                        pool.execute(new SumRunnable(sum, i));
                    }
                    pool.shutdown();
                    while (!pool.isTerminated()) {
                        try {
                        pool.awaitTermination(1000, TimeUnit.SECONDS);
                        } catch (InterruptedException e) {
                        e.printStackTrace();
                        }
                    }
                    if (sum.get() != 499500) {
                        System.err.println("Wrong!");
                    }
                    System.out.println("step " + step + " done.");
                }
            }
        }

    The run method of the SumRunnable class is as follows.

        :::java
        public void run(){
            sum.getAndAdd(addend);
        }

    In the above 3 examples, both thread pool and user-managed threads were used. 
    Using thread pool is more convenient and is scalable for general purpose jobs. 
    However, if you know that all jobs requires almost the same time to run, using
    user-managed threads is more efficient because it creates much fewer objects.
    This is often true in statistics simulations. 

1. After you open a pool, 
    the threads in the pool might still exist and run outside the scope (the method in which the pool is created). 
    To ensure that the pool is destroyed before the end of its scope
    (before the program leaves the method in which the pool is created),
    you must wait for termination of pool manually. 
    Notice that some other packages in java or some other languages might have implemented thread pool differently, 
    but generaly speaking, 
    what java does is the nature way. 
    Depends on what you want to do, 
    you must decide whether to manually wait for termination of the pool carefully.

2. Not all parallel code runs faster than serial code 
    while parallel code is almost surely much hard to develop, 
    so you have to think about your problem and decide whether it is worth writing parallel code to solve your problem. 
    Usually the process of generating random numbers cannot be parallelized, 
    so if the process of generating random numbers is the bottleneck, 
    it is no use to do parallel computing.

3. Remember to use defensive copy for constructors and methods of classes that implement `Runnable`, 
    except for these variables through which threads communicate.

4. `Runtime` in Java can help to find the number of processors that a computer have. 
    Notice that every Java application has a single instance of class Runtime 
    that allows the application to interface with the environment in which the application is running. 
    The current runtime can be obtained from the `getRuntime` method.

5. Never use more threads than the number of processor of the machine on which the Java application will be run on. 
    With the help of `Runtime` we can write universal code for parallel computing.

6. You should always synchronize shared objects among different threads
    because of delay effect in parallel computing. 
    If we can make different threads independent, 
    we'd do it because this not only make the code easy and run faster.

7. You should use thread pool to avoid the cost of creating new thread
    if there are many different parts in parallel computing.

## ThreadLocal 

https://www.youtube.com/watch?v=sjMe9aecW_A

https://stackoverflow.com/questions/7722546/how-can-a-threadpool-be-reused-after-shutdown

https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executors.html