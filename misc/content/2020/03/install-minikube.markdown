Status: published
Date: 2021-05-18 18:08:59
Author: Benjamin Du
Slug: tips-minikube
Title: Tips on Minikube
Category: Software
Tags: Software, Minikube, k8s, Kubernetes

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Microk8s is a more lightweight solution than Minikube 
(even thought Microk8s is only for Linux.)


## Installation

[4 Steps to Install Kubernetes on Ubuntu 16.04 and 18.04](https://matthewpalmer.net/kubernetes-app-developer/articles/install-kubernetes-ubuntu-tutorial.html)


1. [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

2. Install VirtualBox

3. [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)

4. Start minikube. 
	
		:::bash
		minikube start --vm-driver=virtualbox

5. Check status of minikube.

		:::bash
		minikube status


minikube dashboard

minikube ip
