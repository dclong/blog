Status: published
Date: 2020-04-16 14:34:57
Author: Benjamin Du
Slug: make-your-model-training-reproducible-in-pytorch
Title: Make Your Model Training Reproducible in PyTorch
Category: AI
Tags: AI, data science, machcine learning, deep learning, PyTorch, reproducible, random, see, RNG

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

The PyTorch doc 
[Reproducibility](https://pytorch.org/docs/stable/notes/randomness.html)
has very detailed instructions on how to make your model training reproducible.
Basically,
you need the following code.

    :::python
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    random.seed(args.seed)

Notice that `torch.manual_seed` set seeds of RNGs on all devices (both CPU and GPUs).
There is no need to make additional calls of `torch.cuda.manual_seed`
or `torch.manual_seed_all`.

## References

[REPRODUCIBILITY](https://pytorch.org/docs/stable/notes/randomness.html)

[torch.manual_seed](https://pytorch.org/docs/stable/torch.html#torch.manual_seed)

[What is manual_seed?](https://discuss.pytorch.org/t/what-is-manual-seed/5939)

[Difference between torch.manual_seed and torch.cuda.manual_seed](https://discuss.pytorch.org/t/difference-between-torch-manual-seed-and-torch-cuda-manual-seed/13848)
