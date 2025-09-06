Status: published
Date: 2019-12-01 10:06:27
Author: Benjamin Du
Slug: python-sklearn-tips
Title: Tips on Scikit-Learn
Category: AI
Tags: AI, data science, machine learning, Scikit-learn, sklearn, pipeline
Modified: 2021-09-16 21:12:30

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Cross validation in scikit-learn supports pipeline in addition to vanilla models.
    Please refer to 
    [Cross Validation Pipeline](https://chrisalbon.com/machine_learning/model_evaluation/cross_validation_pipeline/)
    for more details.

2. [Label encoding](https://scikit-learn.org/stable/modules/preprocessing_targets.html#label-encoding)
    is an easy way to convert a categorical response/target variable to a numeric one and back to the raw value space.
    For transform of response/target varible in regression,
    please refer to [Transforming Target in Tegression](https://scikit-learn.org/stable/modules/compose.html#transforming-target-in-regression).

3. [Skorch](https://github.com/skorch-dev/skorch)

## Metrics

- [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html)

- [precision_recall_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve)

- [average_precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score)

## References

https://scikit-learn.org/stable/modules/compose.html#transforming-target-in-regression

[Split a Dataset into Train and Test Datasets in Python]( https://www.legendu.net/misc/blog/python-ai-split-dataset ) 
