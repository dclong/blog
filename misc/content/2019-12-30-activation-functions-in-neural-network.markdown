Status: published
Date: 2020-01-17 14:20:03
Author: Benjamin Du
Slug: activation-functions-in-neural-network
Title: Activation Functions in Neural Network
Category: AI
Tags: AI, data science, machine learning, activation function, ReLU, GELU, Switch, Sigmoid

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## GELU

GELU is the best activation function currently (at least in NLP).

$$ GELU(x) == x \Phi(x) $$,

where $\Phi(x)$ is the cumulative distribution function of the standard normal distribution.

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gWibcVsmTEMibWSmOvAkQYXV94vqFIJYiaHkZAQn6UFoChcUicVeZnhGeRsDIiacdQ8PLcxWqib74ibDVXDRw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



## ReLU

## ELU

## Swish

$$ f(x) = x \dot \sigma(x) $$,
where $\sigma(x)$ is the 
[sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function).

## Sigmoid

## References

https://mp.weixin.qq.com/s/LEPalstOc15CX6fuqMRJ8Q
