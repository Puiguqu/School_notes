# Week 4 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_2_min

# Weekly introduction
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/zTIos/weekly-introduction

This course spans 22 weeks, covering several major pillars of artificial intelligence. The initial four weeks focus on Game Playing AI, delving into Reinforcement Learning (RL) and the implementation of the Deep Q-Network (DQN) agent. Technical components covered include the DQN neural network architecture, the associated loss function, and practical training lab activities. Following this, Week 5 introduces the state of the art and ethical considerations within AI game players.

The curriculum then shifts to Evolving Artificial Creatures (Weeks 6-10), utilizing Genetic Algorithms for automatic design. This module incorporates technical practice by building robots using simulation environments such as pybullet and defining structural components via URDF files. The focus here is on genetic encoding schemes, fitness functions, and the state of the art in evolving morphology.

Weeks 11 through 15 explore Generative and Collaborative AI, examining diverse generative systems. Specific practical applications include generating lyrics using GPT-2 and composing music via models like MusicVAE and DiffSinger. This section culminates in a project involving a pop song generator.

The final major module (Weeks 16-20) introduces "A Toy Robot Scientist," focusing on advanced reasoning and planning. Key topics include knowledge representation, system building, and the complex reasoning phase of the Robot Scientist. The course concludes with dedicated time for exam preparation in Week 21, leading into the final exam in Week 22.

---

## 02_Slides_used_in_the_video_lectures_in_week_4_Reading_30_min

# Slides used in the video lectures in week 4
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/xMYWH/slides-used-in-the-video-lectures-in-week-4

This document outlines a comprehensive 22-week course curriculum covering various advanced areas of artificial intelligence. The initial focus (Weeks 1-4) is on Game playing AI, specifically detailing the implementation and architecture of the DQN agent. This section includes modules on formalizing reinforcement learning, reviewing the DQN runtime, and engaging in labs to train or load pre-trained models. The course then shifts to Evolving artificial creatures (Weeks 6-10), delving into automatic design using genetic algorithms. Key technical topics in this phase include building robots using pybullet and URDF files, alongside defining fitness functions and genetic encoding schemes. The mid-course segment (Weeks 11-15) explores Generative and collaborative AI, introducing various systems like generating lyrics with GPT-2. Furthermore, it details music composition techniques utilizing specific models such as MusicVAE and DiffSinger. The subsequent block (Weeks 16-20) focuses on "A toy Robot Scientist," covering system building, knowledge representation, and the complex reasoning and planning phases. These later weeks examine the state of the art in robotics and legal/ethical issues surrounding autonomous systems. The curriculum maintains a practical approach, integrating numerous quizzes, practice assignments, and extensive lab activities throughout all thematic blocks. The final two weeks (Weeks 21 and 22) are dedicated to exam preparation and the final examination, concluding the course.

---

## 03_Overview_of_the_DQN_runtime_Video_15_min

# Overview of the DQN runtime
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/DWN27/overview-of-the-dqn-runtime

The provided transcript offers a comprehensive, step-by-step deep dive into the architecture and runtime mechanics of a Deep Q-Network (DQN) agent, which is a specific type of Reinforcement Learning (RL) agent.

Here is a structured summary of how the DQN agent works, broken down by its core components, memory management, and execution flow.

---

## 🧠 DQN Agent Overview: Architecture and Function

The DQN agent is designed to learn optimal decision-making (policies) within an environment (like a game) by interacting with it, storing its experiences, and iteratively training a neural network to predict the best action value (Q-value) for any given state.

### 1. Core Components

*   **Q-Network (The Main Network):** This neural network takes the current **state** as input and outputs the predicted **Q-value** (expected future reward) for every possible action in that state. Its goal is to be as accurate as possible.
*   **Target Network (The Secondary Network):** This network is a *copy* of the Q-network, but it is updated periodically (not every step). Its role is to provide a stable, fixed reference point during the training process, which prevents the training from becoming unstable.
*   **Replay Buffer (The Memory):** This is the agent's memory. Instead of learning only from the most recent experience, the buffer stores a collection of past experiences (State, Action, Reward, Next State).

### 2. The Memory Mechanism: The Looping Buffer
The agent uses a specific type of memory structure called the **Replay Buffer**.

*   **Function:** It stores the experiences gathered during gameplay.
*   **Mechanism (The Loop):** The buffer acts like a **looping buffer** or a fixed-size circular queue. Once the buffer reaches a certain maximum size, it stops accepting new data at the end and starts *overwriting* the oldest data at the beginning. This ensures the memory never "overshoots" or becomes infinitely large, focusing on a recent, representative sample of the agent's past behavior.
*   **Data Stored:** For every event, it stores the tuple: **(State, Action, Reward, Next State)**.

### 3. The Agent Runtime Cycle: How It Learns
The agent operates in an infinite loop until its performance reaches a defined threshold (e.g., a continuous score of 40). This loop encompasses the entire learning cycle: **Act $\rightarrow$ Store $\rightarrow$ Train $\rightarrow$ Update**.

#### A. Playing the Game (Action Phase)
This phase dictates how the agent chooses an action:

1.  **Environment Reset:** The game starts or resets (beginning a new *Episode*).
2.  **Epsilon-Greedy Strategy:** The agent decides whether to be random or smart:
    *   **Exploration (Random Action):** If $\epsilon$ (Epsilon) is high, the agent chooses a random action. This allows it to discover new possibilities in the environment.
    *   **Exploitation (Network Action):** If $\epsilon$ is low, the agent uses the Q-Network to choose the action it predicts will yield the highest reward.
3.  **Epsilon Decay:** Over time, $\epsilon$ gradually **reduces** (from a high value down to a minimum like 0.1). This shifts the agent from relying primarily on random exploration to relying primarily on its learned knowledge (exploitation).
4.  **Action & Observation:** The agent takes a step in the environment, receives a reward, and observes the new state.

#### B. Learning and Optimization (Training Phase)
After gathering an experience, the agent moves to the learning phase:

1.  **Storage:** The experience tuple is added to the **Replay Buffer**.
2.  **Sampling:** Instead of training on the very latest experience, the agent randomly samples a **batch** of past experiences from the Replay Buffer.
3.  **Training the Network:**
    *   The sampled batches are run through the Q-Network.
    *   A **Loss Function** (the objective function) is calculated. This function measures the discrepancy (the error) between the network's current prediction and the target value (what the Q-value *should* be, based on the reward and the target network).
    *   The loss is fed back into the Q-Network, and the network weights are adjusted (backpropagation) to minimize this error.
4.  **Target Network Synchronization:** Periodically, the weights of the Q-Network are copied over to the Target Network. This keeps the Target Network updated, allowing the agent to continue learning accurately.

### Summary of Key Terminology

| Term | Definition | Role in DQN |
| :--- | :--- | :--- |
| **Episode** | A complete run of the game until the agent loses, or until a maximum step limit (e.g., 10,000 frames) is reached. | Defines a complete learning session. |
| **Frame** | A single step or time unit in the game environment. | The basic unit of interaction between agent and environment. |
| **Epsilon ($\epsilon$)** | The probability of choosing a random action (exploration). | Controls the balance between discovering new things and using known, good actions. |
| **Replay Buffer** | The set of lists that stores past experiences ($\text{State}, \text{Action}, \text{Reward}, \text{Next State}$). | Provides diverse,

---

## 04_The_DQN_neural_network_architecture_Video_11_min

# The DQN neural network architecture
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/4dPYD/the-dqn-neural-network-architecture

This course systematically explores advanced topics in AI, beginning with game playing AI and the formalization of Reinforcement Learning (RL). The initial module heavily focuses on implementing the Deep Q-Network (DQN) agent, covering its runtime, specific neural network architecture, and the critical DQN loss function required for successful training. Practical assignments involve code reviews, lab activities for training models, and self-evaluation of the implementation process. The curriculum then transitions to evolutionary computation, where students learn about automatic design using genetic algorithms. This segment focuses on building artificial creatures and robots, utilizing tools like pybullet and URDF files, and implementing detailed genetic encoding schemes. Furthermore, the course details the processes of fitness function design and selective breeding to achieve evolving morphology. The focus subsequently shifts to Generative and collaborative AI, exploring creative systems like GPT-2 for generating lyrics and MusicVAE and DiffSinger for music composition. The final major project, "A toy Robot Scientist," explores advanced cognitive robotics, covering history, legal and ethical issues, and building the system using knowledge representation. This involves detailed study of the Robot Scientist's reasoning phase, encompassing complex planning and analytical abilities. Across all modules, topics such as the state of the art, ethical considerations in AI game players, and evolving morphology are addressed. The learning sequence culminates in extensive preparation and the final exam, demonstrating the mastery of these diverse AI domains.

---

## 05_DQN_loss_function_and_training_Video_11_min

# DQN loss function and training
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Qp5MZ/dqn-loss-function-and-training

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## 06_Watch_DQN_playing_Breakwall_Video_14_min

# Watch DQN playing Breakwall
Video • 14 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/LSmEM/watch-dqn-playing-breakwall

This course curriculum progresses through several advanced domains of Artificial Intelligence, starting with game playing AI in Weeks 1-4. The initial focus is on implementing the Deep Q-Network (DQN) agent, detailing the formalization of reinforcement learning, the DQN runtime overview, and the architecture of the neural network. Specific technical components include mastering the DQN loss function and training, culminating in a lab activity where students train or load pre-trained models. Weeks 5-10 shift focus to evolving artificial creatures, exploring automatic design using genetic algorithms, building robots with tools like pybullet and URDF files, and defining fitness functions and genetic encoding schemes. The mid-course segment (Weeks 11-15) delves into generative and collaborative AI, covering introductory generative systems, and exploring specific models such as GPT-2 for lyric generation, MusicVAE for composition, and DiffSinger. The study then transitions to robotics and reasoning, starting with a deep dive into "A toy Robot Scientist" (Weeks 16-20). This robotic module covers system building, knowledge representation, the reasoning phase, and planning and analysis within the system. Throughout the course, key technical skills are reinforced through quizzes, practice assignments, and hands-on lab activities, ensuring comprehensive coverage of advanced AI concepts.

---

## 07_Recap_of_week_4_study_Video_1_min

# Recap of week 4 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/k7mBE/recap-of-week-4-study

This document summarizes the culmination of Week 4 of a specialized course on Game Playing AI, detailing the successful implementation of key concepts and outlining the subsequent modules of the curriculum.

The primary technical achievement highlighted is the successful implementation of a working Deep Q-Network (DQN) agent on the student’s machine. Students are expected to demonstrate the ability to observe the DQN agent attempting to play various video games. This week provided a comprehensive understanding of how the DQN agent architecture and its learning system are expressed as functional code. Furthermore, participants should possess the insight necessary to thoroughly evaluate the performance of a trained DQN agent. A critical practical finding involves the deployment of pre-trained models, allowing them to observe agent performance in complex tasks like playing Breakout.

The coursework for Week 4 covered several highly technical components in depth. These included the overview of the DQN runtime environment. Detailed focus was placed on the DQN neural network architecture, which forms the computational backbone of the learning system. Additionally, instruction covered the intricacies of the DQN loss function and the entire training process. Practical application was reinforced through lab activities, which involved both training networks and loading existing pre-trained models.

Looking forward, the curriculum transitions into a broader analysis of the field. Week 5 focuses on the state of the art in AI game players, addressing what systems have emerged since the foundational DQN model was established in 2015. Subsequent modules introduce complex evolutionary and generative systems. Weeks 6 through 10 explore evolving artificial creatures, detailing the use of genetic algorithms for automatic design.

The course then delves into specialized robotics and systems design. Week 7 covers the methodology of building robots using frameworks like Pybullet and standardized URDF files. Weeks 8 and 9 discuss the formal technical details of the genetic encoding scheme and the fitness function utilized during selection. The focus then shifts heavily toward generative and collaborative AI systems. Weeks 11 through 15 examine advanced generative models.

Specific technical applications include generating lyrics using GPT-2 and performing music composition with MusicVAE and DiffSinger. A major conceptual shift occurs in Weeks 16 through 20, focusing on "A Toy Robot Scientist." This module covers system introduction, knowledge representation, the reasoning phase, and complex planning and analysis capabilities. The curriculum concludes with Week 21 and Week 22 dedicated entirely to examination preparation.

---

## 08_Self-evaluation_checklist_Implementation_of_the_DQN_agent_Reading_30_min

# Self-evaluation checklist: Implementation of the DQN agent
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/tPrmI/self-evaluation-checklist-implementation-of-the-dqn-agent

The objectives of Week 4 revolve around the comprehensive implementation, evaluation, and enhancement of Deep Q-Network (DQN) agents. The process begins with the rigorous training of a DQN agent within a defined reinforcement learning framework. Successful training requires implementing the DQN agent using standard environments, such as TensorFlow, PyTorch, or OpenAI Gym. A critical initial step is the correct definition of the agent's environment and its corresponding state-action space. To enhance the learning efficiency of the agent, an experience replay buffer must be implemented. Furthermore, the agent's behavior requires the application of an epsilon-greedy policy for effective action selection. The core learning mechanism hinges on utilizing the Bellman equation to precisely update the Q-values during the training process. A fundamental achievement is successfully training the DQN agent and monitoring its learning progress across multiple episodes.

The second major objective involves the thorough evaluation of the agent's performance metrics. Appropriate performance metrics must be defined to objectively assess the DQN agent's capabilities. These metrics include, but are not limited to, cumulative reward, convergence rate, and win rate. The trained agent must be tested within the environment to record its operational performance data. Subsequent analysis involves visualizing and interpreting the learning curve to confirm whether the agent is demonstrably improving over time. Comparative analysis is essential, requiring the comparison of the trained agent's performance against a baseline or a random policy. Finally, evaluation demands the identification of potential weaknesses or specific areas that require future improvement in the agent's behavior.

The third objective focuses on implementing and testing alternative network architectures for the DQN model. Researchers must explore various modifications, including deeper layers, convolutional networks, and recurrent networks. Modifications to the network architecture must be justifiable, based on predicted improvements in performance. The agent must then be retrained using this modified architecture to observe the direct impact on learning efficiency. A rigorous comparison must follow, evaluating the performance of the alternative architecture against the original DQN model. The final step in this section is the comprehensive documentation of all results, discussing the comparative advantages and disadvantages of the varied architectures.

Overall, successful completion signifies a deep understanding of training DQN agents. It demonstrates the ability to effectively evaluate reinforcement learning agents through quantitative metrics. Furthermore, the learner must comprehend how structural network architectures influence the learning efficiency of a DQN model. This body of knowledge allows the application of these principles to implement and test improvements in deep reinforcement learning models.

---

