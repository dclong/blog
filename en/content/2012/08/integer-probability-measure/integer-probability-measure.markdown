UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Randomly Select an Integer?!
Date: 2013-10-29 17:23:24
Tags: random, statistics, nature number, probability, relatively prime, fun problems
Category: Fun Problems
Slug: integer-probability-measure
Author: Ben Chuanlong Du
Modified: 2013-10-29 17:23:24


[COS]: http://www.legendu.net/en/tag/fun-problems.html

<img src="http://dclong.github.io/media/number/numbers.jpg" height="200" width="240" align="right"/>

I found this "probability" problem when I read a person's blog. 


What's probability that two randomly chosen nature numbers are relatively prime?


It is claimed that there is a very elegant solution for this problem. 
This problem reminds me another one. 
Some people asked for an example of a 0-probability event 
that is not impossible on [COS][]. 
And a person said "randomly pick an integer from all integers".
While this example sounds like a neat one, 
it is invalid actually. 
The example assumes that there exists a probablity measure on all integers
such that the measure for each integer is that same. 
However, such a probabiliy measure does not exists. 
This is easy to see. 
Suppose the probability measure for each integer is 0, 
then from countable additivity the probability measure for all integers is 0, 
which is contrary to the fact that the probability measure for the whole set is 1. 
Suppose the probability measure for each integer is $\delta>0$, 
then from countable additivity the probability measure for all integers is $\infty$,
which is also contrary to the fact that the probability measure for the whole set is 1.
Coming back to the problem mentioned in the title, 
it essentially makes the assumption there there exists a probability measure on
nature numbers such that each the measure on each number is the same. 
From my previous argument we know such a probability measure does not exist, 
thus this problem is nonsense. 
Bummer! What is the ELEGANT solution? 

A reframed (valid) question is as follows.

Let $n$ be a (large) positive integer. 
What's the probability that 2 randomly chosen integers 
between (inclusive) 1 and $n$ are relatively prime? 
And does the probability has a limit as $n$ goes to infinity?
If so, what's the limiting probability?

I will think about how to solve this reframed (valid) question when I have time. 
Possibly the ELEGANT solution mentioned before is a solution to this problem.

PS: Ask the question that randomly pick an number from all integers, what is the probability
that the number is even. 
I bet most people will answer 0.5.
