Status: published
Date: 2020-03-04 14:41:23
Author: Benjamin Du
Slug: device-managment-in-pytorch
Title: Device Managment in PyTorch
Category: Computer Science
Tags: programming

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

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
