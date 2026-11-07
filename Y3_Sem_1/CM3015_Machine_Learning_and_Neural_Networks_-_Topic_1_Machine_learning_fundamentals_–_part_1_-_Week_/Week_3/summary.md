# Week 3 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_2.101_Introduction_to_supervised_Learning_Video_54_sec

# 2.101 Introduction to supervised Learning
Video • 54 sec - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/CozUG/2-101-introduction-to-supervised-learning

The curriculum focuses on Machine Learning fundamentals, specifically beginning with classification methods. Classification is defined as a type of supervised learning. In this paradigm, the labels provided on the training data are inherently discrete or categorical. The introductory materials outline the goal of learning mappings from a set of training data to a corresponding set of labels.

The immediate study plan centers on several simple yet powerful classification algorithms. A key algorithm introduced is the k-nearest neighbor, or k-NN. This method is detailed in the video resource 2.201 K-Nearest Neighbours Classification Video, which has a duration of three minutes. Associated practice is available through the 2.202 KNN Practice Assignment, which requires ten minutes.

Another foundational class of algorithms discussed is the decision tree. The explanation for this powerful tool is provided in 2.301 Decision tree Video, with a duration of seven minutes. Practice for the decision tree concept is available via the 2.302 Decision trees Practice Assignment, lasting ten minutes.

Furthermore, a dedicated resource for exploring real-world examples is 2.401 Real-world datasets for classification Discussion Prompt. This resource is substantial, requiring two hours of engagement.

The structure of the overall course progresses through several major topics over 20 weeks. Week 1 and Week 2 cover the initial Machine Learning fundamentals. Week 3 specifically focuses on Classification topics. Week 4 continues the study of Classification.

Following the classification modules, Weeks 5 and 6 are dedicated to Regression. Week 7 addresses the critical and important topic of Model evaluation and improvement. Subsequently, Week 8 delves into Probabilistic classification.

The curriculum shifts focus to unsupervised learning during Weeks 9 and 10. A substantial portion of the later study is dedicated to advanced topics involving Neural networks and deep learning. This topic occupies Weeks 11 through 18. Finally, Weeks 19 and 20 conclude by covering the Fundamentals of machine learning in depth.

The learning sequence is highly structured, utilizing specific instructional videos. The initial introduction to supervised learning is covered in 2.101 Introduction to supervised Learning, a 54-second video. Technical skills and concepts from these modules build toward advanced model implementation. The overall structure provides a complete progression from basic supervised classification to complex neural network architectures.

---

## 02_2.201_K-Nearest_Neighbours_Classification_Video_3_min

# 2.201 K-Nearest Neighbours Classification
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/tZG9P/2-201-k-nearest-neighbours-classification

This curriculum outlines a comprehensive progression through Machine Learning fundamentals, beginning with an introduction to supervised learning (2.101). Initial core concepts include K-Nearest Neighbour (2.201), which features a practice assignment (2.202), and the Decision Tree algorithm (2.301), also complemented by a practice assignment (2.302). Classification is further explored through real-world datasets (2.401) before transitioning into the principles of regression (Topic 3) in Weeks 5 and 6. The curriculum then dedicates a week to crucial model evaluation and improvement techniques before moving into probabilistic classification (Topic 5) in Week 8. Unsupervised learning (Topic 6) is introduced in Weeks 9 and 10, covering techniques that do not require labeled data. The focus shifts significantly toward deep learning starting in Week 11 (Topic 7). Weeks 12 through 14 are mathematically intense, detailing the foundational building blocks of neural networks (Topic 8). Practical application and implementation of neural networks are covered intensively in Weeks 15 through 18. The final modules revisit the overall fundamentals of machine learning (Topic 10), concluding the extensive 20-week course. Key technical details, including module identifiers like 2.201 and the specific 54-second introduction video, are preserved throughout the structure.

---

## 03_2.301_Decision_tree_Video_7_min

# 2.301 Decision tree
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/AoY5x/2-301-decision-tree

Decision trees constitute a versatile class of machine learning algorithms capable of handling both classification and regression tasks. These models are highly effective for managing complex, non-linear datasets. Specifically, decision trees frequently serve as the foundational classifier within Random Forests, a powerful algorithm class. The structure of a decision tree begins at a root node, which poses a binary question based on the most information-rich feature. In the provided example distinguishing rabbits from hares, the root node uses the burrowing feature, as hares almost never burrow while all rabbits do. If the animal does not burrow, it is classified as a hare. If the animal can be found in a burrow, the process continues to a secondary split using a less distinguishing feature, such as ear length. The final class designations, reached through the traversal, are termed leaf nodes. When new data is presented, it is classified by descending the tree until an appropriate leaf node is reached. A crucial characteristic is that decision trees are "White Box" models, making them highly interpretable. This transparency derives from their foundation in a hierarchy of simple, easily visualized classification rules. This contrasts sharply with "black box" models, such as deep neural networks, where decision-making processes are opaque. Mapping the tree onto the feature space creates a decision boundary, which can be complex and non-linear. The CART algorithm, or Classification and Regression Decision Tree, is a common type; it is a binary tree where each non-leaf node spawns two children. The goal of training a CART is to fit a decision boundary that optimally separates distinct data groups. The algorithm starts at the root node by searching for a single feature and a threshold value that best splits the entire dataset. This optimal split selection is achieved by minimizing the impurity within each resulting decision region. Impurity is a measure of class mixture; aiming for zero impurity means a perfect separation can define a leaf node. If a region remains impure, the tree recursively grows to a second-level split on that subset of the data. This process continues until the dataset is perfectly partitioned into leaf nodes. A significant advantage is the tree's capacity to capture complex data relationships via intricate decision boundaries. However, a major danger is that decision trees are prone to overfitting, meaning they fit training data too perfectly and fail to generalize. This follows the principle of Occam's Razor, favoring simpler, more robust solutions. Practical solutions include regularization, which restricts the tree depth even if misclassifications occur. Alternatively, the preferred approach is to fully grow the tree and then perform pruning to find an optimal compromise. Determining the optimal split and feature combination is an NP-complete problem, rendering it computationally intractable for even small datasets. The CART algorithm mitigates this challenge by employing greedy training, evaluating only the optimal split sequentially at each node. Despite this lack of global optimization, greedy training often yields a robust overall solution. Furthermore, a key strength is that decision trees operate effectively on raw feature data. They do not require the time-consuming pre-processing steps, such as scaling or centering, necessary for algorithms like K-nearest neighbor. These algorithms remain incredibly powerful and flexible, extending from classification to regression tasks.

---

