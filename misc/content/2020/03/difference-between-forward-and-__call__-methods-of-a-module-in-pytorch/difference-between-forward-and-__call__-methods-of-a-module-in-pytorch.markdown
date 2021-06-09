Status: published
Date: 2020-03-05 16:05:30
Author: Benjamin Du
Slug: difference-between-forward-and-__call__-methods-of-a-module-in-pytorch
Title: Difference Between forward and __call__ Methods of a Module in PyTorch
Category: AI
Tags: AI, data science, machine learning, deep learning, PyTorch, forward, __call__

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. The `Module.__call__` method register all hooks and call the method `Module.forward`. 
    In short, 
    when you train the model you should use the method `forward`,
    while when you test the model during training 
    or when you do prediction using a well trained model, 
    you should use the method `__call__`. 
    `model.__call__(data)` is equivalent to `model(data)`.

## References

[Why there are different output between model.forward(input) and model(input)](https://stackoverflow.com/questions/55338756/why-there-are-different-output-between-model-forwardinput-and-modelinput)

[Is model.forward(x) the same as model.__call__(x)?](https://discuss.pytorch.org/t/is-model-forward-x-the-same-as-model-call-x/33460)

[Why can you call model without specifying forward method](https://discuss.pytorch.org/t/why-can-you-call-model-without-specifying-forward-method/24762)

[Any different between model(input) and model.forward(input)](https://discuss.pytorch.org/t/any-different-between-model-input-and-model-forward-input/3690)
