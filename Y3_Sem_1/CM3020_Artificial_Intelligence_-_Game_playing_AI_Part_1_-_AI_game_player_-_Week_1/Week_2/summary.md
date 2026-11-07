# Week 2 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Introduction_to_week_2_study_Video_1_min

# Introduction to week 2 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Plu0b/introduction-to-week-2-study

This comprehensive course begins with foundational concepts in Week 1, focusing on Game Playing AI. Week 2 formally introduces Reinforcement Learning (RL), providing extensive study on the DQN agent, value functions, and classical Q-learning techniques. Technical deep dives in Week 2 cover the DQN agent architecture, visual processing, and the specific derivation of the loss function for the agent. Weeks 3 and 4 transition the theoretical knowledge into practical application through the full implementation of the DQN agent. Following the core RL concepts, Week 5 provides context by examining the state of the art and ethical considerations within AI game players.

The course shifts focus in Weeks 6 through 10 to Evolving Artificial Creatures, utilizing genetic algorithms for automatic design. Specific technical details cover the implementation of robotics using tools like pybullet and URDF files. Key evolutionary components studied include genetic encoding schemes, fitness functions, and selection criteria for optimizing morphology.

Weeks 11 through 15 explore Generative and Collaborative AI systems. The curriculum covers various generation techniques, including generating lyrics with GPT-2 and exploring music composition using specialized models such as MusicVAE and DiffSinger. This culminates in a practical project, the development of a pop song generator.

The latter portion of the course, Weeks 16 to 20, focuses on a detailed case study of "A Toy Robot Scientist." This involves discussing the legal and ethical issues of advanced robotics before delving into system building. Students study knowledge representation, the reasoning phase of the robot scientist, and advanced planning and analysis. The course concludes with Week 21 dedicated to exam preparation and Week 22 for the examination.

---

## 02_Slides_used_in_the_video_lectures_in_week_2_Reading_10_min

# Slides used in the video lectures in week 2
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/lknuc/slides-used-in-the-video-lectures-in-week-2

This course curriculum spans 22 weeks, structured around developing expertise in various fields of Artificial Intelligence, beginning with Game Playing AI.

Week 2 is dedicated to formalizing reinforcement learning (RL) and the Deep Q-Network (DQN) agent, featuring multiple video lectures and practice assignments. Key concepts covered include value functions, the DQN agent architecture, the loss function for DQN, and handling visual processing in states. These initial modules include readings, quizzes, and extensive practice assignments designed to deepen technical understanding.

The course progresses to modules on evolving artificial creatures (Weeks 6-10), focusing on the application of genetic algorithms. This phase involves practical work utilizing tools like pybullet and URDF files, emphasizing genetic encoding schemes, fitness functions, and selection processes.

Next, the curriculum shifts focus to Generative and collaborative AI (Weeks 11-15), exploring systems capable of creation. Specific technical topics include generating lyrics with GPT-2, music composition using MusicVAE, and utilizing DiffSinger.

The course then introduces the project "A Toy Robot Scientist" (Weeks 16-20), covering knowledge representation, the system’s reasoning phase, and planning and analysis techniques.

The material emphasizes a blend of theoretical foundations and practical implementation, with many sections including quizzes and intensive practice assignments. The entire syllabus culminates in Week 21 as exam preparation, followed by the final examination in Week 22.

---

## 03_Formalising_the_problem_Video_7_min

# Formalising the problem
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Z9TPX/formalising-the-problem

This text outlines the formalization of AI game playing using the framework of a Markov Decision Process (MDP). The fundamental process in most games involves an iterated cycle of observation and action. Key components must be identified: states, actions, and rewards. A state ($S$) is defined as the current view of the game, such as the pixel configuration in a game like Breakout. The actions ($A$) are the moves the AI can take, such as moving left, moving right, or staying still. A reward ($R$) is a result associated with an action, providing positive or negative feedback.

For example, in Breakout, hitting a brick yields a positive reward (e.g., +1 point), while missing the ball may result in a heavy negative reward leading to game over. The interaction flow involves the player observing state $S$, taking action $A$, and subsequently observing the next state, $S'$.

Crucially, this transition is often probabilistic, meaning the same action in the same state may lead to multiple possible next states. This probabilistic relationship is formally expressed as the probability of state prime given state and action, $P(S'|S, A)$. This mathematical representation constitutes the state transition matrix.

The reward function, $R(S, A, S')$, dictates the gain or loss associated with the transition from state $S$ via action $A$ to $S'$. Rewards can be positive (points gained), negative (penalties or loss of life), or zero (for inaction in a given frame).

The combination of the probabilistic state transition matrix and the reward function formalizes the problem as a Markov Decision Process (MDP). An MDP is defined as a mechanism for formalizing a stochastic sequential decision problem. The term "stochastic" refers to the inherent probabilistic element determined by the state transition matrix.

The process is "sequential" because the AI must make a continuous series of decisions, determining an action for each frame observed in the game sequence. Finally, it is a "decision problem" because the goal is to determine the optimal sequence of actions.

The curriculum further extends these basic concepts to advanced reinforcement learning techniques. Key topics include the action policy and Q-learning. The program also addresses formalized reinforcement learning using agents like Deep Q-Networks

---

## 04_Value_functions_and_DQN_Video_10_min

# Value functions and DQN
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/xbJBG/value-functions-and-dqn

This curriculum is structured across twenty-two weeks, covering advanced topics in AI game playing, evolutionary systems, generative models, and autonomous robotics. Weeks 1 through 5 focus on Game Playing AI, beginning with basic AI players and transitioning into the rigorous formalization of Reinforcement Learning (RL). A core concept in this section is the Deep Q-Network (DQN) agent, which utilizes value functions to estimate optimal actions within complex environments. The DQN development involves detailed study of its architecture and a specific loss function crucial for training the agent.

The curriculum then shifts to evolutionary computation in Weeks 6-10, focusing on "Evolving artificial creatures." This segment employs genetic algorithms for automatic design and morphology evolution. Technical implementations include building robots using specialized formats like URDF and utilizing concepts like genetic encoding schemes and fitness functions.

Weeks 11 through 15 transition into Generative and Collaborative AI systems. This phase explores advanced generative methods, starting with general system introductions. Specific case studies include generating lyrics using GPT-2, composing music with MusicVAE, and utilizing DiffSinger.

The latter portion of the course, Weeks 16 through 20, tackles autonomous robotics through the "Toy Robot Scientist" project. This area addresses complex topics such as knowledge representation, ethical and legal issues in AI, and sophisticated reasoning phases. The final robotic modules focus on planning and analyzing actions within a constructed AI system.

The course culminates in Week 21, dedicated to exam preparation, leading into the final examination in Week 22. The sequence progresses from basic game-playing to deep learning agents, evolutionary design, complex generative outputs, and finally, integrated autonomous reasoning and robotics.

---

## 05_What_are_the_names_of_the_classic_q-learning_techniques_Reading_2h

# What are the names of the classic q-learning techniques?
Reading • 2h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/wHzzu/what-are-the-names-of-the-classic-q-learning-techniques

Now it is time to have a first look at some of the articles. We would like to set you a simple task: name the value approximation techniques that researchers used prior to the deep Q network technique. You can find this information in the links below. Here is a link to an early version of the DQN paper which is open access: Mnih, Volodymyr, et al. ' Playing atari with deep reinforcement learning .' arXiv preprint arXiv:1312.5602 (2013)....

---

## 06_DQN_agent_architecture_Video_9_min

# DQN agent architecture
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/q4P2b/dqn-agent-architecture

This summary outlines the architecture and operational principles of the Deep Q-Network (DQN) agent, focusing on the mechanisms of autonomous learning and exploration.

1. An agent is defined as an autonomous entity capable of observing its environment and taking decisions within that world.
2. Its primary goal is to maximize accumulated reward over time.
3. The DQN architecture is designed to solve complex problems where traditional state transition matrices and explicit action policies are unavailable.
4. The core function of the agent is to learn a Q function, which allows it to determine the optimal action in any given state.
5. The overall system comprises the agent itself and the game environment, which interacts with the agent.
6. Data flows from the environment to the agent, providing states and rewards, while the agent sends actions back to the environment.
7. Internally, the agent relies on a Replay Buffer, which acts as a massive memory store for past experiences.
8. The Replay Buffer stores experience tuples, structured as $(S, A, S', R, D)$.
9. $S$ represents the current state, $A$ is the action taken, $S'$ is the subsequent state, $R$ is the immediate reward, and $D$ is a boolean indicating if the game concluded.
10. The other critical component is the Q function, implemented as

---

## 07_The_loss_function_for_DQN_Video_12_min

# The loss function for DQN
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Z0jCn/the-loss-function-for-dqn

This course is structured into multiple thematic modules, beginning with foundational work in AI game playing. The initial focus, spanning Week 1 through Week 5, covers general game playing AI and culminates in the implementation of advanced techniques like the DQN agent (Week 4). Week 2 provides a deep dive into formalizing reinforcement learning (RL), including specialized study on value functions and the core architecture of the DQN agent.

The technical instruction emphasizes the specific mathematical requirements of RL, dedicatedly covering the design and application of the loss function for DQN. Key skills are developed through practical assignments focusing on DQN architecture, visual processing of states, and detailed explanations of the underlying loss function.

The curriculum then pivots to evolutionary design in Weeks 6 through 10, exploring how artificial creatures evolve. This section details automated design using genetic algorithms, practical robot building via Pybullet and URDF files, and the establishment of appropriate genetic encoding and fitness functions.

A major thematic shift occurs in Weeks 11 through 15, focusing on Generative and Collaborative AI. This module explores various generative systems, including practical applications such as generating lyrics with GPT-2, composing music using MusicVAE, and advanced synthesis techniques like DiffSinger.

Weeks 16 through 20 address the complex domain of "A toy Robot Scientist." This sequence details system building, knowledge representation, reasoning phases, planning, and analysis within sophisticated robotic projects.

Finally, the course concludes with dedicated preparation time, reserving Week 21 for comprehensive exam preparation, followed by the final examination in Week 22. The course structure maintains a continuous blend of theoretical concepts, architectural discussions, and hands-on implementation exercises throughout all five phases.

---

## 08_Visual_processing_and_states_in_DQN_Video_8_min

# Visual processing and states in DQN
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Z2fbx/visual-processing-and-states-in-dqn

The text details the necessary pre-processing steps required to transform raw data output from an Atari game emulator into a format suitable for training a Deep Q-Network (DQN) agent. These manipulations involve crucial adjustments related to temporal information, artifact removal, and data reduction.

A primary challenge noted is the inherent lack of a sense of time when a neural network processes video input using only a single frame as its state. Because arcade games rely heavily on movement, the AI requires context to predict actions accurately. Standard recurrent systems like LSTM are often used for sequential data, but the DQN architecture employed here is not recurrent. Therefore, the solution involves feeding the network a sequence of frames rather than a single snapshot. Specifically, the state fed into the DQN agent consists of the last three consecutive frames of the game. This three-frame input provides the network with a crucial sense of time, effectively making the state a form of second-order representation.

Furthermore, the raw game frames contain flickering artifacts caused by the hardware limitations of the original Atari 2600 platform. These limitations restricted the number of sprites that could be displayed simultaneously, leading to objects appearing only in alternating even or odd frames. An AI, unlike a human with persistence of vision, registers this flickering as visual instability. To eliminate this, the processing incorporates a compounding technique for each of the three input frames. This technique involves taking the maximum value for

---

## 09_Recap_of_week_2_study_Video_1_min

# Recap of week 2 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/XXMsl/recap-of-week-2-study

This course provides an extensive exploration of modern Artificial Intelligence, structured across four major domains: Game Playing, Evolutionary Design, Generative AI, and Intelligent Robotics.

The initial phase (Weeks 1-5) focuses on Game Playing AI, formalizing problems within reinforcement learning (RL) and detailing the Deep Q-Network (DQN) agent. Key technical concepts include value functions, the DQN agent architecture, and its specialized loss function, alongside methods for visual processing in AI states.

The second major module (Weeks 6-10) delves into Evolving Artificial Creatures, concentrating on automatic design using genetic algorithms. This includes building robots leveraging tools like Pybullet and URDF files, while establishing complex genetic encoding schemes and fitness functions for selection. The curriculum also examines the state of the art in evolving morphology.

The third segment (Weeks 11-15) explores Generative and Collaborative AI, focusing on creating complex content. Students investigate generative systems, using models like GPT-2 for lyric generation, MusicVAE and DiffSinger for advanced music composition, and integrating these elements into comprehensive systems.

The final applied module (Weeks 16-20) centers on "A Toy Robot Scientist," examining the integration of AI for knowledge-intensive tasks. This involves addressing legal and ethical issues, building the system, and implementing sophisticated knowledge representation. The phase culminates in the robot’s reasoning and planning abilities, showcasing state-of-the-art projects in autonomous reasoning.

The study culminates in a thorough recap and an intensive examination week, ensuring mastery of all technical concepts and methodologies presented across the program.

---

## 10_Self-evaluation_checklist_Formalising_reinforcement_learning_Reading_30_min

# Self-evaluation checklist: Formalising reinforcement learning
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/9ynYp/self-evaluation-checklist-formalising-reinforcement-learning

This text serves as a comprehensive self-evaluation checklist for Week 2 of a learning module on Reinforcement Learning (RL), focusing on the formalism of Markov Decision Processes (MDPs), Q-Learning, and Deep Q-Networks (DQN).

The initial learning objective requires a thorough understanding of MDPs, which are the foundational model for sequential decision-making problems in RL. An MDP is defined by several key components: states, actions, transition probabilities, rewards, and discount factors. These components allow a game or decision-making scenario to be accurately represented within the MDP framework. MDPs are crucial because they provide the formal structure necessary for modeling how an agent makes decisions sequentially over time.

The second core concept addressed is Q-Learning and its functional necessity. Q-learning is a specific algorithm designed to learn an optimal action-selection policy by estimating action-value functions (Q-values). It is particularly valuable when the environment’s transition dynamics are unknown, meaning the agent does not know the explicit probabilities of moving between states. A critical element of Q-learning is managing the inherent trade-off between exploration and exploitation. Exploration allows the agent to discover new information, while exploitation maximizes immediate rewards using learned knowledge.

This process is driven by the Bellman equation, which defines the update rule for Q-values over time. The Bellman equation is the core mathematical tool that allows the agent to iteratively refine its estimates of expected future rewards.

The final and most complex topic is the Deep Q-Network (DQN), which addresses the inherent limitations of traditional Q-learning. Traditional methods struggle when the state space is vast, necessitating the use of deep learning to approximate the Q-values. A DQN utilizes a neural network, which acts as the powerful function approximator for the Q-function.

To ensure stable training, DQN incorporates two vital components. The first is experience replay, which stabilizes learning by storing and reusing past experiences. The second is the target network, whose purpose is to reduce instability by providing a fixed target for training. The DQN optimizes its Q-values using a specific loss function. This function quantifies the difference between the predicted Q-values and the target Q-values derived from the Bellman updates. By mitigating the challenges of instability, techniques like experience replay and target networks allow DQN to effectively tackle complex real-world problems.

---

