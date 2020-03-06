UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Java Packages
Date: 2017-06-11 12:03:35
Tags: programming, package, Java
Category: Computer Science
Slug: java-packages
Author: Ben Chuanlong Du

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Date Time
joda time and java.time

## Appach Common

### Appach CommonMath

1. StatUtils.varance is OK.

## Colt

1. `sample` of `RandomSample` is OK.

## Parallel Colt

1. ParallelColt does not make RNG parallized.

## Comparison of Packages

1. Colt is faster in random number generating than CommonMath,
especially for simple random number generation (e.g. normal random numbers), 
but Colt is no longer maintained.

2. The RNGs in Colt, Parallel Colt and CommonMath are all OK from statistical view.

