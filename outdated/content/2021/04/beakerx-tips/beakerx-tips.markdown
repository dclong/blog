Status: published
Date: 2020-04-12 22:02:34
Author: Ben Chuanlong Du
Slug: beakerx-tips
Title: The BeakerX JupyterLab Kernel
Category: Software
Tags: software, BeakerX, JupyterLab, Maven
Modified: 2020-04-12 22:02:34

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

[BeakerX Cheatsheet](https://github.com/twosigma/beakerx/raw/master/doc/Cheatsheet.pdf)

[BeakerX dependencies](https://github.com/twosigma/beakerx/blob/master/configuration.yml#L6)
Currently Java 8 is request.

1. The maven cache is save to the following directory
    `/tmp/share/beakerx/maven/cache/`.

2. Set JVM properties for BeakerX.

https://github.com/twosigma/beakerx/issues/7666

https://github.com/twosigma/beakerx/blob/master/FAQ.md

3. All BeakerX kernels support both Bash and Python via cell magics (`%%bash` and `%%python`).

4. Output of the BeakerX Scala kernel can be disabled by calling `OutputCell.HIDDEN`.

## SQL

1. Connect to SQLite3.

        %defaultDatasource jdbc:sqlite:fts5.sqlite3

2. Connect to SQLite3 in memory

        %defaultDatasource jdbc:sqlite::memory:
    or
        %defaultDatasource jdbc:sqlite:

3. The SQLite3 JDBC driver is located at 
    `/usr/local/lib/python3.6/dist-packages/beakerx/kernel/sql/lib/sqlite-jdbc-3.21.0.jar`.
    You can manually replace it with a higher version to upgrade it.

## Default JDBC Connection

1. Add entry `BEAKERX_SQL_DEFAULT_JDBC` under `env` in the kernelspec file `kernel.json`.

2. Add necessary JARs to the `-cp` option of `java` if needed (e.g., for Teradata SQL).


```
"argv": [
	"java", "-cp", "/opt/conda/lib/python3.6/site-packages/beakerx/kernel/base/lib/*:/opt/conda/lib/python3.6/site-packages/beakerx/kernel/sql/lib/*", "com.twosigma.beakerx.sql.kernel.SQL",  "{connection_file}"
],
"display_name": "Postgres",
"language": "SQL",
"env": {
	"PS1": "Postgres",
	"BEAKERX_SQL_DEFAULT_JDBC": "jdbc:postgresql://some_url:port_number/database_name?user=username&password=password"
}
```

https://github.com/twosigma/beakerx/issues/7518

https://github.com/twosigma/beakerx/pull/7538

https://github.com/twosigma/beakerx/pull/7538#issuecomment-420765574

https://github.com/twosigma/beakerx/issues/8199
