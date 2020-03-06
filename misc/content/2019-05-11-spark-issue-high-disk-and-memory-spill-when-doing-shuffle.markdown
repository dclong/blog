Status: published
Date: 2019-12-05 14:51:10
Author: Benjamin Du
Slug: spark-issue-high-disk-and-memory-spill-when-doing-shuffle
Title: Spark Issue: High Disk and Memory Spill When Doing Shuffle
Category: Computer Science
Tags: programming, Spark, issue, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Symtom

High disk and memory spill when doing shuffle.

## Cause

Insufficient executor memory (You can monitor this spill metrics from Spark UI)

## Solution

1. Increase executor memory: --executor-memory "4096M"

2. For jobs that don't need to persist data in memory we can reduce the cache storage size and enlarge the memory portion for Shuffle

        :::bash
        --conf spark.shuffle.memoryFraction=0.4 
        --conf spark.storage.memoryFraction=0.1 
