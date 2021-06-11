UUID: 853d4fe5-2c55-419c-bcb0-76279a9a6716
Status: published
Date: 2017-08-26 19:35:28
Author: Ben Chuanlong Du
Slug: spcify-java-version-to-use-in-a-scala-project
Title: Spcify Java Version to Use in a Scala Project
Category: Computer Science
Tags: programming
Modified: 2017-08-26 19:35:28

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

    javacOptions ++= Seq("-source", "1.8", "-target", "1.8", "-Xlint")

    initialize := {
      val _ = initialize.value
      if (sys.props("java.specification.version") != "1.8")
      sys.error("Java 8 is required for this project.")
    }

Using `javacOptions ++= Seq("-source", "1.8", "-target", "1.8")` 
does not work if you have no Java sources.
But you can set the target JVM for the Scala compiler in build.sbt:
`scalacOptions += "-target:jvm-1.7"`

## References

[Enforcing Java version for Scala project in sbt?](https://stackoverflow.com/questions/19208942/enforcing-java-version-for-scala-project-in-sbt)

[How to force SBT to use Java 8?](https://stackoverflow.com/questions/25926111/how-to-force-sbt-to-use-java-8)

