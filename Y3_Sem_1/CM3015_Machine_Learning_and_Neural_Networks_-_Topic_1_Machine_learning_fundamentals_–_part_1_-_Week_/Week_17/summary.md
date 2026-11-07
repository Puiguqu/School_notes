# Week 17 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_9.301_A_multiclass_classification_example_Reading_1h

# 9.301 A multiclass classification example
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/B7pmn/9-301-a-multiclass-classification-example

This reading introduces the concept of multiclass classification. Defined as a task where models must choose between more than two possible categories, it represents an advanced application of classification techniques. The material explores how neural networks must be specifically adapted to handle the challenges of multiple class outputs. This discussion builds directly upon the foundational principles established in the earlier binary classification example. As a practical case study, the material focuses on applying these concepts using the Reuters newswire dataset. The primary goal of the reading is to prepare the student for a practical lab scheduled for later in the week. Required reading includes Chollet and Watson (2025), Section 4.2. For full access and necessary details, students must refer to '1.003 How to access Chollet , F. and M. Watson (2025) Deep Learning with Python, Third Edition, Manning Publications ebook'.

---

## 02_9.302_The_Reuters_dataset_Video_1_min

# 9.302 The Reuters dataset
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/Ahamg/9-302-the-reuters-dataset

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 03_9.303_Preparing_the_data_Video_40_sec

# 9.303 Preparing the data
Video • 40 sec - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/95XCz/9-303-preparing-the-data

This curriculum provides a comprehensive progression through machine learning fundamentals, spanning twenty weeks of intensive study. The initial weeks lay the groundwork, starting with Machine Learning fundamentals in Week 1 and continuing into Week 2 labs. The study then progresses into supervised learning, beginning with Classification in Week 3 and extending into further topics in Week 4. Following classification, the curriculum covers Regression in Week 5, which is continued through Week 6. Model evaluation and improvement techniques are dedicated to Week 7, ensuring proficiency in assessing model performance. Week 8 introduces the sophisticated concepts of Probabilistic classification methods. Subsequently, Weeks 9 and 10 are devoted entirely to Unsupervised learning, exploring methods that do not rely on labeled data.

A major conceptual shift occurs in Week 11 with the introduction of Neural networks and deep learning. The structural and mathematical complexity of these models is explored thoroughly during Weeks 12, 13, and 14, focusing on the mathematical building blocks. The practical application phase begins in Week 15, titled "Getting started with neural networks," which is elaborated upon across Weeks 16, 17, and 18. Specific application examples include multiclass classification, as seen in the example 9.301. Practical exercises utilize datasets such as the Reuters dataset, focusing on procedural tasks like data preparation (9.303 and 9.304).

Modules 9.305 through 9.313 outline critical deep learning workflow stages, including building the network (4 min duration), validating the approach (1 min duration), and generating predictions on new data (2 min duration). Specialized topics addressed include a different methodology for handling labels and loss (9.309) and the implementation of bottlenecked models (9.311). The Reuters Lab (9.313) serves as a substantial practical assessment for the concepts covered.

From a technical data processing standpoint, the methods follow the IMDB example, employing factorized samples. Furthermore, labels are specifically handled through one-hot or categorically encoded representations. Throughout the learning environment, essential navigation tools are provided for efficiency, including shortcut keys like CTRL + S, and specialized alternatives (H, J, K, L) for screen reader compatibility. The overall structure ensures a transition from basic fundamentals to advanced network implementation and experimental design.

---

## 04_9.305_Building_your_network_Video_4_min

# 9.305 Building your network
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/ri4rN/9-305-building-your-network

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 05_9.306_Validating_your_approach_Video_1_min

# 9.306 Validating your approach
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/EODmw/9-306-validating-your-approach

The curriculum is structured over 20 weeks, providing a comprehensive overview of Machine Learning fundamentals. The learning journey begins with Week 1 and Week 2, focusing on basic Machine Learning fundamentals, including dedicated lab work. Weeks 3 and 4 are dedicated to the concept of Classification, continuing into Week 4. Subsequently, Weeks 5 and 6 introduce and explore the domain of Regression.

The academic progression features Week 7, which is dedicated to Model evaluation and improvement. Week 8 delves into Probabilistic classification methods. The curriculum then transitions to Weeks 9 and 10, covering Unsupervised learning in depth. The focus significantly shifts in Week 11, initiating the study of Neural networks and deep learning. This subject matter is elaborated upon in Weeks 12, 13, and 14, which cover the mathematical building blocks of neural networks.

Weeks 15, 16, and 17 are devoted to practical implementation, specifically "Getting started with neural networks." These segments include specific examples, such as the multiclass classification example (9.301). Practical application utilizes datasets like the Reuters dataset (9.302 and 9.304). Other essential labs involve preparing data (9.303), building the network (9.305), and validating the approach (9.306).

The instructional sequence culminates with the REUTERS Lab in Week 17 (9.313) and continues into Weeks 18, 19, and 20. These final weeks wrap up the deep dive into Neural Networks and ML fundamentals, addressing Topics 9 and 10.

In a technical training demonstration, a specific experimental setup is outlined. The procedure requires setting aside 1000 samples for the dedicated validation set. Training runs are conducted in large batches, specifically 512 samples per batch. Furthermore, these training batches are run for a total duration of 20 epochs.

The results of the training are meticulously tracked, with both training and validation loss and accuracy saved within the history object. The keys available in this history object include records for training loss, validation loss, training accuracy, and validation accuracy. A crucial finding reveals that overfitting begins to occur after the validation loss reaches its lowest recorded point, which is precisely at 7 epochs.

A subsequent and final training outcome was documented after instantiating a new network and training it across the entire training set. This final network achieved an accuracy very close to 80%. The drawing code necessary to visualize the training process is specifically packed inside the function named `plot_epochs`.

---

## 06_9.308_Generating_predictions_on_new_data_Video_2_min

# 9.308 Generating predictions on new data
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/EdgR4/9-308-generating-predictions-on-new-data

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 07_9.309_A_different_way_to_handle_labels_and_loss_Video_45_sec

# 9.309 A different way to handle labels and loss
Video • 45 sec - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/REOCN/9-309-a-different-way-to-handle-labels-and-loss

The provided document outlines a comprehensive curriculum focused on Machine Learning fundamentals and Deep Learning implementation. The coursework is segmented into 20 weeks, covering a broad spectrum of technical concepts. The initial focus, in Weeks 1 and 2, is dedicated to Machine Learning fundamentals and practical labs. Weeks 3 and 4 introduce the topic of Classification, followed by Weeks 5 and 6 which delve into Regression. Model performance and improvement are covered in Week 7, followed by Probabilistic classification in Week 8. Weeks 9 and 10 are reserved for the concepts of Unsupervised learning.

A significant portion of the curriculum is dedicated to Neural networks and deep learning, starting in Week 11. Weeks 12, 13, and 14 concentrate specifically on the mathematical building blocks of neural networks. Practical application of neural networks begins in Week 15 and continues through Week 18. Additional foundational concepts, such as fundamentals of machine learning, are revisited in Weeks 19 and 20.

Regarding specific implementation details, the provided video transcript addresses a critical topic: handling labels and loss functions. It details an alternative method where labels can be cast as integers, instead of requiring one-hot encoding. When using integer labels, the choice of loss function must be adjusted accordingly. The recommended and current method involves using `sparse_categorical_crossentropy` with integer labels.

Although the function itself, `sparse_categorical_crossentropy`, is technically the same as `categorical_crossentropy`, the programming interface for it has undergone a change. The process of compiling the model requires explicitly using the `sparse_crossentropy` loss function.

The curriculum incorporates practical examples, such as a multiclass classification example (9.301) and work involving The Reuters dataset (9.302, 9.304). Additional advanced topics explored include building networks (9.305), validating approaches (9.306), and investigating bottlenecked models (9.311). The materials also include specific assignments and quizzes, such as the Reuters Lab.

Finally, technical navigation instructions are provided for the user interface, detailing shortcuts (CTRL + S) and screen reader compatibility for navigating the transcript. These elements ensure full accessibility across the learning materials.

---

## 08_9.311_Bottlenecked_model_Video_1_min

# 9.311 Bottlenecked model
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/sViUB/9-311-bottlenecked-model

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 09_9.312_Further_experiments_and_wrapping_up_Video_1_min

# 9.312 Further experiments and wrapping up
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/SuLkS/9-312-further-experiments-and-wrapping-up

This text provides a detailed summary of machine learning fundamentals, covering curriculum topics ranging from basic concepts to advanced neural network architectures, supplemented by specific technical guidelines for classification tasks.

The overall curriculum spans 20 weeks, beginning with Machine Learning fundamentals in Weeks 1 and 2. Week 3 and Week 4 focus specifically on Classification techniques. Subsequently, the material transitions into Regression, covered in Weeks 5 and 6. Model evaluation and improvement are addressed in Week 7.

The core conceptual framework expands into probabilistic classification in Week 8. Weeks 9 and 10 are dedicated to Unsupervised learning methodologies. A major focus area is Neural Networks and Deep Learning, spanning Weeks 11 through 17.

Weeks 12, 13, and 14 delve into The mathematical building blocks of neural networks, providing a foundational understanding of the underlying computation. The practical application of these principles begins in Week 15 and continues through Week 17, focusing on getting started with neural networks. Final topics, Weeks 18, 19, and 20, further explore advanced neural network applications and fundamentals.

Regarding practical implementation, the curriculum includes specific resources related to the Reuters dataset. Video 9.302 introduces the Reuters dataset, while 9.303 details the crucial step of preparing the data.

For technical design, specific instructions are given regarding network architecture testing. Users may experiment with various network configurations, including testing models on networks with different layer sizes, such as 128 units or 32 units. The guidance emphasizes utilizing models featuring one and three hidden layers for testing.

For multi-class classification tasks, the architecture must be correctly structured. Specifically, the output layer in a multi-classifications task must possess a number of units equal to the total number of classes available. The Softmax activation function is required for single-label multi-classifications.

Critically, a Softmax layer outputs a probability distribution across the possible classes. To correctly handle labels, one-hot or code labels—which represent categorical encoding—must be utilized. In single-label multi-class tasks, the appropriate loss function to employ is the categorical crossentropy loss.

A significant design warning is provided against creating "information bottlenecks." This occurs when intermediate layers are defined as excessively small, which can severely limit the network's capacity and ability to learn complex relationships.

Further practical experience is provided through dedicated labs, including the REUTERS Lab (9.313), allowing students to apply the learned techniques.

(Note: The original text contained technical UI instructions (e.g., "CTRL + S" for saving notes, specific key replacements for screen readers), but these instructions were omitted from the summary as they relate to the viewing interface rather than the core technical concepts of the subject matter.)

---

