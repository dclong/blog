Status: published
Date: 2020-04-07 16:29:17
Author: Benjamin Du
Slug: rule-base-image-process
Title: Rule-Base Image Process
Category: Computer Science
Tags: Computer Science, image processing, computer vision, CV, machine learning, data science
Modified: 2020-04-07 16:29:17

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


If you face a relative simple image recognition problem 
which hasn't been studied by other people before 
so that no public data is available for it, 
it is probably less effort to develop a rule-based algorithm
rather than a complicated (CNN-based) model 
(which might require lots of time to collect and label data)
to attack the problem.
Here are some basic tips for developing rule-based algorithms for image processing.

1. Always go for other simpler solutions if image processing is not absolutely necessary.

2. If shape is all that matters in your problem and color doesn't matter,
    it is suggested that you convert images to black/white or grayscale 
    and develop your algorithm based on black/white or grayscale images.

3. Direct image pixle comparision is a good idea 
    if the (relative) position of the object on the image is fixed/standard,
    otherwise, 
    you might want to avoid direct pixle comparison.

4. If both shape and color matters,
    it is usually easier to develop a rule-based algorithm using color information. 
