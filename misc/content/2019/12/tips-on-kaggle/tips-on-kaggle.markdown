Status: published
Date: 2020-02-04 10:37:03
Author: Benjamin Du
Slug: tips-on-kaggle
Title: Tips on Kaggle
Category: Computer Science
Tags: programming
Modified: 2020-02-04 10:37:03

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## General Tips

1. By default,
    internet access from a Kaggle notebook/kernel is turned off.
    You have to manually turn it on from the right-side panel 
    in order to visit access internet.

## Tips for Competition on Kaggle

## Choose the Right Competitions

If you are a beginner, 
tackle the "Getting Started" competitions.
You can try "Research" and "Feature" competitions when you become experienced.

## Set incremental goals

## Review most voted kernels

## Ask questions on the forums



### Keep a logbook or use a model versioning tool 

It is a good to keep a logbook or use a model versioning tool 
since you will typically have many iterations of models.
If you like a simple tool, use a spreadsheet or markdown doc.
Otherwise, find a model versioning tool.

1. Establish a single baseline model to compare all future changes to.

2. Come up with a bunch of tweaks you want to try 
    and run modified versions of the baseline 
    for each tweak independently rather than in a cumulative fashion.

3. Maintain the same (and smallest) CNN Architecture for as long as possible 
    as it will make iteration quicker and with some look many of the hyper-parameters 
    should transfer decently to larger more complex models.

## Get More Data 

If you are doing a image, voice or text related competition,
do some research before you start coding 
and see if a similar competition has been run before 
or if there are any databases of similar labelled training sets you can use. 
More data is never really harmful to your model (assuming the quality of labelling is decent), 
so get as much of it as you can, 
but just don't forget to keep your validation 
and test sets from the original dataset provided to you 
or you may end up with a train-test mismatch.


### Leveraging Existing Kernels

It is always good practice to learn from others
and leverage existing work.

Note: If a kernel suggests a bunch of techniques to use for your model 
you should check if they state the resultant performance gains, 
otherwise be skeptical and conduct tests yourself 
before blindly incorporating them into your own models :)

### Preprocessing Data

#### Images

Cropping & Other Augmentations

### Transfer Learning

### Start from Easy/Simple/Small Models

## Download Datasets from Kaggle Using Kaggle API

1. Install the Python package kaggle. 

2. Generate a token file `kaggle.json` and place it into your directory `$HOME/.kaggle`.
    www.kaggle.com -> Your Account -> Create New API token. 

3. Make sure that `$HOME/.kaggle/kaggle.json` is readable only by you.

        :::bash
        chmod 600 $HOME/.kaggle/kaggle.json

4. Search for datasets on Kaggle using the following command.

        :::bash
        kaggle datasets list -s [keywords]

5. Download a dataset using the command below.

        :::bash
        kaggle datasets download user/dataset


For more details, 
please refer to [Kaggle Public API](https://www.kaggle.com/docs/api)
and
[Easy way to use Kaggle datasets in Google Colab](https://www.kaggle.com/general/51898)
.

## Useful Datasets for Learning

[ML-friendly Public Datasets](https://www.kaggle.com/annavictoria/ml-friendly-public-datasets)

There are lots of machine learning ready datasets available to use for fun or practice 
on Kaggle's [Public Datasets platform](https://www.kaggle.com/datasets). 
Here is a short list of some of our favorites that we've already had the chance to review. 
They're all (mostly) cleaned and ready for analysis!

### Binary Classification
* [Indian Liver Patient Records](https://www.kaggle.com/uciml/indian-liver-patient-records)
* [Synthetic Financial Data for Fraud Detection](https://www.kaggle.com/ntnu-testimon/paysim1)
* [Business and Industry Reports](https://www.kaggle.com/census/business-and-industry-reports)
* [Can You Predict Product Backorders?](https://www.kaggle.com/tiredgeek/predict-bo-trial)
* [Exoplanet Hunting in Deep Space](https://www.kaggle.com/keplersmachines/kepler-labelled-time-series-data)
* [Adult Census Income](https://www.kaggle.com/uciml/adult-census-income)

### Multiclass Classification
* [Iris Species](https://www.kaggle.com/uciml/iris)
* [Fall Detection Data from China](https://www.kaggle.com/pitasr/falldata)
* [Biomechanical Features of Orthopedic Patients](https://www.kaggle.com/uciml/biomechanical-features-of-orthopedic-patients)

### Regression
* [Video Game Sales with Ratings](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings)
* [NYC Property Sales](https://www.kaggle.com/new-york-city/nyc-property-sales)
* [Gas Sensor Array Under Dynamic Gas Mixtures](https://www.kaggle.com/uciml/gas-sensor-array-under-dynamic-gas-mixtures)

### NLP
* [The Enron Email Dataset](https://www.kaggle.com/wcukierski/enron-email-dataset)
* [Ubuntu Dialogue Corpus](https://www.kaggle.com/rtatman/ubuntu-dialogue-corpus)
* [Old Newspapers: A cleaned subset of HC Corpora newspapers](https://www.kaggle.com/alvations/old-newspapers)
* [Speech Accent Archive](https://www.kaggle.com/rtatman/speech-accent-archive)
* [Blog Authorship Corpus](https://www.kaggle.com/rtatman/blog-authorship-corpus)

### Time Series Analysis
* [Cryptocurrency Historical Prices](https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory)
* [Exoplanet Hunting in Deep Space](https://www.kaggle.com/keplersmachines/kepler-labelled-time-series-data)

### Image Processing
* [YouTube Faces with Facial Keypoints](https://www.kaggle.com/selfishgene/youtube-faces-with-facial-keypoints)
* [Fashion MNIST](https://www.kaggle.com/zalando-research/fashionmnist)

### Mapping and Prediction
* [Seattle Police Department 911 Incident Response](https://www.kaggle.com/sohier/seattle-police-department-911-incident-response)
* [Baltimore 911 Calls](https://www.kaggle.com/sohier/baltimore-911-calls)
* [Crimes in Chicago](https://www.kaggle.com/currie32/crimes-in-chicago)
* [Philadelphia Crime Data](https://www.kaggle.com/mchirico/philadelphiacrimedata)
* [London Crime](https://www.kaggle.com/jboysen/london-crime)

### Large Datasets
* [Iowa Liquor Sales](https://www.kaggle.com/residentmario/iowa-liquor-sales)
* [Seattle Library Checkout Records](https://www.kaggle.com/seattle-public-library/seattle-library-checkout-records)

## Misc 

[The Beginner’s Guide to Kaggle](https://elitedatascience.com/beginner-kaggle)

[如何在 Kaggle 首战中进入前 10%](https://dnc1994.com/2016/04/rank-10-percent-in-first-kaggle-competition/)

https://www.kaggle.com/getting-started/44919

https://towardsdatascience.com/how-to-improve-your-kaggle-competition-leaderboard-ranking-bcd16643eddf

https://www.kdnuggets.com/2016/11/rank-ten-precent-first-kaggle-competition.html


https://towardsdatascience.com/how-to-improve-your-kaggle-competition-leaderboard-ranking-bcd16643eddf

https://towardsdatascience.com/how-i-got-in-the-top-1-on-kaggle-79ddd7c07f1c
