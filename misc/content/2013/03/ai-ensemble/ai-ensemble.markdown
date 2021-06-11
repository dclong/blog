Status: published
Date: 2013-03-24 13:51:12
Author: Ben Chuanlong Du
Title: Ensemble Machine Learning Models
Slug: ai-ensemble
Category: AI
Tags: AI, statistics, ensamble, machine learning, data science
Modified: 2019-12-24 13:51:12


The prediction error is a trade-off of bias and variance. 
In statistics, 
we often talk about unbiased estimators (especially in linear regression). 
In this case we restrict the estimators/predictors to be in a (small) class,
and find the optimal solution in this class (called BLUE or BLUP).

Generally speaking, unbiased predictors are not ideas in prediction problems.
In many situations we can easily find predictors with small bias (usually very complexed predictors/models). 
To improve the performance of predictors, 
we often want to decrease their variance at the cost of increase bias. 
This is called decreasing the complexity of the predictors/models.
This can be done by variable/feature selection. 
This is discussed in 
[Regularization in Machine Learning Models](http://www.legendu.net/misc/blog/regularization-in-machine-learning-models/)
.
Here we talk about some ensamble technics to decrease the complexity of predictors/models.
The is inspired by the simple fact that the variance of the mean of `n` i.i.d random variables (with finite variance)
is $\frac{1}{n}$ times the variance of the population of those random variables.
This means that by combining (not strongly correlated) predictors,
e.g., linear combination or majority vote, 
we can greatly reduce the variance and thus achieve better prediction accuracy.

## Decrease Complexity

### Bagging

Bagging is short for Bootstrap Aggregation.
The basic idea is to build predictors based on bootstrap samples (sample with replacement) of the training data. 
Each time we get a different bootstrap sample,
so we have a different predictor.
Hopefully these predictors are not strongly correlated 
so that by averaging (unweighted) them we get a better predictor.
This idea is well demonstrated in random forest. 
To further decrease the correlation between trees, 
the random forest process also restricts the number of variables 
(usually square root of the total number of variables) used to build each tree.
The neuron network can also be considered as a way of Bagging,
since the input of a node is a linear combination of outcomes from last layer.


### Stacking

Stacking is similar to Bagging. 
The difference is that Stacking uses weighted averages of predictors based on their performances. 
The weights are often chosen to minized the prediction error in leave-1-out cross validation. 


## Increase Complexity

An opposite approach to these discussed above is to start from a very simple predictor (big bias but small variance)
and then increase the complexity (decrease bias at cost of increase variance) of the predictor.
This is common in nature, e.g., the human brain is developped from simple to complex. 
This approach is called Boosting.
Boosting algorithms is an iterative functional gradient descent algorithms. 
That is, algorithms that optimize a cost function 
over function space by iteratively choosing a function (weak hypothesis) 
that points in the negative gradient direction. 
There are different version of Boosting 
among which AdaBoosting (Adaptive Boosting) and Gradient Boosting are the most 2 poular ones. 
AdaBoosting is popular in face recognition problems.
Gradient Boosting models dominates traditional (non-deep) machine learning.
[XGBoost](https://github.com/dmlc/xgboost)
is a popular implementation of the gradient boosting framework.


## References

https://en.wikipedia.org/wiki/Boosting_(machine_learning)

https://en.wikipedia.org/wiki/Gradient_boosting
