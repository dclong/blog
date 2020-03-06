Status: published
Date: 2019-05-12 11:12:42
Author: Ben Chuanlong Du
Slug: qt-in-python
Title: Use Qt in Python
Category: Computer Science
Tags: programming, GUI, Python, QT, PyQT5, PySide2

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## PyQt5 vs PySide2

https://www.reddit.com/r/Qt5/comments/a3zt3j/eli5_pyqt5_pyside2_which_one_to_use/

Both PyQt5 (developed by Riverbank) and PySide2 (official Python bindings from Qt) are great.
They have very similar APIs.
However,
PySide2 has a more friendly LGPL licence.
Personally,
I prefer PySide2.

## Installation 
### PySide2
```
pip3 install PySide2
```
### PyQt5
```
pip3 install PyQt5
```

- [PyQt5 GitHub Repository](https://github.com/baoboa/pyqt5)

- [PyQt5 Examples](https://github.com/baoboa/pyqt5/tree/master/examples)

## Git Repository of PySide2

git clone git://code.qt.io/pyside/pyside-setup.git

## PyQt
```
QtCore.QCoreApplication.instance().quit
# vs
QtGui.qApp.quit vs QtGui.QMainWindow (self.close)
```
## Tutorial

https://build-system.fman.io/python-qt-tutorial

https://wiki.qt.io/Qt_for_Python_Tutorial_HelloWorld

https://wiki.qt.io/Qt_for_Python_Tutorial_HelloQML

https://wiki.qt.io/Qt_for_Python_Tutorial_HelloQMessageBox

https://wiki.qt.io/Qt_for_Python_Tutorial_ClickableButton

https://wiki.qt.io/Qt_for_Python_Tutorial_SimpleDialog

https://wiki.qt.io/Qt_for_Python_Tutorial:_Data_Visualization_Tool

https://wiki.qt.io/Qt_for_Python_Signals_and_Slots

https://wiki.qt.io/Qt_for_Python_UsingQtProperties

https://wiki.qt.io/Qt_for_Python_DBusIntegration

https://wiki.qt.io/Qt_for_Python_UiFiles

## References


https://www.qt.io/qt-for-python

https://wiki.qt.io/Qt_for_Python/Tutorial

https://wiki.qt.io/Differences_Between_PySide_and_PyQt

http://zetcode.com/gui/pyqt4/firstprograms/

http://openbookproject.net/thinkcs/python/english3e/events.html
