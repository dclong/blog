UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2014-08-10 13:13:46
Slug: chance-take-own-seat
Author: Ben Chuanlong Du
Title: Chance to Take One's Own Seat?
Category: Fun Problems
Tags: statistics, recursion, probability, fun problems, seat

<img src="http://dclong.github.io/media/seat/seat.jpg" height="200" width="240" align="right"/>

There are $N$ seats on a plane.
Suppose the first passengers is drunk and he takes a seat randomly.
For each of the other passengers, if his/her seat is not taken by other people,
then he/she sits on his/her own seat, otherwise he/she takes a seat randomly.
What is  the probability that the last passenger takes his/her own seat?

Let's use $P_n$ to stand for the probability that the last passenger takes his/her own seat,
given that there're $n$ seats in total, i.e. $N=n$.
If the first passenger takes his own seat,
then the last passenger will take his/her own seat.
If the first passenger takes the last passenger's seat,
then the last passenger cannot take his/her own seat (we know that he/she must take the first passenger's seat).
If the first passenger takes the $i^{th}, 1<i<n$ passenger's seat,
then for the $j^{th}$ passenger, $1< j\lt i$, he/she will takes his/her own seat.
Now the $i^{th}$ passenger has to choose a seat randomly.
Since we don't care about whether the $i^{th}$ passenger takes his/her own seat or not,
we can pretend that the first passenger's seat is the $i^{th}$ passengers.
From this perspective, the problem has been changed to a same problem with $N=n-i+1$.
So conditioning on the seat that the first passenger takes,
we have the following recursive formula:

$$
P_n=\frac{1}{n}\times1+\frac{1}{n}\times0+\sum_{i=2}^{n-1}\frac{1}{n}P_{n-i+1}=\frac{1}{n}\sum_{i=1}^{n-1}P_i,\ n\ge2,
$$

where $P_1=1$.

We can use method of generating function to find the formula of general terms.
However, if we notice from the recursive formula that $P_2=\frac{1}{2}$,
$P_3=\frac{1}{2}$, $P_4=\frac{1}{2}$ and so on.
We can easily see that $P_i=\frac{1}{2}$ for $i\ge2$ is the
unique solution for the general terms.\
So as long as there're more than 1 people,
the probability that the last passenger takes his/her own seat is $\frac{1}{2}$.


