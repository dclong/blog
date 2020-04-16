Status: published
Date: 2020-02-27 10:57:44
Author: Benjamin Du
Slug: tips-on-tensorflow
Title: Tips on TensorFlow
Category: AI
Tags: AI, data science, machine learning, TensorFlow, GPU

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation

The article
[Stop Installing Tensorflow using pip for performance sake!](https://towardsdatascience.com/stop-installing-tensorflow-using-pip-for-performance-sake-5854f9d9eb0c)
suggest installing TensorFlow using conda instead of pip
as the version installed by conda leverages Intel Math Kernel Library 
and is about 8 times faster **on CPU**.

https://www.anaconda.com/tensorflow-in-anaconda/


cuDNN is required by TensorFlow

    :::bash
    pip install tensorflow

https://www.tensorflow.org/install/gpu

https://www.tensorflow.org/install/docker

https://www.tensorflow.org/install/pip

## Docker Images

https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles/dockerfiles


https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/dockerfiles/dockerfiles/gpu.Dockerfile
uses pip (instead of conda) to install Python packages.

## General Tips

1. With TensorFlow 2.0, 
    you should use `tf.keras` instead of the separate Keras package.

https://www.pyimagesearch.com/2019/10/21/keras-vs-tf-keras-whats-the-difference-in-tensorflow-2-0/

## Tutorials

https://www.tensorflow.org/guide/keras/

https://www.tensorflow.org/tutorials/keras/classification
https://www.tensorflow.org/tutorials/quickstart/beginner
https://www.tensorflow.org/guide/keras/functional
https://www.tensorflow.org/guide/keras/train_and_evaluate
https://www.tensorflow.org/guide/keras/custom_layers_and_models
https://www.tensorflow.org/guide/keras/masking_and_padding

[Inside TensorFlow: tf.Keras (part 1)](https://www.youtube.com/watch?v=UYRBHFAvLSs&feature=youtu.be)
[Inside TensorFlow: tf.Keras (part 2)](https://www.youtube.com/watch?v=uhzGTijaw8A&feature=youtu.be)
[TensorFlow 2.0 Full Tutorial - Python Neural Networks for Beginners](https://www.youtube.com/watch?v=6g4O5UOH304)

## GPU Runs Out of Memory

https://stackoverflow.com/questions/36927607/how-can-i-solve-ran-out-of-gpu-memory-in-tensorflow

https://stackoverflow.com/questions/34199233/how-to-prevent-tensorflow-from-allocating-the-totality-of-a-gpu-memory

https://superuser.com/questions/980216/what-happens-when-the-gpu-memory-is-not-enough

## Deep Learning Libraries Based on TensorFlow

[trax](https://github.com/google/trax)
