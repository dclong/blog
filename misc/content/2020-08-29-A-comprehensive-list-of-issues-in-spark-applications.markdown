Status: published
Date: 2020-08-29 22:49:49
Author: Benjamin Du
Slug: A-comprehensive-list-of-issues-in-spark-applications
Title: A Comprehensive List of Common Issues in Spark Applications
Category: Computer Science
Tags: Computer Science, Spark, issue, big data, error

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Debugging Tips 

### Spark/Hadoop Applications UI

1. The `Jobs` tab (default) to check jobs stages, number of jobs, etc. 
2. The `SQL` tab contains all Spark SQLs in your Spark application.
    you can click on each SQL to see visualization of its execuation plans.
    This visualiation of execuation plan has more information than the one in the `Jobs` tab.
    Notice that statistics after each stage will be update in this visualiation
    as the Spark application runs.
    This is extremely helpful for 
        - identifying unexpected behaviors of Spark job
        - better understanding of complexity of your Spark job 
        - tuning parameters to speed up your Spark application 

### Debug Your Spark Application 

Below a few things to check while you debug your Spark applications.

1. Make sure the number of jobs is as expected. 

2. Make sure the job type is as expected. 
    This is critical for improve the performance of your Spark application.
    For example, 
    you might expect Spark to use BroadcastHashJoin but it actually used SortMergeJoin.

## List of Common Issues 

http://www.legendu.net/misc/blog/spark-issue-duplicated-partitions/

http://www.legendu.net/misc/blog/spark-issue-mac-spark-shell-error-initializing-sparkcontext/

http://www.legendu.net/misc/blog/spark-issues-and-solutions/

http://www.legendu.net/misc/blog/spark-issue-too-large-table-for-auto-BroadcastHashJoin/

http://www.legendu.net/misc/blog/spark-issue-executor-out-of-memory-when-running-large-table-join/

http://www.legendu.net/misc/blog/spark-issue-cannot-create-a-path-from-an-empty-string/

http://www.legendu.net/misc/blog/spark-issue-InvalidInputException-for-some-Hive-data-partiions/

http://www.legendu.net/misc/blog/spark-issue-task-not-serializable/

http://www.legendu.net/misc/blog/spark-issue-application-submission-is-not-finished/

http://www.legendu.net/misc/blog/spark-issue-file-not-found-exception/

http://www.legendu.net/misc/blog/spark-issue-java.lang.OutOfMemoryError/

http://www.legendu.net/misc/blog/spark-issue-a-master-url-must-be-set-in-your-configuration/

http://www.legendu.net/misc/blog/spark-issue-high-disk-and-memory-spill-when-doing-shuffle/

http://www.legendu.net/misc/blog/spark-issue-data-skew-on-shuffle-phase/

http://www.legendu.net/misc/blog/spark-issue-timeout-when-communicate-with-driver-during-shuffle/

http://www.legendu.net/misc/blog/spark-issue-table-not-found/

http://www.legendu.net/misc/blog/spark-unable-to-find-encoder-type-issue/

http://www.legendu.net/misc/blog/spark-issue-native-memory-usage-exceed-memoryOverhead/

http://www.legendu.net/misc/blog/spark-issue-too-many-containers-asked/
