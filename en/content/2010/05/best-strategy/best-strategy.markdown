UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-02-20 10:54:32
Slug: best-strategy
Author: Ben Chuanlong Du
Title: Which One Is the Best Strategy?
Category: Fun Problems
Tags: pattern, Markov chain, statistics, sequence, coin, stochastic, martingale, fun problems, MATLAB, best strategy
Modified: 2015-02-20 10:54:32

<img src="http://dclong.github.io/media/pattern/coin.jpg" height="200" width="240" align="right"/>

Another interesting problem I met in statistic is: 
suppose we flip a coin which has probability 0.7 to be head again and again 
and two people choose two different sequences of length 3 (e.g. THH). 
The people whose sequence appears first wins. 
If you're allowed to choose first, which sequence will you choose?

I guess most people will choose sequence HHH. 
However, this sequence is beaten by THH. 
Suppose we first observe sequence HHH at step $n(>3)$, 
then the outcome must be T at step $n-3$, 
which means that we have observed THH at step $n-1$. 
So for HHH to win against THH, 
it must appear at step 3. 
So the probability for HHH to beat THH is 0.7^3=0.343<0.5, 
i.e., HHH is not as good as THH.

A nature question is that does there exist a best choice in this problem? 
The answer is no. 
I have done simulations in MATLAB to find the probability for a sequence to beat another. 
The simulation result shows that none of the 8 sequence can beat all other choices, 
which means that there is no benefit to choose a sequence first.

Talking about the probability for one sequence to come out first against another one, 
there is a much better solution rather than simulation. 
I will make post about this good solution later.

