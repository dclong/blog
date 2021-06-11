Status: published
Title: Loops in Java
Date: 2019-11-06 21:46:23
Slug: loops-in-java
Author: Ben Chuanlong Du
Category: Computer Science
Tags: programming, loop, Java
Modified: 2019-11-06 21:46:23

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. The condition(s) in a regular `for` or `while` loop is recomputed before each iteration.
    Not only the change of loop variables but also other variables involved in the loop condition(s) affect the loop. 
    The `break` statement is often used to jump out of a loop. 
    Sometimes, 
    we want to jump out of nested loops. 
    It is hard to use `break` to achieve this.
    One simple way is just change varibles involved in the loop condition(s)
    to make the nest loops terminate completely.

2. The foreach loop makes things makes things convenient but it has limitations.
    You cannot (should not) use a foreach loop to change the structure of the container 
    (even though you can still use a foreach loop to update elements in th container).
    Consider, for example, the expurgate method. 
    The program needs access to the iterator in order to remove the current element.
    The for-each loop hides the iterator, so you cannot call remove.
    Therefore, the for-each loop is not usable for filtering. 
    Similarly it is not usable for loops where you need to replace elements in a list or array as you traverse it.

        :::java
        for(Type elem : someList){
            /* operations */
        }

3. On a computer support multithreading, 
    multiple small loops runs a little (not significant at all) faster than a big loop 
    with the same number of iterations.

4. The foreach loop in Java perserves the original order to containers.

## References

https://stackoverflow.com/questions/35010846/does-javas-foreach-loop-preserve-order

