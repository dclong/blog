Status: published
Author: Ben Chuanlong Du
Date: 2014-01-22 15:35:31
Title: Hive SQL
Slug: hive-tips
Category: Computer Science
Tags: big data, hadoop, Hive
Modified: 2020-05-22 15:35:31

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 

0. Hive is case-insensitive, both keywords and functions

1. You can use both double and single quotes for strings

1. use `=` rather than `==` for equality comparison
  but it seems that `==` also works

2. use `%` rather than `*` for matching multiple characters

3. use quit or exit

4. when filtering use the where clause
  while when joining use the on clause

5. it seems that it's not necessary to use group before running aggregation functions
  in hive, e.g., when you count the number of records in a table.

6. must separate fields/column names with comma in the select clause or group by clause.

7. it seems to me that Hive runs command from right to left?

8. Random sample from a Hive table.
    http://www.joefkelley.com/736/

        SELECT 
            * 
        FROM 
          my_table
        WHERE 
            rand() <= 0.0001
        DISTRIBUTE BY 
            rand()
        SORT BY 
            rand()
        LIMIT 10000
        ;


## Common Mistakes

1. Forget to separate fields with comma in the select or group by clause.



### Hive

http://stackoverflow.com/questions/18129581/how-do-i-output-the-results-of-a-hiveql-query-to-csv

https://hadoopsters.net/2015/09/18/hadoop-tutorial-how-to-export-hive-table-to-csv-file/

https://analyticsanvil.wordpress.com/2016//python-jdbc-dyanmic-hive-scripting/ 

Hive table, if I need a small part of a big Hive table, does hive load in all data or try to be smart? it seems that it's hard ...



## References

http://www.joefkelley.com/736/
