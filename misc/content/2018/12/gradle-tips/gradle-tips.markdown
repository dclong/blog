Status: published
Date: 2018-12-08 16:57:03
Author: Ben Chuanlong Du
Slug: gradle-tips
Title: General Tips for Gradle
Category: Computer Science
Tags: programming, JVM, Java, gradle, Groovy, compile, compiler, package management
Modified: 2020-04-08 16:57:03

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Install & Upgrade Gradle


The latest version of gradle can be installed via PPA on Ubuntu.

    :::bash
    sudo add-apt-repository ppa:cwchien/gradle
    sudo apt-get update

And gradle can be upgraded using the following command.

    :::bash
    sudo apt-get upgrade gradle

The latest version of Gradle can be installed using Homebrew on Mac.

    :::bash
    brew install gradle

And gradle can be upgraded using the following command.

    :::bash
    brew upgrade gradle

## Tricks and Traps

1. You can set the default logging level to debugging by adding the following line 
    into the file `gradle.properties` under the root directory of the project.

        org.gradle.logging.level=debug

1. It is recommended that you use the gradle wrapper `gradlew` to compile the project.
    You don't have to use the `task` subcommand 
    when using the gradle wrapper `gradlew` to compile the project.
    For example, 
    instead of `gradle task build` you can use `./gradlew build`.

2. You'd better rebuild (using the `build` command) your project 
    before testing running your project or generating a fat jar (using the `shadowjar` command).
    Otherwise, 
    you might run into weird issues such as resource file not found, etc.

3. You can generate a Gradle wrapper (with the given version) 
    or update the version of an existing Gradle wrapper using the following command.

        :::bash
        gradle wrapper --gradle-version 6.0.1

## The IDEA Plugin
You can enable the Gradle IDEA plugin by having the following line in your `build.gradle` file.
```
apply plugin: 'idea'
```
This plugins add a task named `openIdea` and allows you to import a Gradle project from command line.
Sometimes, importing a project from IntelliJ IDEA does not work as expected.
However, 
the command line always works.
```
./gradlew openIdea
```

## Customize Tasks

https://stackoverflow.com/questions/11767713/adding-script-to-build-gradle

## [shadowJar](https://github.com/johnrengelman/shadow) for Gradle
```
plugins {
    id "com.github.johnrengelman.shadow" version "4.0.3"
}
```
```
shadowJar {
    zip64 true
    mergeServiceFiles()
    exclude "META-INF/*.SF"
    exclude 'META-INF/*.DSA'
    exclude 'META-INF/*.RSA'
    exclude "LICENSE*"
}
```

## Shadow

archiveClassifier 

https://github.com/johnrengelman/shadow/issues/463#event-2615996541

## Gradle Sync

1. support only local sync
2. not incremental

Overall it is far behind rsync. 
I'd rather use rsync in shell.

## Gradle SSH Plugin

https://gradle-ssh-plugin.github.io/

I'd rather use ssh/rsync in shell.

## Gradle Home for IntelliJ IDEA

/usr/local/Cellar/gradle/5.1/libexec/
https://stackoverflow.com/questions/18495474/how-to-define-gradles-home-in-idea/34502612

## Specifying Dependencies

https://docs.gradle.org/current/userguide/java_library_plugin.html#sec:java_library_configurations_graph

https://stackoverflow.com/questions/44493378/whats-the-difference-between-implementation-and-compile-in-gradle

## References

https://askubuntu.com/questions/932083/how-do-i-upgrade-gradle

https://ftclausen.github.io/general/gradle_sync_task_is_not_incremental/

https://docs.gradle.org/current/userguide/upgrading_version_4.html

https://docs.gradle.org/current/userguide/java_library_plugin.html#sec:java_library_configurations_graph

https://stackoverflow.com/questions/44493378/whats-the-difference-between-implementation-and-compile-in-gradle
