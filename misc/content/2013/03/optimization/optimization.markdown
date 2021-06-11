Status: published
Title: Optimization Algorithms
Date: 2019-12-30 12:17:07
Tags: numerical analysis, optimization, Research
Category: Research
Slug: science-optimization
Author: Ben Chuanlong Du
Modified: 2019-12-30 12:17:07

**Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!**
 
If the objective function has derivative, 
then an optimization problem is equivalent to finding the root of the derivative of the object function. 

## Finding Root
- Linear Search
Only good for 1-dimensional problem. 
- Newton's Algorithm
- Monotone objective functions. 
A good way is to use binary search which is very fast. 


## Optimization

- Linear Programming

- Quadratic Programming
When the object function is quadratic in the parameters and the restrictions are linear in the parameters. 

- Linear Search 

- (Batch) Gradient Descent

- Stochastic Gradient Descent
This method does not converge to a local maximum/minimum,
but the solutions wonders around a local maximum/minimum.
Stochastic gradient is usually faster than batch gradient descent. 
It also have the advantage of being able to escape from local maximum/minimum.

- Newton's Algorithm

This is actually an algorithm to find the root of equations.
To use this algorithm to do optimization, 
we can solve for the root of the partial derivates of the objective function. 
Since the algorithm itself requires the function to be solved to have partial derivatives, 
the objective function must be twice differtiable. 
Newton's algorithm usually requires less steps to converge than the gradient descent algorithm,
however, it need to computer the Hessian matrix,
which requires more time and sometimes causes numerical problems.

- Coordinate Descent
This trick is used in non-linear models and linear models with covariance matrix differnt from the identity matrix.
SMO algorithm: change 2 parameters at a time

- Genetics Algorithm
Good for computationally intensive problems. 
It also have the advantage of being able to escape from a local maximum/minimum.

- Simulation Anneling Algorithm

- Ant Algorithm

- Monotone Object Functions
Too easy to be true.

- Convex/Concave Object Functions
If twice differentialble or differtiable, we can apply the Newton's algorithm or the gradient descent algorithm.
If not differtiable, another good way is to use 3-fold search which is similar to the binary search for finding root. 



Optimization is really important in science and industry. 
Many problems need to optimize an objective function.
As we discussed before, 
human beings only knows how to optimize some simple case of objective functions. 
To make optimization easy,
we sometimes use functions that are easier to optimize to approximate the original objective function.
Usually a convex function used to approximate the original objective function.

For exponential family, 
we usually have convext optimization probablems and the gradient descent or Newton's algorithm is good.

batch gradient descent

coordinate descent (fixed part of the parameter, optimize the other part)
