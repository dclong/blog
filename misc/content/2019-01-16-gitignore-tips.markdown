Status: published
Date: 2020-06-14 18:01:30
Author: Ben Chuanlong Du
Slug: gitignore-tips
Title: Gitignore Examples
Category: Computer Science
Tags: programming, Git, .gitignore

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Online Tools

- [gitignore.io](https://www.gitignore.io/)

- [github/gitignore](https://github.com/github/gitignore)

## Gitignore Example for Python
```
.DS_Store
.idea/
.theia/
*.ipr
*.iws
.ipynb_checkpoints/
.coverage
.mypy
.mypy_cache
*.crc
__pycache__/
venv/
.venv/
target/
dist/
*.egg-info/
doc*/_build/
*.prof
```

## Gitignore Example for Java
```
# Java 
*.class

## BlueJ files
*.ctxt

## Mobile Tools for Java (J2ME)
.mtj.tmp/

## Package Files
*.jar
*.war
*.ear

# Gradle 
.gradle
/build/
/out/

## Ignore Gradle GUI config
gradle-app.setting

## Avoid ignoring Gradle wrapper jar file (.jar files are usually ignored)
!gradle-wrapper.jar

## Cache of project
.gradletasknamecache

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*

# Mac
.DS_Store

# IDE
.theia/
.idea/
*.ipr
*.iws

# Misc
core
*.log
deprecated

```
