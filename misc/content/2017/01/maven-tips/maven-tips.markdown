Status: published
Date: 2020-05-22 15:06:34
Author: Ben Chuanlong Du
Title: Tips on Maven
Slug: maven-tips
Category: Computer Science
Tags: programming, Maven, tips, Java, Scala
Modified: 2020-05-22 15:06:34

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[The Central Repository](http://search.maven.org/#search)

$HOME/.m2

maven: shade plugin, scala compile plugin, exclude manifest files, ...

import as maven project ...

find an updated version of scala archetype for maven

```sh
mvn package  
mvn clean package  
mvn compile  
mvn build  
mvn -e build
```

intellij scala mavn archtype is too ooooooooooold!!! 
wait for generate complete and then manaully update the pom file


Maven

https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/hdinsight/hdinsight-apache-spark-create-standalone-application.md


How to define a customized archetype for IntelliJ?
If you use maven in intellij for scala, after choose archetype, update the old pom content!!!

http://maven.apache.org/

## Configuration

[Configuring Maven](https://maven.apache.org/guides/mini/guide-configuring-maven.html)

You can either set up a proxy or mirror repositories to speed up Maven compilation (in China).
Both of them are good ways and are easy to set up.

[Using Mirrors for Repositories](https://maven.apache.org/guides/mini/guide-mirror-settings.html)

[Configuring a proxy](https://maven.apache.org/guides/mini/guide-proxies.html)



http://search.maven.org/#search%7Cga%7C1%7C

https://maven.apache.org/guides/introduction/introduction-to-archetypes.html

