Status: published
Date: 2020-03-09 14:49:37
Author: Benjamin Du
Slug: tips-on-nlp
Title: Tips on NLP
Category: AI
Tags: AI, machine learning, data science, NLP, nature language processing

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

https://blog.floydhub.com/
is a great place for deep learning blogging.

## Overview of NLP

[Deep Learning for NLP: An Overview of Recent Trends](https://medium.com/dair-ai/deep-learning-for-nlp-an-overview-of-recent-trends-d0d8f40a776d)
Chapter 8 of the book (Performance of Different Models on Different NLP Tasks) also summarizes the state-of-the-art methods 
fore each sub area of NLP. 

[Ten trends in Deep learning NLP](https://blog.floydhub.com/ten-trends-in-deep-learning-nlp/)

http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/

https://github.com/Oxer11/NLP-task-review


https://nlpoverview.com/

https://arxiv.org/pdf/1703.03906.pdf

The transformer architecture, which was first published at the end of 2017, 
addresses this by creating a way to allow parallel inputs. 
Each word can have a separate embedding and be process simultaneously 
which greatly improves training times which facilitates training on much larger datasets.

Google's BERT and OpenAI's GPT-2 models are based on Transformer.

transformer-XL




## Semantics vs Syntactic

https://medium.com/huggingface/learning-meaning-in-natural-language-processing-the-semantics-mega-thread-9c0332dfe28e

## Coreferences

https://medium.com/huggingface/state-of-the-art-neural-coreference-resolution-for-chatbots-3302365dcf30

https://huggingface.co/coref/

https://github.com/huggingface/neuralcoref

## Machine Translation 

Transformer

In machine translation, 
self-attention also contributes to impressive results. 
For example, 
recently a model, named Transformer, 
was introduced in a paper with a rather bold title “Attention Is All You Need” [Vaswani, 2017]. 
As you can guess, 
this model relies only on self-attention without the use of RNNs. 
As a result, 
it is highly parallelizable and requires less time to train, while establishing state-of-the-art results on WMT2014.


Large embeddings with 2048 dimensions
achieved the best results, but only by a small
margin. Even small embeddings with 128 dimensions seem to have sufficient capacity to
capture most of the necessary semantic information.
• LSTM Cells consistently outperformed GRU
Cells.
• Bidirectional encoders with 2 to 4 layers performed best. Deeper encoders were significantly more unstable to train, but show potential if they can be optimized well.
• Deep 4-layer decoders slightly outperformed
shallower decoders. Residual connections
were necessary to train decoders with 8 layers and dense residual connections offer additional robustness.
• Parameterized additive attention yielded the
overall best results.
A well-tuned beam search with length
penalty is crucial. Beam widths of 5 to 10
together with a length penalty of 1.0 seemed
to work well.

## seq2seq 

https://github.com/IBM/pytorch-seq2seq


## Attention

The article [Attention in NLP](https://medium.com/@joealato/attention-in-nlp-734c6fa9d983)
has a very detailed summary of development and applications of Attention in NLP.


## Libraries 

[SpaCy](https://github.com/explosion/spaCy)
is an industrial-strength Natural Language Processing (NLP) library.


[transformers](https://github.com/huggingface/transformers)
(formerly known as pytorch-transformers and pytorch-pretrained-bert) 
provides state-of-the-art general-purpose architectures (BERT, GPT-2, RoBERTa, XLM, DistilBert, XLNet, CTRL...) 
for Natural Language Understanding (NLU) and Natural Language Generation (NLG) 
with over 32+ pretrained models in 100+ languages and deep interoperability between TensorFlow 2.0 and PyTorch.

[OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py)

https://github.com/jadore801120/attention-is-all-you-need-pytorch

https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/models/transformer.py

https://github.com/google/seq2seq

[gensim](https://github.com/RaRe-Technologies/gensim)


## Data 

[CoLA: The Corpus of Linguistic Acceptability](https://nyu-mll.github.io/CoLA/)

## References

https://medium.com/towards-artificial-intelligence/cross-lingual-language-model-56a65dba9358

https://github.com/huggingface/transformers
