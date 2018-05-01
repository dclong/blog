UUID: d17b677f-1974-4936-b77f-d3bc12b6e03d
Status: published
Date: 2017-08-26 21:28:53
Author: Ben Chuanlong Du
Slug: zeppelin-tips
Title: Zeppelin Tips
Category: Software
Tags: software, zeppelin, notebook

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. Zepplin notebook directory,
if you want to move notebooks to another machine,
must place them into the notebook directory.


2. %sh interpreter is useful!!!


I observe that Hive in Zeppelin is much faster than Spark in Zeppelin.
Why is this?


https://zeppelin.apache.org/docs/latest/interpreter/spark.html#zeppelincontext

Zeppelin context is interesting ...

Previous livy session is expired, new livy session is created. Paragraphs that depend on this paragraph need to be re-executed!



How to set up the resource to use for computation?
And how can I use Hive output in Scala?
how to manually save a notebook?

livy session expired, how to make it alive for a longer time?

Jobs in Zeppelin are not reliable as compared to running them directly via cli.
It is suggested that you use cli more rather than Zeppelin.
Of course, Zeppelin has the advantage of having everything together ...


http://fedulov.website/2015/10/16/export-apache-zeppelin-notebooks/



1. need to set queue in properties.

2. apply for access to spades!!!

https://wiki.vip.corp.ebay.com/display/HADOOP/Zeppelin

https://wiki.vip.corp.ebay.com/display/HADOOP/Getting+Started+with+Zeppelin


1. I verify that clone/rename won't override existing notebook with the same name.

Configuration
https://zeppelin.apache.org/docs/0.5.5-incubating/install/install.html


Questions

3. how to design a dashboard? check Zeppelin doc ...
4. Does Zeppelin support a separate dashboard server? Ask question in the slack channel
zeppelin, local repository?


3. what is Helium?
