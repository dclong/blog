Status: published
Author: Ben Chuanlong Du
Date: 2012-11-22 12:24:54
Title: Experiment Design
Slug: linear-models
Category: AI
Tags: model, statistics, regression, AI, experiement design
Modified: 2020-05-22 12:24:54

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 
1. Complete Randomized Design (CRD)

2. Randomized Complete Block Design (CBD)
	- same RNE as CRD
3. Latin Square Design (LSD)
	- same RNE as CRD
4. Balanced Incomplete Block Design
	- all treatments cannot fit in any one block
	- each treatment appears the same number of times in the design
	- each pair of treatment appears together in the same number of blocks
	- BIBD does not exist for every t (number of treatments), b (number of block) and k (the number of units in each block)
	- inter-block comparison, intra-block information is usually sacrificed (confounded with unknown block effect)
	- when block effect is random, intra-block information can be recovered. There is also a neat trick for BIBD when block effect is random: do inference using block totals (not necessarily better than inter-block information only)
assumptions:


5. Split-plot Design (SPD)

- common in animal science, agriculture, engineering, chemistry, etc.
- can analyze separately for whole-plot and split-plot (sub-plot) parts
- there are random effects in SPD

factorial analysis:

- appearance of higher interactions requires appearance of lower interactions

EFFECT HIERARCHY PRINCIPLE – If an interaction
involving a given set of factors is included in the model, all
main effects and interactions involving subsets of these factors
should also be included.
• EFFECT HEREDITY PRINCIPLE – If an interaction
involving a given set of factors is included in the model, at least
one effect of the next smallest order involving a subset of these
factors should also be included.



some times purposely confound a factor with another (usually these factors are not of interests to us) can be smart

random and fixed effect, fixed is easy most of time,

sometimes if random is too hard (usually seen in generalized linear models), can treat as fixed


3. independent

1. distribution assumption

2. equal variance/dispersion 
	- residual plot


Primary concern about model is lack of fit

Primary concern about variance is equality

Levene Test and BF test 

Simultaneous confidence intervals

Scheffe (all)

Tukey (pairwise)

Dunnett (multiple vs one)	


Estimation of Variance Components

REML vs ML

recursive estimating ... suppose we know variance we can estimate coefficients, and then estimate variances ... repeat ...

non-linear ... based on approximation ...
	
