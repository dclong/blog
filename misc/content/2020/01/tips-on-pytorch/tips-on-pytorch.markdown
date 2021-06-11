Status: published
Date: 2020-01-18 00:39:50
Author: Benjamin Du
Slug: tips-on-pytorch
Title: Tips on PyTorch
Category: Computer Science
Tags: programming, Python, PyTorch, GPU, tips
Modified: 2020-11-18 00:39:50

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## PyTorch Installation

cuda and cuDNN are not required to install PyTorch
unless you build PyTorch from source.

https://github.com/pytorch/pytorch/issues/17445

https://github.com/pytorch/pytorch/issues/698

https://discuss.pytorch.org/t/how-to-check-if-torch-uses-cudnn/21933

https://discuss.pytorch.org/t/newbie-question-what-are-the-prerequisites-for-running-pytorch-with-gpu/698

## Docker Images for PyTorch

The official PyTorch image [pytorch/pytorch:latest](https://hub.docker.com/r/pytorch/pytorch) 
(which is pytorch/pytorch:1.4-cuda10.1-cudnn7-runtime currently)
is a good one.



## PyTorch Tutorials

https://pytorch.org/tutorials/beginner/pytorch_with_examples.html

torch.Sequential is an easy and quick way to construct simple neural netowrks.
For more complicated neural network architextures, 
you'd better implement your own class extending torch.nn.Module.

## Configuration

cudnn.benchmark = true -- uses the inbuilt cudnn auto-tuner to find the fastest convolution algorithms.
                       -- If this is set to false, uses some in-built heuristics that might not always be fastest.

Regarding cudnn.fastest, 
I think it’s because by default it also tries not to use very much memory, 
but when you enable fastest, 
it doesn’t care.

See https://github.com/soumith/cudnn.torch/blob/master/SpatialConvolution.lua#L167-L174

regarding cudnn.benchmark, 
if you have variable length sequences given as inputs, 
benchmark will try to auto-tune for every new input shape, 
and that will result in a huge slowdown.

https://pytorch.org/docs/master/notes/cuda.html#device-agnostic-code
This is the suggested way to control tensors on CPU/GPU. 

## Train and Evaluate Models in PyTorch

model.train() tells your model that you are training the model. 
So effectively layers like dropout, batchnorm etc. 
which behave different on the train and test procedures know what is going on and hence can behave accordingly.

More details: It sets the mode to train (see source code). 
You can call either model.eval() or model.train(mode=False) to tell that you are testing. 
It is somewhat intuitive to expect train function to train model but it does not do that. It just sets the mode.

The bottom line is that 
if you use dropout or batch normalization in PyTorch, 
then you must explicitly set your model into evaluation mode 
by calling the eval() function mode when computing model output values.

It is suggested that you always call the method `.train()` explicitly 
to turn on training mode before you train your model
and call the method `.eval()` explicitly 
to turn on evaluation mode before you run your model for outputs.


https://jamesmccaffrey.wordpress.com/2019/01/23/pytorch-train-vs-eval-mode/

https://stackoverflow.com/questions/51433378/what-does-model-train-do-in-pytorch

https://discuss.pytorch.org/t/trying-to-understand-the-meaning-of-model-train-and-model-eval/20158/2

## PyTorch Tutorials

https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e

https://github.com/pytorch/examples

## Use PyTorch Models in Production

https://medium.com/datadriveninvestor/deploy-your-pytorch-model-to-production-f69460192217

https://pytorch.org/tutorials/advanced/super_resolution_with_caffe2.html

## Questions

> There are significant caveats to using CUDA models with multiprocessing; 
> unless care is taken to meet the data handling requirements exactly, 
> it is likely that your program will have incorrect or undefined behavior.

Apache Ray is essentially multiprocessing, right? 
How does Apache Ray work with PyTorch?

2. shall we every use `inplace=True` when manipulating Layers in PyTorch?

## PyTorch Ecosystem

torchvision: Popular deep learning models for computer vision.

torchtext: Data loaders and abstractions for text and NLP.

torchaudio: Data manipulation and transformation for audio signal processing, powered by PyTorch.

[pytorch_geometric](https://github.com/rusty1s/pytorch_geometric)
is a geometric deep learning extension library for PyTorch.

[PyTorch Hub](https://pytorch.org/hub/) has pretrained deep learning models 
that anyone can download.

[PyTorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning)
The lightweight PyTorch wrapper for ML researchers. 
Scale your models. 
Write less boilerplate 

Note: PyTorch Lightning is very close to what I've done ...

## References

https://stackoverflow.com/questions/48152674/how-to-check-if-pytorch-is-using-the-gpu

https://medium.com/ai%C2%B3-theory-practice-business/use-gpu-in-your-pytorch-code-676a67faed09

https://groups.google.com/forum/#!topic/torch7/CkB57025yRY

[PyTorch Stable Downloads](https://download.pytorch.org/whl/torch_stable.html)