Status: published
Date: 2020-01-08 11:26:35
Author: Benjamin Du
Slug: compresion-of-deep-learning-models
Title: Compresion of Deep Learning Models
Category: AI
Tags: AI, data science, machine learning, deep compression, compression

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding

MobileNet


一、网络修剪

网络修剪，采用当网络权重非常小的时候(小于某个设定的阈值)，把它置0，就像二值网络一般；然后屏蔽被设置为0的权重更新，继续进行训练；以此循环，每隔训练几轮过后，继续进行修剪。

二、权重共享

对于每一层的参数,我们进行k-means聚类,进行量化，对于归属于同一个聚类中心的权重，采用共享一个权重,进行重新训练。需要注意的是这个权重共享并不是层之间的权重共享，这是对于每一层的单独共享。

三、增加L2权重

增加L2权重可以让更多的权重，靠近0，这样每次修剪的比例大大增加。

四、从结构上，简化网络计算

这些需自己阅读比较多相关文献，才能设计出合理，速度更快的网络，比如引入fire module、NIN、除全连接层等一些设计思想，这边不进行具体详述。


[Distilling knowledge from Neural Networks to build smaller and faster models](https://blog.floydhub.com/knowledge-distillation/)

## References

https://blog.floydhub.com/knowledge-distillation/

https://mp.weixin.qq.com/s?__biz=MzU0NTAyNTQ1OQ==&mid=2247484793&idx=1&sn=d18b5f6a0b278d24ee5589dec5d72f9a&chksm=fb7279a5cc05f0b3edce2f2e87467a34dd4e3cda042312082bc5591e438a4dca31044762977d&scene=21#wechat_redirect
