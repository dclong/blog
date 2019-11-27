Status: published
Date: 2019-11-27 00:55:37
Author: Ben Chuanlong Du
Slug: general-programming-tips
Title: General Tips on Programming
Category: Programming
Tags: programming, tips, semantic versioning

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


1. Do NOT chasing the latest versions of libraries/software/tools. 
  Wait for some time for them to be tested thoroughly before adopting them.

2. Follow a good [Semantic Versioning](https://semver.org/) 
  if you release your own library/software.

3. Keep a good habit to use parentheses 
    whenever the precedences of operators are not clear to you.
    For example, 
    bitwise operators and the ternary operator/expression have relative low priority 
    (lower precedence than arithmatical operators) in most programming languages.
    If you omit parentheses in the expression `(1L << 54) - 1` (where `<<` is the bitwise right shift operator),
    the expression is equivalent to `1L << 53` which might not be what you want.
    This kind of mistake is a common and tricky one.

4. Always remembe to check whether you have correct set/reset state of variables 
    when you use loops **especiall while loops**.
    Forgetting to set/reset state of varialbes/objects in while loops is a common mistake 
    and can be tricky to debug sometimes (e.g., if randomization is used in a loop).
