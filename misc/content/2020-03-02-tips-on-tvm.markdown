Status: published
Date: 2020-03-02 18:30:38
Author: Benjamin Du
Slug: tips-on-tvm
Title: Tips on TVM
Category: AI
Tags: AI, data science, machine learning, deep learning, TVM, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
TVM is an open deep learning compiler stack for CPUs, GPUs, and specialized accelerators. 
It aims to close the gap between the productivity-focused deep learning frameworks, 
and the performance- or efficiency-oriented hardware backends. TVM provides the following main features:

- Compilation of deep learning models in Keras, MXNet, PyTorch, Tensorflow, CoreML, DarkNet into minimum deployable modules on diverse hardware backends.
- Infrastructure to automatic generate and optimize tensor operators on more backend with better performance.

In short, 
TVM to deep learning is kind of like LLVM to programming languages.

## References

https://github.com/apache/incubator-tvm

https://discuss.tvm.ai/

https://tvm.apache.org/blog
