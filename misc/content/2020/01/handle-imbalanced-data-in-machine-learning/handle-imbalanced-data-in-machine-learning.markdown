Status: published
Date: 2020-02-18 10:40:49
Author: Benjamin Du
Slug: handle-imbalanced-data-in-machine-learning
Title: Handle Imbalanced Data in Machine Learning
Category: AI
Tags: AI, data science, machine learning, imbalanced data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[scikit-learn-contrib/imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)
is a Python Package to Tackle the Curse of Imbalanced Datasets in Machine Learning.

## Type of Imbalanced Data

- Intrinsic (imbalance is a direct result of the nature of the dataspace)
- Extrinsic (due to time and/or storage, etc.)



- Between-class Imbalance
	- Relative imbalance (OOM)
	- Rare instances a.k.a. absolute rarity (pink blood patient)
- Within-class Imbalance


- Data complexity (primary)
	- Overlapping
	- Lack of representative data
	- Small disjuncts
- Imbalanced
- Small sample size

## Impact of Imbalanced Data on Decision Tree
- Fewer and fewer observations of minority class examples
	resulting in fewer leaves describing minority concepts and successively weaker confidences estimates
- Concepts that have dependencies on different feature space conjunctions 
	can go unlearned by the sparseness introduced through partitionining

## Evaluation

- don't use accuracy (or error rate)
- use ROC, PR curve, F1 score, etc.
- don't get hard classifications
- get probability estimates
- don't use a 0.5 decision threshold blindly
- check performance curves
- test on data to operate on

## Ways to Handle Imbalanced Data

- Do nothing
- Balance the training set
	Oversampling: tied data leading to overfitting
	Undersampling: miss important concepts 
	overall undersampling is preferred if there are enough data.
	However, oversampling might be better if you have very small data.

- Border based approach
- Sampling with Data Cleaning
- Adjust algorithms
- Cluster-based Sampling
- Sampling + Boosting
- New algorithms
- Anomaly detection


## Undersampling

- EasyEnsemble (recommended)
- BalanceCascade
- KNN based (NearMiss-1, NearMiss-2, Near-Miss-3, Most Distant)
- One-sided selection (OSS)

## Border-based Approaches

### Tomek Links
A pair of minimally distanced nearest neighbors of opposite classes. 
 Remove the majority instance of Tomek Links. 
  Makes the border more clear

### SMOTE
Synthetic Minority Oversampling TEchique
 Synthesizing new minority class examples 
  break the tie introduced by simple oversampling and augment the original data
   shown a great success in various applications  
   Similar to mixup for deep learning
### Variation of SMOTE
Borderline-SMOTE
 ADASYN
  SMOTE + Undersampling
   SMOTE-NC (nominal continuous)
     SMOTE-N (nominal)

### Sampling + Data Cleaning
 OSS
  CNN + Tomek Links
   NCL based on ENN
    SMOTE + ENN 
     SMOTE + Tomek

### Adjusting Algorithms
Class weights
 Decision threshold
  Modify an algorithm to be more sensitive to rare classes

## Box Drawings

Construct boxes (axis-parallel hyper-rectangles) around minority class examples
 Concise, intelligible representation of the minority class
  Penalize the number of boxes
   Exact Boxes
    Mixed-integer programming 
     Exact but fairly expensive solution
      Fast Boxes 
       Faster clustering method to generate the initial boxes
        Refine the boxes
         Both perform well among a large set of test datasets


## Anomaly Detection - Isolation Forest
identify anomalies in data (by learning random forests)
     measuring the average number of decision splits to isolate each point
      calculate each data points anomaly score (likelihood to belong to minority)




## References

https://www.youtube.com/watch?v=YMPMZmlH5Bo

http://storm.cis.fordham.edu/~gweiss/small_disjuncts.html

https://www.svds.com/learning-imbalanced-classes/

