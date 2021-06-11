UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2012-10-20 10:36:42
Slug: performance-tips-for-cpp
Author: Ben Chuanlong Du
Title: Performance Tips for C++
Category: Computer Science
Tags: tips, performance, C++, programming
Modified: 2015-02-20 10:36:42


## Performance
1. If there is some block of useless code, 
the compile is smart enough to ignore it and thus speed up the program.

2. Use the option `-O2` to generate optimized code when you are ready to publish your code.

3. Define variables only when needed to avoid the overhead of creating and deleting temporary variables.
It is suggested that you put variables into the smallest possible enclosing brace. 

4. When shuffling data, it is better to shuffle in place 
if objects/data to be shuffled are not expensive to copy 
(e.g., when data are double or integers).
Otherwise, it is better to shuffle indexes/iterators of the container.

5. It is STRONGLY suggested that you specify the size/capacity of a vector 
if you know it. 
Even if you do not know the exactly size of a vector, 
it is often a good idea to initialize the vector with an rough estimate of its final size. 
