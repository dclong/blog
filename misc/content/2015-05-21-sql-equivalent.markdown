Status: published
Date: 2020-09-05 15:38:05
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
    <td rowspan="7"> List all <br> tables <br>in the <br> current <br> database <a href="#footnote1">[1]</a> </td>
    <td> SQLite 3 </td>
    <td> <code> 
        .TABLES
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        SHOW TABLES
    </code> </td>
  </tr>
  <tr>
    <td rowspan="2"> Spark/Hive </td>
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
    <td> Teradata </td>
    <td rowspan="1"> <code> 
        SHOW TABLES
    </code> </td>
  </tr>
  <tr>
    <td> Oracle </td>
    <td> <code> 
        SELECT * <br>
        FROM dba_tables <br>
        WHERE table_schema = 'current database name'
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
    <td> Spark/Hive </td>
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
    <td rowspan="6"> Randomly <br> sample <br> 100 rows </td>
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
    <td> Spark/Hive </td>
    <td> <code> 
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
        <a href="https://docs.databricks.com/spark/latest/spark-sql/language-manual/insert.html"> 
        Spark/Hive 
        </a>
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
    <td> Spark/Hive </td>
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
    <td> Spark/Hive </td>
    <td> <code> 
    /* substr and substring are equivalent in Spark/Hive SQL */ <br>
    SELECT <br> &nbsp; &nbsp; 
        substr('Spark SQL', 5, 1) -- resulting 'k' <br>
    FROM <br> &nbsp; &nbsp;
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
    <td> Spark/Hive </td>
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
    <td> Spark/Hive </td>
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


## References 

https://www.oreilly.com/library/view/high-performance-mysql/9780596101718/ch04.html