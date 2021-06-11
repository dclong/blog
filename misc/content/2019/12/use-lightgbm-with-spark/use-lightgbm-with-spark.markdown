Status: published
Date: 2019-12-05 15:26:31
Author: Benjamin Du
Slug: use-lightgbm-with-spark
Title: Use LightGBM With Spark
Category: Computer Science
Tags: AI, data science, machine learning, Spark, big data, LightGBM, Java, Scala
Modified: 2020-03-05 15:26:31

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


https://github.com/Azure/mmlspark/blob/master/docs/lightgbm.md

[MMLSpark](https://github.com/Azure/mmlspark)
seems to be the best option to use train models using LightGBM on a Spark cluster.
Note that MMLSpark requires Scala 2.11, Spark 2.4+, and Python 3.5+.
You can use MMLSpark to run a LightGBM model on Spark too.
The method `loadNativeModelFromFile` (of a model)
to load a LightGMB model from a native LightGBM text file.
There is no need for you to convert the trained model to PMML or ONNX format.



https://www.reddit.com/r/datascience/comments/9w2qn8/deploying_a_lightgbm_model_with_spark/

https://towardsdatascience.com/build-xgboost-lightgbm-models-on-large-datasets-what-are-the-possible-solutions-bf882da2c27d

## Installation

https://mmlspark.blob.core.windows.net/website/index.html#install

## Tutorials and Examples

[LightGBM - Quantile Regression for Drug Discovery.ipynb](https://github.com/Azure/mmlspark/blob/master/notebooks/samples/LightGBM%20-%20Quantile%20Regression%20for%20Drug%20Discovery.ipynb)

https://github.com/Azure/mmlspark/tree/master/notebooks/samples


## References

https://towardsdatascience.com/build-xgboost-lightgbm-models-on-large-datasets-what-are-the-possible-solutions-bf882da2c27d

https://mmlspark.blob.core.windows.net/docs/1.0.0-rc1/scala/index.html#com.microsoft.ml.spark.lightgbm.LightGBMClassifier

https://mmlspark.blob.core.windows.net/docs/1.0.0-rc1/scala/index.html#com.microsoft.ml.spark.lightgbm.LightGBMRegressor

https://github.com/Azure/mmlspark/blob/master/notebooks/samples/LightGBM%20-%20Quantile%20Regression%20for%20Drug%20Discovery.ipynb

