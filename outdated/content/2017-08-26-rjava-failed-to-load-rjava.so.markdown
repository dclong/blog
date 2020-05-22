UUID: e23473cf-f47a-4ffc-af77-c1caf7f2fcad
Status: published
Date: 2017-09-06 08:01:26
Author: Ben Chuanlong Du
Slug: rjava-failed-to-load-rjava.so
Title: rJava Failed to Load rJava.So
Category: Computer Science
Tags: programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

rJava failed to load rJava.so and libjvm.so

Reconfigure Java for R using the command below resolves the issue.

    sudo R CMD javareconf
