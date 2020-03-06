Status: published
Date: 2020-03-06 12:12:10
Author: Benjamin Du
Slug: subword-algorithms-for-nlp
Title: Subword Algorithms for NLP
Category: AI
Tags: AI, data science, machine learning, deep learning, NLP, subword algorithm, BPE, WordPiece, Unigram Language Model

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Classic word representation cannot handle unseen word or rare word well. 
Character embeddings is one of the solution to overcome out-of-vocabulary (OOV). 
However, 
it may be too fine-grained and miss some important information. 
Subword is in between word and character. 
It is not too fine-grained while able to handle unseen word and rare word.

## General Tips

1. Subword balances vocabulary size and footprint. 
    Extreme case is we can only use 26 token (i.e. character) to present all English word. 
    16k or 32k subwords are recommended vocabulary size to have a good result.
    Many Asian language word cannot be separated by space. 
    Therefore, 
    the initial vocabulary is larger than English a lot. 
    You may need to prepare over 10k initial word to kick start the word segmentation. 
    From Schuster and Nakajima research, 
    they propose to use 22k word and 11k word for Japanese and Korean respectively.

## Byte Pair Encoding (BPE)

Sennrich et al. (2016) proposed to use Byte Pair Encoding (BPE) to build subword dictionary. 
Radfor et al adopt BPE to construct subword vector to build GPT-2 in 2019.

## WordPiece

WordPiece is another word segmentation algorithm and it is similar with BPE. 
Schuster and Nakajima introduced WordPiece by solving Japanese and Korea voice problem in 2012. 
Basically, 
WordPiece is similar with BPE and the difference part is forming a new subword by likelihood but not the next highest frequency pair.

## Unigram Language Model

Kudo. introduced unigram language model as another algorithm for subword segmentation. One of the assumption is all subword occurrence are independently and subword sequence is produced by the product of subword occurrence probabilities. Both WordPiece and Unigram Language Model leverages languages model to build subword vocabulary.

## References

[3 subword algorithms help to improve your NLP model performance](https://medium.com/@makcedward/how-subword-helps-on-your-nlp-model-83dd1b836f46)

[SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing](https://arxiv.org/pdf/1808.06226.pdf)