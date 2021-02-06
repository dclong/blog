Status: published
Title: Summary on Random Number Generators
Date: 2019-05-27 21:14:07
Slug: summary-random-number-generators
Author: Ben Chuanlong Du
Category: AI
Tags: WELL, RNG, statistics, SFMT, dimension, MT, PCG, Java, Python

<img src="http://www.legendu.net/media/rng/random-number-generator.png" height="200" width="240" align="right"/>

## Mersenne Twister

The most popular pseudo random number generator (PRNG) currently is Mersenne Twister. 
It is implemented in many programming languages 
and is the default in many software and programming languages.
Mersenne Twister has many different versions, 
among which the MT19937 is the most widely used one. 
The period of MT19937 is extreemly long ($2^{19937}-1$)
and is equidistributed for generating vectors up to dimension 623. 
The MT19937 generate 32 bits random numbers. 
Combining two random blocks, 
one can generate 64 bits random numbers.
This is often implemented together with the 32 bit version, 
and usually call MT19937_64.
The MT19937_64 is equidistributed for generating vectors up to dimension 311.

## WELL

A more modern family of random number generators than Mersenne Twister 
is the WELL random number generators, 
which have better equidistribution property and are better to escape the zeroland 
(initialization array contains many zero bits). 
However, 
the speed of the WELL generators is about 0.6 to 0.7 compared to the Mersenne Twister generators. 
Also the WELL random number generators has a large inner state 
(e.g., the WELL44497b uses about 33kb for its inner state while the MT19937 uses only about 2.5kb). 
This is usually not a problem on modern computers, 
but if you use lots of random number generators at the same time 
or if the code is run on a embedded device, 
it might worth considering the consume of memories of these generators. 
Among different versions of WELL generators, 
WELL19937c and WELL44497b are commonly used. 

## SFMT 

SIMD-oriented Fast Mersenne Twister (SFMT) is an improved version of Mersenne Twister. 
It uses parallelism of modern CPUs and is about twice faster than mersenne Twister. 
SFMT also has better equidistribution property than Mersenne Twister, 
but not as good as WELL.
SFMT recovers from 0-excess initial state faster than Mersenne Twister, 
but not faster than WELL.
C++ implementations are available but I don't see a popular Java implementation so far.

## [PCG](http://www.pcg-random.org/)

PCG is a family of simple fast space-efficient statistically good algorithms 
for random number generation. 
Unlike many general-purpose RNGs, 
they are also hard to predict.
C++ implementations are available but I don't see a popular Java implementation at this time.


## Libraries for Random Number Generators

### Java 

1. [org.apache.commons.math3.random.RandomDataGenerator](http://commons.apache.org/proper/commons-math/javadocs/api-3.6/org/apache/commons/math3/random/RandomDataGenerator.html)
    is a popular one. 
    By default it uses a Well19937c generator.
    A customized RandomGenerator can be provided in the constructor.

### Python

1. Use the [random](https://docs.python.org/3/library/random.html) model.
    It is based on a Mersenne Twister random number generator.

### Rust 

[sfmt](https://lib.rs/crates/sfmt)

[mersenne_twister](https://lib.rs/crates/mersenne_twister)