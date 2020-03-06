UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-03-03 10:08:36
Slug: graphics-in-MATLAB
Author: Ben Chuanlong Du
Title: MATLAB for Visualization
Category: Computer Science
Tags: image, visualization, programming, plot, graphics, MATLAB


1. To display a new graph on on top of an old one, 
you can use command `hold on`. 
In this way, 
you can create multiple plots in a same window. 
Though `plot` can already do multiple plot, command `hold on` 
can be very useful when you want to add some new points 
or curves to an existing graph (e.g. a histogram).

2. Function `subplot` displays multiple plots in the same window,
which is similar to settings `par(mfrow=c(2,2))` or `par(mfcol=c(2,3))` in R.

3. Function `hist` and `histc` produces histograms.

4. Function `staris` produces step graph.

5. Function `plot` plots `2-D` graph 
while function `surf` plots `3-D` graphs. 
Function `surf` is usually used in conjugate with function `meshgrid` 
which can create a matrix of points over which the surface is to be plotted. 
You can also use `ndgrid` instead of `meshgrid` to generate a matrix of points.
However, 
`ndgrid` is usually higher dimensions and the usage is a little different from `meshgrid`, 
so you have to be careful if you wan to use it.

6. After plotting figures using `plot`, 
you can use `title` to add titles for the figures, 
`axis` to set configurations for the axies,
and `xlabel` and `ylabel` to set labels for the x and y axes. 
You can also use `set` to set all configurations for the plots. 
To do this, 
you have to first get the handle of the elements in the plots that you want to modify, 
and then apply `set` on it.

7. `inpolygon` can check whether given points are inside a polygon or not.

8. `spy` visualizes sparse matrices.

9. `image` can not only display images but also make mosaic plot
(sometimes called heat plot or level plot) of a matrices. 
For example, to show the mosaic plot of matrix `x`, 
you can use `image(x,'CDataMap','CDataMapping','scaled')`.

