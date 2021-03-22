Status: published
Date: 2021-03-22 10:24:16
Author: Benjamin Du
Slug: org.apache.hadoop.security.AccessControlException:-Permission-denied
Title: Org.Apache.Hadoop.Security.Accesscontrolexception: Permission Denied
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, big data, Spark issue, AccessControlException, permission, denied

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Symptom

org.apache.hadoop.security.AccessControlException: Permission denied ...

## Cause
The user of the Spark application has no permission to the query a table or HDFS path.

## Solution

Apply to access to the table to query.