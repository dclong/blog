Status: published
Date: 2020-04-21 11:51:30
Author: Benjamin Du
Slug: use-pytorch-on-gpu
Title: Use PyTorch on GPU
Category: AI
Tags: AI, data science, machine learning, deep learning, PyTorch, GPU
Modified: 2020-04-21 11:51:30

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## PyTorch on GPU

https://pytorch.org/docs/master/notes/cuda.html

You can use the command `torch.cuda.is_available()`
to check whether GPU is available for PyTorch.
Details of GPUs can be obtained using the following code.


    :::bash
    In [1]: import torch

    In [2]: torch.cuda.current_device()
    Out[2]: 0

    In [3]: torch.cuda.device(0)
    Out[3]: <torch.cuda.device at 0x7efce0b03be0>

    In [4]: torch.cuda.device_count()
    Out[4]: 1

    In [5]: torch.cuda.get_device_name(0)
    Out[5]: 'GeForce GTX 950M'

    In [6]: torch.cuda.is_available()
    Out[6]: True

You can force synchronous computation by setting environment variable CUDA_LAUNCH_BLOCKING=1. 
This can be handy when an error occurs on the GPU. 
(With asynchronous execution, such an error isn’t reported until after the operation is actually executed, 
so the stack trace does not show where it was requested.)

## Make Sure that PyTorch is Using GPU

https://discuss.pytorch.org/t/solved-make-sure-that-pytorch-using-gpu-to-compute/4870

## GPU vs CPU Performance 

My personal experience sees a speed up of 3 - 30 using a single GeForce GTX 1080 GPU vs CPU. 
Generally speaking,
the more complicated your neural network is, 
the more speed up you get. 
Also be careful about IO bound when you train simple neural networks in Docker (which is what most people do)
as Docker seems to have issues with a multiprocessing (`num_workers > 0`) DataLoader. 