UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-03-13 15:26:10
Author: Ben Chuanlong Du
Slug: ar1x-process
Title: AR1X Process
Category: AI
Tags: statistics, AR1X, time series, linear regression, model
Modified: 2015-03-13 15:26:10

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



1. talk about the ar1x process, and your simulation, 
GLM might not be as good as OLS for estimating parameters, but be careful about inference, why? 
you use do inference based on simulation ...
more complicated algorithm based on optimization ...




Several different names are used to describe ARIMA models with input series. Transfer function model, intervention model, interrupted time series model, regression model with ARMA errors, Box-Tiao model, and ARIMAX model are all different names for ARIMA models with input series. Pankratz (1991) refers to these models as dynamic regression models.


1. TSA::arimax in R, but the documentation is poor. I even don't know which model specification it uses.
The function was implemented by Kung-Sik Chan in University of Iowa. 
You can contact him and get clear about the model specification.

phone : (319) 335-2849
e-mail: kchan@stat.uiowa.edu

http://stackoverflow.com/questions/25224155/transfer-function-models-arimax-in-tsa

http://www.r-bloggers.com/the-arimax-model-muddle/

http://econometricsense.blogspot.com/2012/01/time-series-intervention-analysis-wih-r.html

http://econometricsense.blogspot.com/2012/01/intervention-analysis.html

2. SAS
Though the following post allows differencing the response variable, it doesn't allow an arbitrary coefficient.
http://support.sas.com/documentation/cdl/en/etsug/63348/HTML/default/viewer.htm#etsug_arima_sect012.htm

3. You can actually estimate the parameters using MLE by yourself. It seems to be very easy.
And you can derive all the theories for it.

I did the math, and it seems to me the MLE (under the assumption of normal) is the same as the OLS estimate,
however, the (asymptoic) distribution of estimate of parameters are much more complicated. 
I have 2 ideas to make inferences. 
