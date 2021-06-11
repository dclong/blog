Status: published
Date: 2019-05-24 14:43:30
Author: Benjamin Du
Slug: spark-issue-file-not-found-exception
Title: Spark Issue: java.io.FileNotFoundException
Category: Computer Science
Tags: programming, Spark, issue, big data, error, file not found, Spark issue, FileNotFoundException
Modified: 2021-03-24 14:43:30

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

        ::bash
        --conf executor-memory=20G

## Cause 2

The shuffle file need to be stored locally for each executor. 
When doing very large shuffle, 
there are chances that the stored temp files exceed the hard limit restricted by yarn.
The local dir for storing the temp files are controlled by `yarn.nodemanager.local-dirs`, 
which is set to 12 folders on the Spark cluster.
The upper bound size for each directory is controlled by `yarn.nodemanager.localizer.cache.target-size-mb`, 
which is 10G by default.

## Solution 2

Users do not have authority to change the yarn properties,
however,
an workaround solution is to ask for more executors
which will give us more temporary directories for storing shuffling data.

    :::bash
    --num-executors 320
