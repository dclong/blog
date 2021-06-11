UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2014-10-23 17:03:01
Author: Ben Chuanlong Du
Slug: expected time to hit zero
Title: Expected Time to Hit Zero
Category: Fun Problems
Tags: fun problems, expected time, hitting time, discrete uniform distribution
Modified: 2014-10-23 17:03:01

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Let DU(0, n) be the discrete uniform distribution on 0, 1, ..., n-1.
X_1 \sim DU(0, n)
X_2 \sim DU(0, X_2)
repeat this process until we get zero.
What is the expected time to hit zero? 

Let T_n be the time needed to hit zero.

t_n=E(T_n) = E\left(E(T_n|X_1)\right) 
= \sum_{i=0}^{n-1} \\frac{1}{n} E(T_n|X_1=i)  
= \sum_{i=0}^{n-1} \\frac{1}{n} (1 + E(T_i))  
= \sum_{i=0}^{n-1} \\frac{1}{n} (1 + t_i)  

nt_n = n + \sum_{i=0}^{n-1} t_i
(n-1)t_{n-1} = (n-1) + \sum_{i=0}^{n-2} t_i

nt_n = n + t_{n-1} + (n-1)t_{n-1} - (n-1)
= nt_{n-1} + 1

t_n - t_{n-1} = \\frac{1}{n}

\sum_{i=1}^n (t_i - t_{i-1}) = \sum_{i=1}^n \\frac{1}{i}

t_0 = 0

t_n = \sum_{i=1}^n \\frac{1}{i}



