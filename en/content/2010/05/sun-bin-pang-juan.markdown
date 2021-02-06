UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Author: Ben Chuanlong Du
Date: 2014-08-06 10:57:40
Slug: sun-bin-pang-juan
Title: Sun Bin PK Pang Juan
Category: Fun Problems
Tags: puzzle, Mathematica, fun problems, math, number, sum, product

<img src="http://dclong.github.io/media/pk/pk.jpg" height="200" width="240" align="right"/>

Dating back to the time when I was a sophomore, 
I read a very interesting problem from "Waming", 
which is a magazine of math department of USTC (University of Science and Technology of China).

One day Guigu Zi (a famous ancient Chinese sophist, 
the teacher of Sun Bin and Pang Juan) came up with two numbers between 1 and 100, 
and told the product of the two numbers to Sun Bin, the sum to Pang Juan. 
The next day when Pang Juan ran into Sun Bin, he boasted, 
"Now I don't know what the 2 numbers are, 
but I'm pretty sure you don't know either." 
"I have to thank you for the information, 
because I did have no idea of what the 2 numbers are, but now I already know." 
responded Sun Bin. 
Pang Juan thought for a while, smiled and then said, 
"Now the same here." Question: what are the two numbers?

If you think are a very smart people and very good at logic, you can spend some time think about this problem. 
My code (written in Mathmatica) for solving this problem is given below. 

    (*function filter possible combinations based on Pang Juan's first words.*)
    PangJuan1[comb_] := Module[{i, n, sum, position, j, Result},
        Result = comb;
        n = Length[Result];
        position = {};
        For[i = 1, i <= n, i++,
            sum = Result[[i, 1]] + Result[[i, 2]];
            If[EvenQ[sum] || PrimeQ[sum - 2] || Floor[sum/2] <= 2, AppendTo[position, {i}]]
        ];
        Result = Delete[Result, position];
        Return[Result];
    ];
    (*function filter possible combinations based on Sun Bin's words.*)
    SunBin[comb_] := 
        Module[{n, i, prod, divisors, len, counter, DivisorCombinations, Result, positions, FlagLower, FlagUpper},
        Result = comb;
        n = Length[Result];
        positions = {};
        For[i = 1, i <= n, i++,
            prod = Result[[i, 1]]*Result[[i, 2]];
            divisors = Divisors[prod];
            (*Build up all possible combinations*)
            len = Length[divisors];
            FlagLower = Floor[len/2] + 1;(*The smallest subscript of the bigger divisors*)
            DivisorCombinations = {};
            (*Find the upper subscript of the bigger divisors*)
            For[FlagUpper = FlagLower, 
                FlagUpper < len && divisors[[FlagUpper]] <= 100, FlagUpper++];
                len++;
                For[counter = FlagUpper - 1, counter >= FlagLower, counter--,
                    AppendTo[
          DivisorCombinations, {divisors[[len - counter]], 
           divisors[[counter]]}]
         ];
        (*There should be only one possible combination according the \
    imformation that Pang Juan provided in his first sentence*)
        If[Length[DivisorCombinations] == 1,
         AppendTo[positions, {i}],
         If[Length[PangJuan1[DivisorCombinations]] != 1,
          AppendTo[positions, {i}]
          ]
         ]
        ];
       Result = Delete[Result, positions];
       Return[Result];
       ];
    (*function filter possible combinations based on Pang Juan's second words.*)
    PangJuan2[comb_] := 
      Module[{n, i, sum, AddendCombinations, j, Result, positions, 
        counter},
       Result = comb;
       n = Length[Result];
       positions = {};
       For[i = 1, i <= n, i++,
        sum = Result[[i, 1]] + Result[[i, 2]];
        (*Build up all the possible combinations*)
    
        AddendCombinations = {};
        counter = sum/2;
        For[j = 2, j <= counter, j++,
         AppendTo[AddendCombinations, {j, sum - j}]
         ];
        If[Length[SunBin[AddendCombinations]] != 1,
         AppendTo[positions, {i}]
         ]
        ];
       Result = Delete[Result, positions];
       Return[Result];
       ];
    (*construct all combinations and use the above three functions to \
    filter the right one*)
    GuiGuzi[] := Module[{Result},
       Result = {};
       For[i = 2, i <= 100, i++,
        For[j = i, j <= 100, j++,
          AppendTo[Result, {i, j}];
          ];
        ];
       (*Use the information that Pang Juan provide in his first sentence \
    to delete those impossible combinations*)
   
       Result = PangJuan1[Result];
       (*Use the information that Sun Bin provide to delete those \
    impossible combinations*)
       Result = SunBin[Result];
       (*Use the information that Pang Juan provide in his second sentenc \
    to delete those impossible combinations*)
   
       Result = PangJuan2[Result];
       Return[Result];
       ];
    (*run the porgram*)
    GuiGuzi[]
    {{4, 13}}

