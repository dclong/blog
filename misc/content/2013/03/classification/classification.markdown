Status: draft
Title: Classification
Date: 2013-03-23 22:22:34
Tags: CART, machine learning, random forests, statistics, classification, SVM, neuron network, regression
Category: AI
Slug: classification
Author: Ben Chuanlong Du
Modified: 2020-05-23 22:22:34

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 

## GBM

## Neuron Network

Use the backpropagation algorithm to learn parameters.
Apply observations 1 by 1, which is a stochastic gradient descent algorithm.
The complexity of Neuron Network is related to the number of nodes in the hidden layers. 

## Support Vector Machine (SVM)
The basic version of SVM is a linear separation.
This is obvious since SVM uses a hyperplane to separate data points.
The kenel version (nonlinear transformation) of SVM uses curves/curved surfaces to separate data points.
The Gaussian kenel is a popular choice.
The kenel version (nonlinear transformation) of SVM is good for situations 
where different classes are separated by simple non-linear functions.
Another way to classify non-separable data points is to use the soft margin version.
The soft margin version of SVM is good situations 
whether most data points except a few data points can be separate by a hyperplane.
In this situation it is often a bad idea to use the kenel version (nonlinear transformation).

- The optimization problem in SVM is a quadratic programming problem,
so it's relatively easy to solve.

- SVM is claimed to be one of the most effective classification methods (though debatable). 

- SVM scales well to high dimension data.
Acutally the kenel version of SVM allows it to deal with data of infinite dimensions.

- The expected prediction error is bounded by $\frac{n}{N-1}$,
where $n$ is the number of support vectors 
and $N$ is the number of observations.

- SVM can be generalized to the multi-class problems. 


##  Logistic Regression 
Linear separation. 
Logistic Regression is a specially case of the generalized linear regression,
where the response is binary. 
The Newton's algorithm can be used to optimize the likelihood.
Can be generalized to the multi-class classification problem using the multinomial distribution.


## Naive Bayesian Classification
Called naive becuase the assumption of conditional independent of covariates given the response variable. 
Despite the assumption is obviously wrong, 
the Naive Bayesian classification is very effective in text mining, 
e.g. predict whether an email is a spam or not. 
The way is works is to carefully select a list of words (according to expert knowledge about whether they can distinguish usually email and spam email or not).
The size of the list is typically around 50,000 (the multinomial approach is nature but have too many parameters, this is why the conditionally independent assumption is used).
Problem arise when words not in the dictionary appears in emails. 
A simple way to add 1 to each category to avoid numerical problems. 
This is caled Laplace smoothing. 
There's actually Bayesian explanation to this Laplace smoothing approach.
It's similar to use priors for parameters. 
This is a very useful trick in many problems though very simple. 

## Some Tips for Classification

1. Feature engineering is more important than model and parameter tuning.

2. Do not forget the const/bias variable/feature.

3. Reguarization is critical 

4. Python packages for classification often encode binary response variable as 0 and 1 (instead of -1 and 1).
