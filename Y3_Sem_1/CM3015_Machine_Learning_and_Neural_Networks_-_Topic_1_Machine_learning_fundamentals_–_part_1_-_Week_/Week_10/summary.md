# Week 10 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_6.301_Dimensionality_reduction_Video_3_min

# 6.301 Dimensionality reduction
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/7IOuL/6-301-dimensionality-reduction

This course structure guides the student through a comprehensive study of machine learning, beginning with foundational concepts in Weeks 1 and 2. The initial phase of supervised learning is established through dedicated study of Classification in Weeks 3 and 4. Following classification, the curriculum addresses Regression models in Weeks 5 and 6. Week 7 is specifically allocated to crucial Model evaluation and improvement techniques. The course then progresses to Probabilistic classification in Week 8, broadening the scope of predictive modeling. Weeks 9 and 10 are dedicated to Unsupervised learning, focusing heavily on Dimensionality reduction. Specific technical components, such as the PCA (Principal Component Analysis) video (6.302) and associated practice assignments (6.303), are explored during this phase. A Mid-term coursework submission serves as a critical checkpoint after the foundational and unsupervised topics. The learning dramatically shifts to deep learning, starting with neural networks and their introduction in Week 11. Weeks 12 through 14 intensively explore the mathematical building blocks required for understanding these neural networks. Practical application and implementation of neural networks are covered over several subsequent weeks, from Week 15 to Week 18. The final segment provides a comprehensive review of core Machine Learning Fundamentals in Weeks 19 and 20. This entire structure is reinforced by dedicated labs, such as the PCA dimensionality reduction Lab (6.401), and further required reading.

---

## 02_6.302_PCA_Video_10_min

# 6.302 PCA
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/BEee6/6-302-pca

Principal Component Analysis (PCA) fundamentally relies on understanding variance within the dataset. When dealing with $N$ samples and $F$ features, the data is represented as a matrix $X$. Calculating the sample mean involves summing over all samples and dividing by the total number of samples. To assess feature relationships in this multidimensional space, we utilize the covariance algorithm. Covariance measures how the data samples move together and how variables change relative to the mean. The core premise of PCA is to linearly transform data from one dimension to another. This transformation is achieved by multiplying the original data $X$ by a PCA transformation matrix, $W$, resulting in output data $Y$ in the new space.

For instance, a 3D to 2D mapping uses a $3 \times 2$ matrix $W$ applied to a $3 \times 1$ feature vector. The critical challenge is determining the values of $W$. The primary objective function is to maximize the covariance of the output data $Y$. Mathematically, this covariance is represented as $W^T \text{Cov}(X) W$. By setting $S = \text{Cov}(X)$, the optimization goal is to find $W$ that maximizes $W^T S W$.

To prevent $W$ from tending toward infinity, a crucial constraint is added: $W^T W = I$, where $I$ is the identity matrix. This constraint ensures that the projected features remain linearly independent and orthogonal. The optimal matrix $W$ is found using Eigenanalysis. This process involves taking the covariance matrix $S$ and performing Eigenanalysis on it. This yields two outputs: a vector of Eigenvalues and a matrix of corresponding Eigenvectors.

These outputs are linked such that multiplying the Eigenvectors $W$ by the covariance matrix $S$ equals multiplying the Eigenvectors by the corresponding scalar Eigenvalues. The PCA procedure begins by centering all data by subtracting the mean from the feature vectors $X$. Next, the covariance matrix $S$ is calculated over the centered data. Eigenvalues and Eigenvectors are then computed using Eigenanalysis.

The fourth step involves reordering the resulting Eigenvalues from largest to smallest. The largest eigenvalues correspond to the Eigenvectors that capture the most variance, which are the principal components. For dimensionality reduction to $k$ dimensions, we select the top $k$ eigenvectors, forming the matrix $W_k$. The final projection is achieved by calculating the output data $Y$ as $Y = W_k^T X$.

A powerful feature of PCA is that the transformation can be reversible if all principal components are retained. We can take $W_k$ and multiply it by the projected data $Y_k$ to map it back into the original dimensional space. This reversal allows for faithful data reconstruction. However, when dropping eigenvectors (i.e., reducing dimensions), the compression is inherently lossy. In a demonstration, three features ($f_1, f_2 = -f_1, f_3 = 2f_1$) were shown to be linearly dependent. These three features could be completely represented by a single dimension, demonstrating that the minimum number of dimensions required is often far less than the features provided.

---

## 03_6.402_Further_reading_Reading_1h

# 6.402 Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/r8eON/6-402-further-reading

This content topic is largely self-contained regarding its core material. Further reading resources are provided to deepen the reader's understanding in specific areas of machine learning. Ethem Alpaydin’s textbook, *Introduction to machine learning*, is a primary reference for advanced topics. Specifically, Sections 6.1 and 6.3 from Chapter 6 of Alpaydin’s book discuss the crucial concepts of dimensionality reduction. These sections also detail the techniques involved in Principal Component Analysis (PCA). Additionally, Chapters 7, Sections 7.1 to 7.3, cover the subject of clustering methods. These chapters include the methodology for k-means clustering. The complete reference for Alpaydin’s work is *Introduction to machine learning* (Cambridge, MA: MIT Press, 2014), 3rd edition, bearing the ISBN 9780262028189.

Another valuable reference is Kevin Murphy’s book, *Machine learning: a probabilistic perspective*. This text introduces the topic of unsupervised learning in its opening sections. Specifically, the introduction, Sections 1.3 to 1.4, presents various applications related to clustering and dimensionality reduction. A notable distinction must be made regarding Murphy's content. Murphy's book carries a more probabilistic interpretation than is covered in the current course material. Therefore, while highly useful for alternative perspectives, this reading is not technically essential for passing the module.

Several administrative caveats pertain to the external links provided on the page. Any URLs presented were checked at the time of publication. However, the module providers cannot guarantee that these external links will remain maintained indefinitely. Students who encounter problems accessing these specific links are required to notify the university via the Student Portal. Furthermore, the University of London explicitly states it cannot assume responsibility for any pages maintained by external providers. The intention of the further reading is to deepen the student's understanding across various areas. Despite the recommendation, consulting this suggested reading or seeking other resources is voluntary. It must be noted that the module does not undertake any guarantee regarding the continued accessibility of the listed resources. The reader may wish to consult these references or others they find independently. However, students must acknowledge that the university cannot guarantee the accessibility of any supplemental reading material. The foundational concepts within the current topic are presented as largely self-contained. This module's structure is designed to allow mastery without mandatory reliance on the provided external readings.

---

