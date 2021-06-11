Status: published
Date: 2020-03-04 16:12:45
Author: Benjamin Du
Slug: gradient-clipping-in-pytorch
Title: Gradient Clipping in PyTorch
Category: Computer Science
Tags: programming
Modified: 2020-03-04 16:12:45

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

    :::python
    optimizer.zero_grad()        
    output = model(data)
    loss = F.nll_loss(output, target)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), args.clip)
    optimizer.step()

1. Use `torch.nn.utils.clips_grad_norm_` (which is in-place)
    instead of `torch.nn.utils.clips_grad_norm` (which returns a copy and has been deprecated).

## References

https://discuss.pytorch.org/t/proper-way-to-do-gradient-clipping/191

[About torch.nn.utils.clip_grad_norm](https://discuss.pytorch.org/t/about-torch-nn-utils-clip-grad-norm/13873)

[How to do gradient clipping in pytorch?](https://stackoverflow.com/questions/54716377/how-to-do-gradient-clipping-in-pytorch)
