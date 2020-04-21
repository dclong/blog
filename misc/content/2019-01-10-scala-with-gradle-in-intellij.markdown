Status: published
Date: 2019-11-26 18:11:29
Author: Ben Chuanlong Du
Slug: scala-with-gradle-in-intellij
Title: Quickly Create a Scala Project Using Gradle in Intellij IDEA
Category: Computer Science
Tags: programming, Scala, Gradle, IntelliJ IDEA, JVM

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Easy Way

1. Create a directory (e.g., `demo_proj`) for your project.

2. Run `gradle init --type scala-library` in terminal in the above directory.

3. Import the directory as a Gradle project in IntelliJ IDEA.
    Alternatively,
    you can add `apply plugin: 'idea'` into `build.gradle`
    and then run the command `./gradlew openIdea` to import the directory as a Gradle project in Intellij IDEA.

## Hard Way

1. Create a Gradle (default Java) project in IntelliJ IDEA. 

2. Create a directory named `scala` under `src/main`.

3. Mark the directory `src/main/scala` as source root directory.

4. Open `build.gradle` and change its content to the following.

        plugins {
            id 'scala'
        }
        apply plugin: 'idea'

        group 'net.legendu'
        version '1.0-SNAPSHOT'

        sourceCompatibility = 1.8

        dependencies {
            // Use Scala 2.12 in our library project
            implementation 'org.scala-lang:scala-library:2.12.7'

            // Use Scalatest for testing our library
            testImplementation 'junit:junit:4.12'
            testImplementation 'org.scalatest:scalatest_2.12:3.0.5'

            // Need scala-xml at test runtime
            testRuntimeOnly 'org.scala-lang.modules:scala-xml_2.12:1.1.1'
        }
