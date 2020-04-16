Status: published
Date: 2019-06-22 19:45:56
Author: Benjamin Du
Slug: spark-issue-application-submission-is-not-finished
Title: Spark Application Submission Is Not Finished
Category: Computer Science
Tags: programming, Spark, big data, issue

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Error Message

> Application submission is not finished, submitted application application__1524215324275_0081 is still in ...

![image](https://user-images.githubusercontent.com/824507/57563475-447c7e00-7353-11e9-8421-4b51e58ef18d.png)

## Possible Causes

The Resource Manager needs to write too much data to ZooKeeper and hit the buffer limit.

## Solution

Ask the Spark Cluster admin to increase the ZooKeeper buffer limit.
