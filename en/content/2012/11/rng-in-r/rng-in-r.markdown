UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Random Number Generating in R
Date: 2012-11-05 00:21:35
Tags: R, programming, RNG
Category: Computer Science
Slug: rng-in-r
Author: Ben Chuanlong Du
Modified: 2013-12-05 00:21:35

1. Functions for sampling random numbers from distributions 
    share a same "basic" random number generator (RNG). 
    If one set a seed for the "basic" RNG in use, 
    it affects all functions for generating observations from distributions. 
    The kind of "basic" RNG can be queried and set by `RNGkind`. 
    The default RNG in R is Mersenne-Twister.

2. When doing a big simulation, 
    some people like to split the simulation into smart parts 
    and run each part on a different machine. 
    Theorectically speaking, 
    this can cause problems, 
    because random numbers generated on different machines might not come 
    from disjoint parts of a same seed 
    (or even not a same kind of random number generator). 
    Parallel computing is an alternative to this approach.
