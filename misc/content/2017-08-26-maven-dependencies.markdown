UUID: 09f15666-6165-484f-996c-db6110b840b1
Status: published
Date: 2017-08-26 21:30:59
Author: Ben Chuanlong Du
Slug: maven-dependencies
Title: Maven Dependencies
Category: Programming
Tags: programming, Scala, Maven, dependencies, dependency management

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Properties

```
<properties>
  <scala.version>2.11.11</scala.version>
</properties>
```

## Plugin 

### scala-maven-plugin
```XML
<plugin>
  <groupId>net.alchim31.maven</groupId>
  <artifactId>scala-maven-plugin</artifactId>
  <version>3.2.2</version>
  <executions>
    <execution>
      <goals>
        <goal>compile</goal>
        <goal>testCompile</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```

### maven-scala-plugin
```
<plugin>
    <groupId>org.scala-tools</groupId>
    <artifactId>maven-scala-plugin</artifactId>
    <version> 2.15.2 </version>
    <executions>
        <execution>
            <goals>
                <goal>compile</goal>
            </goals>
        </execution>
    </executions>
    <configuration>
        <sourceDir>src</sourceDir>
        <scalaVersion>${scala.version}</scalaVersion>
    </configuration>
</plugin>
```

### Maven Surefire Plugin

for unit testing

### maven-shade-plugin
 
```XML
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <version>3.0.0</version>
    <configuration>
    <!-- put your configurations here -->
    </configuration>
    <executions>
        <execution>
            <phase>package</phase>
            <goals>
                <goal>shade</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

```XML
<plugin>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>2.0.2</version>
    <configuration>
        <source>1.6</source>
        <target>1.6</target>
    </configuration>
</plugin>
```

```XML
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <configuration>
         <mainClass>net.legendu.App</mainClass>
    </configuration>
</plugin>
```

## Dependencies

```XML
<dependency>
    <groupId>org.scalaz</groupId>
    <artifactId>scalaz-core_2.11</artifactId>
    <version>7.2.12</version>
</dependency>
```

```XML
<dependency>
  <groupId>com.ebay.scalaplatform</groupId>
  <artifactId>platform-spark_2.11</artifactId>
  <version>1.0-SNAPSHOT</version>
</dependency>
```

### Apache Commons Math3
```
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-math3</artifactId>
    <version>3.6.1</version>
</dependency>
```


```
<dependencies>
    <dependency>
    <groupId>org.scala-lang</groupId>
    <artifactId>scala-library</artifactId>
    <version>${scala.version}</version>
    </dependency>
</dependencies>


    <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <version>2.4.3</version>
    <executions>
    <execution>
    <phase>package</phase>
    <goals>
    <goal>shade</goal>
    </goals>
    <configuration>
    <transformers>
    <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
    <mainClass>org.sonatype.haven.HavenCli</mainClass>
    </transformer>
    </transformers>

    <filters>
    <filter>
    <artifact>*:*</artifact>
    <excludes>
    <exclude>META-INF/*.SF</exclude>
    <exclude>META-INF/*.DSA</exclude>
    <exclude>META-INF/*.RSA</exclude>
    </excludes>
    </filter>
    </filters>
    </configuration>
    </execution>
    </executions>
    </plugin>
    </plugins>
    </build>







    <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <version>2.4.3</version>
    <executions>
    <execution>
    <phase>package</phase>
    <goals>
    <goal>shade</goal>
    </goals>
    <configuration>
    <transformers>
    <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
    <mainClass>org.sonatype.haven.HavenCli</mainClass>
    </transformer>
    </transformers>

    <filters>
    <filter>
    <artifact>*:*</artifact>
    <excludes>
    <exclude>META-INF/*.SF</exclude>
    <exclude>META-INF/*.DSA</exclude>
    <exclude>META-INF/*.RSA</exclude>
    </excludes>
    </filter>
    </filters>
    </configuration>
    </execution>
    </executions>
    </plugin>
    </plugins>
    </build>

    <dependencies>
    <dependency>
    <groupId>org.scala-lang</groupId>
    <artifactId>scala-library</artifactId>
    <version>2.11.11</version>
    </dependency>
    </dependencies>
```


## Test
```
<dependency>

<groupId>junit</groupId>

<artifactId>junit</artifactId>

<version>4.11</version>

<scope>test</scope>

</dependency>

<dependency>

<groupId>io.spray</groupId>

<artifactId>spray-testkit_${scala.compat.version}</artifactId>

<version>${spray.version}</version>

<scope>test</scope>

</dependency>

<dependency>

<groupId>org.specs2</groupId>

<artifactId>specs2-core_${scala.compat.version}</artifactId>

<version>2.4.16</version>

<scope>test</scope>

</dependency>

<dependency>

<groupId>org.specs2</groupId>

<artifactId>specs2-html_${scala.compat.version}</artifactId>

<version>2.4.6</version>

<scope>test</scope>

</dependency>

<dependency>

<groupId>org.specs2</groupId>

<artifactId>specs2-junit_${scala.compat.version}</artifactId>

<version>2.4.6</version>

<scope>test</scope>

</dependency>

<dependency>

<groupId>org.scalatest</groupId>

<artifactId>scalatest_${scala.compat.version}</artifactId>

<version>2.2.4</version>

<scope>test</scope>

</dependency>

</dependencies>
```
