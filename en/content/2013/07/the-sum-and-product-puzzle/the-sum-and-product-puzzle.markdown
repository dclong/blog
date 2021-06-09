UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: The Sum and Product Puzzle
Date: 2015-02-04 23:47:19
Slug: the-sum-and-product-puzzle
Author: Ben Chuanlong Du
Category: Fun Problems
Tags: puzzle, Mathematica, math, Work, fun problems, sum, product

[sun vs pang]: http://www.legendu.net/en/blog/sun-bin-pang-juan/

I talked about an interesting problem [in this post][sun vs pang].
I had onsite-inteviews from Wolfram at the end of April this year,
and I decided to talk how to solve the problem using Mathematica.
I did some research and realized that the problem is a well-known one
which is called the *Sum and Product Puzzle* (aka the *Impossible Puzzle*). 
The *Sum and Product Puzzle* has several different versions. 
I reframe the one mentioned in my previous post as follows.

> Two numbers (not necessarily unique) between 2 and 99 are chosen. 
> The sum of them is told to Sam and the product of them is told to Peter .

> Sam: "Now I don't know what the 2 numbers are, 
> but I'm sure you don't know either."

> Peter: "I have to thank you for the information, 
> because I did have no idea of what the 2 numbers are, 
> but now I already know."

> Sam: "Now the same here."

> Question: what are the two numbers?

## Notations
R: range of the 2 numbers, which is {2,3,. . . ,99} in this case

x0 , y0: a (the) solution to the Puzzle

## Mathematical Information Hidden in Words
"Now I don't know what the 2 numbers are, 
but I'm pretty sure you don't know either." 
	 
1. $\exists$ multiple pairs of $x, y\in R$ such that $x+y=x_0+y_0$

2. For each pair of $x,y\in R$ such that $x+y=x_0+y_0$, 
$\exists$ multiple pairs of $x',y'\in R$ such that $x'\times y'=x \times y$

Let's called the above conditions set I.

"I have to thank you for the information, 
because I did have no idea of what the 2 numbers are, 
but now I already know."
	 
1. $\exists$ multiple pairs of $x, y\in R$ 
such that $x\times y=x_0\times y_0$ (already in conditions set I). 
         
2. Among all pairs $x,y\in R$ such that $x\times y=x_0\times y_0$, 
$\exists$ an unique pair satisfying conditions set I. 

Let's called the above conditions set II.
	 
"Now the same here"
	 
1. $\exists$ multiple pairs of $x, y\in R$ 
such that $x+y=x_0+y_0$ (already in conditions set I). 

2. Among all pairs $x,y\in R$ such that $x+y=x_0+y_0$, 
$\exists$ an unique pair satisfying conditions set II. 
	 
Let's called the above conditions set III.


## Algorithm to Solve the Sum and Product Puzzle

A/The solution (pair of $x_0$ and $y_0$) 
must satisfies conditions set I, II and III at the same time. 

1. Construct all possible combinations of $x,y\in R$. 

2. Select pairs (among all possible pairs) that satisfy conditions set I, II and III at the same time. 


## Mathematica Code for the Sum and Product Puzzle

    TwoAddends[s_Integer, range_List] := Module[{lower, upper},
       lower = range[[1]];
       upper = range[[2]];
       Table[{i, s - i}, {i, Max[lower, s - upper], Min[upper, s - lower, s/2]}]
    ];

    TwoFactors[p_Integer, range_List] := Module[{lower, upper, div, n},
       lower = range[[1]];
       upper = range[[2]];
       div = Select[Divisors[p], # >= Max[lower, p/upper] && # <= Min[upper, p/lower, Sqrt[p]] &];
       Map[{#, p/#} &, div]
    ];

    S1[pair_List, range_List] := Module[{s, candidates},
       s = Total[pair];
       candidates = TwoAddends[s, range];
       Length[candidates] > 1 && Apply[And, Length[TwoFactors[Times @@ #, range]] > 1 & /@ candidates]
    ];

    P1[pair_List, range_List] := Module[{p, candidates},
       p = Times @@ pair;
       candidates = TwoFactors[p, range];
       Length[candidates] > 1 && Total[Boole[S1[#, range] & /@ candidates]] == 1
    ];

    S2[pair_List, range_List] := Module[{s, candidates},
       s = Total[pair];
       candidates = TwoAddends[s, range];
       Length[candidates] > 1 && Total[Boole[P1[#, range] & /@ candidates]] == 1
    ];

    SumProductPuzzle[range_List] := Module[{lower, upper, candidates},
       lower = range[[1]];
       upper = range[[2]];
       candidates = Flatten[Table[{i, j}, {i, lower, upper}, {j, i, upper}], 1];
       Select[candidates, S1[#, range] && P1[#, range] && S2[#, range] &]
    ]

All code and results for this project are hosted on GitHub at [sum_prod](https://github.com/dclong/sum_prod).
As I will continue to study this problem, 
it is the best place to find the most updated code and results for this problem.

## Result
Run the function `SumProductPuzzle` to find a/the solution to the puzzle.

    SumProductPuzzle[{2, 99}]
    {{4, 13}}

## Some Discussions about the Sum and Product Puzzle
It is of great interest to find all ranges of the form $[2, U]$
such that there is an unique solution to the puzzle in these ranges.

Use the following code to do computation in parallel

    DistributeDefinitions[TwoAddends, TwoFactors, S1, P1, S2, SumProductPuzzle]
    rr = Table[ParallelSubmit[{i}, SumProductPuzzle[{2, i}]], {i, 61, 600}]
    WaitAll[rr]

1. The solution depends on the range (can have no, unique or multiple answers).
2. There is no solution in [2, U] for $2 \le U \le 61$.
3. I have verified that an unique solution exists in [2, U] for $62 \le U \le 610$.
4. As the Mathematica code I wrote is more for illustrating my ideas 
and runs slowly.
I will reimplement the algorithm with previous calculated results cached in Java
to further study this problem.



