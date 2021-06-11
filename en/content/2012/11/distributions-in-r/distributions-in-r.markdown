UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Distributions in R
Date: 2012-11-05 00:22:23
Tags: distribution, R, programming, statistics
Category: Computer Science
Slug: distributions-in-r
Author: Ben Chuanlong Du
Modified: 2013-12-05 00:22:23


4. The definition of geometric distribution in R is not the same as the common definition. 
A random variable of geometric distribution in R starts from zero, 
i.e. geometric distribution in R is defined as the number of failures before we succeed.

5. A random variable of negative binomial distribution $NB(r,p)$ in R 
is defined as the number of failures before we succeed for `r` times,
where `p` is the success probability in each trial.

6. The definition of hyper-geometric is the same as common but be careful with the parameters!
