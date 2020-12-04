Status: published
Date: 2020-12-04 12:29:38
Author: Ben Chuanlong Du
Title: Hyper Parameter Tuning and Automatical Machine Learning
Slug: ai-hyper-parameter-auto-ml
Category: AI
Tags: AI, machine learning, framework, AutoML, mlflow, Lugwid, Optuna, turicreate, PyCaret

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Methodology

hyper-parameter tuning, 
grid search
bayesian optimization 
evolutionary algorithms
genetic programming
cross validation
k-fold 
[Neural Architecture Search with Reinforcement Learning](https://openreview.net/pdf?id=r1Ue8Hcxg)

## Libraries

### [Optuna](https://github.com/optuna/optuna)

### auto-sklearn

### [Ludwig](https://github.com/uber/ludwig)

Ludwig is a toolbox that allows to train and evaluate deep learning models without the need to write code.

### [turicreate](https://github.com/apple/turicreate)

Turi Create simplifies the development of custom machine learning models. 
You don't have to be a machine learning expert 
to add recommendations, object detection, image classification, image similarity or activity classification to your app.

- Easy-to-use: Focus on tasks instead of algorithms
- Visual: Built-in, streaming visualizations to explore your data
- Flexible: Supports text, images, audio, video and sensor data
- Fast and Scalable: Work with large datasets on a single machine
- Ready To Deploy: Export models to Core ML for use in iOS, macOS, watchOS, and tvOS apps

### [PyCaret](https://github.com/pycaret/pycaret)

PyCaret is an open source `low-code` machine learning library in Python 
that aims to reduce the hypothesis to insights cycle time in a ML experiment. 
It enables data scientists to perform end-to-end experiments quickly and efficiently. 
In comparison with the other open source machine learning libraries, 
PyCaret is an alternate low-code library 
that can be used to perform complex machine learning tasks with only few lines of code. 
PyCaret is essentially a Python wrapper 
around several machine learning libraries and frameworks 
such as `scikit-learn`, `XGBoost`, `Microsoft LightGBM`, `spaCy` and many more. 

### [autogluon](https://github.com/awslabs/autogluon)

AutoGluon automates machine learning tasks enabling you 
to easily achieve strong predictive performance in your applications. 
With just a few lines of code, 
you can train and deploy high-accuracy deep learning models on tabular, image, and text data.

### Apache Ray Tune

### H2O AutoML

Python: H2OAutoML(...)

### Driverless AI


### tpot looks like a good one

## Platforms/Framework

[Google Cloud AutoML](https://cloud.google.com/automl/)


## Shared Resources of Models

[TensorFlow Hub](https://www.tensorflow.org/hub)

[Google AI Hub](https://cloud.google.com/ai-hub/)

[DAGsHub](https://dagshub.com/)
DAGsHub is a web platform for data version control and collaboration for data scientists and machine learning engineers.
It is like GitHub for data science and machine learning.

[ml-metadata](https://github.com/google/ml-metadata)

[mlflow](https://github.com/mlflow/mlflow)

Kaggle

transformers

## Experiment Tracking
[neptune-client](https://github.com/neptune-ai/neptune-client)

wandb, fitlog, runx

## Examples 

https://github.com/h2oai/driverlessai-recipes

## References

https://arxiv.org/pdf/1908.00709v1.pdf

https://towardsdatascience.com/an-example-of-hyperparameter-optimization-on-xgboost-lightgbm-and-catboost-using-hyperopt-12bc41a271e

