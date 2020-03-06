UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-05-22 01:05:04
Author: Ben Chuanlong Du
Slug: language-equivalents
Title: Language Equivalents
Category: Computer Science
Tags: programming language, equivalent, C, C++, D, Java, R, Python, MATLAB, Julia

**
Things on this page arefragmentary and immature notes/thoughts of the author.
It is not meant to readersbut rather for convenient reference of the author and future improvement.
**

|Description| R |SAS Function|SAS Macro Function|
|:-----------:|:---:|:------------:|:------------------:|
|Convert letters in a string to lower case|tolower(s)|lowcase(s)||
|upper case |toupper(s)|upcase(s)||
|replace|replace|tranwrd||
|uniform random numbers |runif |randurn||
|sub string |substr |substr |%substr|
|get rid of leading and trailing white spaces ||strip|%trim|
|location of non-zero/true elements|which|loc (can we use it in a data step rather than in the IML procedure?)||

## Get Current Working Directory

### Bash
pwd
### C

### C++

### D

### Java

### MATLAB
pwd
### R
getwd 

### Python
os.getcwd

## Change Working Directory
cd
setwd
os.chdir
## List Contents of a Directory
### Bash
ls
### MATLAB
ls
### R
dir 
### Python
os.listdir

## Edit a (script) File

### Julia
edit        

### R
file.edit 

## Install Packages
### Julia
Pkg.add         

### R
install.packages

## Run System Commands
### Julia 
run     

### MATLAB
system  

### R
system

## Read a Table (of Data)
### Julia 
read_table  

### MATLAB
dlmread     

### R
read.table

## Concatenate/Join Strings
### Julia
join        

### R
paste

## Join File Paths
### Julia
joinpath    
### MATLAB
strcat  
### R
paste
## Combine Tables Horizontally
### Julia
cbind/hcat  
### MATLAB
[]  
### R
cbind
## Combine Tables Vertically
### Julia
rbind/vcat  
### MATLAB
[]  
### 
rbind
## Colume Names (of a Table)
### Julia
colnames        
### R
colnames
## Number of Rows (in a Table)
### Julia
nrow    
### MATLAB
size    
### R
nrow
## Number of Columes (in a Table)
### Julia
ncol    
### MATLAB
size    
### R
ncol
## Dimension of Matrix/Table
### Julia
size    
### MATLAB
size    
### R
dim
## Number of Elements in a Vector/Matrix/Table
### Julia
length  
### MATLAB
numel   
### R
length
## With Block
### Julia
with/within!         
### R
with/within
## Apply a Function to Element of a Vector/Factor/Matrix/Table
### Julia
by  
### MATLAB
arrayfun    
### R
apply/lapply/sapply/tapply 

## Frequency of Values

### R
table

### Python
pandas.Series.value_counts

## Missing Values

### R
NA

### Python
numpy.nan

## Check Is Missing

### Python

pandas.Series.isnull

country_freq.isnull()

numpy.isnan

### R

is.na

## Apply Function by Groups

### R
tapply

### Python
pandas.pivot_table

