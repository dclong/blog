Status: published
Date: 2020-10-30 10:41:11
Author: Benjamin Du
Slug: comparing-similarity-of-two-different-clusterings
Title: Comparing Similarity of Two Different Clusterings
Category: Computer Science
Tags: Computer Science, clustering, similarity, cluster, metric, sklearn, paper
The paper
[Comparing Clusterings - An Overview](http://staff.ustc.edu.cn/~zwp/teach/MVA/cluster_validation.pdf)
has a good view of different metrics for comparing the similarity of 2 clusterings.
Overall, Normalized Mutual Information sounds like a good one.
It is implemented in sklearn as 
[sklearn.metrics.normalized_mutual_info_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score)
.
Of course, 
there are many more metrics for measuring similarity of 2 clusters 
(e.g., [Adjusted Rand Index](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html))
implemented in sklearn. 
For more details,
please refer to 
[Clustering Metrics](https://scikit-learn.org/stable/modules/classes.html#clustering-metrics).

## References 

- [Comparing Clusterings - An Overview](http://staff.ustc.edu.cn/~zwp/teach/MVA/cluster_validation.pdf)

- https://hal.inria.fr/hal-01514872/document