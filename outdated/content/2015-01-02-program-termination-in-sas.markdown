UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-01-05 09:14:13
Author: Ben Chuanlong Du
Slug: program-termination-in-sas
Title: Program Termination in SAS
Category: Computer Science
Tags: programming, SAS, termination, exit, quit, stop, error

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

To print an error message into the SAS log

    %put ERROR: error_message;

To print a warning message into the SAS log

    %put WARNING: warning_message;

To print a note message into the SAS log

    %put NOTE: note_message;

To terminate an user-defined module in the IML procedure use `stop;`

exit; 
quit;
