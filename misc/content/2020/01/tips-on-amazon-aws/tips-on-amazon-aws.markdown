Status: published
Date: 2020-03-11 20:47:40
Author: Benjamin Du
Slug: tips-on-amazon-aws
Title: Tips on Amazon AWS
Category: Cloud
Tags: Cloud, Amazon AWS
Modified: 2020-03-11 20:47:40

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tips and Traps

1. By default, 
    AWS shows your resources (VMs, etc.) in one location (data center) only. 
    This can be tricky if you have VMs in mutiple locations (data centers)
    as you might forget that you have VMs in other locations 
    (rather than the currently displayed one to you)
    and forgot to stop them.
    The invoices of AWS includes details of charges. 
    It is suggested that you dig into details of your AWS invoice carefully 
    if the bill looks abnormally high to you.

1. To save cost, 
    it is suggested that you start a VM instance on demand
    and stop it when you finish using it.
    You won't be charged for VM usage after stopping it,
    however, 
    you will still be charged for the corresponding S3 storages.
    Microsoft Azure has a similar pricing strategy 
    to not charge users for stopped VMs but still charge for storages.
    This makes AWS and Azure great choices for flexible on-demand usages.
    Some other cloud services (Vultr, Digital Ocean, etc.) claims to be cheaper (than AWS and Azure)
    but they continue to charge users for stopped VMs. 
    Those are good for long-term usages but not for flexible on-demand usages.

2. You can change the VM instance type to scale up/down.

## CPU Instances

Below is a list of CPU-only instances.
t2.large is a good one for occasional general purpose usage.
![Amazon AWS EC2 Instances](https://user-images.githubusercontent.com/824507/73387307-3c6bc200-4285-11ea-9119-d5396c011cc5.png)

## GPU Instances

Below is a list of instances that have 1 GPU on Amazon AWS.
`g4dn.xlarge` and `g3s.xlarge` 
 are good ones for occasional GPU usage.
![Amazon AWS EC2 Instances](https://user-images.githubusercontent.com/824507/73386836-607ad380-4284-11ea-862a-d04a19b98ee2.png)
