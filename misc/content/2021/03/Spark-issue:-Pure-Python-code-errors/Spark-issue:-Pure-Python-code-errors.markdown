Status: published
Date: 2021-03-22 10:18:22
Author: Benjamin Du
Slug: Spark-issue:-Pure-Python-code-errors
Title: Spark Issue: Pure Python Code Errors
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, big data, Spark issue, Python, error, exception
Modified: 2021-03-22 10:18:22

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

This post collects some typical pure Python errors in PySpark applications.

## Symptom 1
object has no attribute

## Solution 1
Fix the attribute name.


## Symptom 2
No such file or directory

## Solution 2
Correct the path to the file/directory or upload the file using `--file` of the spark-submit command.


## Symptom 3
error: the following arguments are required

## Solution 3
Add the required arguments to the command invoking your Python script. 


## Symptom 4
error: unrecognized arguments

## Solution 4
Correct tthe argument name or remove non-exist arguments from the command invoking your Python script.


## Symptom 5
error: argument
## Solution 5


## Symptom 6
ModuleNotFoundError: No module named

## Solution 6
Fix typo in the module name or install missing modules.

## Symptom 7
SyntaxError: invalid syntax

## Solution 7
Fix syntax error in your Python script.

## Symptom 8
NameError: name .* is not defined

## Solution 8
Fix typo in variable/function name or import/define it.