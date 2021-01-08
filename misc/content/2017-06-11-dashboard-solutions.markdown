Status: published
Date: 2021-01-08 14:01:55
Author: Ben Chuanlong Du
Slug: dashboard-solutions
Title: Dashboard Solutions
Category: Software
Tags: software, dashboard, Jupyter, JupyterLab, Superset, Redash, plotly, dash, Bokeh Server

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## [jupyterlab-interactive-dashboard-editor](https://github.com/jupytercalpoly/jupyterlab-interactive-dashboard-editor)

[jupyterlab-interactive-dashboard-editor](https://github.com/jupytercalpoly/jupyterlab-interactive-dashboard-editor)
is an awesome dashboard plugin for JupyterLab!

## [panel](https://github.com/pyviz/panel)

A high-level app and dashboarding solution for Python. 
Notice that panel does not support ipywidgets currently.

## [StreamLit](https://github.com/streamlit/streamlit)

## [QuantStack/voila](https://github.com/QuantStack/voila)

Turn Jupyter notebooks to standalone web applications and dashboards.
Notice that voila works with ipywidgets only currently.
It does not work with Bokeh/HoloViews currently.

https://github.com/QuantStack/voila/issues/244

[MavenWorks](https://github.com/Mavenomics/MavenWorks)

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



## Redash
Redash is a dashboard tool developed in Python.

Installation of Redash
wget https://raw.githubusercontent.com/getredash/redash/master/setup/ubuntu/bootstrap.sh
sudo ./bootstrap.sh
Note: Redash uses Python2, not Python3, so please make sure to use pip2 to install all required dependencies.

Supported Data Sources
Currently, Redash supports MySQL, PostgreSQL, Hive, Presto, ClickHouse, etc. Teradata is NOT supported directly. I couldn't find an approach to let Teradata be supported at the moment, although I believe it is possible.

Glance of Redash
Creating a dashboard or adding a config in Redash is pretty straightforward, go to http://10.148.177.222/, login with username: test@ebay.com, password: 123456 to have a look at Redash in real.

Create a Dashboard
First go to Queries - New Query, create your first new SQL query, and then publish it;
Then go to Dashboards - New Dashboard, enter name for your new Dashboard;
Click ... on the upper right corner, go to Add Widget, enter the Query name you created before;
A new Dashboard has been created now. You can add more widgets whenever you want.
Problems encountered now:
Teradata is not officially supported by Redash;
Unable to add the Presto and Hive data source to Redash, don't know the reason;

## Superset
At the first glance, Superset is an Apache project, whcih means that it may be more active, maintained by more people, and better-supported.

Installation of Superset
Installing Superset is pretty easy by just following the guide here: https://superset.incubator.apache.org/installation.html

Note: Since I use Python3 instead of Python2 which is used in the guide, need to change sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-pip libsasl2-dev libldap2-dev to sudo apt-get install build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev

Supported Data Source
Superset uses SqlAlchemy as its SQL query engine, hence any data source supported by SqlAlchemy can be supported by Superset as well.

Glance of Superset
Go to http://10.148.177.222:8088, login with username: test, password: 123456 to take a first glance at Superset. Note: If you encountered indefinite waiting after logined with test, please try to use username: mpan2, password: 123456 instead. There are many example dashboards already created by default, which can show you how powerful Superset is.