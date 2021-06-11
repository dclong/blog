Status: published
Date: 2018-09-06 22:08:19
Author: Ben Chuanlong Du
Slug: elasticsearch-tips
Title: Tips on Elasticsearch
Category: Software
Tags: software, Elasticsearch, tips, search engine, database
Modified: 2020-05-06 22:08:19

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

https://www.elastic.co/guide/en/elasticsearch/reference/2.1/setup-service.html

## SQL Support 

1. Elasticsearch supports SQL syntax starting from version 6.3.
    There is also an unofficial SQL support of Elasticsearch by 
    [NLPchina/elasticsearch-sql](https://github.com/NLPchina/elasticsearch-sql)

## Links

https://www.elastic.co/downloads

## Aggregation

The after_key is equals to the last bucket returned in the response 
before any filtering that could be done by Pipeline aggregations. 
If all buckets are filtered/removed by a pipeline aggregation, 
the after_key will contain the last bucket before filtering.

## References

https://logz.io/blog/elasticsearch-sql-support/

https://medium.com/@mustafaakin/previewing-elasticsearch-6-3-sql-feature-2d3a1d60cab4

