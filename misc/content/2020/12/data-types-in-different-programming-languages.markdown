Status: published
Date: 2021-02-20 13:34:55
Author: Benjamin Du
Slug: data-types-in-different-programming-languages
Title: Data Types in Different Programming Languages
Category: Computer Science
Tags: Computer Science, programming, type, data type, primitive, pandas, pyarrow, arrow, SQL, equivalent

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

<div style="overflow-x:auto;">
<style>
    tr:nth-child(even) {background-color: #f2f2f2}
</style>
<table style="width:100%">
  <tr>
    <th> Data Type </th>
    <th> C </th>
    <th> C++ </th>
    <th> Rust </th>
    <th> Java </th>
    <th> Python </th>
    <th> numpy </th>
    <th> pyarrow </th>
    <th> Spark SQL </th>
    <th> SQL </th>
  </tr>
  <tr>
    <td> 8 bit integer </td>
    <td> short (16-bit)</td>
    <td> int8_t </td>
    <td> i8 </td>
    <td> short (16-bit) </td>
    <td> int (arbitrary precision) </td>
    <td> int8 </td>
    <td> </td>
    <td> TinyInt </td>
    <td> </td>
  </tr>
  <tr>
    <td> 16 bit integer </td>
    <td> short </td>
    <td> int16_t </td>
    <td> i16 </td>
    <td> short </td>
    <td> int (arbitrary precision) </td>
    <td> int16 </td>
    <td> </td>
    <td> SmallInt </td>
    <td> SmallInt </td>
  </tr>
  <tr>
    <td> 32 bit integer </td>
    <td> int </td>
    <td> int32_t </td>
    <td> i32 </td>
    <td> int </td>
    <td> int (arbitrary precision) </td>
    <td> int32 </td>
    <td> </td>
    <td> int </td>
    <td> </td>
  </tr>
  <tr>
    <td> 64 bit integer </td>
    <td> long </td>
    <td> int64_t </td>
    <td> i64 </td>
    <td> long </td>
    <td> int (arbitrary precision) </td>
    <td> int64 </td>
    <td> </td>
    <td> BigInt </td>
    <td> BigInt </td>
  </tr>
  <tr>
    <td> 32 bit float </td>
    <td> float </td>
    <td> float </td>
    <td> f32 </td>
    <td> float </td>
    <td> float (64-bit) </td>
    <td> float64 </td>
    <td> </td>
    <td> decimal(n,k) or double </td>
    <td> decimal(n,k) </td>
  </tr>
  <tr>
    <td> 64 bit float </td>
    <td> double </td>
    <td> double </td>
    <td> f64 </td>
    <td> double </td>
    <td> float </td>
    <td> float64 </td>
    <td> </td>
    <td> decimal(n,k) or double </td>
    <td> decimal(n,k) </td>
  </tr>
  
</table>
</div>


## References 

[Overview of Pandas Data Types](https://pbpython.com/pandas_dtypes.html)

http://www-db.deis.unibo.it/courses/TW/DOCS/w3schools/sql/sql_datatypes_general.asp.html

https://spark.apache.org/docs/latest/sql-ref-datatypes.html

https://numpy.org/devdocs/user/basics.types.htmlo

https://arrow.apache.org/docs/python/generated/pyarrow.decimal128.html