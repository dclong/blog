Status: published
Date: 2021-04-26 09:48:16
Author: Benjamin Du
Slug: packaging-Python-Dependencies-for-PySpark-Using-python-build-standalone
Title: Packaging Python Dependencies for PySpark Using Python-Build-Standalone
Category: Computer Science
Tags: Computer Science, programming, Python, portable, standalone, python-build-standalone, Docker, environment
Modified: 2021-03-26 09:48:16
You can build a portable Python environment 
following steps below.

1. Install [python-build-standalone](https://github.com/indygreg/python-build-standalone).

2. Install Python packages using pip of the installed python-build-standalone distribution.

3. Pack the whole python-build-standalone directory into a compressed file, e.g., `env.tar.gz`.


The GitHub repo
[dclong/python-portable](https://github.com/dclong/python-portable)
has good examples of building portable Python environments 
leveraging the Docker image
[dclong/python-portable](https://github.com/dclong/docker-python-portable)
(which has python-build-standalone installed).