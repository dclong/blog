Status: published
Date: 2020-03-17 11:27:12
Author: Benjamin Du
Slug: preparing-data-for-ai
Title: Preparing Data for AI
Category: Computer Science
Tags: Computer Science

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**



1. When you label individual images,
    it is better to use numerical labels 
    (even though text labels are easier to understand)
    so that you can avoid mapping between numbers (use for training)
    and text labels (for human understanding) all the time.

2. If you have no labeled data to start at all,
    do NOT hurry to jumping into labeling yet. 
    Develop a simple rule based algorithm to help you label your data first if feasible.
    After you have some lable data, 
    you can then start to build a model and then leverage it for labeling new data. 
    Iterate this process a few times, 
    you will then collect enough data for modeling.
    If the an intermediate model is not that accurate at labeling new data,
    leverage the prediction of probabilities to divide labeling of new data into high/mid/low confidence groups. 
    This might help you reduce some human judgement time.



[Labeling Data for AI](http://www.legendu.net/misc/blog/labeling-data-for-ai/)