UUID: b08eb030-a54a-4f19-8006-e1d5ce10125d
Status: published
Date: 2015-05-17 18:54:39
Author: Ben Chuanlong Du
Slug: create-a-directory-using-sas
Title: Create a Directory Using SAS
Category: Computer Science
Tags: programming, SAS, directory, file system, filesystem, create, dcreate

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

you can use the function dcreate to create a directory in sas
sas: created don't use "~" in the path, can cause problems
```SAS
x mkdir path;
```

```SAS
new-directory=DCREATE(dir-name<,parent-dir>);
```
too stupid, cannot use dcreate(...); must assigned the return results to another variable.
This applies to other function/calls in sas ...
x mkdir ...; in much more convenient to create directory in sas
dcreate does not recognize "~" while the unix/linux command way can recognize it!!!




