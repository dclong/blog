Status: published
Date: 2020-05-17 11:48:27
Author: Benjamin Du
Slug: Improve Performance of Inserting in Teradata SQL
Title: Fastload in Teradata
Category: Computer Science
Tags: Computer Science, SQL, Teradata, fastload, BTEQ, prepared statement

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Insert Multiple Rows

Teradata SQL does not support `VALUES` with multiple rows in a `INSERT` statement.

1. Multi Statement Request (MSR) + [Teradata BTEQ](https://www.tutorialspoint.com/teradata/teradata_bteq.htm)
    You can run a MSR (with multiple insert statements) BTEQ,
    which submit all insert statements as one block after the final semicolon.
    Note: when thereis a new command starting on the same line,
    it is part of the MSR.

        :::sql
        INSERT INTO Example Values('Steve',4)
        ;INSERT INTO Example Values('James',8)
        ;

    In Teradata SQL Assistant or Teradata SQL Studio,
    they shortcut is `F9` (instead of `F5`).

## Performance

@TODO: convert the Java example to Kotlin code in JupyterLab notebook.

1. [Prepared/Parameterized Statement](https://en.wikipedia.org/wiki/Prepared_statement)
    is recommended to improve performance of query/update/insert. 
	Below is an example of using JDBC in Java.

        :::java
        // These are done once 
        Connection conn = DriverManager.getConnection(url, username, password);
        String sql = "INSERT INTO transactions (cust_id, transaction_date, amount, desc) values (?, ?, ?, ?)";
     
        PreparedStatement ps = conn.prepareStatement(sql);
         
        // the below can be repeated many times with different values
        ps.setInt(1, custID);
        ps.setDate(2, tran_date);
        ps.setBigDecimal(3, amount);
        ps.setString(4, desc);
        ps.executeUpdate();

    In a [DB-API](https://www.python.org/dev/peps/pep-0249/) compatible Python module (e.g., JayDeBeApi),
    you call use the method [execute](https://www.python.org/dev/peps/pep-0249/#id15)
    on a parameterized query with a list/tuple of parameters.

		:::python
		sql = "INSERT INTO transactions (cust_id, transaction_date, amount, desc) values (?, ?, ?, ?)"
		cursor.execute(sql, [cust_id, tran_dt, amount, desc])

	Prepared Statement Batches take your performance to the next level. 
	In addition to the benefits of reusing the Prepared Statement, 
	batching your input values also reduces the number of round trips to the database. 
	A batch size of roughly 5,000 to 10,000 works well for most applications. 
	Using batches can be 10 to 40 times faster than the previous approach.
	Below is an example of using JDBC in Java.

		:::java
		Connection conn = DriverManager.getConnection(url, username, password);
		String sql = "INSERT INTO transactions(cust_id, transaction_date, amount, desc) values (?, ?, ?, ?)";
		PreparedStatement ps = conn.prepareStatement(sql);
		for ( /* Loop through input values */ ) {
			for ( /* Loop through a subset of the input values - the desired batch size */ ) {
				ps.setInt(1, custID);
				ps.setDate(2, tran_date);
				ps.setBigDecimal(3, amount);
				ps.setString(4, desc);
				ps.addBatch(); // adds the row of input values to the batch
			}
			// This is done once per the desired batch size.
			ps.executeBatch(); // sends all the batched rows to the database
		}

    In a [DB-API](https://www.python.org/dev/peps/pep-0249/) compatible Python module (e.g., JayDeBeApi),
    you call use the method [executemany](https://www.python.org/dev/peps/pep-0249/#executemany)
    on a parameterized query with a list/tuple of list/tuple of parameters.

		:::python
		sql = "INSERT INTO transactions (cust_id, transaction_date, amount, desc) values (?, ?, ?, ?)"
		cursor.execute(sql, [
			[cust_id_1, tran_dt_1, amount_1, desc_1],
			[cust_id_2, tran_dt_2, amount_2, desc_2],
			[cust_id_3, tran_dt_3, amount_3, desc_3],
		])

	For loading truly huge amounts of data, 
	JDBC FastLoad can provide even better performance. 
	There are a couple of caveats, however. 
	**JDBC FastLoad can only insert data into an empty table**,
	and JDBC FastLoad is only recommended for loading large amounts of data -- at least 100,000 rows total.
	The nice thing is that your Java code doesn't need to change in order to use JDBC FastLoad. 
	Your application uses the exact same Prepared Statement batches as in the previous example. 
	Just add `TYPE=FASTLOAD` to your connection parameters, 
	and the Teradata JDBC Driver will use JDBC FastLoad for particular SQL requests, if it can.
	Note that the recommended batch size for JDBC FastLoad is much higher 
	than for a regular SQL Prepared Statement batch, which means you may need to increase your JVM heap size. 
	To get top-notch performance, 
	you need to use a batch size of roughly 50,000 to 100,000. 
	Using JDBC FastLoad can be 3 to 10 times faster than the previous approach.
	Please refer to 
	[JDBC FastLoad](https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#BABFGFAF)
	for more discussions on JDBC FastLoad.

## FastLoad

If you have the Teradata ODBC driver installed,
you can access the `fastload` commaand by installing Teradata Tools & Utils.
If you use JDBC, 
it seems that you must write code yourself.

## References

- [JDBC FastLoad](https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#BABFGFAF)

- [Teradata - BTEQ](https://www.tutorialspoint.com/teradata/teradata_bteq.htm)

- [Insert Multiple Rows SQL Teradata](https://stackoverflow.com/questions/39668309/insert-multiple-rows-sql-teradata)

- [Bulk Insert to Teradata using Python](http://www.ebyhr.org/2018/10/bulk-insert-to-teradata-using-python.html)

- [Speed up your JDBC/ODBC applications](https://downloads.teradata.com/connectivity/articles/speed-up-your-jdbcodbc-applications)

- [Teradata-jdbc: What's the point of using Fastload if java has memory limitations?](https://stackoverflow.com/questions/26684648/teradata-jdbc-whats-the-point-of-using-fastload-if-java-has-memory-limitations)

- [Teradata JDBC Driver Sample Programs](https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/samplePrograms.html)

- [Teradata FASTLOAD - Overview , Syntax and Execution](https://www.youtube.com/watch?v=sq5x__EkCJc)
