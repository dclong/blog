Status: published
Date: 2020-05-06 22:02:41
Author: Ben Chuanlong Du
Slug: sql-equivalent
Title: SQL Equivalent
Category: Computer Science
Tags: programming, SQL, database, equivalent, querying

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!


[SQL translation](https://www.jooq.org/translate/)
is a great tool that transalte any SQL statement(s) to a different dialetc using the JOOQ Parser.

    <th> SQLite 3 </th>
    <th> MySQL </th>
    <th> Spark/Hive SQL </th>
    <th> Teradata SQL </th>
    <th> Oracle SQL </th>
    <th> MS SQL Server </th>

<div style="overflow-x:auto;">
<table style="width:100%">
  <tr>
    <th> </th>
    <th> SQL Variant </th>
    <th> Code </th>
  </tr>
  <tr>
    <td> List databases/schemas/namespaces </td>
    <td> SQLite 3 </td>
    <td> <code> 
        .databases
    </code> </td>
  </tr>
  <tr>
    <td> List databases/schemas/namespaces </td>
    <td> MySQL </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
  <tr>
    <td> List databases/schemas/namespaces </td>
    <td> Spark/Hive SQL </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
  <tr>
    <td> List databases/schemas/namespaces </td>
    <td> Spark/Hive SQL </td>
    <td> <code> 
        hdfs dfs -ls /path/to/hive/warehouse
    </code> </td>
  </tr>
  <tr>
    <td> List databases/schemas/namespaces </td>
    <td> Spark/Hive SQL </td>
    <td> <code> 
        /*You can query the Hive Metastore DB if you have access.*/
    </code> </td>
  </tr>
  <tr>
    <td> List databases/schemas/namespaces </td>
    <td> Teradata SQL </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
  <tr>
    <td> List databases/schemas/namespaces </td>
    <td> Oracle SQL </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
  <tr>
    <td> List databases/schemas/namespaces </td>
    <td> MS SQL Server </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
</table>
</div>
<div style="overflow-x:auto;">
<table style="width:100%">
  <tr>
    <td> Choose/use a databases/schemas/namespaces </td>
    <td>  
    </td>
    <td>  
        use database_name
    </td>
    <td>  
    </td>
    <td>  </td>
    <td>  </td>
    <td>  </td>
  </tr>
  <tr>
    <td> List all tables in the current/default database/schema/namespace </td>
    <td>  
    </td>
    <td>  
        show tables;
    </td>
    <td>  </td>
    <td>  </td>
    <td>  
        select 
            * 
        from 
            dba_tables
        where 
            table_schema = 'current database name'
        ;
    </td>
    <td>  
        SELECT 
            table_name 
        FROM 
            information_schema.tables 
        WHERE 
            table_type = 'BASE TABLE' 
        AND 
            table_catalog = 'current database name' 
    </td>
  </tr>
  <tr>
    <td> Describe a table </td>
    <td>  
        DESCRIBE table_name;
    </td>
    <td>  </td>
    <td>  
        HELP TABLE table_name;
        -- or
        HELP COLUMN table_name.*;
    </td>
    <td>  
        DESCRIBE table_name;
    </td>
    <td>  
    </td>
  </tr>
  <tr>
    <td> List all tables owned by the current user </td>
    <td>  
    </td>
    <td>  </td>
    <td>  </td>
    <td>  </td>
    <td>  
        /* there is no "owner" column in user_tables,
           since all tables in user_tables are owned by the current user
         */
        select * from user_tables;
        select * from all_tables where owner="current_user_name";
        select * from dba_tables where owner="curent_user_name";
    </td>
    <td>  </td>
  </tr>
  <tr>
    <td> List all tables accisble by the current user </td>
    <td>  
    </td>
    <td>  </td>
    <td>  </td>
    <td>  </td>
    <td>  
        select * from all_tables;
    </td>
    <td>  </td>
  </tr>
  <tr>
    <td> List all tables in the system </td>
    <td>  </td>
    <td>  </td>
    <td>  </td>
    <td>  
        select * from dba_tables;
    </td>
    <td>  </td>
  </tr>
  <tr>
    <td> Drop a table conditionally </td>
    <td>  </td>
    <td>  </td>
    <td>  </td>
    <td>  
        select * from dba_tables;
    </td>
    <td>  
        IF object_id(table_name) IS NOT NULL THEN 
            DROP TABLE table_name
    </td>
  </tr>
  <tr>
    <td> Limit number of returned rows </td>
    <td>  
        select * from table limit 5;
    </td>
    <td>  
        select * from table limit 5;
    </td>
    <td>  </td>
    <td>  
        select top 5 * from table;
    </td>
    <td>  
        select * from table limit 5;
    </td>
    <td>  
        -- select top 5 queries
        select top 5 * from table;
        -- select top 50% queries
        select top 50 percent * from table;
    </td>
  </tr>
  <tr>
    <td> Randomly sample 100 rows </td>
    <td>  
        select 
            * 
        from 
            table 
        order by 
            random() 
        limit 100;
    </td>
    <td>  
    </td>
    <td>  
    </td>
    <td>  
        select * from table sample 100;
    </td>
    <td>  
    </td>
    <td>  
    </td>
  </tr>
  <tr>
    <td> Randomly sample rows with acceptance ratio 0.1 </td>
    <td>  
        /*
        Note that `random()` generates a pseudo-random integer 
        between -9223372036854775808 and +9223372036854775807. 
        */
        select 
            * 
        from 
            table 
        where
            random() % 10 = 0;
    </td>
    <td>  
    </td>
    <td>  
    </td>
    <td>  
        select * from table sample 0.1;
    </td>
    <td>  
    </td>
    <td>  
    </td>
  </tr>
  <tr>
    <td> Insert multiple rows in one statement </td>
    <td>  
        /*
        Note that `random()` generates a pseudo-random integer 
        between -9223372036854775808 and +9223372036854775807. 
        */
        select 
            * 
        from 
            table 
        where
            random() % 10 = 0;
    </td>
    <td>  
    </td>
    <td>  
    </td>
    <td>  
        INSERT INTO table_name (
            first_name,
            last_name
        ) VALUES 
            ('Fred', 'Smith'),
            ('John', 'Smith'),
            ('Michael', 'Smith'),
            ('Robert', 'Smith')
        ;
    </td>
    <td>  
        insert into pager (PAG_ID,PAG_PARENT,PAG_NAME,PAG_ACTIVE)
        select 8000, 0, 'Multi 8000', 1 from dual
        union all 
        select 8001, 0, 'Multi 8001', 1 from dual
        ;
        -- or
        INSERT ALL
        INTO t (col1, col2, col3) VALUES ('val1_1', 'val1_2', 'val1_3')
        INTO t (col1, col2, col3) VALUES ('val2_1', 'val2_2', 'val2_3')
        INTO t (col1, col2, col3) VALUES ('val3_1', 'val3_2', 'val3_3')
        ;
    </td>
    <td>  
    </td>
  </tr>
</table>
</div>

