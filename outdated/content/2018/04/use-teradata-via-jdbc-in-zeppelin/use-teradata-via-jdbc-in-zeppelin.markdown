Status: published
Date: 2018-04-10 10:00:59
Author: Ben Chuanlong Du
Slug: use-teradata-via-jdbc-in-zeppelin
Title: Use Teradata via JDBC in Zeppelin
Category: Software
Tags: software, Zeppelin, JDBC, Teradata
Modified: 2020-05-10 10:00:59

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

## Use Teradata in Zeppelin

In order to connect Teradata via jdbc, a few things are needed to config the jdbc interpreter for Zeppelin:

1. Set default.user, default.password

2. Set default.url to `jdbc:teradata://server_ip`

3. Import Teradata JDBC driver into Dependencies (the .jar package is attached)

4. Set default.driver to com.teradata.jdbc.TeraDriver

## Related Resources

https://www.progress.com/blogs/using-a-jdbc-driver-with-apache-zeppelin

https://community.mapr.com/docs/DOC-2028-how-to-query-drill-using-zeppelin-on-mapr-cdp-draft

https://zeppelin.apache.org/docs/0.6.2/interpreter/jdbc.html
