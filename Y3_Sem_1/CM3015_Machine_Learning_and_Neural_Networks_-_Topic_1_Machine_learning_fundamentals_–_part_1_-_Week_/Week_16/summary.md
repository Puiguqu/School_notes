# Week 16 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_9.201_A_binary_classification_example_Reading_1h

# 9.201 A binary classification example
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/TzAwY/9-201-a-binary-classification-example

This reading introduces the practical application of binary classification, recognized as one of the most common tasks in machine learning. The specific application explores how to classify movie reviews, distinguishing them as either positive or negative. This analysis utilizes the International Movie Data Base (IMDB) dataset, which constitutes a large collection of labelled text data. The primary goal of this example is to demonstrate how previously learned concepts and tools synthesize into a real-world application. Ultimately, this knowledge serves to prepare the reader for a hands-on lab scheduled for the end of the week. Readers are directed to consult Chollet and Watson (2025), specifically Section 4.1, for the detailed instructional material. For a complete understanding, access details must reference the text titled: '1.003 How to access Chollet , F. and M. Watson (2025) Deep Learning with Python, Third Edition, Manning Publications ebook'. This structured learning segment aims to bridge theoretical machine learning concepts with practical data classification tasks.

---

## 02_9.202_The_IMDB_dataset_Video_1_min

# 9.202 The IMDB dataset
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/bDjmw/9-202-the-imdb-dataset

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 03_9.203_Preparing_the_data_Video_1_min

# 9.203 Preparing the data
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/N2ctK/9-203-preparing-the-data

The provided material consists of a technical video transcript and an accompanying course syllabus detailing machine learning fundamentals. The technical transcript addresses critical data input requirements for neural networks. Specifically, the network demands tensor input rather than traditional Python lists. To facilitate this, three primary methods are outlined. The first approach involves padding lists until they achieve an equal length. A second method involves forming integer tensors and subsequently utilizing a special embedding layer. This layer connects stepped integer tensors to the network. The third method presented is to one-hot encode the data and input the resulting vector to a dense layer.

One-hot encoding is a precise technique that translates categorical data into a numerical format. A one-hot vector is characterized as a vector composed exclusively of zeros and ones. For this encoding, the ones are specifically placed at indices that correspond to the values present in the original list. All other elements within the vector remain zero. A concrete example illustrates this process: the input (3, 5) transforms into a sequence such as (0, 0, 0, 1, 0, 1, 0, 0, etc.). This encoding process involves sampling and converting the input layers to floating-point value tensors.

The discussion also addresses the structure of the training data. The sorted set represents the elements of the training data ordered in ascending magnitude, with any duplicate entries removed. A significant finding is demonstrated when data points are absent; if values, such as three and nine, are missing, the resulting one-hot encoding will correctly register zeros in their corresponding positions.

The accompanying syllabus maps out a comprehensive curriculum spanning multiple weeks. The study begins with Week 1 and Week 2, focusing on Machine Learning fundamentals and associated laboratory exercises. Classification techniques are covered in Week 3 and Week 4. Regression is introduced in Week 5 and Week 6. The module then proceeds to Week 7 for Model evaluation and improvement.

Week 8 is dedicated to Probabilistic classification. Subsequent topics include Week 9 and Week 10, which cover Unsupervised learning. The core deep learning concepts start with Week 11 and continue through Week 14, focusing on Neural networks and their mathematical building blocks. Weeks 15 through 18 detail the practical aspects of getting started with neural networks.

A practical example features a binary classification assignment (9.201), lasting one hour. This section also introduces the IMDB dataset through videos (9.202 and 9.203). Preparing the data for this project is addressed in a 30-minute post-video quiz (9.204). Students then move to building their model (9.205), which involves a 6-minute video followed by a 30-minute practice assignment (9.206).

Further practical steps include validating the approach (9.207) in a 3-minute video and completing a subsequent 30-minute post-quiz (9.208). The module progresses to prediction using a pre-trained network (9.209), followed by further experiments and concluding wrap-up discussions (9.210). A major component is the dedicated IMDB Lab (9.211) spanning one hour. The course concludes its structure with a discussion prompt in Week 12 (9.212). The curriculum cycle continues, revisiting neural networks and fundamentals in Weeks 17 through 20.

---

## 04_9.205_Building_your_model_Video_6_min

# 9.205 Building your model
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/zLzkl/9-205-building-your-model

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 05_9.207_Validating_your_approach_Video_3_min

# 9.207 Validating your approach
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/e9zJw/9-207-validating-your-approach

Machine learning methodology necessitates the use of a validation dataset, which is crucial for hyperparameter tuning. Hyperparameters represent non-trainable parameters, such as the learning rate, which require experimentation. The validation set's primary function is to monitor the training progress of the model. Specifically, the first 10,000 samples of the training set are reserved and sliced off to form this validation set. The remaining data constitutes the partial training set. Similarly, the labels are divided proportionally between the validation and partial training sets.

Training is configured to run for 20 epochs, utilizing mini-batches composed of 512 samples each. Progress is continuously monitored using both validation loss and validation accuracy. The function `Partial.fit` returns a history object, which is provided as a dictionary. This history object contains four key-value pairs: validation and training loss, and validation and training accuracy for every epoch.

During the process, a plot comparing training and validation loss reveals key trends. The training loss consistently decreases throughout the run, thereby confirming that Stochastic Gradient Descent (SGD) is effectively optimizing the model. However, the validation loss initially decreases but subsequently begins to increase. This divergence indicates a critical issue: model overfitting.

Overfitting occurs when the model fits the training data too closely and subsequently fails to generalize on the unseen validation data. The learned representations become excessively specific to the training set. The most important finding regarding the optimization timeline is that validation loss was lowest around epoch 4 or 5. Consequently, training should be halted just as the signs of overfitting kick in at this optimal epoch.

Following this optimal stopping point, a new network must be initialized and trained again. Crucially, this fresh network must be retrained using the complete training set, not just the partial set. After training, the network is evaluated on the complete, unseen test set. The resulting accuracy achieved on the test set was 88%. While this is a functional result for a simple network, the state-of-the-art networks in this domain should aim to achieve 95% accuracy.

The course structure covers these principles across several topics, beginning with foundational concepts in Week 1. Subsequent weeks dive into specific applications, including classification (Week 3), regression (Week 5), and probabilistic classification (Week 8). Advanced study progresses to unsupervised learning (Week 9) and deep neural networks (Week 11). The curriculum utilizes practical examples, such as the IMDB dataset, to guide the learning process. Detailed labs focus on data preparation, model building, and rigorous validation of the approach. The progression from foundational concepts to advanced neural network building ensures a comprehensive understanding of machine learning fundamentals.

---

## 06_9.209_Prediction_with_a_pretrained_network_Video_1_min

# 9.209 Prediction with a pretrained network
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/y62Lc/9-209-prediction-with-a-pretrained-network

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 07_9.210_Further_experiments_and_wrapping_up_Video_1_min

# 9.210 Further experiments and wrapping up
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/8dO3Q/9-210-further-experiments-and-wrapping-up

The presented material outlines core concepts, architectural methodologies, and a structured curriculum for machine learning and deep learning.

Experimentation in neural network development involves testing various parameters, including network architecture, depth, layer size, activation functions, losses, and learning rates. The initial example architecture is deemed reasonable, yet still presents opportunities for significant improvement. A critical initial step in any data pipeline is the thorough preprocessing of the raw data. Sequences of words, a common data type, are typically encoded and represented using binary vectors.

Model construction often relies on standard components such as Dense ReLU layers, which are optimized using the RMSProp optimizer to solve common training problems. A major challenge in neural network training is overfitting. This phenomenon occurs when a network performs exceptionally well on long training runs but fails to maintain strong performance on unseen data. To counteract overfitting, training must be carefully monitored by evaluating the model against a dedicated validation dataset.

When performing binary classification, the model structure requires a final layer composed of a single dense sigmoid unit. This design ensures that the model's output represents a probability of belonging to one class. For this specific binary classification task, the preferred and appropriate loss function is binary cross-entropy. The ultimate objective of the presented lessons is to transition from binary classification to solving a multiclass classification problem.

The curriculum is highly structured, spanning topics from fundamental concepts to advanced deep learning. Week 1 and 2 focus on Machine Learning fundamentals. Weeks 3 and 4 delve specifically into Classification techniques.

The training regimen then expands into Regression, covered in Weeks 5 and 6. Week 7 is dedicated to essential Model evaluation and improvement techniques. Weeks 8 and 9 cover Probabilistic classification and the beginning of Unsupervised learning, respectively.

The focus shifts heavily into neural networks and deep learning starting in Week 11. Weeks 12, 13, and 14 are devoted to exploring the Mathematical building blocks of neural networks in depth. Subsequent weeks (15, 16, 17, and 18) further explore the practical application and fundamentals of getting started with neural networks.

Practical implementations utilize the IMDB dataset, which serves as a primary training example. Practical exercises include data preparation (9.203, 9.204), building the model structure (9.205, 9.206), and subsequently validating the entire approach (9.207, 9.208). Furthermore, the curriculum includes instructions for prediction using pretrained networks (9.209) and conducting further experimental analysis (9.210). The entire learning sequence facilitates a comprehensive understanding of advanced machine learning practices.

---

