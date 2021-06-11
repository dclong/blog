Status: published
Author: Ben Chuanlong Du
Title: Tips on JavaScript
Date: 2021-04-26 12:48:21
Slug: javascript-tips
Category: Computer Science
Tags: tips, programming, JavaScript, JS, web
Modified: 2021-04-26 12:48:21

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**

### [babel](https://github.com/babel/babel)
[babel](https://github.com/babel/babel)
is a compiler for writing next generation JavaScript.

### [webpack](https://webpack.js.org/)
[webpack](https://github.com/webpack/webpack)
is a module bundler. 
Its main purpose is to bundle JavaScript files for usage in a browser, 
yet it is also capable of transforming, bundling, or packaging just about any resource or asset.

### [grunt](https://github.com/gruntjs/grunt)
[grunt](https://github.com/gruntjs/grunt)
is a JavaScript Task Runner.

[Select the Plates](https://flukeout.github.io/)


## Node.js

[Node.js](https:/nodejs.org/en/) is a JavaScript runtime environment outside browsers.

https://github.com/sindresorhus/awesome-nodejs

https://github.com/bnb/awesome-awesome-nodejs
 
[JavaScript Libraries](http://javascriptlibraries.com/)
[JavaScript WikiBooks](http://en.wikibooks.org/wiki/JavaScript)
[W3Schools JavaScript Tutorial](http://www.w3schools.com/js/default.asp)

## Build Tools

https://arstechnica.com/civis/viewtopic.php?f=20&t=1432661

https://www.tutorialsteacher.com/typescript/typescript-build-tools

## Install & Import a Package

This is a common misunderstanding in Node.js and npm. Installing a package globally doesn't ensure that the package can be required. A global install is meant to be used to install executable files. For example, if you want to install the latest version of npm, then you could run the command: npm install -g npm. This command would install the npm package in {prefix}/lib/node_modules and the executable file in {prefix}/bin (that usually is in your PATH).

In your case, I'd suggest the following:

$ mkdir my-project

$ cd my-project

$ npm init -y
[...]

$ npm install web3
[...]

$ npm install ethereum.js

$ jupyter notebook
[so that your notebook is created in the folder where the npm packages have been installed]

https://github.com/n-riesco/ijavascript/issues/118

## Some Useful Libraries

https://github.com/jupyterlab/lumino

## Testing & Debugging

https://github.com/Microsoft/vscode-recipes/tree/master/Docker-TypeScript

## Docker Client API

https://github.com/AgustinCB/docker-api

https://github.com/apocas/dockerode


1. case sensi tive

2. you don't have to write every line of code in HTML,
    you can save JavaScript code in another file and then load it.


3. alert vs confirm vs prompt

An alert box is often used if you want to make sure information comes through to the user.

When an alert box pops up, the user will have to click "OK" to proceed.

A confirm box is often used if you want the user to verify or accept something.

When a confirm box pops up, the user will have to click either "OK" or "Cancel" to proceed.

If the user clicks "OK", the box returns true. If the user clicks "Cancel", the box returns false.

A prompt box is often used if you want the user to input a value before entering a page.

When a prompt box pops up, the user will have to click either "OK" or "Cancel" to proceed after entering an input value.

If the user clicks "OK" the box returns the input value. If the user clicks "Cancel" the box returns null.

## OOP 

[Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)

[https://www.youtube.com/watch?v=YkoelSTUy7A](Prototype basics - Object Creation in JavaScript P3 - FunFunFunction #46)


## Electron
For desktop UI.

## Libraries

1. D3

2. jQuery

3. AJAX relationship between jQuery? seems that jQuery can make AJAX calls

4. plotly, phantomjs

angularJS

## Visulization
1. Google Visualization APIs


[Underscore](http://underscorejs.org/)
is a JavaScript library that provides a whole mess of useful functional programming helpers without extending any built-in objects. 
It's the answer to the question: 
"If I sit down in front of a blank HTML page, 
and want to start being productive immediately, 
what do I need?" ... and the tie to go along with jQuery's tux and Backbone's suspenders. 

## References

[Python vs JavaScript for Pythonistas](https://realpython.com/python-vs-javascript/)

[JavaScript HTML DOM](https://www.w3schools.com/js/js_htmldom.asp)

https://github.com/jashkenas/coffeescript/wiki/list-of-languages-that-compile-to-js

[Web Design for Everybody: Basics of Web Development & Coding Specialization](https://www.coursera.org/specializations/web-design)

[Python vs JavaScript: Most Important Differences](https://hackr.io/blog/python-vs-javascript)

[Python vs JavaScript](https://www.educba.com/python-vs-javascript/)
