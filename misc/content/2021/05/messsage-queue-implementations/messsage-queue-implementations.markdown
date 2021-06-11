Status: published
Date: 2021-05-26 10:32:39
Author: Benjamin Du
Slug: messsage-queue-implementations
Title: Messsage Queue Implementations
Category: Computer Science
Tags: Computer Science, programming, message, queue, Kafka, AMQP, Redis, ZooKeeper, celery, memcached
Modified: 2021-05-26 10:32:39
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Kafka seems to be the most popular message queue currently. 
Redis and memcached are more suitaable for situations where you need cache in memory. 

## Protocols
[AMQP](https://www.amqp.org/)
is the Advanced Message Queuing Protocol, 
an open standard protocol for message orientation, queuing, routing, reliability and security. 
The RabbitMQ messaging server is the most popular implementation of AMQP.

## Servers

### Kafka

Kafka leverages ZooKeeper.

### [celery](https://github.com/celery/celery)
[celery](https://github.com/celery/celery)
is a simple, flexible, and reliable distributed system to process vast amounts of messages, 
while providing operations with the tools required to maintain such a system.

### RabbitMQ

### Redis

## Comparisons 

### Kafka vs RabbitMQ 
Kafka is an overkill when you need to process only a small amount of messages per day (up to several thousand). 
Kafka is designed to cope with the high load. 
Use traditional message queues like RabbitMQ when you don't have a lot of data. 

### Kafka vs Redis

[Difference between Redis and Kafka](https://stackoverflow.com/questions/37990784/difference-between-redis-and-kafka)

## Clients

### [rq](https://github.com/rq/rq)
[rq](https://github.com/rq/rq) (Redis Queue) is a simple Python library 
for queueing jobs and processing them in the background with workers. 
It is backed by Redis and it is designed to have a low barrier to entry. 
It should be integrated in your web stack easily.

### [kombu](https://github.com/celery/kombu)
[kombu](https://github.com/celery/kombu)
The aim of Kombu is to make messaging in Python as easy as possible 
by providing an idiomatic high-level interface for the AMQ protocol, 
and also provide proven and tested solutions to common messaging problems.

### [pika](https://github.com/pika/pika)
[pika](https://github.com/pika/pika)
is a pure-Python implementation of the AMQP 0-9-1 protocol including RabbitMQ's extensions.


## References 

[Difference between Redis and Kafka](https://stackoverflow.com/questions/37990784/difference-between-redis-and-kafka)

[REDIS VS MEMCACHED: WHICH ONE TO CHOOSE?](https://www.imaginarycloud.com/blog/redis-vs-memcached/)