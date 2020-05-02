UUID: 6db9899f-33c5-4c90-8108-1b4979e52feb
Status: published
Date: 2015-05-17 17:21:02
Author: Ben Chuanlong Du
Slug: lasso-in-sas
Title: Lasso in SAS
Category: Computer Science
Tags: programming, SAS, LASSO, feature selection, variable selection, regularization

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**



You can do this in two steps:
1) Use GLMSELECT as if you had an OLS model, and get several sensible models
2) Try those models in LOGISTIC or whichever PROC you like for logistic regression.
This isn't formally "right" but I've had good success with it.


GLMSELECT is designed, as the name suggests, for GLM type models. 
But it implements LASSO and LAR, and there are indications that these work well for binary outcomes as well. 
Thus, I've use GLMSELECT when the DV is 0-1, and it hasn't bombed.

This is a hot area.

Some references (not all of which I've read):

Tutz and Leistenstorfer (2006). Response shrinkage estimators in binary regression. Computational Statistics and Data Analysis, 50, 2878-2901

Caster (2007) Mining the WHO drug safety database using lasso logistic regression.

Meier, van de Geer, Buhlman (2008) The group lasso for logistic regression. JRSS, series B, 70, 53-71

Roth, V. (2004) The generalized Lasso. IEEE transactions

also I think van de Geer had a recent article in Annals of Statistics



There is no LAR or LASSO selection options for generalized linear models, such as logistic regression. 
There is the new HPGENSELECT procedure for distributions in the exponential family (such as binomial, binary), 
but this only has the more traditional stepwise selection methods (which I do not recommend). 
As an ad hoc method, 
you could take your first approach (direct analysis on the binary observations) 
using GLMSELECT, with LASSO or LAR. 
Then you could refit the model in GENMOD just using the LASSO/LAR selected variables from GLMSELECT. 
I am sure there are all kinds of theoretical issues with this, 
but I have others recommend this in talks. 
I would not do your second suggestion (based on residuals).

code 1/-1 or 1/0? especially for lasso?
I don't think this should matter ...

HPGENSELECT proc !!!

There is no LAR or LASSO selection options for generalized linear models, 
such as logistic regression. 
There is the new HPGENSELECT procedure for distributions in the exponential family (such as binomial, binary), 
but this only has the more traditional stepwise selection methods (which I do not recommend). 
As an ad hoc method, you could take your first approach (direct analysis on the binary observations) 
using GLMSELECT, with LASSO or LAR. 
Then you could refit the model in GENMOD just using the LASSO/LAR selected variables from GLMSELECT. 
I am sure there are all kinds of theoretical issues with this, 
but I have others recommend this in talks. 
I would not do your second suggestion (based on residuals). 
