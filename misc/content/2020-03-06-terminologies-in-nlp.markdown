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

Word Embedding
Character Embedding
Subword Embeddling
Tokenization

General Language Understanding Evaluation (GLUE)

Natural Language Generation (NLG)
Natural Language Generation, as defined by Artificial Intelligence: Natural Language Processing Fundamentals, is the “process of producing meaningful phrases and sentences in the form of natural language.” In its essence, it automatically generates narratives that describe, summarize or explain input structured data in a human-like manner at the speed of thousands of pages per second.

Multi-Genre Natural Language Inference (MultiNLI)

Named Entity Recognition (NER) 


Heuristic Analysis for NLI Systems (HANS)

## Data Related

The Stanford Question Answering Dataset (SQuAD)

Situations With Adversarial Generations (SWAG)

Reading Comprehension Dataset (RACE) 

The Cross-Lingual NLI Corpus (XNLI)

## Model Related

Generative Pre-Training (GPT)

### Cross-lingual Language Models (XLM)

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

CLM and MLM are designed for monolingual data while TLM targets on cross-lingual data. BERT use segment embeddings to represent different sentence in a single sequence of input while replace it by language embeddings to represent different language.
Subwords are randomly picked in both language data. Both language subword can be leveraged to predict any MASK word.

### Out-of-Vocabulary (OOV)

### Byte Pair Encoding (BPE) Subword Algorithm

## Take Away
- BERT use segment embeddings (represent different sentence) while XLM use language embeddings (represent different language).
- CLM does not scale to a cross-lingual scenario.
- XLM may not fit for low resource language as if required parallel data (TML) to boost up the performance. Meanwhile, Multilingual Neural Language Models are designed to overcome this limitation.

## References 

[Cross-lingual Language Model](https://medium.com/towards-artificial-intelligence/cross-lingual-language-model-56a65dba9358)

[A Comprehensive Guide to Natural Language Generation](https://medium.com/sciforce/a-comprehensive-guide-to-natural-language-generation-dd63a4b6e548)