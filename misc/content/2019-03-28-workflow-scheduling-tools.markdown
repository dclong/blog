Status: published
Date: 2020-10-30 10:34:40
Author: Benjamin Du
Slug: workflow-managing-tools
Title: Workflow Managing Tools
Category: Computer Science
Tags: programming, workflow manager, scheduling, scheduler, Apache Airflow, mara, Azkaban, StackStorm

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

![Star History of Workflow Management Tools](https://miro.medium.com/max/1750/0*HEZDauOfLr0Def8D.png)

1. Apache Airflow is the recommended tool for managing workflows current!
    A big advantage of Airflow over other workflow managing tools (e.g., UC4)
    is that the workflow is expressed in (simple and concise) Python code. 
    It is easy to version control and review changes in source code 
    while it is extremly hard to do so for graphically expressed workflows,
    especially when the workflow grows large.

## [prefect](https://github.com/PrefectHQ/prefect)

## [apache/airflow](https://github.com/apache/airflow)

## Luigi

## Kubeflow

## MLFlow

## Argo

## [mara/data-integration](https://github.com/mara/data-integration)

## [azkaban/azkaban](https://github.com/azkaban/azkaban)

## [StackStorm/st2](https://github.com/StackStorm/st2)

## [rundeck/rundeck](https://github.com/rundeck/rundeck)

## crontab

## Which One to Use

 - Apache Airflow if you want the most full-featured, 
    mature tool and you can dedicate time to learning how it works, setting it up, and maintaining it.
- Luigi if you need something with an easier learning curve than Airflow. 
    It has fewer features, but it’s easier to get off the ground.
- Argo if you're already deeply invested in the Kubernetes ecosystem 
    and want to manage all of your tasks as pods, defining them in YAML instead of Python.
- KubeFlow if you want to use Kubernetes but still define your tasks with Python instead of YAML.
- MLFlow if you care more about tracking experiments or tracking and deploying models 
    using MLFlow's predefined patterns 
    than about finding a tool that can adapt to your existing custom workflows.

## References 

[Airflow vs. Luigi vs. Argo vs. MLFlow vs. KubeFlow](https://towardsdatascience.com/airflow-vs-luigi-vs-argo-vs-mlflow-vs-kubeflow-b3785dd1ed0c)