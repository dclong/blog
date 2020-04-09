Status: published
Date: 2020-04-08 17:44:37
Author: Ben Chuanlong Du
Slug: dashboard-solutions
Title: Dashboard Solutions
Category: Software
Tags: software, dashboard, Jupyter, JupyterLab, Superset, Redash, plotly, dash, Bokeh Server

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## [panel](https://github.com/pyviz/panel)

A high-level app and dashboarding solution for Python. 
Notice that panel does not support ipywidgets currently.

## [StreamLit](https://github.com/streamlit/streamlit)

## [QuantStack/voila](https://github.com/QuantStack/voila)

Turn Jupyter notebooks to standalone web applications and dashboards.
Notice that voila works with ipywidgets only currently.
It does not work with Bokeh/HoloViews currently.

https://github.com/QuantStack/voila/issues/244

## [Redash](https://github.com/getredash/redash)

### Docs

http://www.ehfeng.com/redash-python-functions/

https://discuss.redash.io/

### Pros & Cons

**Pros**

1. Redash is a great opensource alternative to Tableau! 

2. Code free which makes it suitable for business people.

**Cons**

1. Currently SQL is supported. 
    Even though Redash is developed in Python,
    directly Python script based data manipulation is not nicely supported. 
    There is a large voice in the community on this, 
    so hopefully this will get improved soon.

2. Superset use SQLAlchemy for underlying crunching. 
    SQLAlchemy relies on ODBC for querying databases,
    however, 
    ODBC installation and configuration is often a nightmare for commerical databases
    (such as Teradata, Oracle and SQL Server).
    It is often more convenient to query commerical databases using JDBC,
    but unfortuantely JDBC support in SQLAlchemy is not good.

3. Visualization is via JS. 
    Python visualization libraries (even if JS based) are not supported directly.

### Docker Image

[redash/redash](https://hub.docker.com/r/redash/redash/)

## [Superset](https://github.com/apache/incubator-superset)

Superset is a very similar (both functionalities and underlying techs) product to Redash.

### Pros & Cons

**Pros**

1. Superset is a great opensource alternative to Tableau! 

2. Code free which makes it suitable for business people.

**Cons**

1. Currently SQL Lab is supported. 
    Even though Superset is developed in Python,
    directly Python script based data manipulation is not nicely supported. 
    There is a large voice in the community on this, 
    so hopefully this will get improved soon.

2. Superset use SQLAlchemy for underlying crunching. 
    SQLAlchemy relies on ODBC for querying databases,
    however, 
    ODBC installation and configuration is often a nightmare for commerical databases
    (such as Teradata, Oracle and SQL Server).
    It is often more convenient to query commerical databases using JDBC,
    but unfortuantely JDBC support in SQLAlchemy is not good.

3. Visualization is via JS. 
    Python visualization libraries (even if JS based) are not supported directly.
    
### Docker Image

amancevice/superset

## [minrk/thebelab](https://github.com/minrk/thebelab)

Looks very interesting!

## [Bokeh Server](https://bokeh.pydata.org/en/latest/docs/user_guide/server.html)

It is a great idea to combine Bokeh Serve with Jupyter Notebook and Docker images. 
You can use Jupyter Notebook to quickly prototype
and rely on Docker for quickly deployment. 

### Pros & Cons

**Pros**

1. Very convenient for Python user. 

2. Bokeh Server integrates with Jupyter Notebook very well.
    You can even start a Bokeh Server in a Jupyter Notebook.
    This gives the ability to quickly prototype your dashboard in Jupyter Notebook.

**Cons**

1. Coding required. 
    Users have to be familiar with both Python and the Bokeh package.

## Plotly Dash

Dash is a great (even better) alternative to Bokeh.
I though Dash is based on Plotly APIs but the developers says not 
(see [this issue](https://github.com/plotly/dash/issues/192)).

https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503

https://dash.plot.ly/



## HVF/franchise

## FreeBoard

https://github.com/Freeboard/freeboard

## Mozaik

https://github.com/plouc/mozaik

## Grafana

https://github.com/grafana/grafana

## Keen/Dashboard

https://github.com/keen/dashboards

## Metabase

https://github.com/metabase/metabase


