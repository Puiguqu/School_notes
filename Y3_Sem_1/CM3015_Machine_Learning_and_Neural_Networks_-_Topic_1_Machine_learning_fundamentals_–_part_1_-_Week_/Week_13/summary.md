# Week 13 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_8.301_Tensor_operations_Reading_1h

# 8.301 Tensor operations
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/GChPn/8-301-tensor-operations

This reading explores the fundamental operational mechanics that constitute a functioning neural network. Moving past abstract, high-level conceptual explanations, the focus is on how tensors are precisely manipulated by a series of core operations. These core operations are the foundational engine underpinning the entire model's behavior and functionality. Although these fundamental concepts derive directly from principles in linear algebra, they are presented in a practical and accessible manner. The material bypasses formal mathematical notation, opting instead for short, practical examples using Python and the NumPy library. This instructional approach is specifically designed to facilitate understanding even for readers who lack a strong background in advanced mathematics. By focusing heavily on how these tensor operations are implemented within actual code, the text builds a deep intuitive grasp of data transformation. The central objective is to show how neural networks process and transform input data through these low-level manipulations. Readers are directed to reference Chollet and Watson (2025), specifically Section 2.3, titled 'The gears of neural networks: Tensor operations'. For comprehensive access to the full content, users should consult the section titled '1.003 How to access Chollet, F. and M. Watson (2025) Deep Learning with Python, Third Edition, Manning Publications ebook'.

---

## 02_8.302_Tensor_operations_Video_1_min

# 8.302 Tensor operations
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/XxUhL/8-302-tensor-operations

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 03_8.304_Element-wise_operations_Video_1_min

# 8.304 Element-wise operations
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/OFkXC/8-304-element-wise-operations

The instructional material provides a detailed overview of machine learning concepts, starting with fundamental vector arithmetic and progressing through advanced neural network mathematics. The initial concepts center on element-wise operations applied to vectors and functions. Element-wise addition and general element-wise arithmetic dictate that each element in the vector is treated independently. Similarly, element-wise function application means the designated function is applied individually to every element within the vector.

A key example provided is the ReLU function application on a vector. The function must be applied to each element of the input vector, necessitating a copy of the original vector. For instance, calculating the ReLU of the vector $[-2, 3]$ results in the vector $[0, 3]$. This clearly demonstrates the principle that the vector is returned after the element-wise function application.

The curriculum outline spans approximately 20 weeks, mapping out the systematic study of machine learning. The early phases cover the basics, including Machine Learning fundamentals in Week 1 and Week 2. Classification techniques are introduced in Week 3 and Week 4. Following this, Week 5 and Week 6 focus on Regression methods. Week 7 is dedicated to the critical concept of Model evaluation and improvement.

The learning progression then moves to more complex paradigms, covering Probabilistic classification in Week 8. Weeks 9 and 10 are dedicated to the study of Unsupervised learning. A significant shift occurs in Week 11 with the introduction of Neural networks and deep learning. The deep mathematical grounding of these networks is addressed in Weeks 12, 13, and 14.

A focused module on the mathematical building blocks, specifically starting around section 8.301, details Tensor operations. This section includes specific lessons on Tensor operations (8.302), post-video quizzes (8.303), and element-wise operations (8.304). Detailed components include post-video quizzes for these modules (8.305).

Further mathematical topics cover Broadcasting (8.306), which involves a 2-minute video segment. Tensor dot product is analyzed in lesson 8.308, followed by its associated quiz (8.309). Tensor reshaping is covered in lesson 8.310 and its accompanying quiz (8.311).

The geometric interpretation of tensor operations is presented in lesson 8.312, a three-minute video. The entire curriculum incorporates practical assignments, as evidenced by the inclusion of post-video quizzes for several technical sections. Finally, Week 13 includes a special discussion prompt regarding "Uncrumplings." Weeks 15 through 18 delve into practical implementation, titled "Getting started with neural networks." The course concludes by revisiting the "Fundamentals of machine learning" in Weeks 19 and 20, providing a comprehensive review of the entire scope.

---

## 04_8.306_Broadcasting_Video_2_min

# 8.306 Broadcasting
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/55upo/8-306-broadcasting

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 05_8.308_Tensor_dot_Video_1_min

# 8.308 Tensor dot
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/lXJ74/8-308-tensor-dot

The core focus of the provided material details the mathematical foundation of neural network layers using tensor operations. The dot operation is fundamentally defined as the tensor analog of the traditional dot product. A specific calculation demonstrated is the tensor dot product between factors $(2 \ 3)$ and $(-1 \ 2)$, yielding the result 4 through the calculation $(-2 + 3 \times 2)$. Furthermore, matrix-vector multiplication is identified as a specific instance of general matrix multiplication. The structure of a single layer within a Multilayer Neural Network (MNS) was examined using the transformation $\text{relu}(\text{dot}(W, X) + B)$. Technically, the weight matrix $W$ is specified as a rank 2 tensor with dimensions $(512, 784)$. The input vector $X$ is a rank 1 tensor with dimensions $(784,)$. The bias vector $B$ is a tensor with dimensions $(512,)$.

The computation of $\text{Dot}(W, X)$ results in a tensor of shape $(512,)$. Specifically, the $i$-th element of $\text{dot}(W, X)$ is determined by summing the product of $w_{ij}$ and $x_j$ across the dimensions. This resulting dot product tensor is then added element-wise to the bias vector $B$, which is possible because they share the identical shape $(512,)$. The final step involves applying the ReLU activation function element-wise to the sum $\text{dot}(W, X) + B$. This analysis reveals that the layer transformation $\text{relu}( (W \cdot X) + B)$ is merely a composition of elementary tensor operations.

The accompanying course structure outlines a comprehensive curriculum on machine learning fundamentals. Week 1 introduces Machine Learning fundamentals – part 1, followed by Week 2 covering Machine Learning fundamentals labs. Weeks 3 and 4 focus on the topic of Classification. Weeks 5 and 6 are dedicated to the topic of Regression. Week 7 covers Model evaluation and improvement, followed by Week 8 on Probabilistic classification. Weeks 9 and 10 detail Unsupervised learning.

The later curriculum dives deep into neural networks, starting in Week 11 with Neural networks and deep learning. Weeks 12 and 13 provide an in-depth look at the Mathematical building blocks of neural networks, specifically focusing on Tensor operations (8.301 and 8.302). Practical learning includes quizzes on Tensor operations (8.303) and Element-wise operations (8.305). Other detailed topics include Broadcasting (8.306), Tensor dot (8.308), and Tensor reshaping (8.310). The curriculum also includes sections on the Geometric interpretation of tensor operations (8.312) and a discussion prompt on Uncrumplings (8.314). Weeks 14 through 18 progressively build upon the foundational knowledge by continuing the study of getting started with neural networks. The course concludes with Week 19 and Week 20, revisiting Fundamentals of machine learning (Topic 10).

---

## 06_8.310_Tensor_reshaping_Video_1_min

# 8.310 Tensor reshaping
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/up4Fq/8-310-tensor-reshaping

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 07_8.312_Geometric_interpretation_of_tensor_operations_Video_3_min

# 8.312 Geometric interpretation of tensor operations
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/rQXHU/8-312-geometric-interpretation-of-tensor-operations

The text provides an advanced conceptual overview of neural network layers, focusing on the geometric and mathematical underpinnings of transformations. The foundation begins with the understanding that tensor elements can be interpreted as coordinates defining a high-dimensional geometric object. A single neural network layer implements a transformation defined by the function $f(W\cdot x + b)$.

The initial component, $W\cdot x$, represents a linear transformation of the input data. Mathematically, a function is linear if $f(x+y) = f(x) + f(y)$ and if $f(a \cdot x) = a \cdot f(x)$ for any scalar $a$ and vectors $x$ and $y$. Rotations, for instance, constitute a classic example of a linear function.

This linearity has significant geometric implications; sequential rotations (e.g., a $60^\circ$ rotation followed by a $30^\circ$ rotation) are equivalent to a single rotation by the sum of the angles ($90^\circ$).

However, when the bias term $b$ is introduced, the transformation $W\cdot x + b$ ceases to be linear, unless $b$ is zero. Instead, $W\cdot x + b$ is defined as an affine transformation, which is fundamentally a linear transformation followed by a translation.

Geometrically, this means the input object (like a rotated square example) undergoes both rotation and translation (e.g., translated by one unit right and one-tenth unit down).

The critical concept distinguishing a standard neural network layer is the subsequent application of a non-linear function $f$ to the affine transformation $W\cdot x + b$. Applying this non-linear function introduces distortions to the object.

The Rectified Linear Unit (ReLU) function serves as an example of this non-linear activation applied both before and after the transformations.

In summation, every layer in a neural network executes a non-linear data transformation described by $f(W\cdot x + b)$. This process leverages the combination of affine transformation and non-linear activation.

Collectively, a neural network, operating as a series of chained activations and affine transformations, implements a complex transformation on the input data, which exists as a high-dimensional geometric object. This overarching network function is composed of many simpler, sequential non-linear transformations. The network's capability is to unfold complex data structures—such as a paper sheet crumpled into a 1,000-dimensional ball—into something simple and meaningful.

The curriculum context supports this deep dive, covering topics from Week 1 (Machine Learning Fundamentals) through Week 13, including modules specifically dedicated to Tensor operations, such as $8.301$ (Tensor operations Reading) and $8.312$ (Geometric interpretation of tensor operations). These operations form the core mathematical building blocks of neural networks discussed in Week 12 and Week 13.

---

