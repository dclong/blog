Status: published
Date: 2020-04-06 18:22:00
Author: Ben Chuanlong Du
Slug: advanced-use-head-tail
Title: Advanced Use of "head" and "tail" 
Category: OS
Tags: Linux, shell, command line, head, tail, sed, awk, rows, lines, text manipulation

It is suggested that you **use Python instead of Shell** to manipulate text files!!

Besides passing an unsigned integer as parameter to the option `-n`, 
you can also pass a signed integer to it.
When a signed integer is passed to `-n`, 
it means from/to (inclusive/exclusive similar to most programming languages) the row with this index (1-based). 
More specifically, 
`head -n +/-k` means take rows 1 (inclusive) to `+/-k` (exclusive).
`tail -n +/-k` means take rows `+/-k` (inclusive) to the last row. 
Below are some examples to help you fruther understand how it works.

1. Print all but the last `5` lines.

        # -5 means without the last 5 lines  
        head -n -5 file_name


2. Print lines 6 and after (i.e., all but the first `5` lines).

        # +6 means starting from line 6  
        tail -n +6 file_name 

3. Print lines 10 to 20.

        head -n 20 file_name | tail -n +10  
        # or you can use (11 = 20 - 10 + 1)
        tail -n +10 file_name | head -n 11

    Please refer to 
    [Print Rows from a Text File](http://www.legendu.net/en/blog/print-rows-from-a-text-file/)
    for better ways using `sed` and `awk`. 
