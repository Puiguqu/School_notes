# Week 7 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_4.101_Overfitting_and_underfitting_Video_4_min

# 4.101 Overfitting and underfitting
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/eHS12/4-101-overfitting-and-underfitting

The analysis of model fitting begins by examining the limitations of overly simple models, such as those derived from linear regression. If a model fails to adequately represent the data, it is described as underfitting. This state occurs because the model is overly simple and inflexible, leading to a technical term known as high bias.

Conversely, increasing model complexity, such as fitting data with a fourth-degree polynomial, can lead to overfitting. In an overfit scenario, the line fits the training data perfectly, but its excessive complexity results in high variance. The core goal in machine learning is to develop a model that is highly generalizable, meaning it fits the training data well while performing reliably on new, unseen data.

A guiding philosophical premise for model creation is Ockham’s Razor, which advises using the simplest possible solution that is sufficient to solve the problem. To quantitatively evaluate generalizability, the bias-variance curve is utilized. This curve plots error against a measure of model complexity, such as the degree of a polynomial.

When training on a dataset, the initial error typically decreases as the model complexity increases. However, the error measured on an independent test set follows a different trajectory. At low complexity, the model underfits (high bias); at high complexity, it overfits (high variance). The ideal model exists at a "sweet spot" where the test error is minimized.

To ensure a model is generalizable and avoids this dichotomy, two primary approaches are employed. The first approach is reducing the number of features, often through manual, heuristic feature selection. While effective, this process can be tedious, particularly with complex data.

Alternatively, automation can be used for model or feature selection, often utilizing cross-validation techniques. The second critical strategy is regularization. This method retains all initial features but systematically reduces the magnitude of the parameter values. Regularization effectively diminishes the influence of specific features, making the model less susceptible to noise and improving generalizability.

The provided curriculum structure organizes these concepts across several weeks. Specific modules cover Model evaluation and improvement in Week 7, detailing topics such as Bias-variance (4.101, 4.102), Regularization (4.201, 4.202), and Cross-validation (4.301, 4.302). Future curriculum sections delve into Probabilistic classification (Week 8), Unsupervised learning (Weeks 9/10), and comprehensive deep learning methodologies starting in Week 11.

---

## 02_4.201_Regularisation_Video_4_min

# 4.201 Regularisation
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/D1hvy/4-201-regularisation

The curriculum begins with the foundational concepts of Machine Learning (Weeks 1 and 2), transitioning into specific supervised learning techniques. Weeks 3 and 4 are dedicated to Classification, followed by Weeks 5 and 6, which cover the principles of Regression. Week 7 focuses intensely on Model evaluation and improvement, introducing critical concepts like Bias-variance (overfitting and underfitting, as detailed in sections 4.101 and 4.102). This week also covers Regularisation (4.201 and 4.202) and Cross-validation (4.301 and 4.303), alongside an exploration of The Curse of Dimensionality (4.302). Further practical learning is offered in Week 7 via the Model improvement Lab (4.401) and reading (4.402). The progression continues into probabilistic classification in Week 8, leading to Unsupervised learning in Weeks 9 and 10. Weeks 11 through 14 are dedicated to Neural networks and Deep learning, building the core understanding through the mathematical building blocks (Topic 8). This deep dive into mathematics continues through Week 13 and Week 14. Weeks 15 to 18 focus on the practical application and implementation of Neural networks (Topic 9). The program then revisits the core curriculum, dedicated to Fundamentals of machine learning in Weeks 19 and 20 (Topic 10), concluding with a specific module on Regularisation (4.201) in Week 20.

---

## 03_4.301_Cross-validation_Video_5_min

# 4.301 Cross-validation
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/QyHda/4-301-cross-validation

The primary goal in machine learning is to avoid overfitting, which occurs when the training data is used identically for testing, leading to models that perform poorly on unseen, real-world data. A fundamental technique to mitigate this is the train-test split, where a small portion of the data (e.g., 10%) is set aside exclusively for testing. The remaining data is then used to train the algorithm, and the held-out test data acts as a proxy for real-world, previously unseen data. Due to limited dataset size, this basic approach can be inefficient, leading to the need for a more comprehensive method: N-fold cross-validation.

N-fold cross-validation maximizes data utilization by splitting the entire dataset into $N$ equal sections, or folds. In this procedure, the algorithm trains on $N-1$ folds while testing on the remaining single fold. This process is repeated $N$ times, cycling through each fold as the reserved test set. The final performance metric (accuracy or error) for the algorithm is then determined by calculating the average across all $N$ iteration results. This technique allows every data point to participate both in training and testing, preventing the reliance on a single, potentially biased split.

However, machine learning algorithms often possess multiple hyperparameters (e.g., $k$ in K-nearest neighbors or distance measures like Euclidean or Manhattan) that need optimization. Evaluating these parameters using only the training set results in overfitting, as the hyperparameter selection process is tied to the data being trained on. Similarly, using the final dedicated test set for parameter tuning is improper because it pollutes the test set with information, compromising its integrity.

The definitive solution for simultaneously tuning hyperparameters and evaluating performance without compromising data integrity is N-fold nested cross-validation. This robust method involves an outer loop (the main fold) and an inner loop (the hyperparameter evaluation). First, the entire dataset is split into a final train set and a test set. Within the train set, the nested structure begins.

In the inner loop, the training data is further subdivided into a smaller training subset and a validation set. It is within this validation set that various possible hyperparameters are evaluated. For example, all potential $k$ values and distance measures are trained and tested against the small validation set to find the optimal configuration. Once the best hyperparameters are identified through the inner loop, they are applied to the larger training set of the outer loop. Finally, this optimally tuned algorithm is evaluated on the original, untouchable test set of that fold. This entire process is repeated for all folds, providing an average error that reflects the model's true generalization capability.

---

## 04_4.302_The_Curse_of_Dimensionality_Video_4_min

# 4.302 The Curse of Dimensionality
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/GdYPl/4-302-the-curse-of-dimensionality

The curriculum begins with Machine Learning fundamentals in Week 1 and a dedicated labs session in Week 2, swiftly progressing to focused studies on Classification in Weeks 3 and 4. Weeks 5 and 6 address Regression, expanding the foundational concepts of predictive modeling. The critical area of Model evaluation and improvement is covered in Week 7, introducing crucial concepts like Bias-variance (overfitting/underfitting) via resources 4.101 and 4.102.

Further technical refinement occurs in Week 7 with Regularisation (4.201, 4.202) and Cross-validation (4.301, 4.303), addressing complex issues such as the Curse of Dimensionality (4.302). Topic 4 culminates with the extensive Model improvement Lab (4.401) and supplemental reading (4.402). The scope widens in Week 8 with Probabilistic classification, followed by an entire two-week exploration of Unsupervised learning in Weeks 9 and 10.

A major shift toward advanced modeling begins in Week 11 with the introduction of Neural networks and Deep learning. Weeks 12 through 14 are mathematically intensive, focusing entirely on The mathematical building blocks of neural networks. This theoretical understanding transitions into practical application starting in Week 15, continuing through Weeks 16, 17, and 18, which cover Getting started with neural networks.

The course structure concludes with dedicated reviews of foundational concepts, covering Fundamentals of machine learning in Weeks 19 and 20. This progression systematically moves from basic supervised learning (Classification/Regression) to robust evaluation techniques, and finally into the complex domain of Deep Learning and Unsupervised learning.

---

## 05_4.402_Further_material_Reading_1h

# 4.402 Further material
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/CkkuF/4-402-further-material

This topic’s core content is largely self-contained regarding machine learning concepts.
However, supplementary material is available for students seeking deeper knowledge on specific topics.
Detailed information on overfitting, cross-validation, and managing test sets can be found in the course textbook, Chollet, specifically within Chapter 4, section 4.2.
For additional technical resources, students are directed to online tutorials provided by Scikit-learn.
One specific Scikit-learn tutorial covers model selection and cross-validation, accessible at: `https://scikit-learn.org/stable/auto_examples/model_selection/`.
A further example demonstrating the concept of nested cross-validation is also provided via Scikit-learn: `https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html`.
Students can also consult Section 2.7 of Ethem Alpaydin’s seminal work for an introduction to model selection and generalization.
The full reference for this book is: Alpaydin, E. Introduction to machine learning. (Cambridge, MA: MIT Press, 2014) 3rd edition [ISBN 9780262028189].
It is critical to note that although the URLs provided have been verified at publication, they are not guaranteed to be maintained over time.
Students are encouraged to report access issues with the links via the Student Portal if they become inoperable.
The University of London expressly disclaims responsibility for any content or operational issues maintained by external providers.
While further reading will significantly deepen understanding, it is explicitly stated that these materials are not mandatory for successfully passing the module.
Students may elect to consult these suggested readings or other resources they find beneficial.
Nevertheless, the university cannot guarantee the continuous accessibility of the suggested further reading materials.
Users should also be aware that the provision of these external readings is done without any undertaking or guarantee from the university.

---

