Status: published
Date: 2020-04-09 13:30:28
Author: Benjamin Du
Slug: save-and-load-pytorch-models
Title: Save and Load PyTorch Models
Category: Computer Science
Tags: Computer Science, deep learning, data science, machine learning, PyTorch, save, load, serialization, deserialization

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. PyTorch uses pickle to serialize and deserialize objects.

2. The PyTorch convention is 
    to use the file extension `.pt` or `.pth` for saving model (or its parameters)
    and use the file extension `.tar` for saving checkpoints.

3. It is preferred to save model parameters rather than the whole model.

## References

[SAVING AND LOADING MODELS](https://pytorch.org/tutorials/beginner/saving_loading_models.html)

[SERIALIZATION SEMANTICS](https://pytorch.org/docs/master/notes/serialization.html)