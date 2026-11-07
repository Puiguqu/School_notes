# Week 9 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_6.101_Introduction_to_unsupervised_Learning_Video_2_min

# 6.101 Introduction to unsupervised Learning
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/z95eG/6-101-introduction-to-unsupervised-learning

Supervised learning is introduced as the most straightforward and dominant set of approaches for applying machine learning algorithms. This methodology fundamentally requires the existence of labels to dictate the production or output of an algorithm. These essential labels are typically provided by human experts, such as radiologists annotating X-rays for specific disease types. This reliance on expert judgment, however, presents significant challenges. Firstly, the process of human annotation is inherently costly. Secondly, it is prone to errors because it depends entirely on individual human judgment. The problem is exacerbated when multiple experts assess the same sample, leading to expected deviations among their ratings.

This inherent limitation in labeling introduces the necessity of unsupervised learning. Unsupervised learning allows for thorough data analysis and interpretation without relying on predefined labels. The discourse focuses on two fundamental categories within unsupervised machine learning: clustering and dimensionality reduction. Clustering is defined as an unsupervised method utilized to arrange data into interpretable subgroups. Its primary utility is serving as a powerful tool for data analysis and interpretation itself. Furthermore, clustering can be used to enhance supervised machine learning efficiency. By identifying inherent data groupings, subsequent supervised learning can be performed independently on each cluster, provided labeling information is available.

The second core category discussed is dimensionality reduction. This technique addresses large datasets composed of high-dimensional samples, such as high-resolution images. The chief goal of dimensionality reduction is to reduce the number of dimensions into a lower-dimensional embedding. Crucially, this reduction must occur without losing any useful information from the original dataset. The process aims to preserve the useful information pertinent to the task while actively discarding noise and redundancy.

Principal Component Analysis (PCA) is cited as a specific technique for achieving dimensionality reduction. This method effectively reduces statistical redundancy within the data and mitigates the negative effects associated with the cost of dimensionality. The curriculum structure provides context for these topics. The learning modules include Week 1 Topic 1: Machine learning fundamentals – part 1. Specific learning materials include the "Introduction to unsupervised Learning Video" (6.101), "Clustering Video" (6.102), and the "K-Means Video" (6.103). Practical application is reinforced through the "K-means Clustering Practice Assignment" (6.104). Further laboratory work is covered in "6.2 Topic 6 Lab (part 1)," specifically "K-Means clustering Lab" (6.201). The overall progression covers various topics, including Classification (Week 3 and 4), Regression (Week 5 and 6), and advanced methods like Neural networks and deep learning (Week 11 through Week 18).

---

## 02_6.102_Clustering_Video_2_min

# 6.102 Clustering
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/uSQf3/6-102-clustering

This curriculum outlines a progressive study of machine learning, starting with fundamentals in Weeks 1 and 2. The focus then shifts to supervised learning, covering Classification in Weeks 3 and 4, followed by Regression in Weeks 5 and 6. Week 7 is dedicated to critical Model evaluation and improvement techniques, leading into Probabilistic classification in Week 8.

Weeks 9 and 10 introduce Unsupervised learning, beginning with an introduction (6.101), Clustering (6.102), and K-Means theory (6.103), which is reinforced by the K-means Clustering Practice Assignment (6.104). The core practical application of this concept is covered in the K-Means clustering Lab (6.201).

The advanced segment begins in Week 11 with Neural networks and deep learning. Weeks 12 through 14 deeply explore the mathematical building blocks of neural networks, establishing the theoretical foundation for the subsequent practical sessions. Weeks 15 through 18 are dedicated to getting started with Neural networks, emphasizing hands-on implementation and technical proficiency.

The course concludes with Weeks 19 and 20, providing a final review of Fundamentals of machine learning and reiterating foundational concepts, such as clustering (6.102). This structured progression ensures comprehensive coverage from foundational algorithms to complex deep learning models.

---

## 03_6.103_K-Means_Video_7_min

# 6.103 K-Means
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/UL0mI/6-103-k-means

K-means clustering is a highly effective unsupervised learning algorithm designed to automatically discover patterns and groupings within data, such as separating average and wealthy income groups. The process begins by deciding the number of clusters, denoted as $K$, which defines how many distinct groups the data should be divided into. In the first step, the algorithm selects $K$ random points from the data, which are designated as the initial centroids. Once the centroids are established, the algorithm calculates the distance from every data point to each of these centroids. Data points are then assigned to the cluster corresponding to the nearest centroid, forming initial cluster boundaries. This initial grouping is the starting point for the iterative refinement process. The next critical step is recalculating the centroids; one effective method is to determine the mean of all data points contained within each cluster, establishing new centroid locations. It is important to note that a new centroid does not necessarily need to fall on an actual data point, but can be the precise mean of the cluster data. Using these newly calculated centroids, the algorithm again computes the distance from all data points to each centroid. Points are reassigned to the cluster of their closest centroid, causing the cluster boundaries to shift slightly. This entire sequence—calculating the cluster mean, determining distances, and reassigning points—is then repeated iteratively. The process continues until convergence, which occurs when the centroids cease to move or the cluster shapes no longer change. A significant limitation of K-means is that its final outcome is subject to local minima, meaning the result is heavily dependent on the initial centroid placement. To mitigate this sensitivity, the practical solution is often to restart the algorithm multiple times using various different initial centroids. This methodology applies whether $K$ is two, three, or any higher value representing the desired number of clusters. When dealing with multi-dimensional data, such as adding age to income, the basic procedure remains the same. However, a critical issue arises when features are on wildly different scales, like income measured in hundreds of thousands and age measured in tens. Before running K-means on multi-dimensional data, it is essential to scale the data to ensure all features contribute equally to the distance calculation. This scaling prevents features with large numerical ranges, like income, from dominating the clustering results over smaller-scaled features, such as weight. A common technique is min-max scaling, which restricts all data points to fall within the range of zero and one. The specific formula for min-max scaling is: $X_{scaled} = (X - X_{min}) / (X_{max} - X_{min})$. Utilizing this rescaling ensures that features like weight have a meaningful effect on the final clustering assignment. Beyond K-means, machine learning fundamentals cover topics ranging from classification and regression to neural networks and deep learning. The entire learning process is structured across several modules, from introducing unsupervised learning to advanced model evaluation. Various resources, including practice assignments and specific video lectures (e.g., 6.103 K-Means Video), provide in-depth application of these concepts.

---

