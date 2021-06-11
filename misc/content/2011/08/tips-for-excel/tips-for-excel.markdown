Status: published
Date: 2020-05-22 13:10:13
Slug: tips-for-excel
Author: Ben Chuanlong Du
Title: Tips on Excel
Category: Software
Tags: statistics, MS Office, software, Excel, bug, tips
Modified: 2020-05-22 13:10:13

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## About Statistics Functions

1. Excel is not a reliable software for statistical analysis. 
    It's not even capable for simple operations such as calculating 
    mean and standard deviation when numbers are very big 
    (at least before version 2007, not sure about later versions). 
    If you do have to use Excel for statistical analysis, 
    you'd better verify the results.

2. A bug in Excel 2007 (not sure about later versions) 
    is that the degrees of freedoms of the Chisquare distribution can only be positive integers. 
    If you pass a real number to related functions (density, cdf, etc), 
    the degrees of freedom will first be coerced to an integer 
    (I forget the exact behavior, but it's probably rounding down) and then do the calculation. 
    No warning is shown in this process. Fotunately, 
    the Gamma distribution behaves right in Excel. 
    Be aware of the relationship between Chisquare distribution and Gamma distribution, you can circumambulate this bug. 

3. It seems that the F distribution in Excel can only have integer
    degrees of freedom. If not, the degrees of freedoms will changed to
    integers first. I don't know how to circumvent this problem easily.
    Sure we can write our own functions but it's not worth doing that.

## Tips

1. To unhide a workbook, 
    click the "View" tab and then click the "unhide" button in the window group.

2. You can use the hotkey CTRL + Left/Right/Up/Down Arrow to quickly jump to the end of a used range.

3. You can use macros/functions defined in a workbook if it is open. 
    So you can use put all your macros/functions into a single workbook 
    and just open it for use when needed.
    Or you can put all your macros/functions into "PERSONAL.xlsb" which is a hidden workbook that is always open.

1. insert multiple lines at the same time, select multiple lines, right click and insert

3. after selecting a bunch of cells, right bottom, statistics, you can add more ...
    However, 
    hidden cells in the selection are ignore when calculating statistics.


4. On the Home tab, in the Editing group, click the arrow next to the Clear button Button image, and then do one of the following:
    To clear all contents, formats, and comments that are contained in the selected cells, click Clear All.
    To clear only the formats that are applied to the selected cells, click Clear Formats.
    To clear only the contents in the selected cells, leaving any formats and comments in place, click Clear Contents.
    To clear any comments that are attached to the selected cells, click Clear Comments.

1. counting number of selected cells: bottom right bar  trick -> select ... -> bottom right, summary 

2. trust center -> trust location

## Chart

1. If you select 1 row/column of data with k cells and insert a chart, 
    you get a chart of 1 series at k locations. 
    However, 
    if you select a block of data with m rows and n columns, 
    you get a chart of m series at n locations.


## Functions

1. COUNTIF criteria is a string containing logical comparisons, 
    criteria is a string containing comparison conditions

2. iVal = Application.WorksheetFunction.COUNTIF(Range("A1:A10"),"Green")

## Questions

1. how to open a workbook as hidden by default? You can hide it manually.

5. How to quickly check sum of a banch of cells in a large table where no adjacent cells are available? 
    Is it posisble to use some kind of prompt diaglog? Actually you can write such a function by yourself.

3. learn how to make plots in excel

5. how to adjust series unit? I don't like big long numbers

7. best way to add unit to y? and multiple lines in legends?

8. bar plot with %?

9. save to xlsx by default?

10. auto adjust column width in Excel 2007

1. the bottom line frame in chart?

2. How to use shortcut to quickly switch between worksheets?