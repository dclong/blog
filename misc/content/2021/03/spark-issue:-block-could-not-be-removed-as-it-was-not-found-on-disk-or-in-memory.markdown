Status: published
Date: 2021-03-22 10:27:09
Author: Benjamin Du
Slug: spark-issue:-block-could-not-be-removed-as-it-was-not-found-on-disk-or-in-memory
Title: Spark Issue: Block Could Not Be Removed as It Was Not Found on Disk or in Memory
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, block, remove, not found, disk, memory, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptom

Block rdd_123_456 could not be removed as it was not found on disk or in memory.

## Cause

Not enough memory to persist DataFrames (even if you used the default persist option `StorageLevel.MEMORY_AND_DISK`).

## Possible Solutions

1. Increase memories.

2. Persist to disk only (at a slight lower performance).

3. Do not persist DataFrames (at the cost of lower performance).

