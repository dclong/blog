Status: published
Date: 2020-12-03 01:26:29
Author: Benjamin Du
Slug: tips-on-lightgbm
Title: Tips on LightGBM
Category: AI
Tags: AI, data science, machine learning, LightGBM

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. It is strongly suggested that you specify categorical features manually
    as LightGBM only treat unordered categorial columns as categorical features by default.

		:::bash
		lgb_train = lgb.Dataset(x_train, y_train, feature_name=features,
			categorical_feature=categorical_features)

    It is also suggested that you encode a categorical variable 
    as consecutive integers starting from zero. 
    Be aware that all negative values in categorical features are treated as missing values. 
    The output cannot be monotonically constrained with respect to a categorical feature.

2. The sklearn wrapper of LightGBM lag behind the development of sklearn. 
    Be aware of the latest supported version of sklearn when you use sklearn wrapper of LightGBM.
    It is suggested that you the original API of LightGBM to avoid version issues.

3. It is suggested that you always specify a evaluation set when you call the function `train`.

2. LightGBM supports distributed training on multiple machines (without Spark).

    https://github.com/microsoft/LightGBM/tree/master/examples/parallel_learning


[Parameters](https://lightgbm.readthedocs.io/en/latest/Parameters.html#parameters)
[Metric Parameters](https://lightgbm.readthedocs.io/en/latest/Parameters.html#metric-parameters)

## Hyper Parameter Tuning

[Optuna](http://www.legendu.net/misc/blog/tips-on-optuna)
is a good framework for tuning hyper parameters.

https://sites.google.com/view/lauraepp/parameters

https://lightgbm.readthedocs.io/en/latest/Parameters.html

## GPU 

https://lightgbm.readthedocs.io/en/latest/GPU-Tutorial.html

## References

[LightGMB Benchmark](https://lightgbm.readthedocs.io/en/latest/Experiments.html)

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.Dataset.html#lightgbm-dataset

https://lightgbm.readthedocs.io/en/latest/_modules/lightgbm/sklearn.html

https://www.kaggle.com/nicapotato/multi-class-lgbm-cv-and-seed-diversification

https://sefiks.com/2018/10/13/a-gentle-introduction-to-lightgbm-for-applied-machine-learning/

https://github.com/microsoft/LightGBM/blob/master/examples/python-guide/sklearn_example.py

https://github.com/microsoft/LightGBM/tree/master/examples/python-guide

https://www.kaggle.com/tapioca/multiclass-lightgbm

https://lightgbm.readthedocs.io/en/latest/Features.html

https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.train.html

