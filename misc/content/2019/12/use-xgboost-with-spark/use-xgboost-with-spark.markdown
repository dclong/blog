Status: published
Date: 2020-03-17 11:37:33
Author: Benjamin Du
Slug: use-xgboost-with-spark
Title: Use XGBoost With Spark
Category: AI
Tags: AI, data science, machine learning, XGBoost, Spark
Modified: 2020-03-17 11:37:33

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

The split-by-leaf mode (`grow_policy="lossguide"`) is not supported in distributed training,
which makes XGBoost4J on Spark much slower than LightGBM on Spark.

## XGBoost with Spark

https://towardsdatascience.com/build-xgboost-lightgbm-models-on-large-datasets-what-are-the-possible-solutions-bf882da2c27d

https://xgboost.readthedocs.io/en/latest/jvm/xgboost4j_spark_tutorial.html

https://xgboost.ai/2016/10/26/a-full-integration-of-xgboost-and-spark.html

https://databricks.com/session/building-a-unified-data-pipeline-with-apache-spark-and-xgboost

https://medium.com/cloudzone/xgboost-distributed-training-and-predicting-with-apache-spark-1127cdfb31ae

https://news.developer.nvidia.com/gpu-accelerated-spark-xgboost/

https://towardsdatascience.com/pyspark-and-xgboost-integration-tested-on-the-kaggle-titanic-dataset-4e75a568bdb

https://www.kdnuggets.com/2016/03/xgboost-implementing-winningest-kaggle-algorithm-spark-flink.html

