Status: published
Date: 2021-03-22 10:12:17
Author: Benjamin Du
Slug: spark-issue:-_pickle.PicklingError:-args[0]-from-__newobj__-args-has-the-wrong-class
Title: Spark Issue: _Pickle.Picklingerror: Args[0] from __Newobj__ Args Has the Wrong Class
Category: Computer Science
Tags: Computer Science, programming, Spark, big data, issue, Pickle, serialization, deserialization, Spark issue
Modified: 2021-03-22 10:12:17

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Please refer to
[Spark Issue: Task Not Serializable](http://www.legendu.net/misc/blog/spark-issue-task-not-serializable)
for a similar serialization issue in Spark/Scala.

## Symptom

## Cause

For example,
if you have the following import 

    from nltk.corpus import stopwords

then calling the following in UDF or pandas UDFs might cause this issue. 

    stopwords.words("english")

## Solution 

Simply move `stopwords.words("english")` out of UDFs and/or pandas UDFs to define a global variable. 



## References 

[关于python：Spark-Submit出现“ Pickling错误”“ _pickle.PicklingError：__newobj__ args中的args [0]具有错误的类”](https://www.codenong.com/46878186/)

[_pickle.PicklingError: args[0] from __newobj__ args has the wrong class from cloudpickle.py](https://issues.apache.org/jira/browse/SPARK-22711)