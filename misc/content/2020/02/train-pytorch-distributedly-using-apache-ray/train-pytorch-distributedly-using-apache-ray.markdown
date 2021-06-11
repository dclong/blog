Status: published
Date: 2020-03-01 11:36:44
Author: Benjamin Du
Slug: train-pytorch-distributedly-using-apache-ray
Title: Train PyTorch Distributedly Using Apache Ray
Category: AI
Tags: AI, data science, machine learning, deep learning, PyTorch, distributed, Apache Ray
Modified: 2020-03-01 11:36:44

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Training a Model Implemented in PyTorch

https://github.com/ray-project/ray/tree/master/python/ray/util/sgd/pytorch/examples

[Distributed PyTorch Using Apache Ray](https://ray.readthedocs.io/en/latest/raysgd/raysgd_pytorch.html)

[RaySGD: Distributed Training Wrappers](https://ray.readthedocs.io/en/latest/raysgd/raysgd.html)


## Hyperparameter Optimization for Models Implemented in PyTorch

https://ray.readthedocs.io/en/latest/tune-examples.html

Is the following example running distributed or not?
Do I need to use tags to tell Ray to run it on multiple machines?

```
import torch.optim as optim
from ray import tune
from ray.tune.examples.mnist_pytorch import (
    get_data_loaders, ConvNet, train, test)


def train_mnist(config):
    train_loader, test_loader = get_data_loaders()
    model = ConvNet()
    optimizer = optim.SGD(model.parameters(), lr=config["lr"])
    for i in range(10):
        train(model, optimizer, train_loader)
        acc = test(model, test_loader)
        tune.track.log(mean_accuracy=acc)


analysis = tune.run(
    train_mnist, config={"lr": tune.grid_search([0.001, 0.01, 0.1])})

print("Best config: ", analysis.get_best_config(metric="mean_accuracy"))

# Get a dataframe for analyzing trial results.
df = analysis.dataframe()
```

- data parallelism vs model parallelism  
- use Ring Allreduce (RA) (instead of Parameter Server or Peer to Peer) 
    for synchronization among processes (CPU/GPU on the same node or different nodes)
- Distributed Optimization Algorithm
    - synchronized SGD 
    - asynchronized SGD 
    - 1-bit SGD
    - The Hogwild algorithm
    - Downpour SGD
    - synchronized SGD + large minibatch to reduce update frequency of parameters

## References

[Parallel and Distributed Deep Learning](https://stanford.edu/~rezab/classes/cme323/S16/projects_reports/hedge_usmani.pdf)

[A Comparison of Distributed Machine Learning Platforms](https://cse.buffalo.edu/~demirbas/publications/DistMLplat.pdf)

[Performance Analysis and Comparison of Distributed Machine Learning Systems](https://arxiv.org/pdf/1909.02061.pdf)

[Multiprocessing failed with Torch.distributed.launch module](https://discuss.pytorch.org/t/multiprocessing-failed-with-torch-distributed-launch-module/33056)

https://jdhao.github.io/2019/11/01/pytorch_distributed_training/

[Training Neural Nets on Larger Batches: Practical Tips for 1-GPU, Multi-GPU & Distributed setups](https://medium.com/huggingface/training-larger-batches-practical-tips-on-1-gpu-multi-gpu-distributed-setups-ec88c3e51255)


[DISTRIBUTED COMMUNICATION PACKAGE - TORCH.DISTRIBUTED](https://pytorch.org/docs/stable/distributed.html)

[DistributedDataParallel](https://pytorch.org/docs/master/nn.html#torch.nn.parallel.DistributedDataParallel)

[Distributed data parallel training in Pytorch](https://yangkky.github.io/2019/07/08/distributed-pytorch-tutorial.html)

[Visual intuition on ring-Allreduce for distributed Deep Learning](https://towardsdatascience.com/visual-intuition-on-ring-allreduce-for-distributed-deep-learning-d1f34b4911da)

[Technologies behind Distributed Deep Learning: AllReduce](https://tech.preferred.jp/en/blog/technologies-behind-distributed-deep-learning-allreduce/)

[Writing Distributed Applications with PyTorch](http://seba1511.net/tutorials/intermediate/dist_tuto.html)

https://github.com/ray-project/ray/issues/3609

https://github.com/ray-project/ray/issues/3520

[Accelerating Deep Learning Using Distributed SGD — An Overview](https://towardsdatascience.com/accelerating-deep-learning-using-distributed-sgd-an-overview-e66c4aee1a0c)

[Distributed training of Deep Learning models with PyTorch](https://medium.com/intel-student-ambassadors/distributed-training-of-deep-learning-models-with-pytorch-1123fa538848)

[Scalable Distributed DL Training: Batching Communication and Computation](https://www.aaai.org/ojs/index.php/AAAI/article/view/4465)

https://github.com/dmmiller612/sparktorch

[Awesome Distributed Deep Learning](https://github.com/bharathgs/Awesome-Distributed-Deep-Learning)

[Intro to Distributed Deep Learning Systems](https://medium.com/@Petuum/intro-to-distributed-deep-learning-systems-a2e45c6b8e7)

[Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour](https://arxiv.org/pdf/1706.02677.pdf)
