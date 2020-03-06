Status: published
Date: 2020-03-06 11:29:11
Author: Benjamin Du
Slug: terminologies-concepts-in-nlp
Title: Terminologies and Concepts in NLP
Category: AI
Tags: AI, data science, machine learning, deep learning, NLP

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Terminologies

cross-lingual language models (XLM)
Cross-lingual Natural Language Inference (XNLI)

### Causal Language Modeling (CLM)

CLM consists of a Transformer to learn text representation by providing a set of previous features. 
Given the previous hidden state to the current batch, the model predicts the next word.

### Masked Language Modeling (MLM)

Lample and Connea follow Devlin et al. (2018) approach to pick 15% of subword randomly 
and replacing it by reserved word ([MASK]) 80% of the time, 
by a random word 10% of the time 
and remaining unchanged 10% of the time.
The differences between Devlin et al. (2018) are:

- Using an arbitrary number of sentences but not pairs of sentences only
- Subsample high-frequency subword

### Translation Language Modeling (TLM)
out-of-vocabulary (OOV)
byte pair encoding (BPE) subword algorithm


## References 

https://medium.com/towards-artificial-intelligence/cross-lingual-language-model-56a65dba9358