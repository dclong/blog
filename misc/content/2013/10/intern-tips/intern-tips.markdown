UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Some Tips for Intern Projects
Date: 2019-03-30 17:25:44
Slug: intern-tips
Category: Software
Tags: tips
Modified: 2019-03-30 17:25:44

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 


## Business Resources

1. [Investopedia](http://www.investopedia.com/)

2. [National Council of Real Estate Fiduciaries (NCREIF)](http://www.ncreif.org/)

3. [Google Finance](http://www.google.com/finance)

4. [Federal Reserve](http://www.federalreserve.gov/default.htm)

5. [Federal Housing Finance Agency](http://www.fhfa.gov/)

## Different Models

1. Top Down Model

    Treat all loans in a portfolio as a whole and build a single model.

2. Bottom Up Model

    Build a model for each loan in a profile and then sum them together.

## Accumulated Experience Before

1. We have to avoid overfitting.
    Generally speaking, we can use 1 more covariate with 30 more time points.

2. With 80 time points, we have around 5 covariates.

## Teller

1. Fair Credit Reporting Act

## Some Thoughts

1. In industry, most people care about whether a solutions works.
    They usually don't care about whether it's the best, especially these companies that
    make money easily, e.g. banks. They are usually very converative about new technologies and methods.

2. Even if you can do things perfect, leave some space for others to criticize you.
    And then you improve your work. This is really smart office strategy.


## Some Ideas
### Top-down and Bottom-up Models
1. use weighted average to predict future, 
    I think this is a very good idea

2. used weighted obs to estimate parameters (do some research on this) 

3. there are several different models used 
    and each of them takes a different approach,
    We can aggregate these different models and presumably come up with a better one

4. I think it's good idea to keep old models and compare all of them.
    Yes, it's a good idea to build a website and put everything their, 
    code, documentation and well implemented model embeded in website. 
    Compare them!
    This reduces much work, improves efficiency ...
    In short, first, keep old project,
    second, keep old model implementation for comparision

5. If the top-down model is so good, 
    why don't we use confidence intervals to triangulate portfolio loss?

### About Clustering

1. I think pre-grouping is probably not a good idea.
    I'm thinking about treat all companies individually and cluter them.
    There are some problems in this approach.
    First, there are missing values. We can overcome this by shortening vectors.
    The most important thing is that this makes the work harder to do.

### About Modeling EDF (or PD)

1. What if we don't use median, but put a distribution on all loans in a portfolio?
    This sounds like a good idea.

2. What I worry about is that there are many loans jumping between different buckets.

### YoY vs QoQ annualized

YoY is more smooth, QoQ presumably can catch local change better

### Projects

#### EDF 

1. I found that 0 stands for missing value.

2. get clear about range of Moody's EDF data, this is helpful to argue that the model
    used by Moody's was changed at 2008 (different from before).
