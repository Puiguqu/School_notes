# Week 3 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_2_min

# Weekly introduction
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/iWq1F/weekly-introduction

This transcript introduces Week 3 of the game-playing AI case study, focusing on building foundational AI systems capable of playing games. The primary objective is to delve into the necessary coding tools for developing a Deep Q-Network (DQN) agent. Central to this week’s learning is the utilization of the AI Gym library to establish a proper game simulation environment. A key learning objective is mastering how to correctly construct environments for agent interaction within simulation. Furthermore, participants will develop a basic random game-playing agent to understand the complete agent-building process. The curriculum also introduces the Keras library, which is essential for constructing neural networks used within the DQN agent. A specific focus is placed on understanding the convolutional aspects of these neural networks.

The discussion highlights several examples of available OpenAI Gym environments. These include standard box 2D simulated physics environments. Additionally, a custom version of an Atari game has been developed to avoid copyright issues. The Lunar Lander example serves as another environment demonstration. A particularly exciting concept explored is how a neural network processes video game input. The summary explains what a Convolutional Neural Network (CNN) "sees" when observing game footage. Technically, this involves visualizing the output of filters, such as the 32 filters mentioned. These filters are configured by the network to extract critical and relevant information from the game view. This extraction capability is a fundamental finding of the week.

The supplemental course materials provide a detailed structure for this learning path. For instance, the "Open AI gym - Weekly introduction" video is a core resource. The curriculum involves practical assignments, including setup labs and quizzes for both AI Gym and Keras. Specific technical practice includes a "Lab exercise: controlling agents with neural networks." Subsequent topics outline the progression of the course. Week 4 is dedicated to the full implementation of the DQN agent. Further modules examine the state of the art and ethics in AI game players. Later weeks introduce evolving artificial creatures and advanced generative and collaborative AI systems. Ultimately, these tools are intended to provide a comprehensive foundation for advanced AI research. The study aims to equip participants with the necessary technical knowledge to grasp the mechanisms of modern game-playing AI.

---

## 02_Slides_used_in_the_video_lectures_in_week_3_Reading_30_min

# Slides used in the video lectures in week 3
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/KCMJ1/slides-used-in-the-video-lectures-in-week-3

This 22-week course structure progresses through several major fields of Artificial Intelligence, beginning with Game Playing AI (Weeks 1-3). The initial phase introduces crucial tooling like OpenAI Gym and begins formalizing reinforcement learning, leading to the implementation of the Deep Q-Network (DQN) agent in Week 4. Foundational technical concepts are covered through the introduction of Keras and Convolutional Neural Networks (CNNs), often supplemented by detailed labs and practice assignments. The subsequent module focuses on Evolving Artificial Creatures (Weeks 5-10), utilizing genetic algorithms for automatic design. This section involves building robots using specialized frameworks like PyBullet and defining system structure via URDF files. The course then transitions to Generative and Collaborative AI (Weeks 11-15). Key projects in this phase include generating lyrics with GPT-2 and music composition using MusicVAE and DiffSinger. The curriculum subsequently moves into the complex domain of robotics with the "Toy Robot Scientist" series (Weeks 16-20). This final module emphasizes system building, knowledge representation, and the critical reasoning phase of autonomous agents. Practical learning is integrated throughout the course, featuring weekly labs, quizzes, and self-evaluation checklists. The overall structure builds complexity from basic game AI implementations to advanced generative models and autonomous robotic reasoning systems. The course concludes in Week 21 as an exam preparation week before the final examination in Week 22.

---

## 03_What_is_openai_gym_Video_18_min

# What is openai gym?
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/fVFbW/what-is-openai-gym

This curriculum provides a comprehensive exploration of advanced AI fields, beginning with game-playing AI and Reinforcement Learning (RL). Early modules introduce the DQN agent, formalizing RL concepts and utilizing tooling like OpenAI Gym for agent setup and practice. Students are also introduced to Keras and Convolutional Neural Networks (CNNs) through lab exercises to control agents using neural networks. The focus then shifts to evolving artificial creatures, utilizing Genetic Algorithms (GA) for automatic design. This involves building robots using frameworks such as PyBullet and defining specific genetic encoding schemes and fitness functions. Next, the course covers generative and collaborative AI, delving into systems that create novel content. Practical applications include generating lyrics with GPT-2 and exploring advanced music composition models like MusicVAE and DiffSinger. A significant portion is dedicated to the "Toy Robot Scientist" project, which focuses on building sophisticated systems. This project covers knowledge representation, advanced reasoning, planning, and analyzing AI behavior. The curriculum maintains a critical focus on the state of the art and ethical considerations within AI. The program progresses from basic RL and neural network implementation to complex robotic and generative intelligence. The course concludes with intensive exam preparation covering all major technical concepts.

---

## 04_Introduction_to_keras_and_neural_networks_Video_15_min

# Introduction to keras and neural networks
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/jyY9i/introduction-to-keras-and-neural-networks

This transcript serves as a "crash course" on **Neural Networks**, explaining the core concepts, the mechanics of signal flow, and the process of training the network using libraries like **Keras**.

Here is a summary of the key concepts:

---

### 🧠 Core Components of a Neural Network

1.  **Activation Functions:**
    *   **Purpose:** To control when or how much a neuron outputs. They introduce necessary non-linearity to the network.
    *   **Types:** They come in various shapes (e.g., linear, sinusoidal). You can use built-in functions or write your own.

2.  **Weights (The Connections):**
    *   **Mechanism:** Every connection between neurons is associated with a weight (a number, like 0.1 or 0.2).
    *   **Function:** When inputs flow through, they are **scaled** by their corresponding weights. These weighted inputs are summed up before being passed to the activation function.

3.  **Signal Flow:**
    *   The input data is multiplied by the **weights**, summed together, and the resulting sum is passed through the **activation function** to produce the neuron's output.

### 📉 The Training Process

The goal of training is to adjust the weights so that the network's output is as close as possible to the desired target output. This process relies on the **Loss Function** and **Backpropagation**.

1.  **The Loss Function (Measuring Error):**
    *   **Purpose:** After feeding the network a set of inputs, the loss function compares the network's actual output to the *desired* output (the ground truth).
    *   **Function:** It calculates the difference (the "error" or "how wrong" the network is), providing a single numerical value.
    *   **Customization:** You don't have to use built-in functions; complex tasks (like in DQN) require custom loss functions.

2.  **Training (The Iterative Loop):**
    *   Training is the process of minimizing this calculated loss over many examples.
    *   **The Cycle:**
        1. **Feed Input:** Provide a batch of training examples.
        2. **Calculate Loss:** Determine the network's error.
        3. **Backpropagate:** Feed that calculated loss *backward* through the network (using calculus).
        4. **Adjust Weights:** Based on the error signal, the network slightly adjusts its weights to make the result better next time.
    *   This cycle **repeats iteratively** until the loss value is acceptably low across the dataset.

### 🔄 Summary: The Complete Picture

A neural network is fundamentally a data processing tool that learns through self-correction:

**Build Model (with initial random weights) $\rightarrow$ Feed Data $\rightarrow$ Calculate Loss $\rightarrow$ Backpropagate Loss $\rightarrow$ Adjust Weights $\rightarrow$ Repeat $\rightarrow$ Trained Model**

---

## 05_Convolutional_layers_Video_12_min

# Convolutional layers
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/1JRQ9/convolutional-layers

This curriculum is structured across 22 weeks, starting with Game Playing AI, which formalizes reinforcement learning (RL) and introduces the DQN agent. The early stages leverage tools like OpenAI Gym and build foundational AI skills using Keras and Convolutional Neural Networks (CNNs) to train agents. The study then progresses into evolutionary computation, dedicated to creating evolving artificial creatures via genetic algorithms (Weeks 6-10). This involves specialized robotics techniques, utilizing Pybullet and URDF files, and defining fitness functions for morphological evolution.

The focus shifts next to Generative and Collaborative AI, exploring systems that create content. This phase covers advanced topics such as generating lyrics with GPT-2 and composing music using sophisticated models like MusicVAE and DiffSinger. These studies culminate in building a complete pop song generator.

Subsequently, the course delves into the "Toy Robot Scientist," focusing heavily on complex system design and reasoning. This involves building the system, implementing knowledge representation, and developing the robot’s reasoning and planning phases. Final weeks synthesize these concepts by examining the state of the art and addressing ethical issues across various AI domains. The curriculum concludes with a comprehensive exam preparation period.

---

## 06_Recap_of_week_3_study_Video_1_min

# Recap of week 3 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Af84k/recap-of-week-3-study

This summary provides a comprehensive overview of the AI gaming concepts and the overall curriculum structure presented in the text.

The current focus, Week 3, involves utilizing specific tooling designed for building artificial agents capable of playing video games. Students have been learning how to implement a game simulation environment using the Open AI Gym library. They have successfully developed a baseline random game playing agent that operates within the framework provided by OpenAI Gym. Additionally, the material has focused heavily on the Keras library, which serves as the mechanism for building complex neural networks. A significant technical detail covered was the concept of convolution within these networks. Specifically, detailed insight was gained into how convolution operates in neural networks. This insight allows for understanding exactly what a neural network perceives when presented with a video game screen. The materials reinforce the transition towards more sophisticated agent development. The immediate next steps involve moving from theoretical tooling to actual code implementation. Week 4 marks the commencement of Game Playing AI: Part 4, focusing on the implementation of the Deep Q-Network (DQN) agent. The course also covers important conceptual foundations, such as Week 2’s focus on formalizing reinforcement learning and the DQN agent.

Beyond the immediate AI gaming focus, the curriculum expands into advanced, interdisciplinary areas. Subsequent weeks explore the State of the Art and ethics in AI game players during Week 5. Weeks 6 through 10 pivot to "Evolving artificial creatures." This segment introduces automatic design using genetic algorithms. Key technical components here include building robots using PyBullet and URDF files. The module then delves into the genetic encoding scheme and how fitness functions and selection processes are implemented.

The curriculum then shifts into the domain of Generative and collaborative AI (Weeks 11-15). This section covers introductions to generative systems. Specific applications studied include generating lyrics using GPT-2 and music composition with MusicVAE. Other generative models covered include DiffSinger and the construction of a pop song generator.

The final major technical module, spanning Weeks 16 through 20, is dedicated to "A toy Robot Scientist." This detailed segment covers its introduction, history, legal, and ethical issues. It proceeds to building the system and knowledge representation. Subsequent parts detail the reasoning phase, planning, and analysis capabilities of the Robot Scientist. This entire course structure progresses from basic game agents to advanced robotic and creative AI systems. The final weeks (21 and 22) are dedicated to comprehensive exam preparation and the exam itself.

---

## 07_Self-evaluation_checklist_Game_playing_AI_tooling_Reading_30_min

# Self-evaluation checklist: Game playing AI tooling
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/IwJHT/self-evaluation-checklist-game-playing-ai-tooling

The learning objectives centered on the implementation and testing of a game-playing AI through three critical phases: environment simulation, basic agent development, and advanced neural network training. The first objective involved successfully implementing a Game Simulation Environment utilizing the OpenAI Gym library. Learners must be capable of installing and setting up the OpenAI Gym library effectively. Furthermore, a deep understanding of the structure and components inherent to an OpenAI Gym environment is required. Practical skills involve creating and initializing a game simulation environment using the Gym framework. Interaction with this environment is managed by taking specific actions and observing resulting states, rewards, and termination signals.

The second stage focused on Developing a Random Game-Playing Agent within the reinforcement learning paradigm. This objective requires comprehension of the core concept of a random agent and how it operates within a reinforcement learning setting. Participants must be able to implement a random agent that selects and executes actions within the defined OpenAI Gym environment. Following implementation, the ability to run simulations of the random agent playing the game is necessary for performance analysis. Finally, the process necessitates the ability to log and visualize the outcomes of the agent’s gameplay for quantitative evaluation.

The third major phase involved Building and Training Neural Networks using the Keras library. This objective begins with installing and importing the Keras library specifically for building neural networks. Understanding the fundamental structure of a neural network is crucial, encompassing input, hidden, and output layers. Learners must design a simple neural network using Keras, tailored to process the game state data observed from the simulation. The process also requires training this network using sample data and subsequently evaluating its overall performance.

Successful completion of these checklists indicates the fulfillment of the week's core learning objectives. Reflection prompts guide users toward assessing personal challenges encountered during the implementation of the game-playing AI. These questions encourage introspection on how challenges were overcome and how neural networks fundamentally improve AI agent decision-making beyond simple random action selection. Learners are also prompted to identify additional steps necessary to deepen their understanding of AI within complex game simulations. Achieving all checked boxes validates the successful mastery of this foundational week of AI tooling.

---

