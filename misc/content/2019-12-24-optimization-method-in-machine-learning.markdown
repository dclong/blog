Status: published
Date: 2019-12-30 12:17:07
Author: Benjamin Du
Slug: optimization-method-in-machine-learning
Title: Optimization Method in Machine Learning
Category: AI
Tags: AI, machine learning, data science, optimization algorithms, ADAM, SGD, momentum

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

L-BFGS converges faster and with better solutions on small datasets. 
However, ADAM is very robust for relatively large datasets.
It usually converges quickly and gives pretty good performance. 
SGD with momentum or Nesterov momentum can perform better than those two algorithms 
if the learning rate is correctly tuned.
To sum up, 
**ADAM is the best default optimization algorithm to use for deep learning problems**.
And SGD with Nesterov Momentum is another good alternative (if you are experience at tuning learning rate).

### SGD (Stochastic Gradient Descent)

### Adam (Adaptive Moment Estimation)

Adam realizes the benefits of both AdaGrad and RMSProp.

Instead of adapting the parameter learning rates based on the average first moment (the mean) as in RMSProp, Adam also makes use of the average of the second moments of the gradients (the uncentered variance).

Specifically, the algorithm calculates an exponential moving average of the gradient and the squared gradient, and the parameters beta1 and beta2 control the decay rates of these moving averages.

The initial value of the moving averages and beta1 and beta2 values close to 1.0 (recommended) result in a bias of moment estimates towards zero. 
This bias is overcome by first calculating the biased estimates before then calculating bias-corrected estimates.

### SGD + Nestrov Momentum

### AdaGrad (Adaptive Gradient Algorithm)

### (RMSProp) Root Mean Square Propagation

## References

https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/

https://en.wikipedia.org/wiki/Stochastic_gradient_descent
