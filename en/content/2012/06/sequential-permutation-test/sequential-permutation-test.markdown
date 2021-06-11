UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-03-03 10:17:03
Slug: sequential-permutation-test
Author: Ben Chuanlong Du
Title: Estimation of False Discovery Rate using Sequential Permutation Pvalues
Category: Research
Tags: research, sequential permutation test, biostatistics, Acute Lymphocyctic Leukemia, package, marker, dclong.spt, R, barley, false discovery rate, FDR
Modified: 2015-03-03 10:17:03

<img src="http://dclong.github.io/media/r/r.png" height="200" width="240" align="right"/>
I wrote a paper on sequential permutation test with Tim Bancroft and Dan Nettleton. 
The paper "T. Bancroft, C. Du and D. Nettleton (2012). 
Estimation of False Discovery Rate Using Sequential Permutation P­Values." 
has been accepted by Biometrics. To illustrate ideas in the paper and make sequential 
permutation test easier to use, I wrote an R package **dclong.spt** which is availabe 
on [GitHub](https://github.com/dclong/dclong.spt). In order to make the package smaller, 
I moved these big datasets (used for illustrations in the paper) from the package to this website. 

The data [barley](http://dclong.github.io/media/spt/marker.rda) was produced by experiment 
"Genetic regulation of gene expression of barley in response
to stem rust (Pgt isolate TTKS)" and can be access from PLEXdb (BB64). 
There is a file called "BB64_RMA_tmt_medians.txt" on the download page contains RMA expressions. 
The rma expression for the 75 chips involve fungas infection is the dataset barley in this package. 

The Band T-cell Acute Lymphocyctic Leukemia (ALL) data set can be 
access via the Bioconductor ALL package at <www.bioconductor.org>. 
Measures of messenger ribonucleic acid (mRNA) commonly referred to as expression levels
are available for 12,625 probesets in 128 ALL patients.
Of these 128 patients, we focus on the 21 males who have been classified as having a translocation
between chromosomes 9 and 22 (BCR/ABL) and the 5 males who have a translocation between
chromosomes 4 and 11 (ALL1/AF4). 
This subset of data is the [leukemia](http://dclong.github.io/media/spt/leukemia.rda) used in the paper.

Biologists genetically mutated/changed the genotypes of barley. 
They could not change everywhere, so they changed 378 positions on the chromosome of barley. 
In the map, "A" and "B" are two types (sort of open and close). 
Because they know where the mutations are, they called them "markers"
(so that if a barley with a certain genotype has a higher expression level, then you may infer and
say, oh that may be caused by the 145th marker, etc.). 
The map has 7 chromosomes of barley, 1H, 2H, ..., 7H. 
These numbers are locations of markers on the chromosomes, like coordinates. 
There are some missing values in the original map, a naive method was used to interpolate the missing
values and produced this dataset [marker](http://dclong.github.io/media/spt/marker.rda). 

