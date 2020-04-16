Status: published
Date: 2019-02-09 09:04:52
Author: Benjamin Du
Slug: split-string-into-rows-in-SQL
Title: Split String into Rows in SQL
Category: Computer Science
Tags: programming, SQL, SQLite3, split, string, rows

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## split

```
SELECT
    A.state,
    split.A.value('.', 'VARCHAR(100)') AS String
FROM (
    SELECT 
        state,  
        CAST('<M>' + REPLACE(city, ',', '</M><M>') + '</M>' AS XML) AS string  
    FROM
        TableA
    ) AS A
CROSS APPLY String.nodes ('/M') AS split(a)
```

## References

http://sqljason.com/2010/05/converting-single-comma-separated-row.html

http://www.samuelbosch.com/2018/02/split-into-rows-sqlite.html

https://gist.github.com/dannguyen/1ff581b1e76fddb72cf2ff1542aa6c62

https://stackoverflow.com/questions/34659643/split-a-string-into-rows-using-pure-sqlite
