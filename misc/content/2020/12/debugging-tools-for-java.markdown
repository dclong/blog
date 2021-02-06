Status: published
Date: 2020-12-20 11:43:43
Author: Benjamin Du
Slug: debugging-tools-for-java
Title: Debugging Tools for Java
Category: Computer Science
Tags: Computer Science, Java, JVM, debug, debugging

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## [arthas](https://github.com/alibaba/arthas)
[arthas](https://github.com/alibaba/arthas)

## JDK commands
Thread dump: jstack jvm_pid > <file_name>     (use -F if not responding)

Memory dump: jmap -dump:live,format=b,file=<file_name>.hprof jvm_pid

Heap status:  jmap -heap jvm_pid

GC status: jstat -gccause -h 50 -t jvm_pid 2s  (refresh every 2s, show header every 50 rows, show time stamp)

You can use command jps to find out all pids of currently running jvm process.

Thread dump analysis tool
http://fastthread.io/

Heap dump analysis tool
https://www.eclipse.org/mat/

If MAT can't load your file, you can use jhat to analyze. Then you use your browser to go to 8080 port.

jhat -port 8080 129546.hprof

https://jxray.com/

JXRay is a paid smart heap dump analyzer that other than analyzing the heap dump, it'll also make concrete suggestions on how to fix the problems that it finds.

It's very easy to set up and run, an at the moment (10/2020), it offers free trial of 7 heap analysis for one email.

JVM Profiler
https://www.yourkit.com/

JVM Monitor (Java profiler integrated with Eclipse)
http://www.jvmmonitor.org/
