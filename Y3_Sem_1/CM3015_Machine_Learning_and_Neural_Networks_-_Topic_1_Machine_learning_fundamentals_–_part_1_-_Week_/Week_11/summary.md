# Week 11 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_7.001_Introduction_to_part_2_of_the_course_Video_4_min

# 7.001 Introduction to part 2 of the course
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/48OYe/7-001-introduction-to-part-2-of-the-course

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 02_7.002_What_is_deep_learning_Reading_2h

# 7.002 What is deep learning?
Reading • 2h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/GJ4mu/7-002-what-is-deep-learning

In the second half of this course, we are following Chollet and Watson's Deep learning with Python very closely. A specific reading accompanies each topic and subtopic. The videos are self-contained and provide the key points of the text. You may wish to read the book after watching the videos or you can read the book first (but try not to get bogged down). Or both. Find your best learning method....

---

## 03_7.101_Artificial_intelligence_(AI),_machine_learning_(ML)_and_deep_learning_(DL_Video_2_min

# 7.101 Artificial intelligence (AI), machine learning (ML) and deep learning (DL
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/SKzNo/7-101-artificial-intelligence-ai-machine-learning-ml-and-deep-learning-dl

Artificial intelligence (AI) is fundamentally defined as mechanical thought, enabling machines to execute tasks previously considered solely human capabilities. Early in its development, AI focused on modeling thought through the manipulation of symbols, such as rearranging mathematical equations. This symbolic approach demonstrated logical calculus, exemplified by the syllogism: "If it is raining, I will get wet; it is raining, therefore, I will get wet." However, this traditional logic-based system failed miserably when confronted with tasks possessing undefinable or amorphous rules.

The conventional computational approach involves encoding specific rules, including logic and heuristics (rules of thumb), directly into a program. The program is then presented with data, and the computer processes the defined rules to announce a result. A major paradigm shift occurred in the 1990s with the advent of machine learning (ML). In the ML paradigm, rules are not hard-coded; instead, they are dynamically learned.

The ML process trains by comparing input data against a desired output response. This creates a parameterized map between the input and the target, allowing the machine to derive implicit rules internally. This fundamental change made complex tasks, such as discerning dogs from cats in images—which was impossible through hard coding—now feasible.

Deep learning (DL) represents a more recent and supercharged advancement building upon machine learning. DL is implemented specifically through the use of neural networks. Both ML and DL rely heavily on vast and enormous datasets to function effectively. Crucially, these methods currently lack a firm mathematical base and emphasize a hands-on, practical approach. The ultimate objective of ML and DL remains the search for meaningful transformations of raw data.

The study of these concepts progresses through several defined topics, beginning with fundamental Machine Learning concepts. Key applications include Classification, which is explored in Weeks 3 and 4, and Regression, covered in Weeks 5 and 6. Model evaluation and improvement are tackled in Week 7, alongside Probabilistic classification in Week 8.

The course delves into Unsupervised learning in Weeks 9 and 10, a technique used to find patterns without predefined labels. The deep dive into advanced network structures and methods begins with Neural networks and Deep learning in Week 11. The subsequent weeks systematically build the theoretical foundation.

Weeks 12, 13, and 14 are dedicated to understanding the mathematical building blocks of neural networks. Weeks 15 through 18 focus on practical application, detailing how to get started with neural networks. The curriculum concludes with foundational deep learning topics, including the fundamental principles of machine learning (Weeks 19 and 20). The overall subject tracks the progression from symbolic logic to complex, data-driven, neural network architectures.

---

## 04_7.103_Learning_representations_Video_3_min

# 7.103 Learning representations
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/0Sbl4/7-103-learning-representations

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 05_7.105_The_'deep'_in_deep_learning_Video_4_min

# 7.105 The 'deep' in deep learning
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/LJ5mV/7-105-the-deep-in-deep-learning

Deep learning models operate by applying successive transformations to input data. Initially, 2D red/black vectors are subjected to a sequence of transformations. This sequence includes a linear transformation, followed by a rotation, and finally a nonlinear projection. Each of these specific transformations is performed by a dedicated computational layer. A model is defined as "deep" if it incorporates three or more successive computational layers. Deep learning models fundamentally achieve their function through these multiple transformations.

These statistically deep models are almost invariably implemented as neural networks. Neural networks (or Artificial Neural Networks) were initially conceived as crude analogies to biological neural networks found in the brain. However, it is critical to note that current neural networks do not emulate brain function; they neither think nor learn in the same way that biological brains do. Functionally, we regard these networks more prosaically as a stack sequence of layered computational processes.

To illustrate this, consider training a network to recognize handwritten digits. The input starts as a small 28 by 28 pixel image, each representing a digit. This image must first be vectorized by placing every pixel value into a 1D array, which results in 784 elements. The darker a pixel, the larger its corresponding value in the vector. This vectorized sample is presented to the network's first layer.

Within the network, data is transformed as it flows forward from one layer to the next. The first layer transforms the original 784-element input into a 512-element vector. This resulting representation is often smaller than the original input vector, unless the data is exceptionally sparse. The 512-element vector then feeds into a second transformation layer. This second layer ultimately generates a 10-element vector of floating-point values. These output values represent the classification of the input, where each element corresponds to a specific digit (zero through nine). The magnitude of these values quantifies the network's confidence in its prediction; for instance, a high value in the eighth slot suggests a confident prediction of the digit '7'.

This entire process constitutes the operation of a neural network, and the training component is what allows it to learn. The course structure provides comprehensive coverage of these concepts. Key topics include Machine Learning fundamentals, Classification, Regression, and Model Evaluation (Week 1-9). Specifically, Topic 7 focuses on Neural Networks and Deep Learning. This module includes defining AI, ML, and DL, and detailing the concept of "The 'deep' in deep learning" (7.105). Further deep dives are promised in subsequent weeks, specifically covering the mathematical building blocks of neural networks.

---

## 06_7.107_Understanding_how_DL_works_in_three_figures_Video_2_min

# 7.107 Understanding how DL works in three figures
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/4rAEU/7-107-understanding-how-dl-works-in-three-figures

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 07_7.109_Achievements._Short-term_hype._The_promise_of_AI_Video_4_min

# 7.109 Achievements. Short-term hype. The promise of AI
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/yg4M6/7-109-achievements-short-term-hype-the-promise-of-ai

Deep learning has experienced an ascendant period starting in the early 2010s. This technology addresses problems that machines previously found exceptionally difficult to solve. Its breakthrough progress was fundamentally driven by the convergence of big data, GPU technology, and improved algorithms. Deep learning has generated significant excitement, hope, and some public concern regarding its rapid advancement.

Currently, practical tasks are being accomplished at a near human level. These capabilities include image classification, speech recognition, handwriting transcription, and autonomous driving systems. Other functional areas, such as machine translation, text-to-speech, ad targeting, and search result optimization, have also seen marked improvements. However, fundamental abilities like believable dialogue, complete natural language understanding, and general intelligence remain beyond current reach.

The history of AI demonstrates significant volatility. The initial era of symbolic AI in the 1960s was followed by the first AI winter in the 1970s, marked by disappointing results and reduced funding. An AI revival occurred in the 1980s through the development of expert systems. This led to a second AI winter during the 1990s.

The current boom marks the second coming of neural networks, which now manifests as deep learning in the 2010s. Deep learning technology quickly diffused, leading to media over-reporting of AI's omnipresence. Although some fatalistic views exist regarding the rise of the algorithm, algorithms are both autonomous and moral in potential. Many significant deep learning developments are still awaiting full deployment.

Despite potential stalls in research, there is a continued diffusion of AI into everyday life. New specialized applications are emerging, notably assisting human scientists, climatologists, and accelerating drug discovery processes. This course moves from viewing neural networks at a distance to engaging in hands-on engineering work. The practical application requires using TensorFlow to build, train, and evaluate a neural network model.

The curriculum establishes a structured learning path for mastery. Early topics cover foundational concepts, including Classification (Weeks 3-4) and Regression (Weeks 5-6). Model evaluation and improvement are studied in Week 7, followed by Probabilistic classification in Week 8. Unsupervised learning topics are addressed in Weeks 9 and 10. The study of Neural networks and Deep Learning begins in Week 11.

Detailed instruction on deep learning (Topic 7) covers concepts like what deep learning is (7.1.2) and how it works in three figures (7.1.7). Subsequent topics focus on the mathematical building blocks of neural networks spanning Weeks 12, 13, and 14. Practical implementation begins with getting started with neural networks across Weeks 15 through 18. Finally, the course covers the general Fundamentals of Machine Learning in Weeks 19 and 20. (Note: No specific mathematical formulae or explicit hyperlinked URLs were provided in the source text.)

---

