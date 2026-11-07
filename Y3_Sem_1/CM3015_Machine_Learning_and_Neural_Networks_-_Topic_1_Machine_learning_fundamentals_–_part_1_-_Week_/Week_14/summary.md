# Week 14 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_8.401_The_engine_of_neural_networks_Reading_1h

# 8.401 The engine of neural networks
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/fMSGW/8-401-the-engine-of-neural-networks

The fundamental mechanism enabling neural networks to learn is gradient-based optimization. This process relies on core technical concepts, specifically derivatives, gradients, and Stochastic Gradient Descent (SGD). These foundational elements are subsequently combined through backpropagation to effectively update a model’s parameters. By understanding these concepts, one grasps how neural networks achieve learning through a series of small, incremental improvements derived from data. To explore this mechanism, readers should consult Chollet and Watson (2025). Specifically, the required reading includes Sections 2.4.1–2.4.4, 2.5.1–2.5.4, and 2.6. For comprehensive access details, the full title is *Deep Learning with Python, Third Edition*. This material is published by Manning Publications and is accessible via the reference code 1.003.

---

## 02_8.402_Gradient-based_optimisation_Video_3_min

# 8.402 Gradient-based optimisation
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/9mJAT/8-402-gradient-based-optimisation

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 03_8.404_What's_a_derivative_Video_1_min

# 8.404 What's a derivative?
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/xcnmO/8-404-whats-a-derivative

The core concepts presented revolve around the fundamentals of mathematical calculus and their application in machine learning, specifically gradient-based optimization. A smooth function, denoted as $f$, is defined as one without abrupt changes. This property allows the function to be accurately approximated near any given point $x$. The approximation formula posits that $f(x + \Delta x)$ can be approximated as $f(x + m \cdot \Delta x)$. In this approximation, $\Delta x$ represents a small step, and $m$ is specifically the gradient of the tangent at point $x$.

The gradient of differentiable functions is calculable using simple rules. For instance, the gradient function of $f(x) = x^n$ is the derivative, written as $f'(x)$. This derivative function is mathematically defined as $f'(x) = n \cdot x^{n-1}$. To illustrate, if $f(x) = x^2$, the derived function is $f'(x) = 2x$. Consequently, the gradient at $x=3$ for this function is $6$.

In the context of machine learning implementation, specialized libraries are used to calculate these necessary gradients. Tensorflow, for example, utilizes a mechanism called "gradient tape." This functionality allows users to compute the gradient of a function given a specific point. The specific function, `Tape.gradient(function, point)`, returns the required gradient. This code snippet provided serves merely as an illustration of the automation performed by Tensorflow.

The academic structure covers these concepts extensively, beginning with fundamental machine learning principles. The curriculum includes dedicated modules on Classification (Weeks 3 & 4) and Regression (Weeks 5 & 6). Model evaluation and improvement are addressed in Week 7, followed by probabilistic classification in Week 8. Unsupervised learning is covered in Weeks 9 and 10.

The technical foundation is laid in Weeks 11 through 14, focusing on neural networks and their mathematical building blocks. A critical area of study is Gradient-based optimisation, which utilizes the derivatives calculated earlier. Specific topics within this area include Stochastic Gradient Descent (SGD) and Backpropagation. Detailed resources are provided for understanding the Derivative of a tensor operation.

The application of these complex mathematical tools is seen in the MNIST revisited section, where students are guided through a practical lab involving this data set. The overall course progresses through a structured series of video lectures, quizzes, and practice assignments. The curriculum culminates in reviewing the mathematical principles necessary for deep learning, ensuring a comprehensive understanding of the optimization engine of neural networks.

---

## 04_8.406_Derivative_of_a_tensor_operation_Video_6_min

# 8.406 Derivative of a tensor operation
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/DRPqJ/8-406-derivative-of-a-tensor-operation

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 05_8.408_Stochastic_gradient_descent_Video_4_min

# 8.408 Stochastic gradient descent
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/2OJMN/8-408-stochastic-gradient-descent

Optimizing neural networks requires minimizing a loss function, where the loss is at a minimum when its gradient with respect to weights ($w$) and biases ($b$) is zero. Calculating this gradient using standard methods is computationally prohibitive, especially given the likelihood of multiple solutions. To address this, an iterative scheme is employed that approximates the solution through small, stepwise movements. The fundamental principle involves scaling the gradient in the $w$ and $b$ directions by a small parameter called the learning rate ($\eta$). This scaled gradient is then subtracted from the current parameter values, effectively moving "down the hill" towards a minimum.

The true loss function is the combined loss over the entire training set (the batch), but even Batch Gradient Descent (BGD) is prohibitively expensive. Consequently, Stochastic Gradient Descent (SGD) is used, where the loss and gradient are calculated using small, randomly selected subsets of the training set, approximating the total loss via mini-batch loss. A simple one-dimensional loss function illustrates that multiple points, including local and global minima, can have a zero gradient.

SGD can be conceptualized as rolling a ball down a landscape, where the parameters ($w$ and $b$) are coordinates defining the ball's position. If the step sizes are too small, the ball may get trapped in a local minimum; conversely, if the step size is too large, it may never converge to a minimum. There is no way to know the optimal step size a priori because the loss landscape is unknown. TensorFlow offers several built-in optimizers, including SGD, Adagrad, and RMSprop, all implementing forms of SGD.

Many optimizers utilize momentum to actively attempt to avoid being stuck in local optimums. Momentum draws an analogy to the motion of a ball on a slope, governed by differential update rules. In this physics analogy, the total acceleration ($a$) combines the negative gradient (downward force) and an opposing friction force proportional to velocity.

The resulting algebraic update rule for velocity ($v$) is defined as: $v_{t} = \alpha v_{t-1} + \eta \cdot (-\text{Gradient})$. The parameters ($w$ and $b$) are then updated based on this velocity, treating $\Delta w$ and $\Delta b$ as the velocity components. This scheme is called momentum because the $\alpha \Delta w$ term reinforces motion in the direction of the previous change, similar to inertia.

The Momentum SGD algorithm uses $\alpha$ (the coefficient of friction, $0 \le \alpha \le 1$) and the learning rate ($\eta$) to control the parameter updates. The core idea of momentum is that it provides enough inertia to carry the parameters ($w$ and $b$) over the barrier between local and global optimums.

---

## 06_8.410_Backpropagation_Video_3_min

# 8.410 Backpropagation
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/c0E8Z/8-410-backpropagation

This curriculum provides a comprehensive 20-week progression through fundamental and advanced machine learning concepts. The initial phase begins with Machine Learning fundamentals in Week 1, transitioning into hands-on Machine Learning labs in Week 2. Weeks 3 and 4 focus specifically on the core concept of Classification. Following this, Weeks 5 and 6 delve into the techniques and intricacies of Regression analysis.

A critical shift in learning occurs in Week 7 with the dedicated topic of Model evaluation and improvement. Weeks 8 and 9 introduce specialized domains, starting with Probabilistic classification in Week 8. The curriculum then expands into the realm of Unsupervised learning during Weeks 9 and 10. The focus significantly intensifies with the introduction of Neural networks and deep learning in Week 11.

Weeks 12 through 14 provide a deep dive into the mathematical building blocks of neural networks, ensuring a robust theoretical foundation. Within this intensive section, Topic 8.4 addresses Gradient-based optimisation, which is described as the engine of neural networks. This optimization process is explored through various resources, including a 1-hour video on SGD, followed by a 3-minute video on Gradient-based optimisation. Practical understanding is reinforced by multiple practice assignments, such as the post-video quizzes on SGD and the derivative of a tensor operation.

Furthermore, foundational calculus concepts are covered via videos detailing "What's a derivative?" and its application to tensor operations. The core mechanism of neural networks is clarified through dedicated sections on Stochastic gradient descent and Backpropagation, both supported by specific video and quiz assignments. Section 8.5 provides application context, revisiting the MNIST example through both a general overview and a practical MNIST Lab.

The program culminates with the Topic 8 summary, followed by an end-of-topic quiz and a discussion prompt to synthesize learning. The final weeks continue the application of these advanced concepts, with Weeks 15 through 18 dedicating time to "Getting started with neural networks." The curriculum concludes with Weeks 19 and 20, solidifying the knowledge through a comprehensive study of Fundamentals of machine learning.

---

## 07_8.501_Looking_back_at_our_first_example_Video_2_min

# 8.501 Looking back at our first example
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/CJY13/8-501-looking-back-at-our-first-example

The provided material details the fundamentals of building and training a network to predict handwritten digits, specifically utilizing the MNIST dataset. This project serves as a foundational example in machine learning and deep learning concepts. The MNIST image dataset is explicitly partitioned into separate training and test sets. Technically, the data consists of float32 NumPy tensors. The dimensionality of the training set is $600784$, while the test set contains $100784$ samples. Before network ingestion, the raw image data undergoes vectorization and is scaled to floats, ensuring values fall between 0 and 1. The network architecture is defined as a chain composed of two dense layers. Each layer performs simple tensor operations, which conceptually represent a geometric transformation of the input data. These transformations are entirely parameterized by trainable weights and associated biases. The compilation process requires the specification of three key components: the optimizer, the loss function, and a performance monitoring metric. The training loop is configured for five total epochs. Furthermore, the training utilizes a mini-batch size set at 128 samples per iteration. The core mechanism for minimizing the loss function is mini-batch Stochastic Gradient Descent, commonly known as SGD. In this setup, weights and biases are adjusted after every mini-batch has been processed. Quantitatively, five epochs involving 128-sample batches result in a total of 2345 gradient updates. Following the training phase, the performance of the network is rigorously evaluated using the completely unseen test set. If the network proves successful in this evaluation, it can be deployed for practical applications, such as in post-office sporting rooms. The broader curriculum places this example within the context of mathematical machine learning. Dedicated modules address the mathematical building blocks, including derivatives and tensor operations. Specifically, the training heavily relies on concepts like differentiation and the chain rule. The mechanisms governing the network's tuning involve gradient-based optimization, detailed in sections like 8.4 Gradient-based optimisation (SGD). Concepts such as backpropagation are critical for implementing gradient descent. The supplementary structure highlights dedicated content for "MNIST revisited," reinforcing the practical application of these theoretical components. Overall, the material describes the complete cycle: data preparation, model construction, iterative SGD training, and final performance assessment.

---

## 08_8.503_MNIST_Video_17_min

# 8.503 MNIST
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/ScXpk/8-503-mnist

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 09_8.601_Topic_8_summary_Video_1_min

# 8.601 Topic 8 summary
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/FCP17/8-601-topic-8-summary

Machine learning (ML) is fundamentally defined as a process focused on minimizing the predictive loss of a trained model. Specifically, this learning process utilizes a neural network structure to iteratively improve its performance. Training involves presenting the neural network with numerous patches of labeled sample data. The primary objective during training is the adjustment of network parameters to reduce the discrepancy between the model's prediction and the actual target value. Technically, a neural network operates by implementing a chain of complex differential layer transformations. The crucial mechanism for determining how to adjust these parameters is the computation of the loss-parameter gradient. This gradient computation is efficiently executed via the specialized algorithm known as backpropagation. According to this optimization strategy, parameters are subsequently moved by a small, incremental step. This movement is directed precisely along the path of the negative gradient, leading to reduced loss.

The overall domain emphasizes that deep learning is a highly practical subject requiring hands-on engagement and implementation. The curriculum provides a systematic exploration of core ML topics over many weeks. Topics include Classification, which is covered in depth in Weeks 3 and 4. Regression modeling is introduced later, forming the focus of Weeks 5 and 6. Furthermore, the course structure incorporates vital techniques for assessing model effectiveness, detailed in Week 7. Week 8 delves into Probabilistic classification methods. Unsupervised learning is covered across Weeks 9 and 10.

A major deep dive focuses on the theoretical underpinnings of Week 11’s neural networks and deep learning. The subsequent weeks (12, 13, and 14) concentrate intensely on the mathematical building blocks of these neural networks. Central to these mathematical foundations is gradient-based optimization, specifically Stochastic Gradient Descent (SGD). SGD is identified as the essential "engine" driving neural network training.

The technical development of this engine includes detailed study of derivatives, specifically what a derivative is. Furthermore, the learning material covers the derivative of tensor operations, which are foundational to modern network mathematics. Stochastic gradient descent and backpropagation are presented as critical specialized components of optimization. Backpropagation provides the necessary framework to efficiently calculate the required gradients throughout the network.

A practical application section, Section 8.5, revisits the MNIST example. This provides a concrete laboratory environment for applying all learned concepts. The curriculum also dedicates time to comprehensive topic summaries and end-of-topic quizzes. In summary, the entire framework integrates theoretical concepts, rigorous mathematical derivations, and practical implementation examples like MNIST.

---

