Status: published
Date: 2020-12-30 12:43:37
Author: Benjamin Du
Slug: tips-on-feature-engineering-for-machine-learning
Title: Tips on Feature Engineering for Machine Learning
Category: AI
Tags: AI, machine learning, data science, feature engineering, feature hashing
Modified: 2020-12-30 12:43:37

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

https://towardsdatascience.com/automatic-feature-engineering-using-deep-learning-and-bayesian-inference-application-to-computer-7b2bb8dc7351

Feature selection
Feature extraction
Adding features through domain expertise

FeatureTools a Python library for feature engineering
Deep neural network can extract features too

whether feature engineering is still need ...

Mostly yes, but there maybe some exceptions to this.

One exception I can think of is a scenario when your training dataset is not sufficient to cover all variety that will be involved during run time. In this case, if you are able to design features that are able to model the problem well, then these features might work better than the features provided by deep learning. Because for deep learning data is everything; features are learnt only based on the available data. In contrast, in feature engineering, you can transfer your own understanding of the problem to the model through feature engineering. Assuming that you have a good understanding of the problem and you can model this well enough in the features that you design, then you can reach more generalizable models in the end.

Other than such exceptional scenarios, we can expect deep learning to work better than and to replace feature engineering.


## Categorical Variables

http://www.legendu.net/misc/blog/handling-categorical-variables-in-machine-learning/

## Feature Hashing

https://en.wikipedia.org/wiki/Feature_hashing

https://medium.com/value-stream-design/introducing-one-of-the-best-hacks-in-machine-learning-the-hashing-trick-bf6a9c8af18f

https://booking.ai/dont-be-tricked-by-the-hashing-trick-192a6aae3087

## Useful Libraries

### [FeatureTools](https://github.com/alteryx/featuretools)
[FeatureTools](https://github.com/alteryx/featuretools)
is an open source Python library for automated feature engineering.

### [compose](https://github.com/alteryx/compose)
[compose](https://github.com/alteryx/compose)
is a machine learning tool for automated prediction engineering. 
It allows you to easily structure prediction problems and generate labels for supervised learning.

### [tsfresh](https://github.com/blue-yonder/tsfresh)
[tsfresh](https://github.com/blue-yonder/tsfresh)
is a tool for automatic extraction of relevant features from time series.

## References

https://www.kdnuggets.com/2018/08/automated-feature-engineering-will-change-machine-learning.html
