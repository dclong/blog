Status: published
Date: 2017-07-22 15:07:28
Author: Ben Chuanlong Du
Title: Visualization Using Bokeh in Python
Slug: bokeh-tips
Category: Computer Science
Tags: programming, Python, visualization, Bokeh, Bokeh server, tips
Modified: 2020-05-22 15:07:28

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Links

<http://bokeh.pydata.org/en/latest/>

## Installation

```
sudo pip3 install bokeh jupyter holoviews
```

## Usage
```
bokeh serve --allow-websocket-origin=*:5006 dash.ipynb
```
it seems that only 5006 works ...
might be because ...

## Questions

Can u combine bokeh and Jupyter Notebook to quickly prototype and then deploy? 
This requires support of Bokeh server in Jupyter Notebook.

bokeh, not numeric values, no corresponding warnings due to HTML ...
be careful ...

```
bokeh serve --allow-websocket-origin=server_ip:5006 sliders.py
```

## jupyterlab_bokeh

    wajig install libgif-dev
    sudo jupyter labextension install jupyterlab_bokeh

