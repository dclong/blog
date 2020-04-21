UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2014-11-23 20:37:11
Author: Ben Chuanlong Du
Slug: keywords extracting from text
Title: Keywords Extracting from Text
Category: AI
Tags: machine learning, text mining, data mining, data science

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Word Stemming

1. existing stemming method such as NLTK.PorterStem, etc.

2. didn't -> did not, there's -> there is, etc.
Mr. -> Mister
Mrs. -> ...
Ms. -> ...

## Other things

1. it seems that it is hard to get useful information using 1-gram

2. URLs in text are often important and is relatively easy to extract. 

3. After handing URLs, you can replace "/" and "." with spaces to avoid confusing them with real long words.


2. long words often contain useful information, 
however, you have to be careful about  words of the form "and/or", etc.
And do not confuse it with URLs.


3. the idea of keeping upper/lower quantile (e.g., 5%) of long words, 2-grams, etc. is a very good idea
