Status: published
Title: Calculate Covariance Between Multinomial Categories by Hand
Author: Ben Chuanlong Du
Date: 2013-11-17 15:14:27
Slug: calculate-covariance-between-multinomial-categories-by-hand
Category: Fun Problems
Tags: fun problem, statistics, probability, multinomial, covariance

Let $(X_1, \ldots, X_k)\sim\text{Multinomial}(n, p_1, \ldots, p_k)$. 
I'll show how to calculate $Cov(X_i, X_j), i\ne j$. 
The main purpose of doing this is to illustrate the little trick 
of reducing complexity of problems by decomposing a complicated random variable 
into simple ones. 

Let $(Y_{i1}, \ldots, Y_{ik})\overset{iid}{\sim}\text{Multinomial}(1, p_1, \ldots, p_k), i\ge1$,
then 
$$
X_j = \sum_{i=1}^n Y_{ij}, 1\le j \le k.
$$
So,
\begin{align}
Cov(X_i,X_j) &= Cov(\sum_{l=1}^n Y_{li}, \sum_{m=1}^n Y_{mj})\nonumber\newline
             &= \sum_{l=1}^n\sum_{m=1}^n Cov(Y_{li}, Y_{mj})\nonumber\newline
             &= \sum_{m=1}^n Cov(Y_{mi}, Y_{mj})\nonumber\newline
             &= nCov(Y_{1i}, Y_{1j}) = n(EY_{1i}Y_{1j} - EY_{1i}EY_{1j})\nonumber\newline
             &= -np_ip_j\nonumber\newline
\end{align}
