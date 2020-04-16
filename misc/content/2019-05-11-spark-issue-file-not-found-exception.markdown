Status: published
Date: 2019-05-11 02:50:52
Author: Benjamin Du
Slug: spark-issue-file-not-found-exception
Title: Spark Issue File Not Found Exception
Category: Computer Science
Tags: programming, Spark, issue, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptom

### Symptom 1

15/12/10 07:44:21 ERROR shuffle.OneForOneBlockFetcher: Failed while starting block fetches

java.lang.RuntimeException: java.io.FileNotFoundException: 
/hadoop/1/scratch/local/usercache/dclong/appcache/application_1447357188616_340392/blockmgr-e13c06e0-e52b-467c-84ef-7df716199dce/17/shuffle_0_1564_0.index 
(No such file or directory)
    at java.io.FileInputStream.open(Native Method)


### Symptom 2

15/12/16 18:17:35 ERROR shuffle.OneForOneBlockFetcher: Failed while starting block fetches
java.io.IOException: Connection from 10.115.82.103:42646 closed

## Cause 1

Insufficient memory for executor during the shuffle period, 
so the executor container is being killed by Yarn. 
In this case the executor is either unreachable, 
or the temp files (intermediate file stored locally for shuffle) are removed.

## Solution 1

1. Enlarge the executor memory

## Cause 2

The shuffle file need to be stored locally for each executor, 
when doing very large shuffle, 
there are chances that the stored temp files exceed the hard limit restricted by yarn

The local dir that used to store the temp files are controlled by yarn.nodemanager.local-dirs, which is set to 12 folders on the Spark cluster.

The upper bound size for each dir is controlled by yarn.nodemanager.localizer.cache.target-size-mb, which is 10G by default  (not set on the cluster)

## Solution 2

Since we don't have authority to change the yarn properties, 
we can walk around the issue by enlarging the cluster size. 
In this case we have more temp folder capacity. 
For example, 
to compute 30-day google live item response, we need around 300 executors to resolve the issue

    --num-executors 320
