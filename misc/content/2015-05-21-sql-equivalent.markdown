Status: published
Date: 2020-05-29 21:21:44
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
<table style="width:100%">
  <tr>
    <th> </th>
    <th> SQL Variant </th>
    <th> Code </th>
  </tr>
  <tr>
    <td rowspan="9"> List <br> databases/schemas/namespaces </td>
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
    <td rowspan="6"> Choose/use a databases/schemas/namespaces </td>
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
    <td rowspan="6"> List all tables in the current/default database/schema/namespace </td>
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
    <td> Spark/Hive </td>
    <td> <code> 
        SHOW TABLES
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
        SELECT <br>
            * <br>
        FROM <br>
            dba_tables <br>
        WHERE <br>
            table_schema = 'current database name'
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
        SELECT <br> 
            table_name <br> 
        FROM <br>
            information_schema.tables <br>
        WHERE <br>
            table_type = 'BASE TABLE' <br>
        AND <br>
            table_catalog = 'current database name' 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="7"> Describe a table </td>
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
    <td rowspan="8"> List all tables owned <br> by the current user </td>
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
    <td rowspan="6"> List all tables accessible <br> by the current user </td>
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
    <td rowspan="6"> List all tables in the system </td>
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
    <td rowspan="6"> Drop a table conditionally </td>
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
    <td rowspan="7"> Limit number of returned rows </td>
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
    <td rowspan="6"> Randomly sample 100 rows </td>
    <td> SQLite 3 </td>
    <td> <code> 
        SELECT <br>
            * <br>
        FROM <br>
            table <br> 
        ORDER BY <br>
            random() <br> 
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
    <td rowspan="6"> Randomly sample rows <br> with acceptance ratio 0.1 </td>
    <td> SQLite 3 </td>
    <td> <code> 
        /* <br>
        Note that `random()` generates a pseudo-random integer <br>
        between -9223372036854775808 and +9223372036854775807. <br>
        */ <br>
        SELECT <br> 
            * <br>
        FROM <br>
            table <br> 
        WHERE <br>
            random() % 10 = 0;
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
    <td rowspan="6"> Insert multiple rows in one statement </td>
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
        INSERT INTO table_name ( <br>
            first_name, <br>
            last_name <br>
        ) VALUES  <br>
            ('Fred', 'Smith'), <br>
            ('John', 'Smith'), <br>
            ('Michael', 'Smith'), <br>
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
    <td rowspan="6"> Concatenate Strings </td>
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
    select <br> &nbsp; &nbsp; &nbsp; &nbsp;
        concat('Spark', 'SQL') <br>
    from ...
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
    <td rowspan="6"> Refresh Table Cache </td>
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


