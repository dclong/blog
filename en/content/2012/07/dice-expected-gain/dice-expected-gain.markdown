UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Expected Gain of Tossing a Dice
Date: 2013-10-30 09:37:39
Tags: Mathematica, recursion, statistics, probability, Markov chain, fun problems
Category: Fun Problems
Slug: dice-expected-gain
Author: Ben Chuanlong Du

[table 1]: http://dclong.github.io/media/dice/tables.pdf
[table 2]: http://dclong.github.io/media/dice/tables.pdf
[dice]: http://dclong.github.io/media/dice/dice.png

<img src="http://dclong.github.io/media/dice/dice.png" height="200" width="240" align="right"/>

Suppose you toss a symmetric dice. 
You are allowed to quit the game and
get money which equals the total points you get at any time if 6 has never
showed up. Whenever 6 shows up, the game is over and you get nothing. For
example, if the first three tosses turn out to be 2, 3 and 5 you can quit the
game immediately and gain 10 dollars or you can choose to continue the game.
What is the expected gains of this game?

First we have to decide how to play the game, i.e. when to quit the game.
Suppose $T$ is the total points we get now.
If we choose to continue the game, the distribution of our profit is presented in [Table 1][].
So our net profit is $\frac{15-T}{6}$ if we choose to continue the game,
which suggests us quit the game when $T\ge15$.
Let's use $W$ to denote the final gain in this game,
then $W$ can be either 0 or some element in $A\equiv\{15, 16, 17, 18, 19\}$.
To find the expected gains,
we have to find the distribution of $W$,
i.e. we have to find $P(W=i)$, $i\in A$.
There're at least two ways to do this.
One of them is to use the powerful tool Markov Chain and the other is to use recursion formula.

## Method I: Markov Chain
Let's use $\{X_n\}$, $n\in \mathbb{N}$ to stand for the total points we get at step $n$.
Let $X_0=0$; $X_k=s$ (just a symbol to avoid confusion with the other states of $\{X_n\}$) for $k\ge n$ if the tossing result turns out to 6 at step $n$;
$X_k=t$ for $k\ge n$ if $X_n=t\in A$.
It's easy to check that $\{X_n\}$ is a Markov Chain and its limiting distribution is what we are interested in.
The transition probability matrix of $\{X_n\}$ is given in [Table 1][].
The probabilities that $W=i$ where $i\in A$,
are the probabilities that $X_n$ ends in the corresponding states,
i.e. $lim_n P(X_n=i)$, $i\in A$.
To find these limiting probabilities, we need to find the limit of $P^n$ (actually we only care about the limit property of the second row of the transition matrix since $X_0=0$).
With the help of R, we can easily find these probabilities which are given below:

    > probs.pos
    15         16         17         18         19
    0.13128076 0.10092009 0.07407628 0.04813533 0.02337223

So the average gain of this game is

    > probs.pos%*%15:19
    [,1]
    [1,] 6.153738

## Method II: Recursion Formula
Let $\{X_n\}$, $n\in \mathbb{N}$ and $A$ be the same as in Method I.
Let $E_{t,n}$ be the event that $X_n=t, X_{n-1}<t$ 
and $P_{t,n}\equiv P(E_{t,n})$,
then $P_{t,n}$ stands for the probability that we first achieve total points $t$ at step $n$.
Specially for $t\in A$, $P_{t,n}$ stand for the probability that the game ends with total points at step $n$.
Let $P_t\equiv \sum_{n\ge0} P_{t,n}$, then $P_t$, $t\in A$ are what we're interested in.
Conditioning $E_{t,n}$ on the value $X_{n-1}$ takes, we have the following recursion formula
$$
P_{t,n}=\frac{1}{6}P_{t-1,n-1}+\frac{1}{6}P_{t-2,n-1} +\frac{1}{6}P_{t-3,n-1}\\
    +\frac{1}{6}P_{t-4,n-1} +\frac{1}{6}P_{t-5,n-1},\text{ for } 0<t\le 15,\ n\ge1.  
$$

Because the game is over when $t\ge15$,
we have different formulas for $t>15$ and $n\ge1$

$$
P_{16,n}=\frac{1}{6}P_{14,n-1}+\frac{1}{6}P_{13,n-1}+\frac{1}{6}P_{12,n-1}+\frac{1}{6}P_{11,n-1},
$$

$$ P_{17,n}=\frac{1}{6}P_{14,n-1}+\frac{1}{6}P_{13,n-1}+\frac{1}{6}P_{12,n-1}, $$

$$ P_{18,n}=\frac{1}{6}P_{14,n-1}+\frac{1}{6}P_{13,n-1},$$

$$ P_{19,n}=\frac{1}{6}P_{14,n-1}.  $$

It's obvious that $P_{t,0}=0$ for $t>0$.
Sum the above formulas over $n$ from 1 to $\infty$ we have
$$
P_{t}=\frac{1}{6}P_{t-1}+\frac{1}{6}P_{t-2}+\frac{1}{6}P_{t-3}
+\frac{1}{6}P_{t-4}+\frac{1}{6}P_{t-5},\text{ for } 0<t\le 15,
$$

$$ P_{16}=\frac{1}{6}P_{14}+\frac{1}{6}P_{13}+\frac{1}{6}P_{12}+\frac{1}{6}P_{11}, $$

$$P_{17}=\frac{1}{6}P_{14}+\frac{1}{6}P_{13}+\frac{1}{6}P_{12},$$

$$P_{18}=\frac{1}{6}P_{14}+\frac{1}{6}P_{13},$$

$$P_{19}=\frac{1}{6}P_{14}.$$

To solve this system, we have to ascertain the initial values.
It's not hard to find values for $P_0,\ldots,P_4$, however,
we can make things even easier by extending the recursion formula forward to term
$P_{-4}$.
Under this extension, the initial conditions for this system are as follows

$$ P_{-4}=P_{-3}=P_{-2}=P_{-1}=0 \text{ and } P_0=1.  $$
    
Now we can find values for $P_t$, $t\in A$ easily.
One way is to use method of generating functions to find the general term for $P_t$ when $t\le15$ and then calculate $P_t$ for $t\in A$.
Another easier way and more practical way is use computer to find these values directly based on these formulas given above.
The implementation in Mathmatica and the corresponding result are as follows. 
Notice that their is a built-in function called `LinearRecurrence` in Mathematica which 
does a similar job to the function `LinearRecursion` here. 

    LinearRecursion::SmallOrder = "The order of the linear recursive equation must be at least 2.";
    LinearRecursion::NotMatch = "The length of argument 'coef' doesn't match the length of 'initial'.";
    LinearRecursion[n_, ini_, coef_: Null, start_: 1, irev_: False, crev_: False] :=
    Module[{nmax, result, i, coefficient, order, index, initials},
        order = Length[ini];
        If[order < 2, Message[LinearRecursion::SmallOrder]; Return[]];
        If[coef === Null,
            coefficient = Table[1, {order}],
            If[Length[coef] != order,
                Message[LinearRecursion::NotMatch]; Return[],
                coefficient = coef
            ]
        ];
        If[irev, initials = Reverse[ini], initials = ini];
        If[crev, coefficient = Reverse[coefficient]];
        index = n - start + 1;
        nmax = Max[index];
        If[nmax <= order, Return[initials[[index]]]];
        result = Table[0, {nmax}];
        result[[Table[i, {i, 1, order}]]] = initials;
        For[i = order + 1, i <= nmax, i++,
            result[[i]] = result[[Table[j, {j, i - order, i - 1}]]].coefficient
        ];
        result[[index]]
    ]

    In[142]:=
    ini = {0, 0, 0, 0, 1};
    coef = {1/6, 1/6, 1/6, 1/6, 1/6};
    c1 = coef[[1]];
    c2 = coef[[2]];
    c3 = coef[[3]];
    c4 = coef[[4]];
    c5 = coef[[5]];
    p11 = LinearRecursion[11, ini, coef, -4];
    p12 = LinearRecursion[12, ini, coef, -4];
    p13 = LinearRecursion[13, ini, coef, -4];
    p14 = LinearRecursion[14, ini, coef, -4];
    p15 = LinearRecursion[15, ini, coef, -4];
    p16 = c5 p11 + c4 p12 + c3 p13 + c2 p14;
    p17 = c5 p12 + c4 p13 + c3 p14;
    p18 = c5 p13 + c4 p14;
    p19 = c5 p14;
    probs = {p15, p16, p17, p18, p19};
    gain = probs.Table[i, {i, 15, 19}]

    Out[159]=
    2893395172951/470184984576

The implementation in R and the corresponding result are as below. 

    #' @param n is the subscript of the array to be calculated
    #' @param ini is the initial values vector starting from the first term
    #' @param  coef is the coefficients vector in the linear recursion equation
    fibo=function(n,ini,coef=rep(1,length(ini)),start=1,irev=FALSE,crev=FALSE){
        order=length(ini)
        if(order<2)
        stop("the order of the difference equation must be at least 2.")
        if(length(coef)!=order)
        stop("the lengths of the coefficents vector and the initial
        values vector must be the same.")
        n=n-start+1
        nmax=max(n)
        if(nmax<=order)
        return(ini[n])
        if(irev)
        ini=rev(ini)
        if(crev)
        coef=rev(coef)
        result=rep(0,nmax)
        result[1:order]=ini
        for(i in (order+1):nmax)
        result[i]=result[(i-order):(i-1)]%*%coef
        return(result[n])
    }

    ini=c(0,0,0,0,1)
    coef=rep(1/6,5)
    c1=coef[1]
    c2=coef[2]
    c3=coef[3]
    c4=coef[4]
    c5=coef[5]
    p11=fibo(11,ini,coef,-4)
    p12=fibo(12,ini,coef,-4)
    p13=fibo(13,ini,coef,-4)
    p14=fibo(14,ini,coef,-4)
    p15=fibo(15,ini,coef,-4)
    p16=c5*p11+c4*p12+c3*p13+c2*p14
    p17=c5*p12+c4*p13+c3*p14
    p18=c5*p13+c4*p14
    p19=c5*p14
    probs=c(p15,p16,p17,p18,p19)
    gain=probs%*%15:19
    > gain
    [,1]
    [1,] 6.153738

We can easily generalize this problem by assume the dice to be a nonsymmetric one with $f$ faces having arbitrary points on it.
Both of the two above methods can apply to the generalized problem,
however the second method is simpler for this kind of problems.

