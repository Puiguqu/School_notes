# Week 20 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_10.501_The_universal_workflow_of_machine_learning_Reading_1h

# 10.501 The universal workflow of machine learning
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/axmNz/10-501-the-universal-workflow-of-machine-learning

This reading introduces the universal workflow of machine learning, detailing the structured process required to build effective models. The workflow encompasses key stages, starting from defining the problem and subsequently preparing the necessary data. Following preparation, the process continues through model training, rigorous evaluation, and iterative model refinement. These steps collectively form a systematic and repeatable practical framework for tackling machine learning tasks. For a detailed understanding, readers are directed to Chollet and Watson (2025). Specifically, the required sections are 6.1.1–6.1.4 and 6.2.1–6.2.5 of the source material. Full access details can be found by referencing '1.003 How to access Chollet, F. and M. Watson (2025) Deep Learning with Python, Third Edition, Manning Publications ebook'. The core concept presented is that these stages fit together into a cohesive, structured machine learning process.

---

## 02_10.502_Defining_the_problem_Video_1_min

# 10.502 Defining the problem
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/0zKMJ/10-502-defining-the-problem

This curriculum provides an extensive 20-week journey through machine learning, beginning with introductory fundamentals. Week 1 and 2 establish the basic machine learning fundamentals, followed by dedicated labs to solidify practical understanding. The core study then progresses through critical supervised learning techniques, starting with Classification in Weeks 3 and 4. Following classification, the module explores Regression, covering both basic principles and advanced applications across Weeks 5 and 6.

Model evaluation and improvement constitutes a significant thematic focus in Week 7, ensuring students learn how to critically assess model performance. Week 8 delves into Probabilistic classification, introducing statistical rigor into prediction tasks. The curriculum then transitions into the domain of Unsupervised learning, which is examined in detail across Weeks 9 and 10.

The study subsequently shifts focus to Neural networks and Deep learning, a major component covered in Week 11. Weeks 12, 13, and 14 are dedicated entirely to mastering the mathematical building blocks of neural networks, establishing the technical foundations. Building upon this mathematical groundwork, Weeks 15 through 18 provide practical instruction on "Getting started with neural networks."

The final major topical sections are Fundamentals of machine learning, which are covered in Weeks 19 and 20, synthesizing all learned concepts. A detailed exploration of the Universal Workflow is provided in Topic 10.5, which is structured into 17 interconnected steps. This workflow begins with 10.501, outlining the universal process of machine learning.

The methodological steps start with defining the problem (10.502), followed by choosing a measure of success (10.504). Crucially, students learn to decide upon an evaluation protocol (10.506) and must master the process of preparing their data (10.508). The development phase requires creating a model that performs better than a baseline (10.510), and subsequently scaling up the model (10.512).

Advanced development stages include regularizing the model and tuning hyperparameters (10.514) to ensure robustness and performance optimization. The practical application of this knowledge culminates in the 30-minute Universal Machine Learning Workflow Lab (10.516). The module concludes with a summary (10.601) and a comprehensive end-of-topic quiz.

The overall term requires a major End-of-term coursework submission, a Graded Assignment lasting two hours. Furthermore, the course includes an ungraded End-of-Module Survey via EvaSys.

---

## 03_10.504_Choosing_a_measure_of_success_Video_38_sec

# 10.504 Choosing a measure of success
Video • 38 sec - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/nMXpt/10-504-choosing-a-measure-of-success

This educational material outlines a comprehensive study of Machine Learning fundamentals, covering advanced concepts from Week 1 through Week 20. The core technical principles emphasize that the choice of the measure of success—be it accuracy or precision—is paramount in model development. This critical measure directly dictates the subsequent choice of the appropriate loss function for training. Furthermore, researchers may be required to design a custom loss function if standard options are inadequate for the specific task. A foundational technical requirement for utilizing backpropagation is the absolute necessity of function smoothness.

The curriculum provides a structured progression through various machine learning domains. Initial weeks cover general machine learning fundamentals (Weeks 1 and 2). These concepts are then applied to specialized tasks, commencing with Classification in Weeks 3 and 4. The material proceeds to cover Regression techniques during Weeks 5 and 6. Week 7 is dedicated to Model evaluation and improvement protocols. Probabilistic classification is introduced in Week 8, followed by a detailed exploration of Unsupervised learning in Weeks 9 and 10.

The course dedicates a substantial segment to Neural Networks and Deep Learning, spanning Weeks 11 through 18. The mathematical underpinnings of these complex architectures are rigorously addressed in Weeks 12, 13, and 14. Later modules revisit fundamentals in Weeks 19 and 20, ensuring a holistic understanding of the field.

A detailed operational framework, "The Universal Machine Learning Workflow," is presented in Section 10.5, illustrating the iterative nature of ML projects. This workflow begins with the crucial step of Defining the problem (10.502). Next, the developer must select a precise measure of success (10.504), followed by Deciding an evaluation protocol (10.506). Data preparation is achieved in the subsequent steps (10.508).

The model development phase (10.510) requires creating a model that demonstrably surpasses the established baseline performance. Critical engineering steps include Scaling up the successful model (10.512) and, finally, Regularising the model while tuning its hyperparameters (10.514). The entire Universal ML Workflow Lab is designed to take 30 minutes to complete. The module concludes by discussing the inherent Limitations of the paradigm (10.517).

Assessment components are diverse and rigorous, including end-of-topic quizzes and practice assignments. The term also mandates a graded assignment, allotted two hours for completion. Additionally, an ungraded End-of-Module Survey is scheduled for one hour. This structure ensures students not only grasp the technical concepts but also master the complete lifecycle of a machine learning project.

---

## 04_10.506_Deciding_an_evaluation_protocol_Video_1_min

# 10.506 Deciding an evaluation protocol
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/2MuXp/10-506-deciding-an-evaluation-protocol

### Week 1 Topic 1: Machine learning fundamentals – part 1 ### Week 2 Topic 1: Machine Learning fundamentals labs ### Week 3 Topic 2: Classification ### Week 4 Topic 2: Classification (cont.) ### Week 5 Topic 3: Regression ### Week 6 Topic 3: Regression (cont.) ### Week 7 Topic 4: Model evaluation and improvement ### Week 8 Topic 5: Probabilistic classification ### Week 9 Topic 6: Unsupervised learning ### Week 10 Topic 6: Unsupervised learning (cont.)...

---

## 05_10.508_Preparing_your_data_Video_44_sec

# 10.508 Preparing your data
Video • 44 sec - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/5Lg72/10-508-preparing-your-data

This summary integrates the course structure, the overarching machine learning workflow, and the specific technical requirements for data preparation.

1. The course curriculum covers comprehensive machine learning fundamentals, spanning from Week 1 through Week 20.
2. Early topics focus on foundational concepts, including machine learning fundamentals in Week 1 and Week 2.
3. Specific learning tracks are dedicated to Classification during Weeks 3 and 4, and Regression during Weeks 5 and 6.
4. Model evaluation and improvement constitute a key topic in Week 7.
5. Probabilistic classification is explored in Week 8, followed by Unsupervised Learning in Weeks 9 and 10.
6. The material then progresses into advanced areas, including Neural Networks and Deep Learning (Weeks 11 through 18).
7. A substantial focus is dedicated to understanding the mathematical building blocks of neural networks across Weeks 12, 13, and 14.
8. Weeks 19 and 20 reinforce the Fundamentals of machine learning, ensuring a thorough grasp of core concepts.
9. The material details a universal workflow for machine learning, outlined in Section 10.5.
10. This universal workflow begins with defining the problem itself (Sections 10.502 and 10.503).
11. Following problem definition, the next critical step involves choosing a measure of success (Sections 10.504 and 10.505).
12. A subsequent phase requires deciding upon a formal evaluation protocol (Sections 10.506 and 10.507).
13. The core execution phase involves meticulously preparing the data (Sections 10.508 and 10.509).
14. The workflow mandates developing a model that demonstrably performs better than a baseline (Sections 10.510 and 10.511).
15. This is followed by scaling up the model (Sections 10.512 and 10.513).
16. Essential optimization involves the rigorous process of regularizing the model and tuning hyperparameters (Sections 10.514 and 10.515).
17. Practical application of these principles is covered in the Universal Machine Learning Workflow Lab (Section 10.516).
18. Regarding data preparation, all data must be processed into a form recognizable by the intended network.
19. Technically, neural networks and intended networks require input in the form of tensors.
20. Data values are typically scaled to specific ranges, either [-1, 1] or [0, 1].
21. It is crucial to normalize heterogeneous data to ensure consistency across features.
22. Feature engineering is specifically recommended and required, particularly when tackling data-limited problems.
23. The accompanying interactive materials provide navigation aids, including shortcuts like CTRL + S to save notes.
24. Accessibility features are noted, allowing screen readers to substitute arrow key functions with H, J, K, and L keys.
25. The overall module structure culminates in a graded assignment and an End-of-Module Survey.

---

## 06_10.510_Developing_a_model_that_does_better_than_the_baseline_Video_1_min

# 10.510 Developing a model that does better than the baseline
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/lkS9A/10-510-developing-a-model-that-does-better-than-the-baseline

This comprehensive course structure spans 20 weeks, building from foundational Machine Learning concepts and labs into advanced specialized topics. Early weeks establish the core fundamentals, covering basic Machine Learning topics in Week 1 and Week 2. The curriculum then shifts into supervised learning, dedicating Weeks 3 and 4 to the crucial concept of Classification. Following classification, Weeks 5 and 6 focus on Regression, introducing predictive modeling techniques.

A significant emphasis is placed on Model Evaluation and improvement in Week 7. Week 8 introduces Probabilistic Classification, providing deeper mathematical insight into prediction methods. The course subsequently branches into unsupervised learning, dedicating Weeks 9 and 10 to exploring how models identify patterns without labeled data.

A major segment of the curriculum is dedicated to modern deep learning, beginning in Week 11 with Neural Networks. Weeks 12, 13, and 14 delve into the complex mathematical building blocks of these neural networks. The deep dive continues with practical implementation in Weeks 15 through 18, focusing on "Getting started with neural networks." Weeks 19 and 20 conclude by summarizing the Fundamentals of Machine Learning paradigm.

Section 10.5 details the universal workflow of machine learning, starting with 10.501 "The universal workflow of machine learning" (1 hour duration). This process begins with 10.502 "Defining the problem," followed by 10.504 "Choosing a measure of success" (38 seconds video). Next, the protocol involves 10.506 "Deciding an evaluation protocol" (1 minute video).

Data handling is critical, starting with 10.508 "Preparing your data" (44 seconds video). The core modeling stage is 10.510 "Developing a model that does better than the baseline" (1 minute video). This initial development is followed by the crucial steps of 10.512 "Scaling up" (1 minute video) and 10.514 "Regularising your model and tuning hyperparameters" (1 minute video).

The workflow culminates with an exploration of the 10.517 "Limitations of the paradigm" (15 minutes dialogue). Reinforcement and application are provided through multiple practice assignments and the dedicated 10.516 "The Universal Machine Learning Workflow Lab" (30 minutes). The course concludes with the 10.6 "Topic 10 summary" video, followed by an End-of-topic quiz and the mandatory End-of-term coursework submission.

---

## 07_10.512_Scaling_up_Video_1_min

# 10.512 Scaling up
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/YGNQy/10-512-scaling-up

The comprehensive documentation outlines both the practical principles of machine learning model development and the structured curriculum for mastering the field.

The technical discussion emphasizes that statistical power is a necessary, yet weak, criterion when evaluating a model. A critical consideration is determining if a model possesses sufficient capacity, specifically enough layers and parameters, to adequately model the problem at hand. For instance, a network exhibiting statistical power on the IMDB dataset might achieve 55 percent accuracy, yet still constitute a poor solution overall.

The core process of developing a robust model involves iteratively building progressively larger models until the phenomenon of overfitting is observed. This scaling up process may require extending the number of training epochs. Crucial monitoring demands the tracking of both training and validation loss, alongside the metrics of interest for both sets. The objective is to locate the optimal boundary between underfitting and overfitting, ensuring the model has neither too little nor too much capacity.

This iterative refinement is formally integrated into the universal machine learning workflow described in Section 10.5. This workflow commences with 10.502 Defining the problem. Following this, the next steps involve 10.504 Choosing a measure of success and 10.506 Deciding an evaluation protocol. Subsequent stages require meticulous data preparation, as outlined in 10.508.

The practical application begins with 10.510 Developing a model that performs better than a predetermined baseline. The workflow then proceeds through 10.512 Scaling up and 10.514 Regularizing the model and tuning hyperparameters. Section 10.517 addresses the inherent limitations of the entire machine learning paradigm.

The curriculum structure provides a detailed roadmap for learning these fundamentals. Week 1 establishes machine learning fundamentals, while Weeks 2 through 6 cover Classification and Regression, respectively. Week 7 focuses specifically on Model evaluation and improvement techniques.

The training progresses into advanced modeling in subsequent weeks. Week 8 introduces Probabilistic classification, transitioning to Weeks 9 and 10, which explore Unsupervised learning. Weeks 11 through 16 are dedicated to Neural networks and Deep learning concepts.

Detailed theoretical understanding is built via Weeks 12, 13, and 14, which cover The mathematical building blocks of neural networks. Weeks 15 through 18 continue the foundational learning through Getting started with neural networks. Finally, Weeks 19 and 20 consolidate these principles in Fundamentals of machine learning.

The comprehensive course structure culminates in a Topic 10 Summary (10.6), followed by required assessments. These assessments include a Practice Assignment for the summary and the formal End-of-term coursework submission. The learning experience is rounded out by the Ungraded End-of-Module Survey.

---

## 08_10.514_Regularising_your_model_and_tuning_hyperparameters_Video_1_min

# 10.514 Regularising your model and tuning hyperparameters
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/gLToJ/10-514-regularising-your-model-and-tuning-hyperparameters

This module provides a comprehensive curriculum covering foundational and advanced machine learning concepts across multiple weeks. The initial weeks establish the Machine Learning fundamentals (Week 1 to Week 2), followed by a deep dive into core learning paradigms. Classification is introduced in Week 3 and continued in Week 4, serving as a primary focus for early modeling techniques. Regression modeling is covered in Week 5 and Week 6, focusing on predicting continuous outcomes.

Week 7 addresses crucial Model evaluation and improvement protocols, ensuring rigorous assessment of developed models. Subsequently, Week 8 focuses on Probabilistic classification methods, while Weeks 9 and 10 detail the principles of Unsupervised learning. The curriculum then shifts significantly into advanced architecture by introducing Neural networks and deep learning in Week 11. The technical underpinnings of these systems are explored extensively from Week 12 through Week 14, detailing the mathematical building blocks. Weeks 15 through 18 continue the application and practical implementation of neural networks.

Finally, Weeks 19 and 20 summarize the core Fundamentals of machine learning, leading into the structured workflow detailed in Section 10.5. This section outlines the universal workflow of machine learning, beginning with the foundational step of Defining the problem (10.502). The process continues by Choosing a measure of success (10.504) and subsequently Deciding an evaluation protocol (10.506).

A critical phase involves Preparing your data (10.508), which is followed by the central task of Developing a model that does better than the baseline (10.510). This is followed by the complex phase of Scaling up (10.512) to manage increasing data volume and complexity. A key element of robust design is Regularising your model and tuning hyperparameters (10.514), which prevents overfitting and optimizes model performance. The entire process culminates in examining the Limitations of the paradigm (10.517). Practical learning is cemented through various practice assignments, including the Universal Machine Learning Workflow Lab (10.516). The module concludes with a summary of Topic 10 (10.601) and an end-of-topic quiz.

---

## 09_10.601_Topic_10_summary_Video_1_min

# 10.601 Topic 10 summary
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/qk9z0/10-601-topic-10-summary

This summary comprehensively details the universal machine learning workflow and outlines the progressive curriculum structure of the course material.

The core technical finding is presented as a comprehensive seven-step deep learning workflow. First, the process necessitates defining the problem and collecting necessary samples and labels. Second, a specific success criterion and crucial monitoring metrics must be chosen to track performance. Third, the practitioner must select an appropriate validation protocol for model testing. Fourth, thorough data preparation is required before modeling begins. Fifth, the initial development phase involves creating a first model specifically designed to be underfitting, while maintaining statistical power. Sixth, the model is subsequently developed into a larger, more complex version, resulting in an overfitting state. Finally, the seventh step is vital: regularizing the overfitting model and tuning its hyperparameters based on performance observed on the designated validation data. This entire workflow operates cyclically, requiring continuous retraining with the entire training set and subsequent evaluation on an unseen test set.

The supplementary content establishes a detailed academic progression across 20 weeks. The initial phase covers Machine Learning Fundamentals, starting with Week 1 and Week 2 Labs. Weeks 3 and 4 focus specifically on the topic of Classification. The curriculum then moves into Regression during Weeks 5 and 6. Model evaluation and improvement are covered in depth during Week 7. Subsequent weeks introduce advanced topics, beginning with Probabilistic Classification in Week 8. Weeks 9 and 10 are dedicated to Unsupervised Learning.

The most advanced topics concern neural networks and deep learning, commencing in Week 11. Weeks 12, 13, and 14 delve into The mathematical building blocks of neural networks. The practical application of deep learning begins in Week 15 and continues through Week 18. Weeks 19 and 20 provide a final review of Fundamentals of Machine Learning.

The structured learning environment includes defined sub-sections, such as Topic 10.5: The workflow, which details specific procedural lessons. These procedural lessons range from 10.501 (The universal workflow) to 10.517 (Limitations of the paradigm). The curriculum also integrates various learning components, including video lessons, post-video quizzes, and extensive practice assignments. Furthermore, modules 10.502, 10.504, and 10.506 emphasize the critical importance of choosing a measure of success and deciding on an evaluation protocol. The course structure also incorporates end-term coursework submission and an End-of-Module Survey to assess overall learning.

---

