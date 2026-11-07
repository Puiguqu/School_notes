# Week 15 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_9.101_Introduction_to_Keras_Reading_1h

# 9.101 Introduction to Keras
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/kCr9m/9-101-introduction-to-keras

The following reading gives an introduction to Keras, which is a deep learning API for Python that provides a convenient way to define and train any kind of deep learning model. Read Chollet and Watson (2025), Section 3.6. For full access details, refer back to ' 1.003 How to access Chollet , F. and M. Watson (2025) Deep Learning with Python, Third Edition, Manning Publications ebook'....

---

## 02_9.102_Anatomy_of_a_neural_network_Video_1_min

# 9.102 Anatomy of a neural network
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/vgjjk/9-102-anatomy-of-a-neural-network

This curriculum provides a comprehensive, multi-phase study of machine learning, beginning with core fundamentals and progressing to advanced deep learning techniques. The initial weeks (W1-W2) lay the groundwork by establishing machine learning fundamentals. Subsequently, the course tackles supervised learning, dedicating significant time to Classification (W3, W4) and Regression techniques (W5, W6).

Model evaluation and improvement forms a crucial bridge (W7), leading into probabilistic classification (W8). The study then transitions to Unsupervised Learning (W9, W10), exploring methods used when labeled data is scarce.

The core focus shifts dramatically in Week 11 with the introduction to Neural Networks and Deep Learning. Weeks 12, 13, and 14 are devoted to understanding the mathematical building blocks necessary to govern neural network operations. The practical application phase begins in Week 15 by introducing Keras (9.101).

This practical segment details the architecture of a neural network, beginning with the anatomy (9.102), followed by specific components like Layers (9.104) and complex Models composed of these layers (9.106). Critical to the learning process are the discussions regarding Loss functions and optimizers (9.108). Practical assignments and quizzes are integrated throughout this phase (e.g., 9.103, 9.105, 9.107, 9.109).

The program includes vital contextual discussions, addressing the ethical risks associated with AI and Artificial Superintelligence (ASI) (9.110). These practical and theoretical concepts are reinforced throughout Weeks 16, 17, and 18. The course culminates with a foundational review of machine learning principles in Weeks 19 and 20, ensuring a robust grasp of the fundamentals.

---

## 03_9.104_Layers_Video_5_min

# 9.104 Layers
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/pCZpv/9-104-layers

The foundational building block of a neural network is the layer, which functions by mapping tensors to tensors. These layers are parameterized by specific weights and biases and update their parameters via the Stochastic Gradient Descent (SGD) feedback loop. A typical neural network processing involves feeding a sample, transforming the data through successive layers, and ultimately producing an output.

In a dense or fully connected layer, the transformation involves an $n \times m$ weight matrix, where the incoming vector has length $m$ and the resulting transformed vector has length $n$. An associated bias tensor is an $n$-component vector that contributes to the layer's transformation.

A Recurrent Neural Network (RNN) features internal loops, enabling it to process ordered data by iterating through sequential elements. RNN layers are optimally suited for samples that possess a time ordering, such as weather measurements. Conversely, Convolutional Layers (ConvNets) are the preferred method for computer vision applications, using a small window to move across a 2D image and map the response to layer weights.

The function of different network types dictates their optimal use: dense networks process vector data, recurrent networks handle sequence data, and convolutional layers are recommended for computer vision tasks. Returning to dense layers, the fundamental operation is an affine transformation followed by the application of an element-wise function.

An affine transformation is defined as $w \cdot x + b$, which constitutes a 2D matrix transformation—such as rotation, reflection, or shear—followed by a translation. While affine transformations preserve straight lines and parallel lines, they are insufficient alone for data uncrumpling. This necessitates the inclusion of a non-linear element-wise activation function.

Common activation functions include Sigmoid, Rectified Linear Unit (ReLU), and Tanh. The Sigmoid function, for instance, acts as a smoothed-out, differentiable step function, mapping large positive inputs to 1 and large negative inputs to 0, with a smooth transition near zero.

In implementation, the input and output tensor shapes of a TensorFlow Keras layer are fixed upon creation. For example, a layer might receive an input shape with axis 1 having dimensions $7, 8, 4$, with the batch dimension (axis 0) remaining unspecified. The layer may then output a vector of length 32.

A downstream layer must be configured to accept this specific input vector length; if the subsequent layer requires 16 elements, it is specified using `layers.dense(16)`. Technically, the layer's weight tensor has a shape of $m \times n$, which is the reverse of the conventional matrix size $n \times m$.

The organizational structure of TensorFlow utilizes matrix transposes for tensor operations, though computationally, all quantities are arrays, and operations are executed as loops with defined counters and end conditions. This ensures that even complex matrix-vector multiplications function seamlessly within the framework. These concepts form the core mathematical and architectural blocks necessary for deep learning.

---

## 04_9.106_Models_networks_of_layers_Video_1_min

# 9.106 Models: networks of layers
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/rC2La/9-106-models-networks-of-layers

This comprehensive curriculum begins with the fundamental concepts of Machine Learning during Weeks 1 and 2. The core machine learning tasks are introduced sequentially, starting with Classification in Weeks 3 and 4. This is followed by Regression, which covers continuous prediction models throughout Weeks 5 and 6.

The study then shifts to model performance and advanced techniques, dedicating Week 7 to Model Evaluation and Improvement. Further foundational concepts include Probabilistic Classification in Week 8 and Unsupervised Learning in Weeks 9 and 10, exploring methods like clustering.

The curriculum transitions dramatically toward modern deep learning starting in Week 11, introducing Neural Networks. The theoretical backbone is built over Weeks 12, 13, and 14, focusing heavily on the Mathematical Building Blocks of Neural Networks.

A significant portion of the latter modules focuses on practical implementation using Keras, beginning in Week 15. This practical track starts with 9.101 Introduction to Keras and moves into the 1-minute overview provided in 9.102 Anatomy of a Neural Network Video. Subsequent modules cover fundamental architectural elements, including 9.104 Layers and 9.106 Models: networks of layers.

The practical understanding is deepened through dedicated assignments, such as the post-video quizzes for Layers and Models, and by covering the crucial role of 9.108 Loss functions and optimizers. Furthermore, the course includes high-level discussions on complex topics, such as 9.110 The risks of AI and ASI.

The program continues with extended practical sessions in Weeks 16, 17, and 18, reinforcing the application of neural networks. The course concludes by revisiting the foundational principles of machine learning in Weeks 19 and 20, providing a holistic review of the entire domain.

---

## 05_9.108_Loss_functions_and_optimizers_keys_to_configuring_the_learning_process_Video_1_min

# 9.108 Loss functions and optimizers: keys to configuring the learning process
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/W8n5d/9-108-loss-functions-and-optimizers-keys-to-configuring-the-learning-process

The training of neural networks involves significant arbitrary design choices regarding structure and methodology. Neural networks possess arbitrary model architecture, meaning the depth, size of individual layers, and layer activations can be chosen freely. Furthermore, the overall training scheme itself is subject to arbitrary selection rather than determined by the system. Critical components like the loss function and the optimizer are chosen by the user rather than being calculated automatically. Parameters that dictate the training process, such as the SGD learning rate and the network depth, are not learned by the model. Instead, these critical parameters must be manually tuned by humans, although automatic tuning methods are acknowledged as a future possibility. These user-selected, controlling parameters are formally defined as hyperparameters. The choice of the appropriate loss function is critically important for model performance. Standard loss functions exist for common machine learning problems. Categorical cross entropy is a common and appropriate choice for numerous classification tasks. For regression problems, Mean Squared Error is frequently employed as the standard loss function. Regarding optimization, TensorFlow.keras provides options for optimizers, which are predominantly variations of SGD. Despite this, the framework maintains versatility to accommodate non-gradient optimization techniques. Users can implement methods such as genetic algorithms and swarm optimization, provided the necessary code is written. The accompanying curriculum outlines a comprehensive study spanning several weeks. The initial topics focus on foundational machine learning concepts in Weeks 1 and 2. The program progresses into specialized fields, beginning with Classification in Weeks 3 and 4. Following classification, the curriculum covers Regression in Weeks 5 and 6. Week 7 is dedicated to crucial Model Evaluation and improvement techniques. Week 8 introduces Probabilistic classification methods.

The study then shifts to unsupervised learning, covered across Weeks 9 and 10. The deep learning module begins in Week 11, focusing on Neural networks and deep learning concepts. The core mathematical underpinnings of these networks are thoroughly explored in Weeks 12, 13, and 14. Specific practical learning modules are provided, such as 9.101 Introduction to Keras and 9.108 Loss functions and optimizers: keys to configuring the learning process. The curriculum structure remains rigorous, continuing with more applications and fundamentals through Weeks 15 through 20.

---

