Status: published
Date: 2019-12-30 12:21:11
Author: Benjamin Du
Slug: regularization-in-machine-learning-models
Title: Regularization in Machine Learning Models
Category: AI
Tags: AI, machine learning, data science, regularization
Modified: 2019-12-30 12:21:11

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Regularization add a penalty term to the loss function in machine learning models.
The type of regularizatin depends on the type of penalty used 
(not the type of the objective function).
Below is a summary of commonly seen regularizations.

## Mallow's Cp

## Adjusted R^2

## AIC

## BIC 

## L1 Regularization

L1 both hard and soft shrinkage (good if you can give a picture here)

A regression with L1 regularization is also called LASSO regression.

## L2 Regularization 

L2 regularization results in soft shrinkage. 

Regression with L2 regularization is also called Ridge regression.

## Lp ($1 < p < 2$) Regularization

## Elastic Net Regularization

Elastic Net Regularization is a lienar combination of L1 and L2 penalty.

## Early Stopping

In machine learning, 
early stopping is a form of regularization used to avoid overfitting 
when training a learner with an iterative method, such as gradient descent. 
Such methods update the learner so as to make it better fit the training data with each iteration. 
Up to a point, 
this improves the learner's performance on data outside of the training set. 
Past that point, 
however, 
improving the learner's fit to the training data comes at the expense of increased generalization error. 
Early stopping rules provide guidance as to how many iterations can be run before the learner begins to over-fit. 
Early stopping rules have been employed in many different machine learning methods, 
with varying amounts of theoretical foundation.

Below are some regularization technique specific to neural networks.

## Dropout

Dropout is a regularization technique patented by Google 
for reducing overfitting in neural networks 
by preventing complex co-adaptations on training data. 
It is a very efficient way of performing model averaging with neural networks.
The term "dropout" refers to dropping out units (both hidden and visible) in a neural network.

## Reference

