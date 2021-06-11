UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Automated Phone Bill Using Ruby Program
Date: 2012-06-18 08:17:18
Tags: Python, programming, Verizon, Ruby, email, phone
Category: Computer Science
Slug: automated-verizon-bill-using-ruby
Author: Ben Chuanlong Du
Modified: 2014-06-18 08:17:18

[code]: https://github.com/dclong/Ruby-Verizon

I have decided to try different programming languages. 
I learn Python a month ago. 
I would like to say that Python is great scripting language. 
The only thing I do not like so far is inconsistent about methods and functions.
It is annoying to remember whether a call should be made by method or by function. 
I started learning Ruby a few weeks ago.
I have to say that the syntax of Rudy looks weird to me at first,
and I even doubted whether it is worth my effort to learn this language since I already 
know how to program in Python. 
But I have long heard about cool stuff such as Ruby on Rails, Cucumber and so on. 
So I finally convinced myself to continue on studying Ruby. 
As I mentioned in another post, the best way to learn a language is to use it.
I have been thinking about writing a program to parse the statement (in pdf) of 
my Verizon family plan, calculating bill for each member and send email to notify
the bill each of them has to pay automatically. 
I had a R script which can do the calculation part provided that I type some
information manually. 
I decided to make my job as the primary user of the family plan easier.
I am happy that I left this coding job to Ruby for practise. 
[My code](https://github.com/dclong/Ruby-Verizon) is on GitHub.
If the code does not run, 
you have to install a few ruby packages in order to use it. 

    sudo gem install pdf-reader actionmailer highline

The code only works for current Verizon family plan statement. 
I wish Verizon not to change the format of the family plan statement so that
this program can be used by people like me for a long time, otherwise I have to
make this program more robust to support statement in other format as well.

