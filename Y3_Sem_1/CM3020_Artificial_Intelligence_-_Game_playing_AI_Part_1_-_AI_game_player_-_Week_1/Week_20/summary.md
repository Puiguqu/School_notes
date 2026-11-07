# Week 20 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

## 02_State_of_the_art_-_slides_Reading_10_min

# State of the art - slides
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/RtgkX/state-of-the-art-slides

This curriculum progression begins with Game Playing AI, covering topics from basic AI game players (Week 1) to formalizing reinforcement learning and the DQN agent (Week 2-4), culminating in a "State of the Art and Ethics" review (Week 5). The focus then shifts to Evolving Artificial Creatures (Week 6-10), detailing automatic design using genetic algorithms, robot construction with pybullet and URDF files, genetic encoding, and fitness function analysis. Generative and Collaborative AI follows (Week 11-15), exploring systems such as generating lyrics with GPT-2, music composition with MusicVAE, and advanced models like DiffSinger. Weeks 16-20 are dedicated to "A Toy Robot Scientist," which encompasses introduction, knowledge representation, the Robot Scientist reasoning phase, planning, and analysis. The latter portion of the course emphasizes advanced applications, including meta-analysis and multi-agent communication systems. Specific technical tools utilized include pybullet, URDF files, DQN agents, genetic algorithms, GPT-2, and MusicVAE. The study structure incorporates various learning modalities, including videos, detailed readings, and practical assignments to reinforce theoretical concepts. The final weeks are dedicated to exam preparation and a comprehensive review of the State of the Art in the field. Overall, the module culminates in an understanding of complex AI system design, from game-playing agents to sophisticated robot scientists.

---

## 03_Meta-analysis_agent_Video_10_min

# Meta-analysis agent
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/41Cx2/meta-analysis-agent

The robot scientist utilizes a core set of agents to execute a full scientific investigation cycle. These agents include the Knowledge Agent, which encodes underpinning knowledge for the robot scientists. Following this, the Hypothesis Generation Agent formulates new hypotheses to be tested. The Planning Agent then produces an experimental protocol based on these hypotheses. Next, the Automated Robotic Lab Agent executes this protocol and meticulously records all experimental results. Finally, the Experimental Results Analysis Agent determines whether the initial hypothesis was confronted or refuted. To enhance the performance of these scientists, additional agents, such as a Meta Analysis Agent, are utilized. A Meta Analysis Agent collects information about all previous experimental rounds and results. It also compares the performance of various agents, determining under what specific situations they function optimally. For instance, it can advise on which methods the Hypothesis Generation Agent should employ. The specific implementation of such an agent for the robot scientists utilized a method called disk method cosine. The core technique powering this advanced capability is meta learning, or "learning to learn." Meta machine learning is a powerful approach that learns about machine learning algorithms and their parameters. Specifically, it determines which algorithms perform best on certain datasets. The robot scientist Yves applies this technique through Meta-QSAR learning to predict chemical compounds based on their structure and activity. This work is detailed in the open access paper, *Meta-QSAR, a large-scale application of meta learning to drug design and discover*. The detailed methodology is also available in the Journal of machine learning. The QSAR task involves giving a target, typically a protein, and a set of chemical compounds, also known as small molecules. These compounds are associated by their activity, such as inhibiting the target. The fundamental principle underlying Meta-QSAR is the "no free lunch theorem." This theorem posits that no single, universal machine learning algorithm performs best across all possible datasets. Therefore, meta learning seeks to understand which learning method is better suited for specific scenarios. The motivation was to understand the performance characteristics of baseline machine learning methods in QSAR learning. The Meta-QSAR goal was to select the best combination of QSAR and molecular representations for any given problem. Researchers considered over 8,000 QSAR datasets for this analysis. These datasets featured various characteristics, including number of examples and mutual information. Eighteen base-level learning algorithms were evaluated, including linear regression, support vector machines, neural networks, regression trees, and random forests. Before the meta-learning stage, nearly 3,000 drug targets were extracted from ChEMBL, a curated public database. Each chemical compound was represented by binary fingerprints showing presence or absence. Initial baseline learning showed that Random Forest was the best performer, achieving high accuracy in more than 1,000 targets. However, Random Forest was not superior in over 50 percent of cases, necessitating the meta-learning approach. To facilitate meta-learning, comprehensive meta-datasets were constructed using key features. These features, or meta-features, included dataset characteristics and drug target properties. These meta-features were organized using the Meta-QSAR ontology. This ontology described properties like the number of compounds and mutual information. The final meta-dataset contained over 2,000 meta-features spanning more than 8,000 datasets. After training the meta-QSAR learner, performance was evaluated against a default Random Forest baseline. The results demonstrated that most algorithms suggested by the meta-QSAR learner performed better than the initial random forest default. This confirms that meta-learning successfully optimizes algorithm selection for specific QSAR tasks. Furthermore, this meta-analysis agent framework can be generalized to solve other complex learning problems beyond QSAR.

---

## 04_Communication_in_multi-agent_systems_Video_20_min

# Communication in multi-agent systems
Video • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/o9CXA/communication-in-multi-agent-systems

This comprehensive curriculum covers four major areas of advanced artificial intelligence, beginning with AI game playing. The game playing module formalizes Reinforcement Learning (RL), specifically detailing the implementation and state-of-the-art applications of the Deep Q-Networks (DQN) agent, alongside ethical considerations in AI. Next, the course delves into evolving artificial creatures through Genetic Algorithms (GA), focusing on automatic design, genetic encoding schemes, and fitness function optimization. Practical robotic development is addressed by building physical simulations using specialized tools like Pybullet and URDF files. The generative AI segment introduces systems for creative output, utilizing models such as GPT-2 for lyric generation, MusicVAE and DiffSinger for sophisticated music composition, culminating in a pop song generator. A significant portion is dedicated to the "Toy Robot Scientist" project, exploring systems that involve knowledge representation, advanced reasoning phases, and complex planning capabilities. This module also addresses the legal and ethical perspectives inherent in designing sophisticated artificial agents. Finally, the curriculum synthesizes these concepts by examining meta-analysis agents and the dynamics of communication within multi-agent systems, preparing students for final examination.

---

## 05_Reading_articles_Reading_1h

# Reading articles
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/UkC4o/reading-articles

...

---

## 06_Robot_Scientist_new_projects_Video_17_min

# Robot Scientist: new projects
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/BpwGy/robot-scientist-new-projects

The lecture introduces two cutting-edge projects leveraging robotic scientists: "Action on Cancer" and "AMBITION."

The first project, Action on Cancer, is a decision support system aimed at designing personalized cancer treatments. This initiative is a collaboration involving the University of Cambridge and Goldsmiths College, funded by the Research Council UK (EPSRC) with a budget of £1.4 million over four years. The core objective is to develop an AI prototype capable of recommending personalized drug cocktails for cancer patients.

Cancer is identified as a critical global health threat, with estimates pointing to 13 million deaths and 20 million new cases annually by 2025. Traditional single-drug chemotherapy is insufficient because cancer easily develops resistance mechanisms, necessitating a more complex approach.

Action focuses specifically on combinations of multiple drugs, typically recommending between six and twelve agents. This

---

## 07_Recap_of_week_20_study_Video_1_min

# Recap of week 20 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/LLPvV/recap-of-week-20-study

This curriculum explores diverse domains of advanced AI, starting with Weeks 1-5, which focus on Game Playing AI through the formalization of Reinforcement Learning and the implementation of the Deep Q-Network (DQN) agent, alongside an examination of related ethical considerations. The focus shifts in Weeks 6-10 to Evolving Artificial Creatures, where genetic algorithms are utilized for automatic design and building robots using simulation tools like Pybullet and URDF files, underpinned by specific genetic encoding schemes and fitness functions. Weeks 11-15 delve into Generative and Collaborative AI, introducing systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition, culminating in integrated projects like pop song generators. The latter half of the course is dedicated to the "Toy Robot Scientist" (Weeks 16-20), a sophisticated system involving knowledge representation, specialized reasoning phases, planning, and the analysis of multi-agent systems. Key components of the Robot Scientist include meta-analysis agents and structured frameworks for state-of-the-art projects. Technical coverage spans from discrete reinforcement learning techniques to continuous system modeling and complex multi-agent communication. The module emphasizes practical implementation, as seen in the construction of the DQN agent and the building of evolving robotic systems. Throughout the curriculum, significant time is allocated to understanding the legal and ethical issues surrounding AI systems and advanced automated design. The course concludes with extensive preparation and examination weeks (Weeks 21-22) to synthesize the vast range of AI concepts and findings.

---

## 08_Self-evaluation_checklist_Part_5_-_State_of_the_art_Robot_Scientist_projects_Reading_30_min

# Self-evaluation checklist: Part 5 - State of the art Robot Scientist projects
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/nXsMP/self-evaluation-checklist-part-5-state-of-the-art-robot-scientist-projects

Use this checklist to assess whether you have met the expected learning outcomes for this week. 1. Critical Assessment of Automated Scientific Discovery ☐ I can explain the concept of automated scientific discovery and its significance. ☐ I can describe the Robot Scientist project and its contributions to this field. ☐ I have critically assessed the current state of research on Robot Scientists, including strengths and limitations....

---

