Status: published
Date: 2020-03-09 18:13:01
Author: Benjamin Du
Slug: kubernetes-tips
Title: Tips on Kubernetes
Category: Software
Tags: Software, Kubernetes, k8s, minikube, kubectl

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

https://www.youtube.com/watch?v=ZpbXSdzp_vo


https://github.com/kubernetes/minikube


https://github.com/kubernetes/kubernetes


[Kubertenes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

## Some Kubernetes Distributions

Microk8s seems like a good option.

- k3s - a light-weight Kubernetes distribution ideal for edge and development - compatible with Raspberry Pi & ARM64 (Packet, AWS Graviton)

- k3d - makes k3s available on any computer where Docker is also running

- microk8s - a Kubernetes distribution, specifically for Ubuntu users.

- minikube - a popular, but heavy-weight option that creates a Linux virtual machine your computer using VirtualBox or similar

- Docker for Mac/Windows - Docker's Desktop edition has an option to run a local Kubernetes cluster

## Example

```
---
apiVersion: v1
kind: Service
metadata:
  name: helloworldserivce
spec:
  selector:
    app: hello-world
  ports:
    - protocol: "TCP"
      port: 8080
      targetPort: 80
      nodePort: 30001
  type: LoadBalancer


---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
spec:
  replicas: 5
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-world
        image: tutum/hello-world
        ports:
        - containerPort: 80

```
Another good example is to 
[Deploy Apache Ray on Kubernetes](https://ray.readthedocs.io/en/latest/deploy-on-kubernetes.html)
.

## References

- [helm](https://github.com/helm/helm) is the Kubernetes Package Manager

[Multipass and MicroK8s: the Quickest Route to Ubuntu and Kubernetes?](https://dzone.com/articles/-multipass-and-microk8s-the-quickest-route-to-ubun)
