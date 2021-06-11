UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: How Many People Stay in the Same Position?
Date: 2013-11-17 15:16:03
Tags: same position, statistics, probability, linear recursion, fun problems, conditional expectation, permutation
Category: Fun Problems
Slug: same-position-permutation
Author: Ben Chuanlong Du
Modified: 2013-11-17 15:16:03


<img src="http://www.legendu.net/media/people/same.jpg" width="240" height="200" align="right">

There are 100 seats on a plane.
If each of the 100 passengers randomly take a seat,
how many people will have his/her own seat on average?

There is a classic way to solve this problem, 
which is to decompose a (complicated) random variable into a sum of simple random variables.
This is an important trick. 
See [this post](http://www.legendu.net/en/blog/calculate-covariance-between-multinomial-categories-by-hand/) 
for the use of this trick to calculate the covariance 
of observastions in two categories in a multinomial distribution.

Let's generalize this problem to assume that 
there are $n$ seats and $n$ passengers. 
Let $Y_i=I(\text{passenger } i \text{ takes its seat})$, $1\le i \le n$,
where $I$ is an indicator function. 
$Y_i$'s are exchangeable, 
which means that for a fixed $k$ ($1\le k\le n$), 
any subset of $\\{Y_i: 1\le i \le n\\}$ with $k$ elements has the same distribution.
Specially,
it's easy to see that 

$$
Y_i\overset{iid}{\sim}\text{Bernoulli}(\frac{1}{n}),
$$

$$
Y_iY_j\overset{iid}{\sim}Bernoulli(\frac{1}{n(n-1)}), i\ne j.
$$

So we have 

$$
EY_i=\frac{1}{n},
$$

$$
EY_iY_j=\frac{1}{n(n-1)}, i\ne j, 
$$

$$
Var(Y_i)=\frac{n-1}{n^2},
$$

$$
Cov(Y_1,Y_2)=EY_1Y_2-EY_1EY_2=\frac{1}{n^2(n-1)}.
$$

Let $X_n\equiv\sum_{i=1}^nY_i$, 
which is the number of passengers taking their own seats.
From above results we know that

$$
E(X_n)=E\left( \sum_{i=1}^nY_i\right)=\sum_{i=1}^n E Y_i=n E Y_1=n\frac{1}{n}=1,
$$

\begin{align}
Var\left( X_n\right) &= Var\left( \sum_{i=1}^nY_i\right)
                =\sum_{i=1}^n Var(Y_i)+\sum_{i\ne j}Cov(Y_i,Y_j) \nonumber \newline
                     &=  nVar(Y_1)+n(n-1)Cov(Y_1,Y_2) \nonumber \newline
                     &=  n\frac{n-1}{n^2}+n(n-1)\frac{1}{n^2(n-1)}=1. \nonumber
\end{align}

Surprisingly, both the mean and the variance of $X_n$ is 1,
which suggests that we can predict $X_n$,
i.e. the number of integers that have the same position as their
original position very well.

The above solution is elegant. 
However, 
I'd like to try to solve this problem using my preferred universal procedure.
Let $Y_i$ and $X_i$, $1\le i \le n$, be as defined above. 
Conditioning $X_n$ on $Y_1$ gives us a recursive/differtial equation.
If $Y_1=1$ (with probability $\frac{1}{n}$), 
i.e., the first passenger sits on its seat,
then $X_n = 1 + X_{n-1}$;
It's a little tricky when $Y_1=0$ (with probability $1-\frac{1}{n}$),
i.e., the first passenger sits on other people's seat. 
Assume the first passenger takes $k^{th}$ ($2\le k\le n$) passenger's seat.
If we pretend that seat 1 is the $k^{th}$ passenger's seat,
then we have $X_n = X_{n-1}$. 
However, seat 1 is not $k^{th}$ passenger's seat,
and we cannot count it into $X_{n-1}$. 
Let $E_k\equiv I(\text{passenger } k \text{ sits on seat 1})$. 
We only miss count $X_{n-1}$ by extra 1 when $E_k=1$, 
so when $Y_1=0$ we have 
$$
X_n = X_{n-1} - E_k.
$$
It's easy to see that $E_k\sim\text{Bernoulli}(\frac{1}{n-1})$. 
So using the conditional expectation formula, we have
\begin{align}
EX_n &= E(E(X_n|Y_1))\nonumber\newline 
     &= E\left(\frac{1}{n}(1 + X_{n-1}) + (1-\frac{1}{n}) (X_{n-1} - E_k)\right)\nonumber\newline
     &=EX_{n-1},
\end{align}
where $EX_1=1$.
This is the simplest recursive/differential equation. 
Anyone can immediately see that $EX_n=1, \forall n\ge1$ is the solution to this recursive/differential equation.

