UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-05-10 22:05:12
Author: Ben Chuanlong Du
Slug: generating-random-numbers-in-sas
Title: Generating Random Numbers in SAS
Category: Computer Science
Tags: programming, SAS, random number generating, RANDGEN, rand

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**



CALL RANDGEN( result, distname<, parm1><, parm2><, parm3>);
or
   u = rand("Uniform"); /* u ~ U[0,1] */ based on Mersenne-Twister
in a data step

forget about other random number genrating functions

```SAS
data random;
    call streamInit(123);
    do i = 1 to 10;
        x1 = rand('Cauchy');
        output;
    end;
run; 
```




rand can also be used in the IML procedure, 
same method as RANDGEN, the differeence is that rand generate 1 at a time while randgen can generate multiple ones (optimized for IML)

RANDGEN Call
in iml procedures

----------------------------------------------------------------------------
NORMAL (seed) ; only for N(0, 1) distribution, 
UNIFORM (seed) ; U(0, 1)

not suggested as RANDGEN generate better quality random numbers


The following functions ranDist are not good!!!

Functions for Generating Random Numbers and Simulations
NORMAL function
generates a pseudorandom normal deviate

RANDGEN call
generates random numbers from specified distributions

RANDSEED call
initializes seed for subsequent RANDGEN calls

SAMPLE function
generates a random sample of a finite set

UNIFORM function
generates pseudorandom uniform deviates

You can also call functions in Base SAS software such as those documented in the section Random Number Functions and Subroutines.
For sampling from multivariate distributions, you can use the following functions:
RANDDIRICHLET
generates a random sample from a Dirichlet distribution

RANDMULTINOMIAL
generates a random sample from a multinomial distribution

RANDMVT
generates a random sample from a multivariate Student’s $t$ distribution

RANDNORMAL
generates a random sample from a multivariate normal distribution

RANDWISHART
generates a random sample from a Wishart distribution



Random Number Functions and Subroutines
NORMAL
returns a random variate from a normal distribution
RANBIN
returns a random variate from a binomial distribution
RANCAU
returns a random variate from a Cauchy distribution
RAND
returns a random variate from a specified distribution. (See the RANDGEN subroutine.)
RANEXP
returns a random variate from an exponential distribution
RANGAM
returns a random variate from a gamma distribution
RANNOR
returns a random variate from a normal distribution
RANPOI
returns a random variate from a Poisson distribution
RANTBL
returns a random variate from a tabled probability
RANTRI
returns a random variate from a triangular distribution
RANUNI
returns a random variate from a uniform distribution
CALL STREAMINIT
specifies a seed value to use for subsequent random number generation by the RAND function. (See the RANDSEED subroutine.)
UNIFORM
returns a random variate from a uniform distribution
