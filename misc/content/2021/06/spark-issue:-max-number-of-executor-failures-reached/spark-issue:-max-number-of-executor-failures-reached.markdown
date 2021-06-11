Status: published
Date: 2021-06-09 14:44:30
Author: Benjamin Du
Slug: spark-issue:-max-number-of-executor-failures-reached
Title: Spark Issue: Max Number of Executor Failures Reached
Category: Computer Science
Tags: Computer Science, programming, Spark, big data, Spark issue, executor, failures
Modified: 2021-06-09 14:44:30
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

21/06/01 15:03:28 INFO ApplicationMaster: Final app status: FAILED, exitCode: 11, (reason: Max number of executor failures (6) reached)

## Possible Causes

The option `spark.yarn.max.executor.failures`
is set to a value which is too small.
In my case,
I believe the Hadoop team misconfigured the option when they update the version of Spark.

## Possible Solutions

By default,
`spark.yarn.max.executor.failures`
is set to $numExecutors \times 2$.
A simple fix is to manually set 
`spark.yarn.max.executor.failures`
to $numExecutors \times 2$.
