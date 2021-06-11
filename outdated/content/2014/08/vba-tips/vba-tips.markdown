Status: published
Author: Ben Chuanlong Du
Date: 2014-08-22 13:04:29
Title: Tips on VBA
Slug: vba-tips
Category: Computer Science
Tags: programming, VBA, tips
Modified: 2020-05-22 13:04:29

**
Things on this page are 
fragmentary and immature notes/thoughts of the author.
It is not meant to readers 
but rather for convenient reference of the author and future improvement.
**



## Syntax

8. In some programming languages, an ending semicolon is optional. 
    However, you cannot end statements with semicolons in VBA.

## String

6. String must quoted by double quotation marks instead of single quotation marks.

## Array

8. By default, array or string comparion/search is 1-based in VBA.

11. You must use pass an array by reference in VBA (use the keyword byref)

4. UBound returns the upper bound (inclusive) of an array 
    and LBound gets the lower bound (inclusive) of an array.

8. When you define an array in a usual way, 
    e.g., 
    `Dim arr(10) as Integer`,
    the array `arr` is 0-based (the default), 
    but the upper bound (10) is inclusive 
    which is different from most other programming languages (upper bound is pass-by-1).

1. VBA use parentheses `()` for slicing arrays and array index starts from 1 by default in VBA.

2. define a dynamic integer arrary

        :::vba
        Dim Zombies() As Integer

however, you have populate it using ReDim before you can use it

## Object

2. You can assign values to non-object variables directly (e.g., a = 3),
    however, you must assign values to an object variable using `set`.

1. Selection is an object not a type.
    Selection of cells in Excel share many properties with the range object.

### Range Object

1. The `Offset` method of the `Range` object counts from the top-left most cell. 
        Range("A1").Offset(2,3).Value = 4

2. You cannot do vector/matrix calculations directly on `Range` values.
    For example, `range.value + 1`, `range.value / 10`, etc. raise errors.
    However, you can use set a value for all cells in a range. 
    For example, `Range("A1:F5").value = 1`.

3. prompt to select range

        :::vba
        Set UserRange = Application.InputBox(Prompt:="Please Select Range", Title:="Range Select", Type:=8)

If you want to the range to be highlighted after OK is clicked 

        :::vba
        Application.GoTo UserRange 

## Misc

13. You can either omit an optional argument of a function or leave it blank (i.e., pass a blank value to it) in VBA. 

14. There is no loop control statement such as next/continue, break, etc. in VBA. 
    You have to use the goto statement instead. 
    You can also use `Exit For`, `Exit Do` and `Exit While` as alternatives to `break`.
    You can use `Exit Sub` and `Exit Function` to exit subroutines and functions.

6. Application.CountA: number of cells in the selected range.

7. One way to call an Excel function is 
    to assign the Excel function as a formula to a cell 
    and then extract the value of the cell.
    Mostly of the time, 
    you can call an Excel function directly by `application.funname`. 

9. VBA uses parentheses to slice array, 
    which is the same as matlab 
    and different from most other programming languages 
    (which uses square brackets to slice array).

## Error Handling

4. The `On Error GoTo line_label` trick for handling errors.
    `On Error GoTo 0` 
    turns off error handling.

## Tricks and Traps

3. Code that relies on selction/activation to work is considered harmful
    unless the selection/activation is temporary and absolutely won't cause problems.

## User-defined Modules/Functions/Subroutins/Macro

4. Subroutins in VBA perform actions but does not return any value 
    while a function can perform actions and return a value.
    You cannot change values of others cells in a function? <check it>

5. You'd better use modules instead of plain functions in code editor, 
    not sure about the difference

7. You can run macro defined in another workbook

        Private Sub Workbook_Open() 
            Workbooks.Open "\\scsrv-03\mktgdata$\Adcopy\Ad Master2.xls" 
            Application.Run "'Ad Master2.xls'!DisplayBriefDetails" 
            Workbooks("Ad Master2.xls").Close True 
        End Sub 
