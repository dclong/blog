Status: published
Date: 2019-12-24 11:36:04
Title: Ensemble Machine Learning Models
Slug: ai-ensemble
Author: Ben Chuanlong Du
Category: AI
Tags: AI, statistics, ensamble, data science, machine learning

The prediction error is a trade-off of bias and variance. 
In statistics, 
we often talk about unbiased estimators (especially in linear regression). 
In this case we restrict the estimators/predictors to be in a (small) class,
and find the optimal solution in this class (called BLUE or BLUP).

Generally speaking, 
unbiased predictors are not ideas in prediction problems.
In many situations we can easily find predictors with small bias (usually very complexed predictors/models). 
To improve the performance of predictors, 
we often want to decrease their variance at the cost of increase bias. 
This is called decreasing the complexity of the predictors/models.
This can be done by variable/feature selection. 
This is discussed in [the regularization post]().
Here we talk about some aggregation/ensamble technic to decrease the complexity of predictors/models.
The is inspired by the simple fact that the variance of the mean of `n` iid random variables (with finite variance)
is `1/n` times the variance of any of them. 
This means that by combining (not strongly correlated) predictors,
e.g., linear combination or majority vote, 
we can get (much) better predictors. 

## Decrease Complexity

### Bagging
Bagging is short for Bootstrap Aggregation.
The basic idea is to build predictors based on bootstrap samples (sample with replacement) of the training data. 
Each time we get a different bootstrap sample,
so we have a different predictor.
Hopefully these predictors are not strongly correlated so that by averaging (unweighted) them we get a better predictor.
This idea is well used in random forest. 
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
There are different version of Boosting, e.g., Gradient Boosting and AdaBoosting (Adaptive Boosting).
AdaBoosting is popular in face recognition problems.

