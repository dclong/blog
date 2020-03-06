UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Make Plots in SAS
Date: 2012-07-11 00:00:00
Tags: image, SAS, graphics, programming
Category: Computer Science
Slug: sas-plot
Author: Ben Chuanlong Du

<img src="http://dclong.github.io/media/sas/sas.jpg" height="200" width="240" align="right"/>

2. There are functions to add points, lines and legends to an existing plot in R.
In SAS, there is no way to do this. 
What you can do is to add plotting commands in the plotting procedure and rerun your code. 

3. Staring from version 9.2, SAS offers new procedures such as PROC SGPLOT and PROC SGPANEL for making plots.
PROC SGPLOT (sophisticated graphical plot) produces high quality plots. 
PROC SGPANEL divides the window into several parts and make plots on these sub area.

4. It is possible to call R from SAS which means that you can use R to make plots in SAS if you like. 
