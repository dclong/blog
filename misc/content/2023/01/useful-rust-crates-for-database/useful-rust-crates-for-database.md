Status: published
Date: 2023-01-13 15:46:22
Modified: 2025-06-04 14:31:23
Author: Benjamin Du
Slug: useful-rust-crates-for-database
Title: Useful Rust Crates for Database
Category: Computer Science
Tags: Computer Science, programming, Rust, database, crate, SQL, big data, streaming

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## [Neon](https://github.com/neondatabase/neon)
[Neon](https://github.com/neondatabase/neon)
is a serverless open-source alternative to AWS Aurora Postgres. 
It separates storage and compute and substitutes the PostgreSQL storage layer 
by redistributing data across a cluster of nodes.

## [sqlx](https://github.com/launchbadge/sqlx)
[SQLx](HTTPS://GITHUB.COM/LAUNCHBADGE/SQLX)
is an async, pure Rust† SQL crate featuring compile-time checked queries without a DSL.
Supports PostgreSQL, MySQL, and SQLite.

## [gluesql](https://github.com/gluesql/gluesql)
[GlueSQL](https://github.com/gluesql/gluesql)
is an open source SQL database engine fully written in Rust 
with pure functional execution layer, 
easily swappable storage and web assembly support!

## [surrealdb](https://github.com/surrealdb/surrealdb)
[SurrealDB](https://github.com/surrealdb/surrealdb)
is an end-to-end cloud native database for web, mobile, serverless, Jamstack, backend, and traditional applications. 
SurrealDB reduces the development time of modern applications by simplifying your database and API stack, 
removing the need for most server-side components, 
and allowing you to build secure, performant apps quicker and cheaper. 
SurrealDB acts as both a database and a modern, real-time, collaborative API backend layer. 
SurrealDB can run as a single server or in a highly-available, 
highly-scalable distributed mode, 
with support for SQL querying from client devices, GraphQL, ACID transactions, WebSocket connections, structured 
and unstructured data, graph querying, full-text indexing, geospatial querying, and row-by-row permissions-based access.

https://github.com/quickwit-oss/quickwit

https://github.com/cberner/redb

https://github.com/quickwit-oss/tantivy

## [indradb](https://github.com/indradb/indradb)
[indradb](https://github.com/indradb/indradb)
is a graph database written in rust.

## [oxigraph/](https://github.com/oxigraph/oxigraph/)
[oxigraph/](https://github.com/oxigraph/oxigraph/)
Oxigraph is a graph database implementing the SPARQL standard.
Its goal is to provide a compliant, safe, 
and fast graph database based on the RocksDB and Sled key-value stores. 
It is written in Rust. 
It also provides a set of utility functions for reading, writing, and processing RDF files.
Oxigraph is in heavy development and SPARQL query evaluation has not been optimized yet.

### [skytable](https://github.com/skytable/skytable)
[Skytable](https://github.com/skytable/skytable)
is a free and open-source NoSQL database 
that aims to provide flexible data modeling at scale. 
Simplicity, performance and flexibility are the guiding design principles.

### [bolt-rs](https://github.com/lucis-fluxum/bolt-rs)
[bolt-rs](https://github.com/lucis-fluxum/bolt-rs)
aims to provide a comprehensive set of libraries 
that allow for interaction with graph database servers 
that support the Bolt protocol, namely, Neo4j. 
This set of libraries allows interacting with servers 
supporting versions 1 through 4.1 of the protocol, 
which includes Neo4j 3.1 through 4.2.

### [neo4rs](https://github.com/yehohanan7/neo4rs)
[Neo4rs](https://github.com/yehohanan7/neo4rs)
is a Neo4j rust driver implemented using bolt specification.
This driver is compatible with neo4j 4.x versions

## [qdrant](https://github.com/qdrant/qdrant)
[Qdrant](https://github.com/qdrant/qdrant)
is a vector similarity search engine and vector database. 
It provides a production-ready service with a convenient API 
to store, search, and manage points - vectors with an additional payload. 
Qdrant is tailored to extended filtering support. 
It makes it useful for all sorts of neural-network or semantic-based matching, faceted search, and other applications.

## Embedded Databases

https://github.com/tursodatabase/limbo
Limbo is a project to build the modern evolution of SQLite.

### [rusqlite](https://crates.io/crates/rusqlite)
[rusqlite](https://crates.io/crates/rusqlite)
is an ergonomic wrapper for SQLite.

SurrealDB
https://surrealdb.com/docs/surrealdb/embedding
can be embedded.

https://github.com/PoloDB/PoloDB
PoloDB is an embedded document database.

## [sled](https://github.com/spacejam/sled)
[sled](https://github.com/spacejam/sled)
is an embedded key-value pair databases written in Rust.

https://github.com/vincent-herlemont/native_db
Drop-in embedded database in Rust

https://github.com/tonbo-io/tonbo
A portable embedded database using Arrow.


## OLAP Specific Databases

### [seafowl](https://github.com/splitgraph/seafowl)
[Seafowl](https://github.com/splitgraph/seafowl)
is an analytical database for modern data-driven Web applications.
Its CDN and HTTP cache-friendly query execution API 
lets you deliver data to your visualizations, 
dashboards and notebooks by running SQL straight from the user's browser.

## Time Series Databases 

### [ceresdb](https://github.com/CeresDB/ceresdb)
[CeresDB](https://github.com/CeresDB/ceresdb)
is a high-performance, distributed, cloud native time-series database.

### [cnosdb](https://github.com/cnosdb/cnosdb)
[CnosDB](https://github.com/cnosdb/cnosdb)
An Open Source Distributed Time Series Database with high performance, high compression ratio and high usability.

### [influxdb_iox](https://github.com/influxdata/influxdb_iox)
[Influxdb IOX](https://github.com/influxdata/influxdb_iox)
(short for Iron Oxide, pronounced InfluxDB "eye-ox") 
is the future core of InfluxDB, an open source time series database. 
The name is in homage to Rust, 
the language this project is written in. 
It is built using Apache Arrow and DataFusion among other things. 

## Storage
### [datenlord](https://github.com/datenlord/datenlord)
[DatenLord](https://github.com/datenlord/datenlord)
is a next-generation cloud-native distributed storage platform, 
which aims to meet the performance-critical storage needs from next-generation cloud-native applications, such as microservice, serverless, AI, etc. On one hand, DatenLord is designed to be a cloud-native storage system, which itself is distributed, fault-tolerant, and graceful upgrade. These cloud-native features make DatenLord easy to use and easy to maintain. On the other hand, DatenLord is designed as an application-orientated storage system, in that DatenLord is optimized for many performance-critical scenarios, such as databases, AI machine learning, big data. Meanwhile, DatenLord provides high-performance storage service for containers, which facilitates stateful applications running on top of Kubernetes (K8S). The high performance of DatenLord is achieved by leveraging the most recent technology revolution in hardware and software, such as NVMe, non-volatile memory, asynchronous programming, and the native Linux asynchronous IO support.
## Log Storage

openobserve
https://github.com/openobserve/openobserve
OpenObserve is a cloud native observability platform built specifically for logs, metrics, traces and analytics designed to work at petabyte scale.
🚀 10x easier, 🚀 140x lower storage cost, 🚀 high performance, 🚀 petabyte scale - Elasticsearch/Splunk/Datadog alternative for 🚀 (logs, metrics, traces).




### [parseable](https://github.com/parseablehq/parseable)
[Parseable](https://github.com/parseablehq/parseable)
is a lightweight, cloud native log observability engine. 
It can use either a local drive or S3 (and compatible stores) for backend data storage.
Parseable is written in Rust and uses Apache Arrow and Parquet as underlying data structures. 
Additionally, it uses a simple, index-free mechanism to organize and query data allowing low latency, 
and high throughput ingestion and query.

### [zincobserve](https://github.com/zinclabs/zincobserve)
[ZincObserve](https://github.com/zinclabs/zincobserve)
is a cloud native observability platform built specifically 
for logs, metrics, traces and analytics designed to work at petabyte scale.
It is very simple and easy to operate as opposed to Elasticsearch 
which requires a couple dozen knobs to understand and tune 
which you can get up and running in under 2 minutes.
It is a drop-in replacement for Elasticsearch 
if you are just ingesting data using APIs 
and searching using kibana (Kibana is not supported nor required with ZincObserve. 
ZincObserve provides its own UI which does not require separate installation unlike kibana).

## [minio-rs](https://github.com/minio/minio-rs)
[MinIO Rust SDK](https://github.com/minio/minio-rs)
is Simple Storage Service (aka S3) client 
to perform bucket and object operations to any Amazon S3 compatible object storage service.

## Cache
https://github.com/06chaynes/http-cache
A caching middleware that follows HTTP caching rules
A caching middleware that follows HTTP caching rules, thanks to http-cache-semantics. By default, it uses cacache as the backend cache manager.



## Data Layer 

https://github.com/vectordotdev/vector
Vector is a high-performance, end-to-end (agent & aggregator) observability data pipeline that puts you in control of your observability data. Collect, transform, and route all your logs, metrics, and traces to any vendors you want today and any other vendors you may want tomorrow. Vector enables dramatic cost reduction, novel data enrichment, and data security where you need it, not where it is most convenient for your vendors. Additionally, it is open source and up to 10x faster than every alternative in the space.



https://github.com/grafbase/grafbase

### [Dozer](https://github.com/getdozer/dozer)
[Dozer](https://github.com/getdozer/dozer)
makes it easy to build low-latency data APIs (gRPC and REST) from any data source. 
Data is transformed on the fly 
using Dozer's reactive SQL engine and stored in a high-performance cache 
to offer the best possible experience. 
Dozer is useful for quickly building data products.


### [OpenDal](https://github.com/apache/incubator-opendal)
[Apache OpenDal](https://github.com/apache/incubator-opendal)
makes data accessing freely, painlessly, and efficiently.

### [cube.js](https://github.com/cube-js/cube.js)
[cube.js](https://github.com/cube-js/cube.js)
is the semantic layer for building data applications. 
It helps data engineers and application developers access data from modern data stores, 
organize it into consistent definitions, and deliver it to every application.

## Database Clients for Rust 

Please refer to 
[Database Clients for Rust](https://www.legendu.net/misc/blog/querying-a-sql-database-in-rust)
for details
.

## Metrics and Monitoring

https://github.com/frolicorg/frolic
Frolic is an open source project (written in Rust) to build customer facing dashboards 10x faster. You can directly connect your database to the project and use ready made APIs to query data and create customer facing dashboards. You can also use frolic-react for your UI along with frolic to create full stack dashboards much faster.



## Command-line Tools
https://github.com/timvw/qv
A simply CLI to quickly view your data. Powered by DataFusion.


## Big Data

- [rewrite-bigdata-in-rust/RBIR](https://github.com/rewrite-bigdata-in-rust/RBIR)

    A collection of RBIR projects and posts for anyone interested in joining this journey.

- [Rust for Big Data and Parallel Processing Applications](https://www.xenonstack.com/blog/rust-big-data-applications)

### [datafuse](https://github.com/datafuselabs/datafuse)

### [fluvio](https://github.com/infinyon/fluvio)

### [DataBend](https://github.com/datafuselabs/databend)

### [kamu-cli](https://github.com/kamu-data/kamu-cli)

### [datafusion](http://www.legendu.net/misc/blog/tips-on-datafusion)

### [ballista](https://github.com/apache/arrow-ballista)

### [Polars](http://www.legendu.net/misc/blog/tips-on-polars)   

## References

- [Difference between Apache parquet and arrow](https://stackoverflow.com/questions/56472727/difference-between-apache-parquet-and-arrow)

- https://arrow.apache.org/

- [Database-like ops benchmark](https://h2oai.github.io/db-benchmark/)

- [Rust For Big Data!](https://blog.devgenius.io/rust-for-big-data-40fc48df9703)

- [Cube: Creating a Semantic Data Layer!](https://jlgjosue.medium.com/cube-creating-a-semantic-data-layer-a947fd0b6a5c)
