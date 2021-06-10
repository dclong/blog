Status: published
Date: 2021-06-10 09:39:25
Author: Benjamin Du
Slug: tips-on-openfaas
Title: Tips on OpenFaaS
Category: Software
Tags: Software, Kubernetes, k8s, OpenFaaS, serverless, function

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**
## Tutorials

https://blog.alexellis.io/quickstart-openfaas-cli/

https://www.youtube.com/watch?time_continue=6&v=LQa8-JvIeWA&feature=emb_logo

## [Deploy OpenFaaS with Kubernetes](https://docs.openfaas.com/deployment/kubernetes/)

Deploy OpenFaaS from static YAML, via helm, or via new YAML files generated with helm template
Find your OpenFaaS gateway address
Log in, deploy a function, and try out the UI.

[Getting started with OpenFaaS on minikube](https://medium.com/faun/getting-started-with-openfaas-on-minikube-634502c7acdf)

[Deploy OpenFaaS Using helm](https://github.com/openfaas/faas-netes/blob/master/HELM.md)

### Install OpenFaaS CLI

	:::bash
	curl -sL https://cli.openfaas.com | sudo sh

You can also use the following command to install faas-cli on macOS.

	:::bash
	brew install faas-cli


faas-cli --help

## References

https://www.youtube.com/watch?time_continue=6&v=LQa8-JvIeWA&feature=emb_logo

[helm](https://github.com/helm/helm)

[OpenFaaS Workshop](https://github.com/openfaas/workshop)
