# Week 18 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_9.401_A_regression_example_Reading_1h

# 9.401 A regression example
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/uca3d/9-401-a-regression-example

This reading section, identified as 9.401 A regression example, introduces the fundamental concept of regression within machine learning. Regression is defined as a specific type of machine learning problem. Its primary objective is to predict continuous values rather than discrete categories. The focus of this unit is how to estimate numerical outcomes from a given set of input data. A primary example used throughout the material is house price prediction. Through this example, students will explore the practical application of neural networks. Specifically, the material demonstrates how these networks can estimate numerical outcomes. This reading builds directly upon prior knowledge acquired from earlier classification examples. It serves as essential preparation for a practical lab scheduled for the end of the week. Students are specifically instructed to read Chollet and Watson (2025), Section 4.3. For complete details on accessing the primary text, students must refer back to the resource titled '1.003 How to access Chollet, F. and M. Watson (2025) Deep Learning with Python, Third Edition, Manning Publications ebook'. A critical technical detail must be noted regarding data set differences between the textbook and the course material. This particular version of the textbook employs the Californian housing price dataset. In contrast, the course lab and accompanying videos utilize the Boston house price dataset. However, both the Californian and the Boston datasets function as valid examples of regression. Furthermore, both datasets are designed to follow the same predictive methodology and steps. For those seeking to study the Boston house price dataset specifically in the textbook, an alternative resource is provided. Optionally, students may access Chollet, F. Deep learning with Python. (Shelter Island, NY: Manning, 2017) 2nd edition. This specific content is located in Section 3.6 of the older edition. The text also provides instructions for locating the material through institutional libraries. This required reading is accessible via the Online Library. Additionally, the material is available through the ProQuest Collection. Students are advised to find specific search instructions to locate the book within these platforms.

---

## 02_9.402_The_Boston_house_price_dataset_Video_2_min

# 9.402 The Boston house price dataset
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/LcTSz/9-402-the-boston-house-price-dataset

This course systematically introduces the fundamentals of machine learning, beginning with foundational concepts in Week 1 and progressing through practical labs in Week 2. The curriculum then dives into core supervised learning methodologies, dedicating Week 3 and Week 4 to the technical intricacies of Classification. Following this, Week 5 and Week 6 explore Regression, establishing techniques for predicting continuous values. Model evaluation and improvement techniques are thoroughly covered in Week 7, leading into Probabilistic Classification in Week 8.

A major shift occurs with the introduction of Unsupervised Learning in Week 9 and Week 10, focusing on discovering hidden patterns without labeled data. The focus then moves to advanced deep learning with Neural Networks in Week 11, followed by an intensive focus on the mathematical building blocks of these networks across Weeks 12, 13, and 14. Weeks 15, 16, 17, and 18 provide practical hands-on experience, guiding students through "Getting started with neural networks."

Throughout the material, validation methods, such as K-fold validation, are key concepts reinforced in Week 6 and Week 7. Specific practical applications are detailed in Section 9.4, which uses a regression example centered on the Boston house price dataset. This section includes preparatory steps (9.403) and dedicated training processes (9.409, 9.410 BOSTON Lab).

Further reinforcing the material, Section 9.5 provides a summary of Topic 9, followed by the fundamental concepts of machine learning in Week 19 and Week 20. The learning structure includes multiple practice assignments, post-video quizzes, and laboratory exercises to ensure comprehensive mastery of the technical details.

---

## 03_9.403_Preparing_the_data_Video_2_min

# 9.403 Preparing the data
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/OEmaS/9-403-preparing-the-data

The provided text covers machine learning fundamentals, emphasizing critical data preprocessing techniques, specifically normalization, alongside a detailed curriculum outline. A central focus is the process of normalizing training data by shifting and rescaling it to achieve a mean of 0 and a standard deviation of 1. Test data must then be normalized using the mean and standard deviation derived solely from the training set. Crucially, the workflow must never be polluted with any property that has been derived from the test set.

Normalization is performed by calculating the mean across the samples, typically axis by axis (column by column) in the sample feature table. This calculated mean is then subtracted from each sample, thereby ensuring the mean of the resulting shifted data is zero. Following the subtraction, division by the standard deviation scales the data to achieve a standard deviation of one.

The text defines these statistical concepts, noting that the mean is exactly the average (total divided by the number of items). The standard deviation is defined as the square root of the average square deviation from the mean. The use of "square deviation" is necessary because deviations can be both positive and negative, and the goal is to measure spread.

An example illustrates this process: data with a mean of 30 and a standard deviation of 14 is normalized into data distributed around zero with a range of 2.8. While the initial mean was 30, the normalized data, conversely, has a standard deviation of 20 when viewed in this context.

Matrix operations are also covered, specifically summing along different axes of a matrix $X$. For a three-by-two matrix, summing along the column axis yields sums of 9 and 12, while summing along axis 1 yields row sums of 3, 7, and 11.

The academic structure outlines a comprehensive study spanning 20 weeks. This curriculum moves through classification (Weeks 3-4), regression (Weeks 5-6), and model evaluation (Week 7). Subsequent weeks delve into probabilistic classification (Week 8), unsupervised learning (Weeks 9-10), and the mathematical building blocks of neural networks (Weeks 11-14).

Specific practical application examples include the use of the Boston house price dataset for regression examples (Section 9.4). Activities involve preparing data (9.403), building the network (9.405), and validating models using k-fold techniques (9.406). Further concepts include training the final model and logging validation via epochs (9.408). The coursework integrates laboratory sessions (e.g., BOSTON Lab) and regular quizzes/practice assignments to reinforce the concepts.

---

## 04_9.405_Building_your_network_Video_1_min

# 9.405 Building your network
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/Hvlr8/9-405-building-your-network

The curriculum begins with foundational studies, establishing Machine Learning fundamentals in Week 1, followed by practical application labs in Week 2. The theoretical focus then shifts to supervised learning, dedicating Weeks 3 and 4 entirely to the principles of Classification. Following this, Weeks 5 and 6 cover the concepts of Regression, continuing the focus on supervised learning methods. Week 7 addresses critical skill development through Model evaluation and improvement techniques. The material progresses to more complex areas, introducing Probabilistic classification in Week 8. Weeks 9 and 10 pivot to Unsupervised learning, detailing how algorithms identify hidden patterns without labeled data.

A major shift occurs in Week 11, where the curriculum introduces Neural networks and deep learning as core subjects. Weeks 12, 13, and 14 delve into the essential mathematical building blocks of neural networks, providing deep theoretical understanding. Practical application begins in Week 15, focusing on "Getting started with neural networks," a theme maintained through Week 18. Section 9.4 provides a detailed regression example utilizing the Boston house price dataset. This practical sequence covers data preparation (9.403), network construction (9.405), and rigorous validation using k-fold techniques (9.406). Further training involves managing epochs, logging validation, and smoothing plots (9.408) before the final model training. Weeks 19 and 20 serve as a comprehensive review, reinforcing the fundamentals of machine learning (Topic 10). The overall structure culminates in a summary (9.5) and quizzes to assess mastery of the broad range of techniques covered.

---

## 05_9.406_Validating_k-fold_Video_2_min

# 9.406 Validating – k-fold
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/ccdQR/9-406-validating-k-fold

The core challenge addressed is that the initial training set is small. If this set is divided into a training and validation split, the resulting validation set becomes exceptionally tiny. Validation scores derived from such a small subset are highly sensitive to the specific constitution of that set.

K-fold cross-validation serves as the common solution to mitigate this sensitivity. In this technique, the entire dataset is systematically split into K distinct partitions. Typically, K is set to four or five partitions for the dataset. Consequently, K identical models are instantiated for training.

The methodology dictates that for any given fold, the network is trained on all data except that fold's partition. For example, in fold one, the model is trained on partitions two, three, four, up to K. Subsequently, the model is validated specifically on partition one.

A fresh network must be instantiated for each fold to ensure impartiality. For fold two, the training set includes partitions one, three, four, up to K, while the validation occurs on partition two. This robust process significantly reduces the dependence of the validation score on any single small set.

The specific implementation involves a K-fold training code where K is defined as four. Both training and validation processes are managed within a continuous loop. At each pass, a new network is instantiated, and a partial training set is sliced from the full training data.

The primary metric monitored is the validation mean absolute error (MAE). It is crucial to note that the MAE is recorded only at the termination of the training run, not after each individual epoch. Therefore, no history object is maintained for epoch-level tracking.

The training run observed utilized 100 epochs. The resulting MAE scores across the folds varied between 2.07 and 2.5. The derived average MAE was deemed significant because the target price range for the house prices spans from $10,000 to $50,000.

Contextually, this work relates to a broader curriculum covering machine learning fundamentals. Topics range from classification (Week 3 and 4) to regression (Week 5 and 6). The curriculum progresses to model evaluation and improvement in Week 7.

Advanced concepts include probabilistic classification in Week 8 and unsupervised learning in Weeks 9 and 10. Neural networks and deep learning are covered extensively across Weeks 11 through 16. Weeks 12, 13, and 14 focus on the mathematical building blocks of neural networks.

Practical applications are demonstrated using the Boston house price dataset. Specific resources include video 9.402 covering the dataset and preparing the data. The specific video section detailing the K-fold validation is 9.406 Validating – k-fold.

Students can further explore the regression example using resource 9.401 House prices. The application is rooted in the Boston house price dataset, as detailed in section 9.404. The practical implementation culminates in the BOSTON Lab, section 9.410.

The overall course structure provides continuous learning, culminating in topics such as Fundamentals of machine learning in Weeks 19 and 20.

---

## 06_9.408_More_epochs,_validation_log,_plotting,_smoothing_Video_1_min

# 9.408 More epochs, validation log, plotting, smoothing
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/wQogM/9-408-more-epochs-validation-log-plotting-smoothing

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 07_9.409_Training_the_final_model_and_wrap_up_Video_1_min

# 9.409 Training the final model and wrap up
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/ROZIa/9-409-training-the-final-model-and-wrap-up

This document outlines the fundamental concepts and technical methodologies required for machine learning, spanning from foundational theory to advanced neural network applications. The curriculum is structured across 20 weeks, covering topics such as ML fundamentals (Week 1), Classification (Weeks 3-4), and Regression (Weeks 5-6). Later weeks delve into advanced concepts including Probabilistic classification (Week 8), Unsupervised learning (Weeks 9-10), and the critical study of Neural networks and deep learning (Weeks 11-18).

A primary focus area detailed is regression, demonstrated using the Boston house price dataset (Section 9.4). The general machine learning workflow requires building, fitting, and subsequently evaluating the model. For practical training, an optimal number of epochs was identified as approximately 116.

During training, it is crucial to remember on all training data, rather than utilizing partial training sets. The evaluation process must be rigorously handled, particularly when dealing with small datasets. If a dataset is small, the recommended approach is to use a minimal network, typically one or two hidden layers.

Technical data preparation requires normalizing the features if they exhibit varying ranges. Model validation is achieved through K-fold validation, ensuring robustness across the entire dataset.

Regarding performance metrics, the Mean Squared Error (MSE) is established as the standard regression loss function. This MSE was observed in the prediction error on unseen data, amounting to $2,771$. Crucially, the text emphasizes that there is no formal concept of "regression accuracy."

However, Mean Absolute Error (MAE) is commonly employed for monitoring the model's performance during the training phase. The process involves starting with the data preparation (e.g., Section 9.403), building the network (9.405), and then conducting validation (9.406).

Specific links and lab assignments are provided, such as the BOSTON Lab and various practice assignments (9.404, 9.407), which accompany detailed video modules. The content addresses both the abstract theory and practical application, such as training the final model and wrap up (9.409).

Technical navigation within the video content is supported by specific keyboard shortcuts for efficiency. For instance, one can save notes using CTRL + S, or expand and contract selections utilizing CTRL + arrow keys.

These technical guidelines ensure that all aspects of model training, from data normalization to the determination of optimal epochs, are covered comprehensively. The structure facilitates a thorough learning experience across various machine learning domains.

---

## 08_9.501_Topic_9_summary_Video_1_min

# 9.501 Topic 9 summary
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/d4FET/9-501-topic-9-summary

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

