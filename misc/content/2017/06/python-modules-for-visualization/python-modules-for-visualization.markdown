Status: published
Date: 2021-05-08 10:20:38
Author: Ben Chuanlong Du
Slug: python-modules-for-visualization
Title: Python Modules for Visualization
Category: Computer Science
Tags: programming, visualization, Python, HoloViews, bokeh, plotly, matplotlib, pandas, library
Modified: 2021-05-08 10:20:38

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

The website [The Python Graph Gallery](https://python-graph-gallery.com/)
displays hundreds of charts, always providing the reproducible python code! 
It aims to showcase the awesome dataviz possibilities of python and to help you benefit it. 

## General Purpose Visualization Libraries Based on JavaScript

### [hvplot](https://github.com/pyviz/hvplot)

A high-level plotting API for pandas, dask, xarray, and networkx built on HoloViews 

### [Cufflink](https://github.com/santosjorge/cufflinks)

Enables plotly plots in pandas DataFrame (via the `iplot` method) directly. 

https://plot.ly/pandas/getting-started/

https://medium.com/@kbrook10/day-7-data-visualization-how-to-use-plotly-and-cufflinks-for-interactive-data-visualizations-3a4b85fdd999

### HoloViews

HoloViews is my favorate JS-based visualization package in Python.
It has the simpliest yet rigorous syntax.

### bokeh

Bokeh is a great JS-based package for visualization in Python and is also available in other programming languages.
It is a free and opensource alternative to plotly (which is not totally free).
Both bokeh and plotly is feature-rich.
They supports all kinds of charts, data table and can easily build a dashboard.

### [plotly](https://plot.ly/python/user-guide/)

Plotly is great (even better than Bokeh) but unfortunately not totally free (very limited API calls per day).

## General Purpose Visualization Libraries Based on `matplotlib`

### matplotlib

The old default visualization package in Python.


has display issues without x server ...

http://stackoverflow.com/questions/11264521/date-ticks-and-rotation-in-matplotlib

http://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib

http://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib

### pandas

`pandas` integrates some visualization features based on matplotlib.
It makes things convenient if you have to work with data frame a lot.

### [Graphviz](https://github.com/xflr6/graphviz)

## Domain Specific Libraries

### [ipyvolume](https://github.com/maartenbreddels/ipyvolume)

3-D plotting in Python.

### [pydot/pydot](https://github.com/pydot/pydot)

### [slundberg/shap](https://github.com/slundberg/shap)

A unified approach to explain the output of any machine learning model.

### [ResidentMario/missingno](https://github.com/ResidentMario/missingno)

Missing data visualization module for Python.

### [hiplot](https://github.com/facebookresearch/hiplot)

HiPlot makes understanding high dimensional data easy

### [scattertext](https://github.com/JasonKessler/scattertext)

Beautiful visualizations of how language differs among document types.

### [geemap](https://github.com/giswqs/geemap)
[geemap](https://github.com/giswqs/geemap)
is a Python package for interactive mapping with Google Earth Engine, ipyleaflet, and folium.

### Blender Python

https://docs.blender.org/api/current/info_quickstart.html

https://medium.com/@behreajj/creative-coding-in-blender-a-primer-53e79ff71e

https://blenderscripting.blogspot.com/

## References

http://jakevdp.github.io/blog/2014/01/10/d3-plugins-truly-interactive/

http://blog.ynema.com/?p=192
