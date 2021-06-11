UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: String in Different Programming Languages
Date: 2014-09-14 16:34:30
Tags: Python, programming, Java, string, bash, Ruby, R
Category: Computer Science
Slug: summary-string-popular-programming-language
Author: Ben Chuanlong Du
Modified: 2014-09-14 16:34:30

A string is essentially a sequence of characters. 
This is how string is implemented in many programming languages (string in Java is different).
For this reason, you can operate string like an array in some programming languages.
This post is a shallow summary on strings in different programming languages.
For a deep discussion, please check other posts. 

## Representate

- C++: double quotes (single quotes for char type)
- Java: double quotes (single quotes for char type)
- Bash: single or double quotes (double quotes allows expansion of varialbes while single quotes not) 
- Python: single or double quotes (exchangeable)
- Ruby: single or double quotes (single preserve escapes while double interpret them)
- R: single or double quotes (exchangeable)

## Substring

- C++: use iterators and constructor of the std::string class
- Java: substring() as a method
- Bash: `${str:0:3}` where `str` is a string variable
- Python: used like an array `str[2:]`, `str[:2]`, `x[:-2]`, ...
- Ruby: `slice()` as a method or used like an array str[3..-1], str[2,3], ...
- R: `substr()` as a function

## Concatenate

- C++: +
- Java: +
- Bash: `"${str1}other_str"` where `str1` is a string variable. If no white space, double quotes can be omitted
- Python: +
- Ruby: + 
- R: paste() as a function

## Length

- C++: size() as a method
- Java: length() as a method
- Bash: `${#v}` where `v` is a variable in bash 
- Python: len() as a function
- Ruby: length() as a method

