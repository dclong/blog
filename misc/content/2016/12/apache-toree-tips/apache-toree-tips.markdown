Status: published
Date: 2019-12-12 20:32:58
Author: Ben Chuanlong Du
Slug: apache-toree-tips
Title: Apache Toree Tips
Category: Computer Science
Tags: programming, Apache Toree, Jupyter Notebook, JupyterLab, Jupyter Lab, Spark
Modified: 2019-12-12 20:32:58

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


<https://github.com/apache/incubator-toree/blob/master/etc/examples/notebooks/magic-tutorial.ipynb>


```bash
anaconda3/bin/jupyter toree install --user --spark_home=/apache/spark
```


## Dependency Managemnt

    %AddJar jar_url
    %AddDeps
    printHelp(printStream, """%AddDeps my.company artifact-id version""")


    %AddDeps com.databricks spark-csv_2.10 1.2.0 --transitive


    %AddDeps tech.tablesaw tablesaw-core 0.11.6 --transitive


    kernel.magics.addDeps("com.databricks spark-csv_2.10 1.2.0 --transitive")


    %AddDeps org.apache.spark spark-mllib_2.10 1.6.2
    %AddDeps com.github.haifengl smile-core 1.1.0 --transitive
    %AddDeps io.reactivex rxscala_2.10 0.26.1 --transitive
    %AddDeps com.chuusai shapeless_2.10 2.3.0 --repository https://oss.sonatype.org/content/repositories/releases/
    %AddDeps org.tmoerman plongeur-spark_2.10 0.3.9 --repository file:/Users/tmo/.m2/repository


    %AddDeps "graphframes" % "graphframes" % "0.1.0-spark1.6" --repository http://dl.bintray.com/spark-packages/maven


Currently it supports only https://repo1.maven.org/maven2/, but not all projects deploy there.