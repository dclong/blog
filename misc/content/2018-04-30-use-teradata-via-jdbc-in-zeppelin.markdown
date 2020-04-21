UUID: 1582da29-75ae-4fc4-8007-a2768222782f
Status: published
Date: 2018-04-30 18:00:03
Author: Ben Chuanlong Du
Slug: use-teradata-via-jdbc-in-zeppelin
Title: Use Teradata via JDBC in Zeppelin
Category: Software
Tags: software, Zeppelin, JDBC, Teradata

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Use Teradata in Zeppelin

In order to connect Teradata via jdbc, a few things are needed to config the jdbc interpreter for Zeppelin:

1. Set default.user, default.password

2. Set default.url to jdbc:teradata://vivaldi.vip.ebay.com

3. Import Teradata JDBC driver into Dependencies (the .jar package is attached)

4. Set default.driver to com.teradata.jdbc.TeraDriver

## Related Resources

https://www.progress.com/blogs/using-a-jdbc-driver-with-apache-zeppelin

https://community.mapr.com/docs/DOC-2028-how-to-query-drill-using-zeppelin-on-mapr-cdp-draft

https://zeppelin.apache.org/docs/0.6.2/interpreter/jdbc.html

https://wiki.vip.corp.ebay.com/display/TNSRA/Teradata+and+JDBC

https://wiki.vip.corp.ebay.com/display/~magardner/Python+JDBC+connection+to+Teradata
