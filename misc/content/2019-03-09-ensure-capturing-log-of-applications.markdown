Status: published
Date: 2019-03-09 23:49:57
Author: Benjamin Du
Slug: a-trick-to-ensure-capturing-log
Title: Ensure Capturing Log of Applications
Category: Programming
Tags: programming, logging, rediction, exception

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Logging is critical for debugging applications.
For production applications,
it is best to send log information into a file instead of the standard output
so that the log information is persisted.
One command way to keep log into a file is to redict standard output into a file.

```Bash
some_command arg1 arg2 > log_file
```

There is some issue with this approach. 
If an exception throws in `some_command arg1 arg2`,
no log is redicted into the log file
as the rediction happens after `some_command` runs sucessfully.
One way to fix the issue is to let the underlying application log into files. directly 
instead of relying on shell redirection. 
However, 
this is not always feasible. 
Another even simple way is to wrap `some_command` into a `try ... catch ...` block
to ensure that `some_command` runs without throwing exceptions
so that the log redirection will always happen.
