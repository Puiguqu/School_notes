# Week 12 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_8.101_Looking_at_a_neural_network_Reading_1h

# 8.101 Looking at a neural network
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/OdD5n/8-101-looking-at-a-neural-network

This reading provides a practical examination of neural network operation, building upon introductory lectures. The specific practical example utilized for this study is handwritten digit classification, which is noted as a simple yet widely used application. Key technical concepts covered involve how data must be represented for neural networks, specifically detailing the components of samples, labels, and tensors. A critical focus is placed on understanding why the manner in which this data is structured is fundamentally important for the learning process of the network. Readers are directed to consult Chollet and Watson (2025), referencing Sections 2.1 ('A first look at a neural network') and 2.2 ('Data representations for neural networks'). For full access to the required material, the text refers to '1.003 How to access Chollet, F. and M. Watson (2025) Deep Learning with Python, Third Edition, Manning Publications ebook'. Ultimately, the material demonstrates the relationship between proper data structuring, core technical elements (samples, labels, tensors), and the practical performance of a neural network.

---

## 02_8.102_MNIST._Loading_MNIST_in_Keras._Network_architecture_Video_2_min

# 8.102 MNIST. Loading MNIST in Keras. Network architecture
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/aro39/8-102-mnist-loading-mnist-in-keras-network-architecture

This comprehensive curriculum provides a structured deep dive into machine learning fundamentals, progressing sequentially through theoretical concepts and practical implementations. The initial weeks introduce Machine Learning fundamentals (Week 1 and 2), establishing the necessary theoretical groundwork before moving into specific modeling tasks. The course rapidly advances to Classification (Week 3 and 4), teaching methods for discrete data prediction. This is followed by a dedicated study of Regression (Week 5 and 6), focusing on continuous value prediction.

A critical component of the curriculum is Model Evaluation and Improvement (Week 7), ensuring students can assess model efficacy before proceeding. The program then explores advanced topics, including Probabilistic Classification (Week 8), which deals with uncertainty in classification outcomes. Unsupervised learning is covered extensively in Weeks 9 and 10, focusing on methods like clustering and dimensionality reduction when labels are absent.

The course culminates with a focus on Neural Networks and Deep Learning (Week 11), moving beyond traditional ML approaches. The mathematical foundation of these networks is meticulously developed in Weeks 12, 13, and 14. A significant portion of the technical instruction revolves around practical application using the MNIST dataset and the Keras framework.

Specifically, the module 8.102 details the process of loading the MNIST dataset into Keras to establish a network architecture. Subsequent sections (8.103 through 8.111) meticulously break down the lifecycle of a deep learning model. These steps include the Compilation phase (8.104/8.105), Building the network (8.106/8.107), Training the network (8.108/8.109), and finally, Testing the network (8.110/8.111).

A core conceptual area is the representation of data, detailed in Section 8.2. This covers Scalars (8.201), Vectors (8.201), Matrices (8.203), and Tensors (8.203), emphasizing their key attributes (8.205). Furthermore, students learn how to manipulate these tensors in Numpy, focusing on Data Batches (8.207). Real-world tensor examples are provided (8.209), solidifying the connection between abstract mathematics and practical data handling.

The curriculum incorporates practical labs, such as "The perceptron Lab" (8.212), providing hands-on implementation opportunities. The subsequent weeks (15 through 18) reinforce and expand upon getting started with neural networks. The course concludes by reviewing the Fundamentals of Machine Learning (Week 19 and 20), integrating all learned components for a holistic understanding of AI systems.

---

## 03_8.104_Compilation_(pre-process)_Video_2_min

# 8.104 Compilation (pre-process)
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/cZoWS/8-104-compilation-pre-process

Data preprocessing is a crucial initial step required to prepare data for acceptance by a neural network. The fundamental requirement is that the data must be reshaped into a format acceptable to the network. Specifically, the network anticipates input samples presented as vectors, which are one-dimensional arrays of floating-point values.

To achieve this, the initial pixel map image must be flattened or straightened into a linear sequence of values. The Matplotlib graphics library is mentioned as a tool used in the process of displaying grayscale images.

The preprocessing phase consists of three distinct steps that must be executed sequentially. First, the original map data is flattened using a call to a reshape function. This function requires supplying the desired resulting shape to pull the correct dimensions.

A practical example provided is transforming a dataset of 60,000 images, each originally 28x28. The resulting two-dimensional array shape is specifically set to 60,000 by 784.

The second step involves casting the input integer values to floating-point values. Following the type conversion, the third and final step is re-scaling the data. This re-scaling ensures that all pixel values lie within the normalized range of zero and one.

In addition to image data, the labels used for classification require a specific transformation. The network requires labels to be provided in a categorically encoded format. This process is often referred to as one-hot encoding.

One-hot encoding is represented as a seemingly wasteful change of data representation. The conversion results in a vector where all elements are zero, except for a single 'hot' entry. This 'one' is strategically placed at a vector position corresponding to the specific label category.

For instance, if the label is seven, the encoding places the single 'one' in the eighth slot of the corresponding vector. The conversion to one-hot encoding can be easily executed through a function like `to_categorical`.

The overall course structure covers a wide range of machine learning fundamentals. Early topics include classification (Weeks 3 & 4) and regression (Weeks 5 & 6).

Model evaluation and improvement are addressed in Week 7, while probabilistic classification is covered in Week 8. The curriculum then delves into unsupervised learning in Weeks 9 and 10.

Neural networks and deep learning are the primary focus of Week 11. The mathematical underpinning of these complex structures is detailed across Weeks 12, 13, and 14.

Further in-depth study of neural networks begins in Week 15, continuing through Week 18. Week 19 and Week 20 reinforce the fundamentals of machine learning.

Theoretical foundations cover diverse representations, starting with scalars and vectors (8.201). This progresses to matrices and tensors (8.203), which are critical data structures.

Key attributes related to these tensors and vectors are analyzed, including manipulation techniques using NumPy (8.207). A specific practical exercise involves manipulating tensors in Numpy to handle data batches.

The course also introduces foundational concepts like the perceptron lab (8.212). Practical application involves several modules related to the MNIST dataset, including loading, compilation, building, training, and testing the network architecture.

These hands-on modules address network compilation (8.104), network building (8.106), network training (8.108), and network testing (8.110).

The fundamental concepts of machine learning are built upon these mathematical blocks, including the representation of data types like scalars, vectors, and tensors. The ability to manipulate and understand these tensors is essential for advanced learning.

---

## 04_8.106_Building_the_network_Video_2_min

# 8.106 Building the network
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/YXhbN/8-106-building-the-network

This comprehensive curriculum begins with foundational machine learning concepts in Week 1 and Week 2, establishing the basic principles and providing hands-on laboratory practice. The core supervised learning domain starts in Week 3 and Week 4, dedicated entirely to the topic of Classification. This is followed by Weeks 5 and 6, which extensively cover Regression techniques.

Progression continues through Week 7, focusing on crucial Model Evaluation and Improvement strategies necessary for robust deployment. In Week 8, the subject shifts to the more complex area of Probabilistic Classification. Week 9 and Week 10 are reserved for Unsupervised Learning, providing instruction on how models identify patterns without labeled data.

The focus then transitions dramatically in Week 11 to Neural Networks and Deep Learning fundamentals. Weeks 12, 13, and 14 are devoted to the detailed mathematical building blocks of neural networks. These sessions introduce fundamental data representations, starting with Scalars and Vectors. Crucially, the material expands into Matrices and Tensors, requiring students to understand their key attributes.

Practical implementation in Week 12 involves manipulating tensors using Numpy, specifically demonstrating the concept of Data Batches. The course includes real-world tensor examples, reinforcing the abstract mathematical principles. A significant practical exercise is the exploration of the perceptron via a dedicated lab session.

The application of deep learning is initially introduced using the MNIST dataset. Specific learning modules guide students through the entire network lifecycle, from loading MNIST in Keras to final testing. This process includes detailed steps for Compilation (pre-processing), Network Building, Training the network, and finally, Testing the trained network.

This cyclical structure—Load, Compile, Build, Train, Test—is reiterated across various assignments and quizzes. The curriculum also includes a dedicated discussion prompt to encourage critical thinking alongside technical skill development. Weeks 15 through 18 continue the deep dive into advanced Neural Network topics, ensuring comprehensive understanding.

Finally, Weeks 19 and 20 serve as a rigorous review of Fundamentals of Machine Learning, synthesizing all the concepts covered from classification to deep learning. The detailed modules cover essential implementation steps like building the network and testing it, ensuring the mastery of both theory and practical application.

---

## 05_8.108_Train_network_Video_2_min

# 8.108 Train network
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/MWixK/8-108-train-network

The course material provides a comprehensive structure covering machine learning fundamentals, ranging from classification (Week 3) and regression (Week 5) to advanced topics like unsupervised learning (Week 9) and deep learning (Week 11). A critical section delves into the mathematical building blocks of neural networks, which involve understanding data representations. Technical foundations require knowledge of scalars, vectors, matrices, and tensors. Specific training techniques include manipulating tensors within Numpy, often used when processing data batches.

The neural network training workflow is detailed in segments like 8.101 (Loading MNIST) through 8.111 (Testing network). This process begins with network compilation and architecture building. The training phase is initiated through a call to `fit`, which accepts the labeled training sample data, the specified number of epochs, and batch settings.

The core of the training process is handled by the optimizer, specifically RMS prop. This optimizer continually tweaks the layer parameters, which include both weights and biases, in an effort to minimize the loss. The loss is defined as the discrepancy between the network's prediction and the true target value. During training, the goal is for the optimizer to drive this loss toward zero.

The procedure also requires defining crucial training hyperparameters: the mini-batch size, which determines the number of samples processed in a single pass, and the number of epochs, representing complete passes through the entire training set. Monitoring information, such as the accuracy (the count of correctly classified samples), is printed at the end of each epoch.

As the network trains, the loss is observed to decrease while the accuracy slowly increases, indicating learning progress. When training is complete, the optimizer has adjusted the layer weights and biases, resulting in a high accuracy (e.g., almost 99% recognition on the training set).

However, a critical finding is that achieving high accuracy on the training data does not guarantee robust performance on unseen data. This principle highlights the essential role of testing the network to ensure it performs effectively for general tasks, such as automatic letter sorting. The overarching purpose of training is the automatic identification of patterns in new inputs, ensuring the model successfully generalizes beyond the initial dataset.

---

## 06_8.110_Test_network_Video_2_min

# 8.110 Test network
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/xaivZ/8-110-test-network

This comprehensive course curriculum spans 20 weeks, progressively covering the fundamental concepts and advanced mathematical building blocks of machine learning and deep learning. The initial phase establishes Machine Learning fundamentals in Weeks 1 and 2. The core theory progresses into Classification in Weeks 3 and 4, followed by Regression analysis in Weeks 5 and 6.

Week 7 is dedicated to crucial Model evaluation and improvement techniques, while Week 8 introduces Probabilistic classification methods. The study expands into Unsupervised learning in Weeks 9 and 10, allowing students to explore pattern recognition without labeled data. This foundational knowledge then transitions significantly to Neural networks and Deep learning in Week 11.

Week 12, focused on The mathematical building blocks of neural networks, introduces a detailed, procedural approach to network implementation. Section 8.1 provides a practical guide, starting with "Looking at a neural network" (8.101). The practical application centers on utilizing MNIST data by "Loading MNIST in Keras" (8.102), followed by stages including Compilation (8.104), Building the network (8.106), Training (8.108), and Testing the network (8.110). Each procedural step is reinforced by post-video quizzes and practice assignments.

The technical language is formally defined in Section 8.2, "Representations." This section begins by differentiating between Scalars and vectors (8.201). It then deepens the understanding into Matrices and tensors (8.203), examining their key attributes (8.205). Students learn the practical application of manipulating tensors within NumPy, including the handling of Data batches (8.207). Furthermore, real-world tensor examples are provided (8.209).

A key theoretical deliverable is "The perceptron Lab" (8.212). The mathematical study continues through Week 13 and Week 14, maintaining the focus on the mathematical building blocks. The course further expands into initial practical applications and deepening understanding of neural networks across Weeks 15 through 18. The curriculum concludes with dedicated modules on Fundamentals of machine learning in Weeks 19 and 20. All instructional units are meticulously designed, often including specific videos, post-video quizzes, and dedicated practice assignments to ensure mastery of the technical material.

---

## 07_8.201_Scalars_and_vectors_Video_2_min

# 8.201 Scalars and vectors
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/qXHWs/8-201-scalars-and-vectors

This technical overview covers the fundamental building blocks of deep learning, focusing primarily on tensor operations and network optimization. The course curriculum spans several topics, beginning with machine learning fundamentals and advancing through classification, regression, and probabilistic classification. Later modules delve into unsupervised learning, concluding with detailed studies of neural networks and their mathematical prerequisites. Specifically, Week 11 covers Neural Networks and Deep Learning, while Weeks 12, 13, and 14 focus on the mathematical building blocks of these networks.

The initial concepts begin with a review of basic Python lists and then transition to NumPy arrays, which serve as a far more efficient representation for multidimensional data containers. Arrays are a core data structure, implemented in Python using lists. The dimensionality of an array is formally defined as the number of indices required to retrieve a specific value within it. For instance, a 0D array requires no indices, representing a simple single value. Conversely, a 1D array necessitates only a single index, while a 2D array requires two indices.

TensorFlow utilizes a multidimensional structure analogous to the NumPy array, which is termed a tensor. A critical technical detail is that a tensor axis is equivalent to an array dimension. The total number of tensor axes defines the tensor's rank. Mathematically, a 0D tensor is a container for a single value, corresponding to a mathematical 'scalar.' This rank zero tensor can be created using the `Np array` function, resulting in a NumPy array with rank zero.

The rank of any NumPy array can be directly accessed using the `ndim` attribute. A 1D tensor, which functions as a list of values, is a Rank 1 tensor. Higher-rank tensors are constructed by passing lists to the `np array` function, establishing the creation of a single axis, or rank 1, tensor. It is crucial to maintain the distinction between the dimension of a mathematical vector (which is the number of elements) and the tensor dimension (which refers to the number of axes).

The supplementary material details advanced concepts such as Scalars and vectors, Matrices and tensors, and methods for manipulating tensors in NumPy. These discussions lead to understanding real-world tensor examples and foundational principles. The progression culminates in labs covering the perceptron, demonstrating the essential mathematical foundations required for subsequent deep learning studies.

---

## 08_8.203_Matrices_and_tensors_Video_2_min

# 8.203 Matrices and tensors
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/PY23C/8-203-matrices-and-tensors

This comprehensive course spans 20 weeks, beginning with the essential Machine Learning fundamentals in Week 1 and progressing into practical application labs in Week 2. The initial phase of the curriculum focuses on core predictive modeling techniques, starting with Classification in Weeks 3 and 4. Following this, Week 5 and Week 6 delve into Regression, covering its theoretical and practical aspects. The understanding of how models perform is introduced in Week 7, focusing on Model Evaluation and Improvement.

The curriculum then advances to more sophisticated modeling in Week 8 with Probabilistic Classification. Weeks 9 and 10 are dedicated to Unsupervised Learning, exploring how models find structure in data without pre-labeled outcomes. A major shift occurs in Week 11 with the introduction to Neural Networks and Deep Learning. This leads directly into Weeks 12, 13, and 14, which focus on "The mathematical building blocks of neural networks."

The mathematical foundation is robustly established, starting with the conceptualization of data types. Section 8.2 introduces Scalars and vectors (8.201), followed by the crucial study of Matrices and tensors (8.203). Subsequent topics cover Key attributes (8.205) and the practical application of manipulating tensors in Numpy, specifically addressing data batches (8.207). Real-world tensor examples are then illustrated (8.210), culminating in a foundational lab on the Perceptron (8.212).

The practical application of these concepts is heavily emphasized through structured modules, such as the deep dive into MNIST data loading and network architecture (8.102, 8.103). These modules detail the full lifecycle of network development, including Compilation (8.104), Building the network (8.106), and Training/Testing the network (8.108, 8.110). Each step is backed by dedicated video lectures and associated practice assignments/quizzes.

The course also incorporates essential theoretical discussions, such as the decision-making process documented in 8.211. Later weeks ensure consolidation of knowledge. Weeks 15 through 18 focus on "Getting started with neural networks," providing continued practical experience. Finally, Weeks 19 and 20 serve to reinforce and expand the Fundamentals of Machine Learning (Topic 10), ensuring a holistic understanding of the entire ML pipeline. Specific technical elements include the utilization of Keras for MNIST loading and the foundational concepts of data batching in Numpy.

---

## 09_8.205_Key_attributes_Video_2_min

# 8.205 Key attributes
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/oAiZ9/8-205-key-attributes

Tensors and arrays are fundamental concepts used in computational implementation for representing data structures like vectors and matrices. Arrays refer to any computational implementation of vectors and higher-dimensional structures. Tensors are a special construction within NumPy, though the terms are often used interchangeably, and "tensor" also appears in mathematical language. A rank 1 tensor is equivalent to a 1D array, or a vector. The tensor rank, also known as dimension, signifies the total number of axes present in the structure. The tensor shape defines the number of elements along each specific axis. The type of a tensor refers to the specific data type of the contained data, such as `float 32` or `uint 8`.

Conceptually, the shape of a scalar entity is described as having "nothing at all." Tensor shape is formally represented as a Python tuple. Because Python tuples consist of values separated by commas, a vector's shape might appear unusually structured, such as having the shape `length,` to denote a single dimension. For example, a $2 \times 3$ matrix or array possesses the shape `2, 3`. A specific example provided is the MNIST image tensor, which exhibits a rank of 3 and a shape of `60,000, 28, 28`, utilizing the `uint 8` type.

The curriculum outlines a comprehensive journey through machine learning fundamentals. Weeks 1 and 2 cover initial ML fundamentals, followed by dedicated modules on Classification in Weeks 3 and 4. Week 5 and 6 delve into Regression techniques. Model evaluation and improvement are the focus areas of Week 7.

The content continues with advanced topics, including Probabilistic Classification in Week 8. Week 9 and 10 introduce Unsupervised Learning techniques. A significant pivot occurs in Week 11, introducing Neural Networks and Deep Learning. Weeks 12 through 20 maintain a focus on the mathematical building blocks of neural networks and fundamental ML concepts.

Specific module outlines detail practical application, such as the `Perceptron Lab` and various sections dedicated to using Keras for loading and testing MNIST data. Module 8.1 covers the entire process: loading, compilation, building, training, and testing the network. Module 8.2 addresses data representations, specifically detailing scalars, vectors, matrices, and tensors. The curriculum utilizes structured practice assignments and post-video quizzes to solidify learning.

Key instructional elements include video content, practice assignments, and discussion prompts. Resources are available for both the beginner and advanced learner, covering topics like "Key attributes" and "Manipulating tensors in Numpy. Data batches." The entire structure culminates in mastering the foundational mathematical concepts necessary for modern deep learning implementations.

---

## 10_8.207_Manipulating_tensors_in_Numpy._Data_batches_Video_4_min

# 8.207 Manipulating tensors in Numpy. Data batches
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/2rdPO/8-207-manipulating-tensors-in-numpy-data-batches

This curriculum details a comprehensive progression through Machine Learning fundamentals, starting in Week 1 with basic concepts. Early instruction covers the core principles of Machine Learning, transitioning into practical applications and laboratory exercises in Week 2. The focus then shifts to classification techniques, which are covered in depth across Weeks 3 and 4. Following classification, the curriculum addresses regression analysis during Weeks 5 and 6.

The methodological depth increases in Week 7, focusing on model evaluation and improvement techniques crucial for robust system design. Week 8 introduces probabilistic classification methods, moving beyond simple decision boundaries. The learning path then bifurcates, dedicated to unsupervised learning in Weeks 9 and 10.

A major segment of the course is dedicated to artificial intelligence, starting with neural networks and deep learning in Week 11. Weeks 12, 13, and 14 dive into the mathematical building blocks of neural networks, establishing the theoretical foundation. A practical exploration of neural network construction begins in Week 15, continuing through Week 18.

The technical implementation phase is characterized by working with data structures and core components. Modules detail the process of building and training a network, using the MNIST dataset loaded within Keras (8.102, 8.103). This includes crucial steps like compilation and network architecture definition (8.104, 8.106). The subsequent sections focus on the practical steps of training and testing the network (8.108, 8.110).

Fundamental mathematical representations are covered extensively in Section 8.2, starting with scalars and vectors (8.201). The curriculum progresses to matrices and tensors, highlighting their key attributes (8.203, 8.206). A significant technical skill developed is manipulating these tensors using Numpy, specifically dealing with data batches (8.207).

The progression reinforces practical application with real-world tensor examples (8.209) and concluding with the historical and mathematical significance of the perceptron (8.212). The latter weeks of the course, Weeks 19 and 20, consolidate these concepts by reviewing the overall fundamentals of machine learning. The curriculum is highly structured, integrating video lectures, practice assignments, and specialized lab work throughout its duration.

---

## 11_8.209_Real-world_tensor_examples_Video_1_min

# 8.209 Real-world tensor examples
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/UCF7e/8-209-real-world-tensor-examples

This text describes fundamental concepts in machine learning, focusing particularly on data representation using tensors and outlining a structured course curriculum.

The core technical concept presented is the definition of data tensors and their dimensionality in real-world datasets. A tensor is a multi-dimensional array used to organize data, where the "samples" axis typically refers to individual data points. For instance, collecting population data—such as postcode, age, and income—results in samples where each person surveyed constitutes a vector of collected information.

Time-series data, such as weather readings, is exemplified by measurements like precipitation and temperature recorded at fixed intervals, specifically at 10-minute intervals, which are then connected across successive days or samples. A color image dataset serves as an example of rank 4 information, where each pixel holds an RGB vector.

The most complex examples involve videos, which are represented as rank 5 tensors. A video inherently involves a time series of frames, and each individual frame is itself a 2D color image, thereby increasing the tensor’s dimensionality.

The overall curriculum is highly structured, covering a wide range of machine learning disciplines over several weeks. Early topics focus on machine learning fundamentals, leading into Week 3 and Week 4, which address Classification techniques.

The curriculum then moves to Week 5 and Week 6, dedicated to the topic of Regression. Subsequently, Week 7 focuses on critical Model evaluation and improvement methodologies.

The study progresses to Week 8, covering Probabilistic classification, and Week 9 and Week 10 explore Unsupervised learning methods.

Later topics dive into advanced architectures, including Week 11, which covers Neural networks and deep learning, followed by Week 12, detailing The mathematical building blocks of neural networks.

The course structure provides specific, practical tutorials under Section 8.1 and Section 8.2. Section 8.1 guides students through practical neural network applications, utilizing the MNIST dataset as a primary example.

Within Section 8.1, students learn the entire network lifecycle: loading, compilation (pre-process), building the network, training the network, and testing the network. These processes are reinforced through associated video lectures and practice assignments.

Section 8.2 shifts focus to the fundamental representations of data: Scalars, vectors, Matrices, and Tensors. The material highlights how these concepts are manipulated using libraries like NumPy.

Specifically, Section 8.207 addresses the practical aspect of manipulating tensors in NumPy, including handling Data batches. Section 8.209 provides further context on Real-world tensor examples, tying the abstract mathematical concepts to practical applications.

The course also incorporates specialized activities, such as a discussion prompt in Section 8.211 and a foundational lab in Section 8.212 focusing on the perceptron.

In summary, the content systematically builds knowledge from basic data structures (scalars, vectors) up through complex deep learning models, ensuring students understand both the mathematical representation and the operational flow of modern ML algorithms.

---

