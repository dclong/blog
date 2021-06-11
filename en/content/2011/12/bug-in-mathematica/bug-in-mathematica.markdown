UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: A Bug in Mathematica
Date: 2016-08-15 21:22:23
Slug: bug-in-mathematica
Author: Ben Chuanlong Du
Category: Computer Science
Tags: Mathematica, programming, bug
Modified: 2016-08-15 21:22:23

<img src="http://dclong.github.io/media/computer/bug.jpg" height="200" width="240" align="right"/>

Mathematica is a very intelligent and powerful math software. 
I use it in my study and research a lot. 
Mathematica's ability to take derivative and to calculate 
limit is obvious powerful–way much beyond many mathematician's ability. 
Mathematica's ability to calculate integral is also powerful. 
There are many integrals than I'm not able to solve while Mathmatica can. 
For a long time I totally trusted Mathematica. 
I thought that it is so intelligent an software that whenever 
it's able to give me a result it must right, 
until one day I asked Mathematica to do some integrals.  
See whether you can find what's wrong with Mathematica.

What I learn is not just this bug in Mathmatica. 
What I learned is that software has bugs, no matter how intelligent it is. 
Bugs happens when a software grow large. 
Never fully trust a software. You should always judge the result based on your own knowledge.

    Integrate[Cos[theta] Exp[Cos[theta] + Sin[theta]] / (2 Pi), {theta, 0, 2 Pi}]
    0
    NIntegrate[Cos[theta] Exp[Cos[theta] + Sin[theta]] / (2 Pi), {theta, 0, 2 Pi}]
    0.635862
    N[Integrate[Cos[theta] Exp[Cos[theta] + Sin[theta]] / (2 Pi), {theta, 0, 2 Pi}]]
    0
