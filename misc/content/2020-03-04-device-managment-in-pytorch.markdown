Status: published
Date: 2020-04-20 08:52:01
Author: Benjamin Du
Slug: device-managment-in-pytorch
Title: Device Managment in PyTorch
Category: Computer Science
Tags: programming, AI, machine learning, data science, deep learning, PyTorch, device, CUDA, CPU

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

0. Modules can hold parameters of different types on different devices, 
    so it's not always possible to unambiguously determine the device.
    The recommended workflow in PyTorch is to create the device object separately and use that everywhere. 
    However,
    if you know that all the parameters in a model are on the same device, 
    you can use `next(model.parameters()).device` to get the device.
    In that situation,
    you can also use `next(model.parameters()).is_cuda` 
    to check if the model is on CUDA.


1. It is suggested that you use use method `.to` to move a model/tensor to a specific device.

        :::python
        model.to("cuda")
        tensor.to("cpu")

    Notice that the method `.to` is in-place.



## Function for Managing Device

[torch.cuda.current_device](https://pytorch.org/docs/stable/cuda.html#torch.cuda.current_device)
Returns the index of a currently selected device.

[torch.cuda.device](https://pytorch.org/docs/stable/cuda.html#torch.cuda.device)
Context-manager that changes the selected device.

[torch.cuda.device_count](https://pytorch.org/docs/stable/cuda.html#torch.cuda.device_count)
Returns the number of GPUs on the machine (no matter whether they are busy or not).

[torch.cuda.device_of](https://pytorch.org/docs/stable/cuda.html#torch.cuda.device_of)
Context-manager that changes the current device to that of given object.

[torch.cuda.get_device_capability](https://pytorch.org/docs/stable/cuda.html#torch.cuda.get_device_capability)
Gets the cuda capability of a device.

[torch.cuda.get_device_name](https://pytorch.org/docs/stable/cuda.html#torch.cuda.get_device_name)

[torch.cuda.set_device](https://pytorch.org/docs/stable/cuda.html#torch.cuda.set_device)


## Use Multiple GPUs on the Same Machine

Below is a typical pattern of code to train/run your model on multiple GPUs.

	:::python
	device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
	model.to(device)
	model = torch.nn.DataParallel(model)
	model(data)

1. `torch.nn.DataParallel` parallels a model on GPU devices only. 
	It doesn't matter which device the data is on if the model is wrapped by `torch.nn.DataParallel`. 
	It can be on a CPU or any GPU device.
	It will get splitted and distributed to all GPU devices anyway.

2. If GPU devices have different capabilities,
	it is best to have the most powerful GPU device as device 0.

[OPTIONAL: DATA PARALLELISM](https://pytorch.org/tutorials/beginner/blitz/data_parallel_tutorial.html)

[Does DataParallel matters in CPU-mode](https://discuss.pytorch.org/t/does-dataparallel-matters-in-cpu-mode/7587)

[torch..nn.DataParallel](https://pytorch.org/docs/stable/nn.html#torch.nn.DataParallel)

[My recurrent network doesn’t work with data parallelism](https://pytorch.org/docs/stable/notes/faq.html#my-recurrent-network-doesn-t-work-with-data-parallelism)

## Use Multiple Processes or GPUs on Different Machines

https://pytorch.org/docs/stable/nn.html#distributeddataparallel

1. Similar to `torch.nn.DataParallel`, 
	`torch.nn.DistributedDataParallel` works for GPU only.

2. It is suggested that you spawn multiple processes (on each node)
	and have each process operate a single GPU.

2. `nccl` is the suggested backend to use. 
	If not available, 
	then use the `gloo` backend.

3. If you use torch.save on one process to checkpoint the module, 
	and `torch.load` on some other processes to recover it, 
	make sure that map_location is configured properly for every process. 
	Without `map_location`, 
	`torch.load` would recover the module to devices where the module was saved from.

https://pytorch.org/docs/stable/distributed.html


## References

[torch.cuda](https://pytorch.org/docs/stable/cuda.html#module-torch.cuda)


[Which device is model / tensor stored on?](https://discuss.pytorch.org/t/which-device-is-model-tensor-stored-on/4908)

[How to get the device type of a pytorch module conveniently?](https://stackoverflow.com/questions/58926054/how-to-get-the-device-type-of-a-pytorch-module-conveniently)

[[Feature Request] nn.Module should also get a `device` attribute #7460](https://github.com/pytorch/pytorch/issues/7460)

[.device property on layers #12135](https://github.com/pytorch/pytorch/issues/12135)

[Which device is model / tensor stored on?](https://discuss.pytorch.org/t/which-device-is-model-tensor-stored-on/4908)
