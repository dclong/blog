UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Parallel Computing in MATLAB
Date: 2014-06-19 19:45:42
Tags: HPC, parallel, concurrency, programming, MATLAB
Category: Computer Science
Slug: parallel-computing-in-MATLAB
Author: Ben Chuanlong Du
Modified: 2014-06-19 19:45:42


1. It is very easy to do parallel computing in MATLAB. 
Usually what you have to do is to change `for` to `parfor` 
for the loop that you want to run in parallel. 
The parallel code can also be run on a single thread and you will not lose much efficiency, 
so you are always encouraged to write parallel code in MATLAB. 
However, to benefit from parallel computing, 
you must open pool of MATLAB sessions first either manually or automatically in your code. 
To open a pool of 4 MATLAB sessions manually, 
you can use the following code

        % before R2013b
        matlabpool open 'local' 4; 
        % from R2013b
        parpool('local', 4)

To close a pool of MATLAB sessions manually, 
you can use

        matlabpool close

If you want to make your MATLAB parallel code portable, 
you'd better open the pool of MATLAB sessions manually 
instead of open it automatically in your code, 
because different computers have different number of cores.

2. Though parallel computing in MATLAB is easy, 
it is hard to fix problems if there is any. 
Here is some strategies that you can use 
to avoid problems in parallel computing in MATLAB. 
If a reduced variable does not work well, 
you can use a sliced variable instead, 
and it is more efficient, generally speaking.

3. MATLAB complains if your code is not written appropriately. 
To avoid variable problems in parallel computing in MATLAB, 
you can use the following strategies.

    - Make a full copy of the array you want to use into each thread.

    - Use a sliced array instead of sum variables.

