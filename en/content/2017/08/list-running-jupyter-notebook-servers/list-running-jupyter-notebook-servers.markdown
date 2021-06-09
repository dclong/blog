UUID: 14b087dd-1a27-4fcf-9f46-622f5375c616
Status: published
Date: 2017-10-22 12:21:29
Author: Ben Chuanlong Du
Slug: list-running-jupyter-notebook-servers
Title: List Running Jupyter Notebook Servers
Category: Software
Tags: software, notebook, Jupyter Notebook, JupyterLab, Python, root, running servers, list

You can list running Jupyter Notebook servers using the following command.

    jupyter notebook list

It works well most of the time. 
However, 
if the servers are launched using the root account (e.g., in a Docker container), 
you might encounter issues. 
In this case,
a better alternative is to list running servers using Python script.

    from notebook import notebookapp
    servers = list(notebookapp.list_running_servers())
    print servers

For more please refer to 
<https://stackoverflow.com/questions/41782255/how-to-get-the-current-jupyter-notebook-servers-in-python>.


