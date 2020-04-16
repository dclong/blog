Status: published
Date: 2020-03-08 22:15:55
Author: Benjamin Du
Slug: machine-learning-libraries-computing-frames-programming-languages
Title: Machine Learning Libraries, Computing Frames and Programming Languages
Category: AI
Tags: AI, machine learning, data science, computing frameworks, programming languages, GPU, Python, Rust

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



1. GPU is more accisible for average individual people.
    GPU is still the main tool for deep learning right now.

2. Python Distributed Computing Frameworks (Ray, Modin, etc.)
    servers as a mid solution between GPU and Spark. 
    It can handle more data than GPU but less then Spark.
    Ray, Modin, etc is easier to use and maintain than Spark.

3. Even though there are many libraries making it possible to run deep learning on Spark,
    I still don't it is the right choice unless you have really large data 
    that cannot be handled by other frameworks.
    There are rarely such situations.
    Real big data mostly occur in the ETL and preprocessing stage 
    rather than in the model training stage.

4. Python and Rust are good choices. 
    C is not productive. 
    C++ is too complicated.
    JVM-based languages are first-class citizens for production.
    Rust seems to have a bright future. 

5. As the development of Kubernetes, 
    there will be distributed computing frameworks that does not limit you into a specific languages. 
    Once that is a common situation,
    people will start shifting away from JVM languages and seek for better performance and easier to use solutions.
    Rust is a good language choice for performance 
    while Python is a good choice for glue-language that is easy to use.


## Machine Learning Frameworks

scikit-learn

LightGBM / XGBoost

PyTorch

TensorFlow 2

[Apache MXNet](https://github.com/apache/incubator-mxnet)

Caffe2 is often used for productionizing models trained in PyTorch
and it is part of the PyTorch project now.


Notice that H2O-3 (less popularity and lower quality compared to the above libraries),
[AI-Blocks](https://mrnothing.github.io/AI-Blocks/index.html),
and [Nvidia DIGIGS](https://developer.nvidia.com/digits)
provides user-friendly UI for training models.


## Computing Frameworks

Multi-threading & Multi-Processing are not discussed here 
since they are relatively simple for scientific computing.

### GPU

[ZeRO + DeepSpeed](https://github.com/microsoft/DeepSpeed)
is a deep learning optimization library 
that makes distributed training on GPU clusters easy, efficient, and effective.

Apache Ray

### Python Distributed Computing Frameworks (Ray, Celery, Dask, Modin, etc.)
### Spark
### TPU

## Programming Languages
Python
Rust
JVM (Java, Scala, Kotlin)
C/C++

## References

- (Machine Learning and Deep Learning frameworks and libraries for large-scale data mining: a survey)[https://link.springer.com/article/10.1007/s10462-018-09679-z]

- [caffe2/AICamera](https://github.com/caffe2/AICamera) 
    is a demonstration of using Caffe2 inside an Android application.

- [Comparison of AI Frameworks](https://pathmind.com/wiki/comparison-frameworks-dl4j-tensorflow-pytorch)

[Accelerating Deep Learning Using Distributed SGD — An Overview](https://towardsdatascience.com/accelerating-deep-learning-using-distributed-sgd-an-overview-e66c4aee1a0c)

[Demystifying Parallel and Distributed Deep Learning: An In-Depth Concurrency Analysis](https://spcl.inf.ethz.ch/Publications/.pdf/distdl-preprint.pdf)

[Scalable Distributed DL Training: Batching Communication and Computation](https://www.aaai.org/ojs/index.php/AAAI/article/view/4465)

[Scalable Deep Learning on Distributed Infrastructures: Challenges, Techniques and Tools](https://arxiv.org/pdf/1903.11314.pdf)

[A Hitchhiker’s Guide On Distributed Training of Deep Neural Networks](https://arxiv.org/pdf/1810.11787.pdf)

[Distributed training of Deep Learning models with PyTorch](https://medium.com/intel-student-ambassadors/distributed-training-of-deep-learning-models-with-pytorch-1123fa538848)

[Awesome Distributed Deep Learning](https://github.com/bharathgs/Awesome-Distributed-Deep-Learning)

[Intro to Distributed Deep Learning Systems](https://medium.com/@Petuum/intro-to-distributed-deep-learning-systems-a2e45c6b8e7)

[Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour](https://arxiv.org/pdf/1706.02677.pdf)
