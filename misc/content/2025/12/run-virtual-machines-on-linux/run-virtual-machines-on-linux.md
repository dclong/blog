Status: published
Date: 2025-12-16 23:39:50
Modified: 2025-12-16 23:39:50
Author: Benjamin Du
Slug: run-virtual-machines-on-linux
Title: Run Virtual Machines on Linux
Category: Computer Science
Tags: Computer Science, programming, VM, KVM, virtual, machine, Linux, QEMU, Virtual Machine Manager, GNOME Boxes

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

While VirtualBox is a popular cross-platform tool for running virtual machines,
KVM is a superior solution for Linux 
as KVM is a type-1 hypervisor which runs directly on the hardware via the Linux kernel
while VirtualBox is a type-2 hypervisor which runs as an application on top of your OS.
Since KVM is part of the Linux kernel, 
it has lower overhead and offers near-native CPU and disk performance. 
For more detailed comparisions,
please refer to
[Chat with Gemini: KVM vs. VirtualBox for Linux](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%2210w5VDJtO6r3t4oHGB2G6WucWNeuyJzlF%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.


It is a common confusion that KVM is much harder to use compared to VirtualBox. 
Technically speaking, it's true. 
However, 
standard users never use KVM directly.
KVM is like an engine (for running VMs)
and there are GUI tools to make it easy to use KVM (and related tools such as QEMU and libvirt).

## GNOME Boxes vs virt-manager

GNOME Boxes and 
[Virtual Machine Manager (virt-manager)](https://virt-manager.org/)
are 2 popular choices (based on KVM, QEMU and libvirt) for Linux.
GNOME Boxes is very simple to use 
while Virtual Machine Manager offers more options and is more suitable for power users.
For more detailed comparision,
please refer to
[Chat with Gemini: GNOME Boxes vs virt-manager](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221hQepi_tkMePT1PJY71TWc8TaCbnTPkc7%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## References

- [Chat with Gemini: qemu vs kvm vs virt-manager](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221XCnG8dxf0HA3EblgIxjpRJb85dIRaiLn%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

- [Chat with Gemini: GNOME Boxes vs virt-manager](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221hQepi_tkMePT1PJY71TWc8TaCbnTPkc7%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

