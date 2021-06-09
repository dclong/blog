UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Make Eclipse Support C++11
Date: 2012-08-20 00:00:00
Tags: C/C++, software, eclipse
Category: Software
Slug: eclipse-cpp11
Author: Ben Chuanlong Du

<img src="http://dclong.github.io/media/eclipse/cdt.png" height="200" width="240" align="right"/>

1. Make a new C++ project

1. Default options for everything

2. Once created, right-click the project and go to "Properties"

3. C/C++ Build -> Settings -> Tool Settings -> GCC C++ Compiler -> Miscellaneous -> Other Flags. 
Put -std=c++0x at the end. 

4. C++ General -> Paths and Symbols -> Symbols -> GNU C++. 
Click "Add..." and paste `__GXX_EXPERIMENTAL_CXX0X__` (ensure to append and prepend two underscores) 
into "Name" and leave "Value" blank.

5. Hit Apply, do whatever it asks you to do, then hit OK.

