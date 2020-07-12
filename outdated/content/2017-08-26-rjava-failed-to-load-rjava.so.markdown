UUID: e23473cf-f47a-4ffc-af77-c1caf7f2fcad
Status: published
Date: 2017-09-06 08:01:26
Author: Ben Chuanlong Du
Slug: rjava-failed-to-load-rjava.so
Title: rJava Failed to Load rJava.So
Category: Computer Science
Tags: programming

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

rJava failed to load rJava.so and libjvm.so

Reconfigure Java for R using the command below resolves the issue.

    sudo R CMD javareconf
