UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-05-17 17:26:53
Title: SAS Error Messages
Slug: sas-error-messages
Category: Computer Science
Tags: SAS, programming, error, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers 
but rather for convenient reference of the author and future improvement.
**
 

## Error Messages

1. NOTE 484-185: Format $DATE was not found or could not be loaded.
This is probably because the variable 
that you try to format to date is a character variable 
while you need a numeric variable. 

2. ERROR 180-322: Statement is not valid or it is used out of proper order.
If this error is macro related, 
then it is probably because the macro is not defined


3. NOTE 49-169: 
This is a warning not an error. It is caused by quotation marks followed by semicolon. 
The recommended way to fix this warning is to restart SAS (Enterprise Guide).

4.  Usage Note 49014: 
This is probably because there are no space on the disk 
or you have reached the limit of number of opened files. 
If the latter, restart SAS can often solve the problem.

5. The following error might due to no permission the databases.
Make you have access to the database
and have updated your password on the SAS Grid server.

        17                              CONNECT TO &AMLPTERA.;
                                                             _
                                                             22
        ERROR 22-322: Expecting a name.  




Error Message:
ERROR: Cannot open %INCLUDE file GOPTIONS.
Possible Reason:
The ending ";" is missing.

Error Message:
ERROR: Matrix has not been assigned a value.
Possible Reason
it is possible that you passed an invalid parameter

ERROR: (execution) Invalid subscript or subscript out of range.

SAS submatrix, slicing, if loc returns no element then problemamtic

assign a matrix to an incompatible matrix might not cause any error but stops the program, very tricky!!!

ERROR: (execution) Matrix has not been set to a value.
probably due to miss used argument, e.g., typo, etc.

Unable to read the SAS report file
Change the result format to HTML by selecting Tools ► Options ► Results, deselecting SAS Report, and selecting HTML.

ERROR: There are no valid observations.
Reason: All values of a column are missing.
