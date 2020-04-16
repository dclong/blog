Status: published
Date: 2020-03-03 11:02:27
Author: Benjamin Du
Slug: training-deep-neural-networks
Title: Training Deep Neural Networks
Category: AI
Tags: AI, machine learning, data science, deep learning, deep neural network, DNN

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Rules of Thumb for Training

https://arxiv.org/pdf/1206.5533.pdf**

https://towardsdatascience.com/17-rules-of-thumb-for-building-a-neural-network-93356f9930af

https://hackernoon.com/rules-of-thumb-for-deep-learning-5a3b6d4b0138

https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw

## Terminology

1 Epoch = 1 Forward pass + 1 Backward pass for ALL training samples.
Batch Size = Number of training samples in 1 Forward/1 Backward pass. (With increase in Batch size, required memory space increases.)
Number of iterations = Number of passes i.e. 1 Pass = 1 Forward pass + 1 Backward pass (Forward pass and Backward pass are not counted differently.)

In neural networks generally, an epoch is a single pass through the full training set. 
You don't just run through the training set once, 
it can take thousands of epochs for your backpropagation algorithm to converge on a combination of weights with an acceptable level of accuracy. 
Remember gradient descent only changes the weights by a small amount in the direction of improvement, 
so backpropagation can't get there by running through the training examples just once.




https://mp.weixin.qq.com/s?__biz=MzUxNjcxMjQxNg==&mid=2247488694&idx=1&sn=167b8b9897165d3dcb285ffd12ff7aef&scene=21#wechat_redirect

https://mp.weixin.qq.com/s/aW9yF15lPQWIrQTPu8ki2A

https://jeffmacaluso.github.io/post/DeepLearningRulesOfThumb/

https://pcc.cs.byu.edu/2017/10/02/practical-advice-for-building-deep-neural-networks/

http://theorangeduck.com/page/neural-network-not-working

https://zhuanlan.zhihu.com/p/59918821

https://ml-cheatsheet.readthedocs.io/en/latest/index.html

https://karpathy.github.io/2019/04/25/recipe/

When the minibatch size is multiplied by k, multiply the learning rate by k.

## Regularization

DNNs are prone to overfitting because of the added layers of abstraction, 
which allow them to model rare dependencies in the training data. 
Regularization methods such as Ivakhnenko's unit pruning[29] 
or weight decay ( {\displaystyle \ell _{2}} \ell _{2}-regularization) 
or sparsity ( {\displaystyle \ell _{1}} \ell _{1}-regularization) can be applied during training to combat overfitting.[111] 
Alternatively dropout regularization randomly omits units from the hidden layers during training. 
This helps to exclude rare dependencies.[112] 
Finally, 
data can be augmented via methods such as cropping and rotating 
such that smaller training sets can be increased in size to reduce the chances of overfitting.[113]

## References

https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9
