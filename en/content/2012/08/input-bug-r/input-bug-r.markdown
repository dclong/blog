UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: An IO Bug in R
Date: 2012-08-15 21:22:47
Slug: input-bug-r
Author: Ben Chuanlong Du
Category: Computer Science
Tags: warning, IO, programming, R, bug
Modified: 2016-08-15 21:22:47

<img src="http://dclong.github.io/media/computer/bug.jpg" height="200" width="240" align="right"/>

I encountered an input/output bug in R in Linux system. 
The symptom is that input and output are not displayed in the terminal 
and the warning message 
"An unusual circumstance has arisen in the nesting of readline input. 
Please report using bug.report()" is shown. 
I found that though input and output are not displayed, you can still 
interact with the underlying R session. 
A safe way is to save the R workspace, quit the R session, open a new 
R session and load in the saved workspace. To save the R workspace,
just type in `save.image('ws_name')` in the console, where `ws_name` 
is the name of the workspace. Notice that you will not see anything 
happen on the console, so you have to make sure that you do not make 
any mistake typing in the command. To quit the R session after saving 
the workspace, you can type in 'q('no')' in the console. 
Similarly, you won't see anything in the console, so make sure you do not 
make any mistake. Now can open a new R session, and then load in the saved 
workspace. 
