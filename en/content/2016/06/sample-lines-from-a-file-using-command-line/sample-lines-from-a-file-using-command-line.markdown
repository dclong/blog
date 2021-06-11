UUID: 1f35c839-fcf9-46f5-9c77-002c630d2a6c
Status: published
Date: 2016-06-28 10:52:36
Author: Ben Chuanlong Du
Slug: sample-lines-from-a-file-using-command-line
Title: Sample Lines from a File Using Command Line
Category: OS
Tags: Linux, shell, command line, sample, shuffle, shuf, q, text, SQL
Modified: 2017-10-28 10:52:36


NOTE: the article talks about sampling "lines" rather than "records". 
If a records can occupy multiple lines, 
e.g., if any field contains a new line (`\n`),
the following tutorial does not work 
and you have to fall back to more powerful tools such as Python or R.

Let's say that you want sample 500 lines (without replacement) from a file.
This can be done easily using a scraping language such as R or Python. 
However, if samling lines is all you have to do,
it is much faster to do it in shell. 
While there are many command lines tools you can use, 
the one I found to be elegantest is 'shuf'.
`shuf` permuates lines of a file. 
If you want to sample 500 lines, 
then you you just have to keep the first 500 shuffled lines.
```sh
shuf -n 500 file
```
It is a little more work if the file contains a header line
and you want to keep the header line and sample from the rest lines.
```sh
# keep the header
head -n 1 file > sample_500
# sample from the rest line and append to sample_500
tail -n +2 file | shuf -n 500 >> sample_500
```
There is another tool named [q](http://harelba.github.io/q/)
for performing SQL operations on structured text files. 
If the text file is structured,
then task can be done even easier with `q`.
Assume the text file is tab delimited and has a header, 
then you can use the following command to sample 500 lines from it.
The option `-O` outputs the header also.
```sh
q -t -H -O 'select * from file order by random() limit 500'
```
`q` can be installed with the command below. 
```
wajig install q-text-as-data
```

Even thougt I'm Linux fan, 
I'm a practical Linux fan 
not liking some enthusiasium of Linux 
who broadcasting about solving every probelm using command line.
If there is a simple and elegant command line tool to get your work done,
then use it. 
Otherwise, instead of cooking up a weird, unreadable, anti-human shell command, 
R or Python is a much better choice.
