Status: published
Date: 2021-02-20 09:12:14
Author: Ben Chuanlong Du
Slug: sql-equivalent
Title: SQL Equivalent
Category: Computer Science
Tags: programming, SQL, database, equivalent, querying

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


[SQL translation](https://www.jooq.org/translate/)
is a great tool that transalte any SQL statement(s) to a different dialetc using the JOOQ Parser.

<div style="overflow-x:auto;">
<style>
    tr:nth-child(even) {background-color: #f2f2f2}
</style>
<table style="width:100%">
  <tr>
    <th> </th>
    <th> SQL Variant </th>
    <th> Code </th>
  </tr>
  <tr>
    <td rowspan="9"> List <br> databases <a href="#footnote1">[1]</a> </td>
    <td> SQLite 3 </td>
    <td> <code> 
        .DATABASES
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        SHOW DATABASES
    </code> </td>
  </tr>
  <tr>
    <td rowspan="4"> Spark/Hive </td>
    <td> <code> 
        SHOW DATABASES
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SHOW DATABASES LIKE "*user*"
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        hdfs dfs -ls /path/to/hive/warehouse
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        /* <br>
        You can query the Hive Metastore DB <br>
        if you have access. <br>
        */
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
        SHOW DATABASES
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        SHOW DATABASES
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
        SHOW DATABASES
    </code> </td>
  </tr>
  
  <tr>
    <td rowspan="6"> Use a <br> databases <a href="#footnote1">[1]</a> </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        USE database_name
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td rowspan="1"> <code> 
        USE database_name
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        USE database_name
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
        USE database_name
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="9"> List all <br> tables <br>in the <br> current <br> database <a href="#footnote1">[1]</a> </td>
    <td> SQLite 3 </td>
    <td> <code> 
        .TABLES <br>
        SELECT name 
        FROM db.sqlite_master 
        WHERE type='table'
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        SHOW TABLES
    </code> </td>
  </tr>
  <tr>
    <td rowspan="4"> Spark/Hive </td>
    <td> <code> 
        SHOW TABLES
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SHOW TABLES in db_name
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SHOW TABLES in db_name like '*cust*'
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SHOW TABLE EXTENDED in db_name like '*cust*'
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td rowspan="1"> <code> 
        SHOW TABLES
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        /*All tables in a database*/
        SELECT * <br>
        FROM dba_tables <br>
        WHERE table_schema = 'current database name'<br>
        The table `all_tab_cols` contains information about tables and their columns
        <br>
        /* List all tables owned by the current user.*/
        select * from user_tables;
        List all tables accessible to the current user.
        select * from all_tables;
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
        SELECT table_name <br> 
        FROM information_schema.tables <br>
        WHERE table_type = 'BASE TABLE' <br>
        AND table_catalog = 'current database name' 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="7"> Describe <br> a table </td>
    <td> SQLite 3 </td>
    <td> <code> 
        .SCHEMA table_name
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        DESCRIBE table_name
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
        DESCRIBE table_name
    </code> </td>
  </tr>
  <tr>
    <td rowspan="2"> Teradata </td>
    <td> <code> 
        HELP TABLE table_name;
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        HELP COLUMN table_name.*;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        DESCRIBE table_name
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
        DESCRIBE table_name
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="7"> Source code <br> of a table </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
        SHOW CREATE table_name
    </code> </td>
  </tr>
  <tr>
    <td rowspan="2"> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="8"> List all <br> tables <br> owned <br> by the <br> current <br> user </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td rowspan="1"> <code> 
    </code> </td>
  </tr>
  <tr>
    <td rowspan="3"> Oracle </td>
    <td> <code> 
        /* there is no "owner" column in user_tables, <br>
           since all tables in user_tables are owned by the current user <br>
         */ <br>
        SELECT * <br>
        FROM user_tables;
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SELECT * <br>
        FROM all_tables <br> 
        WHERE owner = "current_user_name";
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SELECT * <br>
        FROM dba_tables <br> 
        WHERE owner = "curent_user_name";
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="6"> List all <br> tables <br> accessible <br> by the <br> current <br> user </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td rowspan="1"> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        SELECT * <br>
        FROM all_tables;
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="6"> List all <br> tables <br> in the <br> system </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td rowspan="1"> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        SELECT * FROM dba_tables;
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Create <br> a <br> table </td>
    <td> SQLite 3 </td>
    <td> <code> 
    CREATE TABLE IF NOT EXISTS queries ( <br> &nbsp; &nbsp;
        query Text NOT NULL PRIMARY KEY, <br> &nbsp; &nbsp;
        timestamp Real NOT NULL, <br> &nbsp; &nbsp;
        data Blob NOT NULL <br> 
    )
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    CREATE TABLE IF NOT EXISTS queries ( <br> &nbsp; &nbsp;
        query VarChar NOT NULL PRIMARY KEY, <br> &nbsp; &nbsp;
        timestamp Decimal(18, 3) NOT NULL, <br> &nbsp; &nbsp;
        data Blob NOT NULL <br> 
    )
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/spark-sql-tips/"> Spark/Hive </a>
    </td>
    <td> <code> 
    CREATE TABLE IF NOT EXISTS queries ( <br> &nbsp; &nbsp;
        query String NOT NULL, <br> &nbsp; &nbsp;
        timestamp Double NOT NULL, <br> &nbsp; &nbsp;
        data Binary NOT NULL <br> 
    )
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    CREATE TABLE IF NOT EXISTS queries ( <br> &nbsp; &nbsp;
        query VarChar NOT NULL PRIMARY KEY, <br> &nbsp; &nbsp;
        timestamp Number NOT NULL, <br> &nbsp; &nbsp;
        data Blob NOT NULL <br> 
    )
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    CREATE TABLE IF NOT EXISTS queries ( <br> &nbsp; &nbsp;
        query Text NOT NULL PRIMARY KEY, <br> &nbsp; &nbsp;
        timestamp Decimal(18, 3) NOT NULL, <br> &nbsp; &nbsp;
        data Blob NOT NULL <br> 
    )
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    CREATE TABLE IF NOT EXISTS queries ( <br> &nbsp; &nbsp;
        query VarChar NOT NULL PRIMARY KEY, <br> &nbsp; &nbsp;
        timestamp Decimal(18, 3) NOT NULL, <br> &nbsp; &nbsp;
        data Blob NOT NULL <br> 
    )
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Drop a <br> table <br> if exists </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td rowspan="1"> <code> 
        DROP TABEL IF EXISTS table_name
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        IF object_id(table_name) IS NOT NULL THEN <br>
            DROP TABLE table_name
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="7"> Limit <br> number <br> of <br> returned <br> rows </td>
    <td> SQLite 3 </td>
    <td> <code> 
        SELECT * <br>
        FROM table <br>
        LIMIT 5;
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        SELECT * <br>
        FROM table_name <br> 
        LIMIT 5;
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
        SELECT * <br>
        FROM table_name <br> 
        LIMIT 5;
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
        SELECT TOP 5 * <br>
        FROM table;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        SELECT * <br>
        FROM table <br>
        LIMIT 5;
    </code> </td>
  </tr>
  <tr>
    <td rowspan="2"> MS SQL Server </td>
    <td> <code> 
        SELECT TOP 5 * <br> 
        FROM table;
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SELECT TOP 50 PERCENT * <br> 
        FROM table;
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="8"> Randomly <br> sample <br> 100 rows </td>
    <td> SQLite 3 </td>
    <td> <code> 
        SELECT * <br>
        FROM table <br> 
        ORDER BY random() <br> 
        LIMIT 100;
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td rowspan="3"> Spark/Hive </td>
    <td> <code> 
    SELECT * <br>
    FROM table <br>
    TABLESAMPLE (1 PERCENT) <br>
    LIMIT 100;
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    SELECT * <br>
    FROM table <br>
    ORDER BY random() <br>
    LIMIT 100;
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    /* NOTE: the following does NOT work!!! <br>
    It is equivalent to `LIMIT 100`
    */ <br>
    SELECT * FROM table <br>
    TABLESAMPLE (100 ROWS)
    </code> </td>
  </tr>
  <tr>
    <td rowspan="1"> 
        <a href="https://docs.teradata.com/reader/2_MC9vCtAJRlKle2Rpb0mA/XTSw8n_~xbTDRIHwHyUiWA"> Teradata </a>
      </td>
    <td> <code> 
        SELECT * <br>
        FROM table <br>
        SAMPLE 100;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="6"> Randomly sample <br> rows with <br> acceptance <br> ratio 0.1 </td>
    <td> SQLite 3 </td>
    <td> <code> 
        /* <br>
        Note that `random()` generates a pseudo-random integer <br>
        between -9223372036854775808 and +9223372036854775807. <br>
        */ <br>
        SELECT * <br>
        FROM table <br> 
        WHERE random() % 10 = 0;
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
    SELECT * FROM table <br>
    TABLESAMPLE (10 PERCENT)
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
        SELECT * <br>
        FROM table <br>
        SAMPLE 0.1;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>


 <tr>
    <td rowspan="6"> Randomly <br> sample <br> buckets </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
    <a href="http://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-sampling.html"> Spark/Hive </a>
     </td>
    <td> <code> 
    SELECT * FROM table <br>
    TABLESAMPLE (BUCKET 4 out of 10)
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
 

    
  <tr>
    <td rowspan="6"> Insert <br> multiple <br> rows in <br> one <br> statement </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/spark-sql-tips/"> Spark/Hive </a>
    </td>
    <td> <code> 
    INSERT INTO tablel_name PARTITION ( <br> &nbsp; &nbsp;
        par_col_1 = pv1, <br> &nbsp; &nbsp;
        par_col_2 = pv2 <br>
    ) VALUES ( <br> &nbsp; &nbsp;
        v11, v12, ... <br>
    ), ( <br> &nbsp; &nbsp;
        v21, v22, ... <br>
    )
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
        INSERT INTO table_name ( <br> &nbsp; &nbsp;
            first_name, <br> &nbsp; &nbsp;
            last_name <br>
        ) VALUES  <br> &nbsp; &nbsp;
            ('Fred', 'Smith'), <br> &nbsp; &nbsp;
            ('John', 'Smith'), <br> &nbsp; &nbsp;
            ('Michael', 'Smith'), <br> &nbsp; &nbsp;
            ('Robert', 'Smith') <br>
        ;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        INSERT INTO pager (pag_id, pag_parent, pag_name, pag_active) <br>
        SELECT 8000, 0, 'Multi 8000', 1 FROM dual <br>
        UNION ALL  <br>
        SELECT 8001, 0, 'Multi 8001', 1 FROM dual <br>
        ; <br>
        -- or <br>
        INSERT ALL <br>
        INTO t (col1, col2, col3) VALUES ('val1_1', 'val1_2', 'val1_3') <br>
        INTO t (col1, col2, col3) VALUES ('val2_1', 'val2_2', 'val2_3') <br>
        INTO t (col1, col2, col3) VALUES ('val3_1', 'val3_2', 'val3_3')
        ;
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="7"> Update </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark </td>
    <td> <code> 
    - not supported as of Spark 2.4.5 <br>
    - Spark SQL 3.0.0 has update/delete APIs but not implemented <br>
    - Update/delete is feasible using Detal Lake
    </code> </td>
  </tr>
  <tr>
    <td> Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="7"> Insert <br> or <br> Replace </td>
    <td> 
    <a href="https://www.sqlitetutorial.net/sqlite-replace-statement/"> SQLite 3 </a> 
    </td>
    <td> <code> 
    REPLACE INTO phonebook ( <br> &nbsp; &nbsp;
        name, phonenumber, validdate <br>
    ) VALUES ( <br> &nbsp; &nbsp;
        'Alice', '704-555-1212', '2018-05-08' <br>
    )
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark </td>
    <td> <code> 
    - not supported as of Spark 2.4.5 <br>
    - Spark SQL 3.0.0 has update/delete APIs but not implemented <br>
    - Update/delete is feasible using Detal Lake
    </code> </td>
  </tr>
  <tr>
    <td> Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

   <tr>
    <td rowspan="7"> Upsert </td>
    <td> 
    <a href="https://sqlite.org/lang_UPSERT.html"> SQLite 3 </a> 
    </td>
    <td> <code> 
    INSERT INTO phonebook ( <br> &nbsp; &nbsp;
        name, phonenumber, validDate <br>
    ) VALUES ( <br> &nbsp; &nbsp;
        'Alice', '704-555-1212', '2018-05-08' <br>
    ) ON CONFLICT (name) DO UPDATE <br>
    SET <br> &nbsp; &nbsp;
        phonenumber=excluded.phonenumber, <br> &nbsp; &nbsp;
        validDate=excluded.validDate <br>
    WHERE <br> &nbsp; &nbsp;
        excluded.validDate > phonebook.validDate
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark </td>
    <td> <code> 
    - not supported as of Spark 2.4.5 <br>
    - Spark SQL 3.0.0 has update/delete APIs but not implemented <br>
    - Update/delete is feasible using Detal Lake
    </code> </td>
  </tr>
  <tr>
    <td> Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="7"> Delete </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark </td>
    <td> <code> 
    - not supported as of Spark 2.4.5 <br>
    - Spark SQL 3.0.0 has update/delete APIs but not implemented <br>
    - Update/delete is feasible using Detal Lake
    </code> </td>
  </tr>
  <tr>
    <td> Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Insert </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    INSERT INTO some_table <br>
    SELECT * FROM another_table
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Refresh <br> Table <br> Cache </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive </td>
    <td> <code> 
    REFRESH TABLE table_name
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

    
  <tr>
    <td rowspan="6"> Concatenate <br> Strings </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT concat('Spark', 'SQL') <br>
    FROM table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Substring </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    /* substr and substring are equivalent in Spark/Hive SQL */ <br>
    SELECT <br> &nbsp; &nbsp; 
        substr('Spark SQL', 5, 1) -- resulting 'k' <br>
    FROM <br> &nbsp; &nbsp;
        table <br>
    left/right
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    substr
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> trim </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    ltrim/rtrim/trim
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    trim
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> substitute </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    replace/translate/regexp_replace
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    oreplace, otranslate
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> length of string </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    char_length
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Index of substring </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    substring_index
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    POSITION('de' IN 'abcdefg') <br>
    regexp_instr('abc', 'a') -- 1-base index;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> upper case </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    ucase/upper
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> decode base64 </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    unbase64
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> decode hex </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    unhex
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> generate an uuid </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    uuid
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> reverse a string </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    reverse
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> string matching </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    /* like is Case sensitive */
    like/rlike
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    /*like is case insensitive by default, 
    however, 
    you can specify the keyword CaseSpecific to make it case sensitive
    */
    like
    SELECT 
        empname 
    FROM 
        tbl_emp 
    WHERE 
        empname (CaseSpecific) like '%JO%’
    ;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    /*like is case sensitive*/
    like / regexp_like(name, 'string$', 'i')
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> shift string </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    shiftleft/shiftright
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> ocurrence of char </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-string/"> Spark/Hive </a>
    </td>
    <td> <code> 
    shiftleft/shiftright
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    char_length('Teradata is Relational Database') - char_length(Oreplace('Teradata is Relational Database', 'a', ''))
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Cast to date </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT <br> &nbsp; &nbsp;
        to_date("2000-01-01") AS date <br>
    FROM <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    cast(str_col as date format 'YYYY-MM-DD')
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="7"> Cast to timestamp </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT 
        <br> &nbsp; &nbsp;
        to_timestamp("2000-01-01") AS date 
        <br>
    FROM  
        <br> &nbsp; &nbsp; 
        table
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        to_timestamp("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Cast to UTC timestamp </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        to_utc_timestamp("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Cast to Unix timestamp </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        to_unix_timestamp("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Extract year </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        year("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Extract quarter </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        quarter("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Extract month </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        montofyearh("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="7"> Extract day </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        day("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        dayofmonth("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Extract minute </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        minute("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Extract second </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        second("2000-01-01") AS date
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="7"> Add days to a date </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        date_add(current_date, 3) AS date3
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    /* The + operator for date and int <br>
    is support since Spark 3 */ <br>
    SELECT
        <br> &nbsp; &nbsp;
        current_date + 3 AS date3
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Add months to a date </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        add_months(current_date, 3) AS date3
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="7"> Subtract days from a date </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        date_sub(current_date, 3) AS date3
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    /* The - operator for date and int <br>
    is supported since Spark 3 */
    <br>
    SELECT
        <br> &nbsp; &nbsp;
        current_date - 3 AS date3
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> Diff between two dates </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT
        <br> &nbsp; &nbsp;
        datediff(date1, date2) AS diff
        <br>
    FROM 
        <br> &nbsp; &nbsp;
        table
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>

  <tr>
    <td rowspan="6"> truncate date </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    SELECT date_trunc('2015-03-05T09:32:05.359', 'YEAR');
    -- 2015-01-01T00:00:00

    SELECT date_trunc('2015-03-05T09:32:05.359', 'MM');
    -- 2015-03-01T00:00:00

    SELECT date_trunc('2015-03-05T09:32:05.359', 'DD');
    -- 2015-03-05T00:00:00

    SELECT date_trunc('2015-03-05T09:32:05.359', 'HOUR');
    -- 2015-03-05T09:00:00

    SELECT trunc('2009-02-12', 'MM');
    -- 2009-02-01

    SELECT trunc('2015-10-27', 'YEAR');
    -- 2015-01-01
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="6"> sth </td>
    <td> SQLite 3 </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> 
        <a href="http://www.legendu.net/misc/blog/pyspark-func-date/"> Spark/Hive </a>
    </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
</table>
</div>

<p id="footnote1">
[1] The terminology (database, schema or namespace) might be different for differennt databases.
</p>


A [NOT] LIKE B¶
NULL if A or B is NULL, TRUE if string A matches the SQL simple regular expression B, otherwise FALSE. The comparison is done character by character. The character in B matches any character in A (similar to . in posix regular expressions) while the % character in B matches an arbitrary number of characters in A (similar to .* in posix regular expressions). For example, 'foobar' like 'foo' evaluates to FALSE whereas 'foobar' like 'foo ' evaluates to TRUE and so does 'foobar' like 'foo%'.

A RLIKE B
NULL if A or B is NULL, TRUE if any (possibly empty) substring of A matches the Java regular expression B, otherwise FALSE. For example, 'foobar' RLIKE 'foo' evaluates to TRUE and so does 'foobar' RLIKE '^f.*r$'.

A REGEXP B
Same as RLIKE.

A || B
Concatenate A and B (as of Hive 2.2.0).


## References 

[Ten SQL Tricks that You Didn’t Think Were Possible (Lukas Eder)](https://www.youtube.com/watch?v=mgipNdAgQ3o)

[Column Alias in SQL](http://www.legendu.net/misc/blog/column-alias-in-sql)

http://www.legendu.net/misc/blog/Use-tablesample-in-sql

http://www.legendu.net/misc/blog/spark-dataframe-func-date

http://www.legendu.net/misc/blog/spark-dataframe-func-string

https://www.oreilly.com/library/view/high-performance-mysql/9780596101718/ch04.html

https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-StringFunctions

https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-StringOperators

https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-RelationalOperators