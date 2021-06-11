UUID: bfc7638c-d92d-4b83-9afb-b2fa8c890645
Status: published
Date: 2016-12-10 01:52:37
Author: Ben Chuanlong Du
Slug: install-jupyter-scala-for-jupyterlab
Title: Install Jupyter-Scala for JupyterLab
Category: Computer Science
Tags: programming, Scala, Jupyter, JupyterLab, jupyter-scala, kernel
Modified: 2016-12-10 01:52:37

Note: Apache Toree is a better alternative than Jupyter Scala.
It is suggested that you use Apache Toree instead of Jupyter Scala.

You can install Jupyter Scala following the steps below.

1. Make sure Java and Scala are installed.

        wajig install openjdk-8-jdk scala

2. Download coursier and move it to a searchable path. 
I place it in `$HOME/bin` which I have included in `$PATH`.

        curl -L -o coursier https://git.io/vgvpD && chmod +x coursier 

3. Clone the jupyter-scala repository.

        git clone git@github.com:alexarchambault/jupyter-scala.git

4. Run the following command insider the directory to insall Jupyter Scala.

        ./jupyter-scala

    You might have issues due to no permission to create directories/files under `$HOME/.local/share/jupyter`.
    If that happens, 
    change the permission of the directory and try again.

        sudo chmod -R 777 $HOME/.local/share/jupyter

