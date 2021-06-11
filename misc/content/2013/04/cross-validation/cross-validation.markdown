Status: published
Author: Ben Chuanlong Du
Date: 2013-04-03 00:00:00
Title: Cross Validation in Machine Learning
Slug: cross-validation-machine-learning
Category: AI
Tags: AI, data science, machine learning, cross validation
Modified: 2013-04-03 00:00:00

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
## Training and Testing Data Set

- good when you have large amount of data

- usually use 1/5 to 1/3 of the data as testing data set.

## K-fold CV

- suitable when you have medium number of data

- K=10 is popular

- computationally extensive

## Leave-k-out CV

- Use this way only when you have very limited number of data.

- Leave-1-out is a specially case of the K-fold CV.

- computationally very extensive

## Some Rules:

- 10 times number of parameters, probably in good shape

- 20 times number of prameters, usually perfect good
