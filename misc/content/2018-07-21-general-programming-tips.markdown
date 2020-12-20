Status: published
Date: 2020-12-20 00:25:59
Author: Ben Chuanlong Du
Slug: general-programming-tips
Title: General Tips on Programming
Category: Computer Science
Tags: programming, tips, semantic versioning

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. Do NOT chase the latest versions of libraries/software/tools. 
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
    If you use the Kotlin programming language, 
    it is suggested that you use the bitwise methods instead of the bitwise operators.

4. Always remembe to check whether you have correct set/reset state of variables 
    when you use loops **especiall while loops**.
    Forgetting to set/reset state of varialbes/objects in while loops is a common mistake 
    and can be tricky to debug sometimes (e.g., if randomization is used in a loop).
    It is suggested that you avoid using plain for/while loops if possible
    and use high-level alternatives such as `forEach`, `map`, `filter`, etc.

5. Any initialization that might involve network, etc. 
    which might either fail or take a long time
    should be delayed as much as possible.
    For example,
    if you define command-line options using the library `argparse`
    and a default value might take a long time to run,
    it is better to set the defautl value to `None` 
    and then calculalte the default value when the corresponding command is called.
