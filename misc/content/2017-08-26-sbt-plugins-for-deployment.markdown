UUID: b41a895b-b2e7-4cf2-911f-48dec9e533d6
Status: published
Date: 2017-12-23 09:30:38
Author: Ben Chuanlong Du
Slug: sbt-plugins-for-deployment
Title: sbt Plugins for Deployment
Category: Computer Science
Tags: programming, sbt, plugin, Scala

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. sbt Assembly is recommended, generally speaking. 

## sbt-assembly

sbt-assembly creates a fat JAR,
i.e., a single JAR file containing all class files from your code and libraries. 
By evolution, 
it also contains ways of resolving conflicts 
when multiple JARs provide the same file path (like config or README file). 
It involves unzipping of all library JARs, 
so it is a bit slow, but these are heavily cached.

## sbt-pack

sbt-pack keeps all the library JARs intact, 
moves them into target/pack directory 
(as opposed to ivy cache where they would normally live), 
and makes a shell script for you to run them.

## sbt-native-packager

sbt-native-packager is similar to sbt-pack but it was started by a sbt committer Josh Suereth, 
and now maintained by highly capable Nepomuk Seiler (also known as muuki88). 
The plugin supports a number of formats like Windows msi file and Debian deb file. 
The recent addition is a support for Docker images.

All are viable means of creating deployment images. 
In certain cases like deploying your application to a web framework etc., 
it might make things easier if you are dealing with one file as opposed to a dozen.
