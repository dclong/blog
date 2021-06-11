Status: published
Date: 2019-10-10 21:00:55
Author: Benjamin Du
Slug: update-a-line-in-standard-output
Title: Update a Line in Standard Output
Category: Computer Science
Tags: programming, Python, sys.stdout, standard output, return, return and new line
Modified: 2019-10-10 21:00:55

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

The trick is to use `\r` (return) instead `\n` (return and new line).
I will use Python to illustrate. 
The following Python code

:::Python
import sys

for idx in range(5):
    sys.stdout.write(f'\nLine {idx}')

outputs the following lines.

Line 0
Line 1
Line 2
Line 3
Line 4

while the following Python code

:::Python
import sys

for idx in range(5):
    sys.stdout.write(f'\rLine {idx}')

outputs `Line i` (where i runs from 0 to 4)
to the same line in standard output.
