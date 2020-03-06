UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Java Programming Style
Date: 2012-12-03 00:00:00
Tags: style, Java, programming
Category: Computer Science
Slug: java-programming-style
Author: Ben Chuanlong Du

## Good Writing Style

1. It is recommend to always use `{}` if even there is only one statement inside it. 
The reason is that you never know whether you are going to add more statements into it or not. 
And it will make the code more readable.

2. Feel free to declare the variable in the smallest `{}` block possible. 
The compiler will optimize this kind of code for us. 
So it is better to make the code more readable.

3. It is always good to write code similar to how you would solve the problem naturely. 
It is easy to make mistakes when we try to make the code more concise. 
Unless you can dramatically improve the performance of the code, 
do not change the code for conciseness.

4. Avoid using a same name for a different types (instance, local and argument) of variables.

