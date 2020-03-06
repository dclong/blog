UUID: 6d9e6ebf-094b-4712-b283-c1b05466e543
Status: published
Date: 2015-05-10 21:12:54
Author: Ben Chuanlong Du
Slug: choose-a-procedure-for-modeling-in-sas
Title: Choose a Procedure for Modeling in SAS
Category: Computer Science
Tags: programming, SAS, procedure, proc

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. `proc glm` has many adavantages over `proc reg` and `proc anova`. 
For example, 
`proc glm` supports categorical variables while `proc reg` does not.
It is suggested that that you use `poc glm` in place of `proc reg` and `proc anova`.
The only disadvantage of `proc glm` is that it is computationally heavier
compared to `proc reg` and `proc anova`,
but this is usually not a concern at all. 
