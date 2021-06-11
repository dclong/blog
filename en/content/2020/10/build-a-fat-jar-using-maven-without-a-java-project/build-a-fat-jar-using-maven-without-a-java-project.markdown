Status: published
Date: 2020-10-21 17:22:39
Author: Benjamin Du
Slug: build-a-fat-jar-using-maven-without-a-java-project
Title: Build a Fat JAR Using Maven Without a Java Project
Category: Computer Science
Tags: Computer Science, Java, Maven, POM, JAR, fat jar, assembly
Modified: 2020-11-21 17:22:39


You can use Maven to download dependencies of Java packages without creating a Java project.
For example,
if you want to download all dependencies of `arrow-jvm` and `arrow-memory` 
and build everything into a single fat jar (for easy use in other places),
you can first crate a file `pom.xml` containing the following content
and then run the command `mvn assembly:single`.
A copy of the built fat JAR can be download at 
[arrow-jvm-1.0-jar-with-dependencies.jar](http://www.legendu.net/media/java/arrow-jvm-1.0-jar-with-dependencies.jar)
.

    :::xml
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>net.legendu</groupId>
        <artifactId>arrow-jvm</artifactId>
        <version>1.0</version>
        <packaging>jar</packaging>

        <name>arrow-jvm</name>

        <properties>
            <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        </properties>

        <dependencies>
            <dependency>
                <groupId>org.apache.arrow</groupId>
                <artifactId>arrow-jdbc</artifactId>
                <version>2.0.0</version>
            </dependency>
            <dependency>
                <groupId>org.apache.arrow</groupId>
                <artifactId>arrow-memory</artifactId>
                <version>2.0.0</version>
                <type>pom</type>
            </dependency>
        </dependencies>
        
        <build>
        <plugins>
            <plugin>
            <artifactId>maven-assembly-plugin</artifactId>
            <configuration>
                <archive>
                <manifest>
                    <mainClass>com.uwekorn.Main</mainClass>
                </manifest>
                </archive>
                <descriptorRefs>
                <descriptorRef>jar-with-dependencies</descriptorRef>
                </descriptorRefs>
            </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.0</version>
                <configuration>
                    <source>8</source>
                    <target>8</target>
                </configuration>
            </plugin>
        </plugins>
        </build>
    </project>
