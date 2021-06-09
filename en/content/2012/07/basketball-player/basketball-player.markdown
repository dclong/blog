UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2014-07-28 21:56:16
Slug: basketball-player
Author: Ben Chuanlong Du
Title: Basketball Player
Category: Fun Problems
Tags: statistics, condition, probability, fun problems, basket ball player

[Table 1]: http://dclong.github.io/media/basketball-player/table.pdf

<img src="http://dclong.github.io/media/basketball-player/basketball.jpg" 
height="200" width="240" align="right"/>

Suppose a basketball player make $N$ shots,
and we know that in the first $n(\le N)$ shots he sinked $m(\le n)$ shots.
If from the $(n+1)^{th}$ shot, 
his ratio of sink a shot is his accumulative ratio before the shot,
e.g., suppose he sinked 40 shots in the first 50 shots,
then his ratio of sink the next shot is 80%.
What's the probability that he will make $M$ shots finally?

Using the knowledge of permutation and combination, we can solve this problem directly.
Let $E_{m,n}$ be the event that $m$ success in the first $n$ shots.
It turns out to be that

$$
P\left( E_{M,N}\mid E_{m,n}\right)
=\frac{ {N-M-1 \choose n-m-1} }{ {N-1 \choose n-1} } ,\ m\le M\le N-(n-m).
$$

Notice that

$$
P\left( E_{M,N}\mid E_{1,2}\right)=\frac{1}{N-1},\ 1\le M\le N-1.
$$

i.e., the number of sinked shots $M$ is uniformly distributed on its support
given that the player only sinked 1 shot in the first 2 shots.

Let $X_k, n\le k\le N$ be the number of shots the player sinks in the first $k$ shots,
then the distribution of $X_{k+1}$ conditioning on $X_{k}$ is given in [Table 1][].
Using the similar method as we've done in the first 3 problems,
we can easily find the first and second moment of $X_k$ which are given below:

$$
E(X_k\mid E_{m,n})=k\frac{m}{n},\ n\le k\le N;
$$

$$
E(X_k^2)=(k+1)k\frac{(m+1)m}{(n+1)n}-k\frac{m}{n},\ n\le k\le N.
$$

So the variance of $X_k$ is

$$
Var(X_k)=EX_k^2-\left( E X_k\right)^2=k(k-n)\frac{m(n-m)}{n^2(n+1)},\ n\le k\le N.
$$

From the above formulas, we can know that the expectation and variance
of the number of sinked shots are linear quadratic functions of $k$ respectively,
and both of them increase as $k$ increases.
This makes it hard for us to predict $X_k$ when $k$ is big.
The 2-$\sigma$ intervals for $X_k$ is shown in the follow figure. 

<img src="http://www.legendu.net/media/basketball-player/interval.png" 
height="200" width="240" align="middle"/>
<!---
![a picture](http://www.legendu.net/media/basketball-player/interval.png) 
-->

Since we know the distribution of the number of sinked shots 
given that the player sinked $m$ shots in the first $n$ shots,
we can calculate the first and second moments directly, 
which yields the following equations:

$$
\sum_M \frac{ {N-M-1 \choose n-m-1} }{ {N-1 \choose n-1} }=1;
$$

$$
\sum_M M\frac{ {N-M-1 \choose n-m-1} }{ {N-1 \choose n-1} }=N\frac{m}{n};
$$

$$
\sum_M M^2\frac{ {N-M-1 \choose n-m-1} }{ {N-1 \choose n-1} }=(k+1)k\frac{(m+1)m}{(n+1)n}-k\frac{m}{n}.
$$
