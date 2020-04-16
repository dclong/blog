Status: published
Date: 2020-02-18 11:56:57
Author: Benjamin Du
Slug: sort-top-by-cpu-or-memory-usage
Title: Sort top by CPU or Memory Usage
Category: OS
Tags: OS, Linux, top, macOS, top, CPU, memory

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

By default the result of the `top` command is sorted by CPU usage on Linux.
The table below list options to sort the result of the `top` command 
by different criterias on Linux and macOS


|                      | Linux        | macOS         |
|----------------------|--------------|-------------|
| Sort by CPU usage    | top          | top \-o cpu |
| Sort by Memory usage | top \-o %MEM | top \-o mem |

Note: The above table is generated with the help of [TableConvert Online](https://tableconvert.com/).
