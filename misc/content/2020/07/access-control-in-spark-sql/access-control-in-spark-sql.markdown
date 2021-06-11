Status: published
Date: 2020-07-22 10:11:21
Author: Benjamin Du
Slug: access-control-in-spark-sql
Title: Access Control in Spark SQL
Category: Computer Science
Tags: Computer Science, Spark SQL, SQL, big data, Spark, access control, permission, user
Modified: 2020-12-22 10:11:21

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Grant Permission to Users

    GRANT
        priv_type [, priv_type ] ...
        ON database_table_or_view_name
        TO principal_specification [, principal_specification] ...
        [WITH GRANT OPTION];
    
Examples:
    
    GRANT SELECT ON table1 TO USER user1;
    GRANT SELECT ON DATABASE db1 TO USER user1;
    GRANT SELECT ON table1 TO ROLE role1;

Grant on database grants privileges on all tables or views under this database.
If a user is granted a privilege `WITH GRANT OPTION` on a table or view, 
then the user can also grant/revoke privileges of other users and roles on those objects. 


## Remove Permission of Users

    REVOKE [GRANT OPTION FOR]
        priv_type [, priv_type ] ...
        ON database_table_or_view_name
        FROM principal_specification [, principal_specification] ... ;
    
    principal_specification
    : USER user
    | ROLE role
    
    priv_type
    : SELECT
        UPDATE
        INSERT
        DELETE
    
Examples:

    REVOKE SELECT ON table1 FROM USER user1;
    REVOKE SELECT ON DATABASE db1 FROM USER user1;

If a user is granted a privilege `WITH GRANT OPTION` on a table or view, 
then the user can also grant/revoke privileges of other users and roles on those objects. 
The grant option for a privilege can be removed 
while still keeping the privilege by using `REVOKE GRANT OPTION FOR <privilege>`.

## References 

https://docs.databricks.com/spark/latest/spark-sql/language-manual/security-grant.html
