Status: published
Date: 2021-02-15 12:10:03
Author: Ben Chuanlong Du
Slug: syntax-of-teradata-sql
Title: Syntax of Teradata SQL
Category: Computer Science
Tags: programming, Teradata SQL, syntax, style, error
Modified: 2021-02-15 12:10:03

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**


## Syntax

1. Each Teradata SQL statement must be ended by a semicolon.

5. The keyword `inner` is optional in an `inner join`.

6. To estimate the time and space complexity, 
    you can prefix your SQL code by `explain`,
    or you can just press the `Explain` button if you use Teradata SQL Assistant.

2. Column names in `select` and `group by`, `order by`, etc. are separated by comma. 
    There can be no comma after the last column name.
    This is easy to understand. 
    If you put comma after the last column in a, e.g., `select` clause,
    the `from` keyword will be treated as the last column and results in syntax error.


## Common Syntax Errors

1. Using a comma after the last column or missing a comma 
    after a non-last column in the `select` clause.

2. Miss `then` in  a `case` statement.

        :::sql
        case 
            when condition_1 then v_1 
            when condition_2 then v_2 
            ...
            else v_k 
        end 

3. For `with data` or `with no data` when creating a table. 
    CREATE TABLE Failed. 3706: Syntax error: expected something between ')' and ';'.

## SQL Style

1. It is suggested that you write SQL code in the following style.

    :::sql
    create table t0 as (
    select distinct top 5 *
    from
        t1
    inner join
        t2
    on
        condition
    where
        condition
    group by
        1
    having
        condition
    order by
        1
    )
    with data
    primary index (f1, f2)
