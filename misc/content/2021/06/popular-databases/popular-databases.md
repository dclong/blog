Status: published
Date: 2021-06-10 10:33:02
Author: Benjamin Du
Slug: popular-databases
Title: Popular Databases
Category: Computer Science
Tags: Computer Science, programming, database, MySQL, ClickHouse, TiDB, neo4j, Elasticsearch, TiDB, TDengine, Redis
Modified: 2025-06-03 00:35:19

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The YouTube video
[How to Choose The Right Database](https://www.youtube.com/watch?v=kkeFE6iRfMM)
has great advices on how to choose the right databases.

## Types of Databases

- relational 
- non-relational 
  - key value database
    - document database
    - wide column database
  - graph database
  - search engine database
  - time series database

Advantages of Relational Databases
- consitency
- security
- ease of backup and recovery

Advantages of Non-relational Databases
- flexibility
- scalability
- cost of effectiveness

## Storage Format

- row storage
- columnar storage

columnar storage is good for analytical operations

## Comparison of Databases

<table style="width:100%">
  <tr>
    <th> Name </th>
    <th> Language </th>
    <th> Opensource/Free </th>
    <th> PACELC </th>
    <th> Advantages </th>
    <th> Disadvantages </th>
    <th> Comment </th>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/mysql">SQLite</a>
    </td>
    <th> SQL </th>
    <td> Opensource </td>
    <th> -/ELC </th>
    <td> </td>
    <td> </td>
    <td> the most popular embedded database </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/mysql">DuckDB</a>
    </td>
    <th> SQL </th>
    <td> Opensource </td>
    <th> -/ELC </th>
    <td> </td>
    <td> </td>
    <td> 
    - embedded OLAP
    - a good raising alternative to SQLite 
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/mysql">PostgreSQL</a>
    </td>
    <th> SQL </th>
    <td> Opensource </td>
    <th> PC/EC </th>
    <td> </td>
    <td> </td>
    <td> a better alternative to MySQL </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/mysql">MySQL</a>
    <a href="#footnote7">[1]</a>
    </td>
    <th> SQL </th>
    <td> Opensource </td>
    <th> PC/EC </th>
    <td> </td>
    <td> </td>
    <td> the most popular opensource RDBMS </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/ClickHouse/ClickHouse">ClickHouse</a>
    <a href="#footnote7">[2]</a>
    </td>
    <th> SQL </th>
    <td> Opensource </td>
    <th> </th>
    <td> OLAP for big data </td>
    <td> </td>
    <td> Has very good performance </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/pingcap/tidb">TiDB</a>
    <a href="#footnote7">[3]</a>
    </td>
    <th> SQL </th>
    <td> Opensource </td>
    <th> </th>
    <td> OLAP for big data </td>
    <td> </td>
    <td> good performance, support integration with Spark </td>
  </tr>
  <tr>
    <td> 
    <a href="">Cassandra</a>
    <a href="#footnote7">[1]</a>
    </td>
    <th> CQL (Cassandra <br> Query Language) </th>
    <td> Opensource </td>
    <th> PA/EL </th>
    <td> real-time </td>
    <td> no join </td>
    <td> </td>
  </tr>
  <tr>
    <td> 
    <a href="">HBase</a>
    <a href="#footnote7">[1]</a>
    </td>
    <th> </th>
    <td> Opensource </td>
    <th> PC/EC </th>
    <td> real-time </td>
    <td> no join </td>
    <td> </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/redis">Redis</a>
    <a href="#footnote7">[4]</a>
    </td>
    <th> DSL (hashmap <br> API-like) </th>
    <td> Opensource </td>
    <th> </th>
    <td> Distributed in-memory cache for real-time applications </td>
    <td> Queries or joins </td>
    <td> </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/neo4j">neo4j</a>
    <a href="#footnote7">[5]</a>
    </td>
    <th> Cypher (Graph <br> Query Language) </th>
    <td> Opensource </td>
    <th> </th>
    <td> Graph applications </td>
    <td> </td>
    <td> The most popular graph database </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/elastic">Elasticsearch</a>
    <a href="#footnote7">[6]</a>
    </td>
    <td> DSL, SQL </td>
    <td> Opensource </td>
    <th> </th>
    <td> Out-of-the-box search engine for large documents </td>
    <td> </td>
    <td> Designed as a search engine but also popularly used as a database </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/taosdata/TDengine">TDengine</a>
    <a href="#footnote7">[7]</a>
    </td>
    <td> SQL </td>
    <td> Opensource </td>
    <th> </th>
    <td> IoT </td>
    <td> </td>
    <td> IoT, good performance </td>
  </tr>
</table>

[2] [ClickHouse](https://github.com/ClickHouse/ClickHouse)
is an open-source column-oriented database management system 
that allows generating analytical data reports in real time.

## [yugabyte-db](https://github.com/YugaByte/yugabyte-db)
[yugabyte-db](https://github.com/YugaByte/yugabyte-db)

## [scylladb](https://github.com/scylladb/scylladb)
[Scylla](https://github.com/scylladb/scylladb)
is the real-time big data database 
that is API-compatible with Apache Cassandra and Amazon DynamoDB. 
Scylla embraces a shared-nothing approach that increases throughput and storage capacity 
to realize order-of-magnitude performance improvements and reduce hardware costs.

## MongoDB
MongoDB is a document-oriented, disk-based database optimized 
for operational simplicity, schema-free design and very large data volumes. 

## Distributed In-memory Cache

A distributed in-memory cache is essentially a distributed key-value storage/database.
You can think it as a hashmap over network.

[Redis](https://github.com/redis)
is the most popular in-memory cache which is implemented in C.
[memcached](https://github.com/memcached/memcached)
is another (not so popular) in-memory cache and is also implemented in C.
[pelikan](https://github.com/twitter/pelikan)
is Twitter's unified cache backend
which is implemented in C and Rust.

## References

- [How Discord Stores Trillions of Messages | Deep Dive](https://www.youtube.com/watch?v=xynXjChKkJc)

- [Relational vs. Non-Relational Databases](https://www.youtube.com/watch?v=E9AgJnsEvG4)

- [6.1 The Challenge of Distributed Database Systems](https://berb.github.io/diploma-thesis/original/061_challenge.html)

- [MySQL vs PostgreSQL -- Choose the Right Database for Your Project](https://developer.okta.com/blog/2019/07/19/mysql-vs-postgres)

- [Why Uber Engineering Switched from Postgres to MySQL](https://eng.uber.com/postgres-to-mysql-migration/)

- [Yes We Can! Distributed ACID Transactions with High Performance](https://blog.yugabyte.com/yes-we-can-distributed-acid-transactions-with-high-performance/)

- [A Beginner’s Guide to CAP Theorem for Data Engineering](https://www.analyticsvidhya.com/blog/2020/08/a-beginners-guide-to-cap-theorem-for-data-engineering/)
