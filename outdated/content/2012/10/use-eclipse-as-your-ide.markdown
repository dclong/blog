Status: published
Date: 2020-05-22 13:41:22
Slug: use-eclipse-as-your-ide
Author: Ben Chuanlong Du
Title: Use Eclipse as Your IDE
Category: Software
Tags: IDE, programming, Eclipse, software, editor, 


1. There are at least 3 ways to jump to errors quickly in Eclipse

    - Click these red icons on the right margin.
    - Click the `Previous Annotation` button 
    or `Next Annotation` buttons on the tool bar or under the `Navigation` menu.
    - Use hot keys (`Ctrl+.` for `Next Annotation` and `Ctrl+,` for `Previous Annotation` by default).

2. To tidy code, 
    use the `Format` button under the `Source` menu.

3. To quickly comment selected code in Eclipse, 
    you can use hot keys `Crtl+/`. 
    To uncomment selected code, 
    simply press the hot keys again.

4. To quickly import a package which has no `.jar` files 
    (i.e. you have available all source code) to an existing project, 
    you can simply drag the package on the `src` folder 
    in the corresponding project in eclipse. 
    Another way is to first create a new package with the same
    name as the existing package, 
    then right click on the newly created
    package and choose `Import...` in the short menu. 
    In the prompt out,
    you can choose either `Archive File` or `File System` under
    the `General` tab depending on whether there are `.jar` files in the package
    or not. 
    Then you can choose which files you want to import into
    the package and click finish after you have done.

5. To change a variable name, you'd better use refactor which will
    automatically change all occurrences.

6. Use `TODO` to add task in eclipse.

7. To build projects manually, 
    follow instructions 
    [here](http://help.eclipse.org/helios/index.jsp?topic=%2Forg.eclipse.platform.doc.user%2Ftasks%2Ftasks-75.htm).


1. install MarketPlace after you install eclipse

2. To change editor fonts in Eclipse.

Menu -> Windows -> Preference -> General -> Apprearance -> Colors and Fonts -> Text Font -> Edit (on the right panel) 

3. Eclipse has an extensive amount of settings. 
    Sometimes it is hard to find the right settings you want. 
    A better way is to type in text in the search box to search for the settings you want.


## Eclipse for Java

1. You can use `format` button under `source` menu to tidy the code.


## Speed up Eclipse

http://stackoverflow.com/questions/316265/how-can-you-speed-up-eclipse


Eclipse Che seems like a good cloud IDE, keep your eyes on it!!!
eclipse che seems to be a good remote IDE, codenvy is based on it; but seems a little bit hard to get started, not out of box experience

https://ist.berkeley.edu/as-ag/tools/howto/eclipse-plugins.html

http://askubuntu.com/questions/81341/install-eclipse-ide-for-java-ee-dev-via-apt-get-is-it-possible

## Teradata SQL Plugin for Eclipse

https://downloads.teradata.com/download/tools/teradata-plug-in-for-eclipse

https://community.teradata.com/t5/Tools/Error-during-Teradata-Plug-in-for-Eclipse-Installation/td-p/18066

http://stackoverflow.com/questions/5482554/how-to-install-plugin-for-eclipse-from-zip


http://developer.teradata.com/tools/articles/getting-started-with-teradata-plug-in-for-eclipse

## References

[Useful Plugins for Eclipse](http://www.legendu.net/en/blog/useful-plugins-for-eclipse/)