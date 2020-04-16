Status: published
Date: 2019-05-11 02:50:52
Author: Benjamin Du
Slug: spark-issue-data-skew-on-shuffle-phase
Title: Spark Issue Data Skew on Shuffle Phase
Category: Computer Science
Tags: programming

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptom

org.apache.spark.shuffle.FetchFailedException: Too large frame: 2200180718
Caused by: java.lang.IllegalArgumentException: Too large frame: 2200289525
at org.spark_project.guava.base.Preconditions.checkArgument(Preconditions.java:119)

## Reason

There is data skew in some column(s).

## Solution 

1. split and broadcast

2. add another random column to help reduce skew

        joinWithoutSkew(df1:DataFrame, df2:DataFrame, joinCols:Array[Column], duplicationNum:Int): DateFrame = {
          ...
        }

    df1: bigtable, append random num to the join columns. keep the row count no change.
    df2: smalltable, duplicate df2 by duplicationNum times and got df2Duplicate, 
    df2Duplicate.count = df2.count * duplicationNum
    append random num to the join columns.
    joinCols: the joinCols to be join on
    duplicationNum: duplication nums of df2
