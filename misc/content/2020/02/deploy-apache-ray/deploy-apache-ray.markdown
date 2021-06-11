Status: published
Date: 2020-02-10 09:39:25
Author: Benjamin Du
Slug: deploy-apache-ray
Title: Deploy Apache Ray
Category: Computer Science
Tags: programming, Apache Ray, distributed computing, deploy, deployment, setup, configure, Kubernetes, k8s, Spark, cluster
Modified: 2021-06-10 09:39:25

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## [Manual Cluster Setup](https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html)

It is very easy to set up Apache Ray on a small cluster manually.
The instructions at
[Manual Cluster Setup](https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html)
is very clear.
Just one comment.
You do not need to configure SSH keys for nodes in the cluster for manual configuration.
When you start the master node manually (using the command `ray start --head`), 
it will print a command to add new nodes into the cluster.
The command 
(e.g., `ray start --address='10.148.186.18:12030' --redis-password='5241590000000000'`)
includes the Redis password for authentication to join the cluster.

By default, 
the Ray dashboard is visitable only on the head node.
To make it visitable by public IP,
you can include the option `--webui-host=0.0.0.0` when starting Ray on the head node.

## Private Cluster

https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/local/example-full.yaml

1. The Ray autoscaler installs Ray on the head and worker nodes by default.
    That is if you don't set values for the fileds `head_setup_commands` and `setup_commands`,
    Ray is automatically installed/updated on the head and worker nodes.
    You can disable this behavior by set a dummy command (e.g., `echo "Starting Ray ..."`) for the 2 fileds.

https://github.com/ray-project/ray/issues/4902

https://github.com/ray-project/ray/issues/4559

https://github.com/ray-project/ray/issues/3408

https://github.com/ray-project/ray/issues/4811

https://github.com/ray-project/ray/issues/5326

https://github.com/ray-project/ray/issues/5437

https://github.com/ray-project/ray/issues/5442

https://github.com/ray-project/ray/issues/3190

https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html

https://ray.readthedocs.io/en/latest/autoscaling.html

https://ray.readthedocs.io/en/latest/autoscaling.html#quick-start-private-cluster

https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html

## GCP

https://github.com/ray-project/ray/issues/2660

## AWS 

https://gist.github.com/edoakes/0f7f62b7d9aa5481482bca23be5f622a

## Kubernetes

[Deploying on Kubernetes](https://ray.readthedocs.io/en/latest/deploy-on-kubernetes.html)

https://github.com/ray-project/ray/tree/master/doc/kubernetes

https://ray.readthedocs.io/en/latest/autoscaling.html#kubernetes

https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/kubernetes/example-full.yaml

## Ray with Spark 

## References

https://github.com/ray-project/ray/issues/7025
