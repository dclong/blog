Status: published
Date: 2019-12-28 23:22:29
Author: Benjamin Du
Slug: tips-on-xgboost
Title: Tips on XGBoost
Category: AI
Tags: AI, data science, machine learning, XGBoost
Modified: 2019-12-28 23:22:29

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. It is suggested that you use the sklearn wrapper classes `XGBClassifier` and `XGBRegressor`
    so that you can fully leverage other tools of the sklearn package.

2. There are 2 types of boosters (`gbtree` and `gblinear`), 
    It is suggested that you always use tree booster (`gbtree`) 
    as it always outperformas the linear booster (`gblinear`).

3. Instead of training, validation and testing sets,
    people typically use training and testing sets 
    and parameter tuning is done using cross validation based on the training data.
    The advantage of this way is that the data is better used. 

4. Feature engineering and ensemble are usually more important 
    (in terms of improving model performance) than parameter tuning.

5. split-by-leaf mode (grow_policy='lossguide') makes XGBoost run much faster.

## Parameters

### General Parameters

It is suggested that you keep the default values for the general parameters 
(`booster`, `silent` and `nthrad`).

#### booster [default=gbtree]

The booster parameter specifies the type of model to run. 
It has 2 options `gbtree` (tree-based models) and `gblinear` (linear models).
It is suggested that you keep the default value (`gbtree`) 
as `gbtree` always outperforms `gblinear`.

#### silent [default=0]

The silent mode is activated (no running messages will be printed) when the `silent` parameter is set to 1.
It is suggested that you keep the default value (deactivate the silent mode)
which helps you understanding the model and training.

#### nthread [default to maximum number of threads available]

Number of threads to be used in training.
It is suggested that you keep the default value.

### Booster Parameters

The following is focused on gbtree only
as it always outperforms `gblinear`.

#### `eta`, `learn_rate` [default=0.3]

`eta` is analogous to learning rate.
The typical final values to be used is between 0.01 and 0.2.
It is suggested that you tune the value using cross validation.

#### \* min_child_weight [default=1]

Defines the minimum sum of weights of all observations required in a child.
It is used to control over-fitting. 
Higher values prevent a model from learning relations 
(which might be highly specific to the particular sample selected for a tree)
while too high values can lead to under-fitting hence.
It is suggested that you tune the value using cross validation.


#### \* max_depth [default=6]

The maximum depth of a tree, same as GBM.
Used to control over-fitting as higher depth will allow model to learn relations very specific to a particular sample.
Should be tuned using CV.
Typical values: 3-10

#### max_leaf_nodes

The maximum number of terminal nodes or leaves in a tree.
Can be defined in place of max_depth. Since binary trees are created, a depth of ‘n’ would produce a maximum of 2^n leaves.
If this is defined, GBM will ignore max_depth.

#### gamma [default=0]
A node is split only when the resulting split gives a positive reduction in the loss function. Gamma specifies the minimum loss reduction required to make a split.
Makes the algorithm conservative. The values can vary depending on the loss function and should be tuned.

#### max_delta_step [default=0]

In maximum delta step we allow each tree’s weight estimation to be. If the value is set to 0, it means there is no constraint. If it is set to a positive value, it can help making the update step more conservative.
Usually this parameter is not needed, but it might help in logistic regression when class is extremely imbalanced.
This is generally not used but you can explore further if you wish.

#### subsample [default=1]

Same as the subsample of GBM. Denotes the fraction of observations to be randomly samples for each tree.
Lower values make the algorithm more conservative and prevents overfitting but too small values might lead to under-fitting.
Typical values: 0.5-1

#### colsample_bytree [default=1]

Similar to max_features in GBM. Denotes the fraction of columns to be randomly samples for each tree.
Typical values: 0.5-1

#### colsample_bylevel [default=1]

Denotes the subsample ratio of columns for each split, in each level.
I don’t use this often because subsample and colsample_bytree will do the job for you. but you can explore further if you feel so.

#### lambda [default=1]

L2 regularization term on weights (analogous to Ridge regression)
This used to handle the regularization part of XGBoost. Though many data scientists don’t use it often, it should be explored to reduce overfitting.

#### alpha [default=0]

L1 regularization term on weight (analogous to Lasso regression)
Can be used in case of very high dimensionality so that the algorithm runs faster when implemented

#### scale_pos_weight [default=1]

A value greater than 0 should be used in case of high class imbalance as it helps in faster convergence.
 


### Number of Decision Trees (`n_estimators`)

### max_features

### Depth of Decision Trees (`max_depth`)

### Early Stopping (`early_stopping_rounds`)

Prevent overfitting.

### subsample

`subsample` is for each tree the percentage of rows taken to build the tree. 
I recommend not taking out too many rows, 
as performance will drop a lot. Take values from 0.8 to 1.

### colsample_bytree

Maximum percentage of features used by each tree.

number of columns used by each tree. In order to avoid some columns to take too much credit for the prediction (think of it like in recommender systems when you recommend the most purchased products and forget about the long tail), take out a good proportion of columns. Values from 0.3 to 0.8 if you have many columns (especially if you did one-hot encoding), or 0.8 to 1 if you only have a few columns.

## Booster Parameters

### gamma

A regularization parameter. 
Either 0, 1 or 5.

## [XGBClassifier.fit](https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=classifier#xgboost.XGBClassifier.fit)

The method `XGBClassifier.fit` takes a parameter `eval_set`
which is a list of tuples of the format (x, y).
Notice that this parameter is NOT used for grid search but for tracking performance for early stopping only.
If `eval_set` contains multiple datasets,
then only the last dataset is used for early stopping.

## Set Parameters for XGBClassifier or XGBRegressor

It is suggested that you use the method `set_params` to set parameters after creating a model
instead of setting parameter on model creation.

https://stackoverflow.com/questions/34674797/xgboost-xgbclassifier-defaults-in-python

## Parameter Tuning 

https://sites.google.com/view/lauraepp/parameters

https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/

## GPU

https://xgboost.readthedocs.io/en/latest/gpu/

## Questions 

Any difference between xgboost.cv and the cross validation in sklearn?
which one should I use?

## References

https://xgboost.readthedocs.io/en/latest/parameter.html#xgboost-parameters

https://github.com/dmlc/xgboost/tree/master/demo/guide-python

https://machinelearningmastery.com/tune-number-size-decision-trees-xgboost-python/

https://towardsdatascience.com/fine-tuning-xgboost-in-python-like-a-boss-b4543ed8b1e

https://towardsdatascience.com/a-beginners-guide-to-xgboost-87f5d4c30ed7

https://www.datacamp.com/community/tutorials/xgboost-in-python

https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/

