UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Which One Is the Best Strategy? (continued)
Date: 2013-10-30 15:13:01
Tags: Mathematica, pattern, Markov chain, statistics, probability, sequence, coin, fun problems
Category: Fun Problems
Slug: best-strategy-2
Author: Ben Chuanlong Du

[Table 1]: http://dclong.github.io/media/pattern/pattern-first-out-probability.pdf
[How Long Does It Take to Observe a Sequence?]: http://dclong.github.io/en/blog/how-long-observe-pattern/
[Which One Is the Best Strategy?]: http://dclong.github.io/en/blog/best-strategy/ 

<img src="http://dclong.github.io/media/pattern/coin.jpg" height="200" width="240" align="right"/>

Suppose we flip a coin which has probability 0.7 to be head again 
and again and two people choose two different sequences of length 3 (e.g., THH). 
The people whose sequence appears first wins. 
If you are allowed to choose first, which sequence will you choose?

I discussed about the following interesting probability problem in my post 
[Which One is the Best Strategy?][] before.
I mentioned that there are better ways to solve this problem. 
I will talk about these methods here. 

In this problem, we have to calculate the probabilities for two given sequences to come out first. 
There are at least two ways to do this. 
The first way is to use Markov Chain, which is simple and direct. 
As long as we can write down the transition matrix,
we can calculate the limiting probabilities in various ways.
Since this process is similar to Example ??, I will just skip it here. 
The other way is by introducing a new random variable $M = min\{X_1 , X_2 \}$, 
where $X_1$ and $X_2$ are the steps needed for the two patterns to first come out. 
Conditioning on the event $E_1 \equiv \text{pattern 1 comes out first}$, 
we get an equation involves $P_1 \equiv P (E_1 )$, $E(M )$ 
and the expected time for some patterns (pattern 1, pattern 2 and probably some new patterns) to occur. 
Similarly, conditioning on the event $E_2 \equiv \text{pattern 2 comes out first}$, 
we get an equation involves $P_2 \equiv P (E_2 )$, $E(M )$
and the expected time of some patterns (pattern 1, pattern 2 and probably
some new patterns) to occur. 
In addition, we have the constraint $P_1 + P_2 = 1$. 
I have already talked about how to calculate the expected time for a sequence to occur 
in the post [How Long Does It Take to Observe a Sequence?][],
so what we have to do is just to solve a group of linear equations. 

Before doing any calculation, I guess many people will choose pattern "HHH". 
However, this pattern is beaten by "THH". 
There's an easy way to show this. 
Suppose we first observe sequence HHH at step $n(>3)$, 
then the outcome must be "T" at step $n − 3$,
which means that we have observed "THH" at step $n − 1$. 
So for "HHH" to win against "THH", it must appear at step 3. 
So the probability for "HHH" to beat "THH" is $0.7^3 = 0.343 < 0.5$, 
i.e. "HHH" is not as good as "THH".
This method is very neat, but unfortunately it does not work for all pairs of patterns. 
To compare other pairs of patterns, 
we can use function "PatternFirstComeOurProbability" in the code of the post 
[How Long Does It Take to Observe a Sequence?][]. 

    PatternFirstComeOutProbability[{ {1, 1, 1}, {0, 1, 1} }, {1, 0}, {7/10, 3/10}]
    {219/49, 343/1000, 657/1000}

From the above result we can see that the chance for pattern "HHH" to beat
pattern "THH" is $343/1000 = 0.343 < 0.5$ which matches the results I got
before.

Now we already know that pattern "HHH" is beaten by pattern "THH". 
A nature question people might ask is that cannot pattern "THH" beat all other
patterns? The answer is no, and actually there's no pattern which can beat all
other patterns in this problem. 
The following Mathematica code will help us
to calculate the probability for a pattern to come our first when compared to
some other pattern.

    patterns = Tuples[{0, 1}, 3];
    ProbMatrix = Table[Null, {8}, {8}];
    For[i = 1, i < 8, i++,
        For[j = i + 1, j <= 8, j++,
            probs =
            PatternFirstComeOutProbability[{patterns[[i]], patterns[[j]]}, {1, 0}, {7/10, 3/10}];
            ProbMatrix[[i, j]] = probs[[2]];
            ProbMatrix[[j, i]] = probs[[3]];
        ]
    ];
    For[i = 1, i <= 8, i++,
        AppendTo[ProbMatrix[[i]],
        Min[Drop[ProbMatrix[[i]],
        Flatten[Position[ProbMatrix[[i]], Null]]]]]
    ];
    names = StringJoin /@ IntegerString /@ patterns;
    TableForm[ProbMatrix, TableHeadings -> {AppendTo[names, "Min"], names}]

The result of the above code is presented in 
[Table 1][]. 
From Table 1, we can see
that none of the 8 rows has values that're all at least 0.5, which means that none
of the 8 patterns can beat all other patterns. 
Though we cannot find a pattern
which can always give you a higher chance to win against other patterns, we still
have to make a decision. Suppose we have to let our competitor know which
pattern we choose , and he/she is smart enough (which means that he/she will
always make the best choice based the pattern we choose), we want to choose
the pattern which yields highest winning probability. So we have to choose
the pattern which is the best (yields the highest winning probability) in the
worst situation. This is kind of like the Mini-Max rule in decision theory. The
following Mathematica code help us find the right pattern.

    patterns[[Flatten[Position[ProbMatrix[[All, 9]], Max[ProbMatrix[[All, 9]]]]]]]
    { {"T", "H", "H"} }

So if the other player is smart enough, we should choose pattern "THH".
Though in this problem we only compare two patterns at a time, function
"PatternFirstComeOurProbability" can handle the case when multiple patterns
are involved. For example, suppose 3 people are in this game and they choose
pattern "THH", "HHH" and "TTT" respectively. Running function 
"PatternFirstComeOurProbability" in Mathematica yields the following result.

    PatternFirstComeOutProbability[{ {"T", "H", "H"}, {"H", "H","H"}, {"T", "T", "T"} }, {"H", "T"}, {7/10, 3/10}]
    {30441/7270, 418509/727000, 343/1000, 5913/72700}
    N[%]
    {4.18721, 0.575666, 0.343, 0.0813343}

That is the probabilities for the 3 people to win are about 0.576, 0.343 and 0.081
respectively.
Indeed function "PatternFirstComeOurProbability" is powerful, but it also
has a limitation. It might give us wrong results when patterns with different
lengths are compared with function PatternFirstComeOurProbability. 
For example, pattern "HT" will definitely appear before pattern "HHTH", however,
function PatternFirstComeOurProbability doesn't give us the right answer.

    PatternFirstComeOutProbability[{ {"H", "T"}, {"H", "H", "T", "H"} }, {"H", "T"}]
    {9/2, 3/4, 1/4}

These kind of situations are easy to handle. A always safe way compare patterns
with differen lengths is to change the problem to one in which all patterns have
the same length. For example, instead of letting function PatternFirstComeOur-
Probability compare patterns "HH" and "HTH", we can let it compare patterns
"HHT", "HHH" and "HTT".
Based on the above idea, it's easy to write a function which is able to handle
all situations, however, this is trivia and I don't think it's worth my time. Time
is finite while knowledge is infinite. We should spend time on more valuable
things.

Actually we've killed multiple birds with one stone in this problem. We can
also calculate the expected time for a pattern to show up, given that some
other pattern has already occurred, 
see function PatternAdditionalExpected Time. 
However, this function have a similar issue as function PatternFirst-
ComeOurProbability has. And what's more, we have to carefully define what
"addition step needed" means.
