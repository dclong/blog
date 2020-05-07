Status: published
Date: 2020-05-06 00:45:31
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
    <td rowspan="9"> List databases/schemas/namespaces </td>
    <td> SQLite 3 </td>
    <td> <code> 
        .databases
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
  <tr>
    <td rowspan="4"> Spark/Hive SQL </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        show databases like "*user*"
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        hdfs dfs -ls /path/to/hive/warehouse
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        /*You can query the Hive Metastore DB if you have access.*/
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
    <td> <code> 
        show databases
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
        show databases
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
        use database_name
    </code> </td>
  </tr>
  <tr>
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td rowspan="1"> <code> 
        use database_name
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
    <td> <code> 
        use database_name
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
        use database_name
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="6"> List all tables in the current/default database/schema/namespace </td>
    <td> SQLite 3 </td>
    <td> <code> 
        .tables
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        show tables
    </code> </td>
  </tr>
  <tr>
    <td> Spar/Hive SQL </td>
    <td> <code> 
        show tables
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td rowspan="1"> <code> 
        show tables
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
    <td> <code> 
        select 
            * 
        from 
            dba_tables
        where 
            table_schema = 'current database name'
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
        SELECT 
            table_name 
        FROM 
            information_schema.tables 
        WHERE 
            table_type = 'BASE TABLE' 
        AND 
            table_catalog = 'current database name' 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="7"> Describe a table </td>
    <td> SQLite 3 </td>
    <td> <code> 
        .schema table_name
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        DESCRIBE table_name
    </code> </td>
  </tr>
  <tr>
    <td> Spar/Hive SQL </td>
    <td> <code> 
        DESCRIBE table_name
    </code> </td>
  </tr>
  <tr>
    <td rowspan="2"> Teradata SQL </td>
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
    <td> Oracle SQL </td>
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
    <td rowspan="8"> List all tables owned by the current user </td>
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
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td rowspan="1"> <code> 
    </code> </td>
  </tr>
  <tr>
    <td rowspan="3"> Oracle SQL </td>
    <td> <code> 
        /* there is no "owner" column in user_tables,
           since all tables in user_tables are owned by the current user
         */
        SELECT * 
        FROM user_tables;
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SELECT * 
        FROM all_tables 
        WHERE owner = "current_user_name";
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        SELECT * 
        FROM dba_tables 
        WHERE owner = "curent_user_name";
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="6"> List all tables accisble by the current user </td>
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
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td rowspan="1"> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
    <td> <code> 
        SELECT * 
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
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td rowspan="1"> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
        select * from dba_tables;
    <td> <code> 
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
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td rowspan="1"> <code> 
        DROP TABEL IF EXISTS table_name
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
    <td> <code> 
        IF object_id(table_name) IS NOT NULL THEN 
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
        select * from table limit 5;
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
        SELECT * FROM table_name LIMIT 5;
    </code> </td>
  </tr>
  <tr>
    <td> Spark/Hive SQL </td>
    <td> <code> 
        SELECT * FROM table_name LIMIT 5;
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td> <code> 
        SELECT TOP 5 * FROM table;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
    <td> <code> 
        select * from table limit 5;
    </code> </td>
  </tr>
  <tr>
    <td rowspan="2"> MS SQL Server </td>
    <td> <code> 
        select top 5 * from table;
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
        select top 50 percent * from table;
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="6"> Randomly sample 100 rows </td>
    <td> SQLite 3 </td>
    <td> <code> 
        select 
            * 
        from 
            table 
        order by 
            random() 
        limit 100;
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td rowspan="1"> 
        <a href="https://docs.teradata.com/reader/2_MC9vCtAJRlKle2Rpb0mA/XTSw8n_~xbTDRIHwHyUiWA"> Teradata SQL </a>
      </td>
    <td> <code> 
        select * from table sample 100;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> MS SQL Server </td>
    <td> <code> 
    </code> </td>
  </tr>
    
  <tr>
    <td rowspan="6"> Randomly sample rows with acceptance ratio 0.1 </td>
    <td> SQLite 3 </td>
    <td> <code> 
        /*
        Note that `random()` generates a pseudo-random integer 
        between -9223372036854775808 and +9223372036854775807. 
        */
        SELECT 
            * 
        FROM 
            table 
        WHERE
            random() % 10 = 0;
    </code> </td>
  </tr>
  <tr>
    <td> MySQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td> <code> 
        select * from table sample 0.1;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
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
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td> <code> 
        INSERT INTO table_name (
            first_name,
            last_name
        ) VALUES 
            ('Fred', 'Smith'),
            ('John', 'Smith'),
            ('Michael', 'Smith'),
            ('Robert', 'Smith')
        ;
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
    <td> <code> 
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
    <td> Spar/Hive SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Teradata SQL </td>
    <td> <code> 
    </code> </td>
  </tr>
  <tr>
    <td> Oracle SQL </td>
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


