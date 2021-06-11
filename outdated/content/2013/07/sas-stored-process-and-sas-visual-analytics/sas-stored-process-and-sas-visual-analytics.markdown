UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: SAS Stored Process and SAS Visual Analytics
Date: 2016-07-13 22:11:25
Tags: sas, visualization, stored process, visual analytics, software
Category: Software
Slug: sas-stored-process-and-sas-visual-analytics
Author: Ben Chuanlong Du
Modified: 2016-07-13 22:11:25

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 

## SAS Stored Process

1. %stpbegin and %stpend initialize the output delivery system (ODS).
They are not needed if you don't have to use ODS.

4. *ProcessBody; (don't forget the semicolon, this an example of using comment as markup)

2. It seems that SAS 9.2 is messy on this,
so be aware of the version of SAS that you are using.

5. It it recommended that you begin all stored process
(regardless of the server types)
with %global declarations for all of you input parameters
followed by the *ProcessBody; comment.
In SAS 9.3, the *ProcessBody; is not needed

6. Special characters:
ampersand (&), apostrophe('), percent sign (%), quotation marks ("),
and semicolon (;).
Be care about accepting these characeters from user client.

7. accepting multiple values is messy and can result in errors if input values is the same as one of the generated variables ....

8. use masked single line for password entry

9. It's suggested that you always require non-blank input for a textbox.
Otherwise, the stored process might run without prompt on SVA.

10. it's recommended to store source code in metadata (available in sas 9.3)

11. the header function (stpsrv_header) must be placed before any code that writes results to _webout.)

12. The stpsrv_header is data step function used to add or modify a header

## SAS Visual Analytics

1. To insert the Stored Process, 
navigate to "Insert->Other->Stored Process".

1. use the original address fix the problem of SAS Visual Analytics

2. SVA is for large data, 
but since we work on servers, we have to upload data. 
How much time do we need to upload, e.g., 10G data in an average corparate network?

