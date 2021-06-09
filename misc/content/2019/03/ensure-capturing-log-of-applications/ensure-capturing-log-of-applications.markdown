Status: published
Date: 2020-08-11 08:26:52
Author: Benjamin Du
Slug: a-trick-to-ensure-capturing-log
Title: Ensure Capturing Log of Applications
Category: Computer Science
Tags: programming, logging, log, redirect, redirection, exception

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Logging is critical for debugging applications.
For production applications,
it is best to send log information into a file instead of the standard output
so that the log information is persisted.
One command way to keep log into a file is to redirect standard output into a file.

```Bash
some_command arg1 arg2 > log_file
```

There is some issue with this approach. 
If an exception throws in `some_command arg1 arg2`,
no log is redirected into the log file
as the redirection happens after `some_command` runs sucessfully.
One way to fix the issue is to let the underlying application log into files. directly 
instead of relying on shell redirection. 
However, 
this is not always feasible. 
Another even simple way is to wrap `some_command` into a `try ... catch ...` block
to ensure that `some_command` runs without throwing exceptions
so that the log redirection will always happen.


## References

https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels
