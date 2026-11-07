# Week 19 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

## 02_New_Reading_Reading_10_min

# New Reading
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/2Dyvv/new-reading

This curriculum progresses through several advanced topics in artificial intelligence, beginning with AI Game Playing. The early phase (Weeks 1-5) introduces foundational AI players, culminating in the implementation of the Deep Q-Network (DQN) agent, covering concepts like formal reinforcement learning and ethical considerations in AI game players. The focus then shifts to evolving artificial creatures (Weeks 6-10), exploring automatic design through genetic algorithms and the construction of robots using tools like pybullet and URDF files. Key elements in this segment include genetic encoding schemes and the development of robust fitness functions and selection processes for evolving morphology. Following this, the module delves into Generative and Collaborative AI (Weeks 11-15), examining systems from introductory concepts to practical applications. Specific projects feature generating lyrics using GPT-2, composing music with MusicVAE, and utilizing advanced models like DiffSinger, ultimately culminating in a complete pop song generator. The final major theme is "A Toy Robot Scientist" (Weeks 16-20), which focuses on building a complex reasoning system. This includes knowledge representation, introducing the Robot Scientist reasoning phase, and mastering planning and scheduling of experiments. The practical exercises involve analyzing experimental results and modifying the planning and analysis agents. The entire program concludes with a comprehensive preparation phase and subsequent exam week.

---

## 03_Crash_course_in_planning_and_scheduling_Video_8_min

# Crash course in planning and scheduling
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/UbymE/crash-course-in-planning-and-scheduling

This mini-lecture outlines the complexities of planning and scheduling, addressing both classical and real-world scenarios. Planning is a critical application in fields such as manufacturing and robotics. The field utilizes dedicated languages, such as PDDL (Planning Domain Definition Language), which serves as a primary standard for planning. Classical planning handles observable, deterministic situations and is modeled as a search problem. This involves defining an initial state, possible actions, and the desired goal state. The objective is to find a sequence of actions that successfully transitions the system from the initial state to the goal state. Algorithms employed for searching and planning include breadth-first search, depth-first search, and heuristic search. Deductive reasoning can also be applied by reasoning agents to locate solutions for planning tasks. Actions are typically formalized using a schema that specifies parameters, preconditions, and effects. For instance, a schema for "flying the plane" requires preconditions (e.g., plane at origin, airport access) and defined effects (e.g., plane is no longer at origin).

A classic illustration of this process is the blocks world problem, where a robot arm manipulates blocks on a table. This state is represented using predicate notation, identifying relations like `on(Block, Object)` or `clear(Object)`. The initial state is a list of predicates describing the arrangement of blocks and locations. An action's preconditions specify when it can occur, while its effects list the resulting changes to the system's relationships.

Real-world planning fundamentally differs from classical planning due to environmental uncertainties. Classical planning relies on the closed world assumption, meaning non-explicitly mentioned information is assumed not to exist. In contrast, agents operating in real environments must adhere to the open world assumption, recognizing that undefined information is simply unknown. Real-world agents must often produce contingent plans, which involve conditional branching due to partial observability and non-determinism. Furthermore, dynamic environments necessitate continuous monitoring and potential re-planning if goals or expected outcomes change unexpectedly.

Beyond just sequencing actions, the real world introduces temporal and resource constraints, which form the basis of scheduling problems. Planning typically focuses on *what* actions to perform, while scheduling focuses on *when* and *how long* they take, often requiring separate solutions. Resource constraints involve both reusable resources (like staff) and consumable resources (like chemicals).

Multi-agent planning introduces further complexity by requiring coordination between multiple autonomous agents. Agents may cooperate toward a shared goal, compete, or operate independently. Joint planning generates plans for coordinated actions, and agents may or may not need communication. Ultimately, the scope encompasses finding solutions in environments that are partially observable, non-deterministic, and constrained by resources and agent interactions.

---

## 04_Planning_and_scheduling_experiments_by_the_Robot_Scientists_Video_12_min

# Planning and scheduling experiments by the Robot Scientists
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Lohom/planning-and-scheduling-experiments-by-the-robot-scientists

This curriculum is structured across various advanced AI disciplines, beginning with game playing AI. The first phase covers AI game players, detailing the progression from foundational AI concepts (Weeks 1-3) to formalizing reinforcement learning and implementing the Deep Q-Network (DQN) agent (Weeks 2-4). Further exploration into this domain addresses state-of-the-art techniques and ethical considerations regarding AI game players (Week 5).

Next, the focus shifts to evolving artificial creatures, introducing automatic design methods using genetic algorithms (Week 6). This segment also covers the practical construction of robots using specific tools like pybullet and URDF files (Week 7), alongside detailed technical components such as genetic encoding schemes and fitness function selection (Weeks 8-9). The study concludes this module by reviewing the state of the art in evolving morphology (Week 10).

The third major block explores generative and collaborative AI, starting with an introduction to generative systems (Week 11). Technical implementations include generating lyrics using GPT-2 (Week 12), composing music with MusicVAE (Week 13), and examining advanced models like DiffSinger (Week 14), culminating in a comprehensive pop song generator project (Week 15).

The final and most extensive section introduces "A Toy Robot Scientist," covering its foundational history, perspectives, and legal/ethical issues (Week 16). The system development progresses through knowledge representation (Week 17), the core reasoning phase (Week 18), and planning and analyzing experimental results (Weeks 19-20). Week 19 specifically details crash courses in planning, scheduling, and system analysis, which are essential for the robot's operation, before concluding with state-of-the-art Robot Scientist projects in Week 20.

---

## 05_Planning_and_scheduling_Reading_1h

# Planning and scheduling
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/wFAmo/planning-and-scheduling

Essential reading: Read the following research articles and pay particular attention to how experiments were planned: Williams, K., Bilsland, E., Sparkes, S et al. Cheaper faster drug development validated by the repositioning of drugs against neglected tropical diseases . Journal of the Royal Society Inerface (2015). King, R.D., Rowland, J., Oliver, S.G., Young, M., Aubrey, W., Byrne E., Liakata, M., Markham, M., Pir, P. Soldatova, L.N., Sparkes, A., Whelan, K.E., Clare, A....

---

## 06_Walkthrough_the_toy_planning_agent_Video_20_min

# Walkthrough the toy planning agent
Video • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/wKlGo/walkthrough-the-toy-planning-agent

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## 07_Analysing_experimental_results_by_the_Robot_Scientists_Video_8_min

# Analysing experimental results by the Robot Scientists
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/KQjyV/analysing-experimental-results-by-the-robot-scientists

This curriculum explores three major areas of modern artificial intelligence: Game Playing, Evolutionary Design, and Generative Systems, culminating in the advanced topic of autonomous scientific reasoning. The study of Game Playing AI begins with foundational concepts, transitioning into formal Reinforcement Learning and the implementation of the Deep Q-Network (DQN) agent. Key technical details include understanding the state of the art, ethical considerations in AI game players, and the full implementation cycle of the DQN agent.

The curriculum then shifts to Evolving Artificial Creatures, focusing on automatic design using Genetic Algorithms. This section details the construction of robots utilizing environments like PyBullet and specific structural definitions through URDF files. Core concepts involve establishing a genetic encoding scheme and defining robust fitness functions for selection processes, leading to an examination of evolving morphology.

Next, Generative and Collaborative AI is covered, introducing various generative systems. Specific projects include generating lyrics with GPT-2 and composing music using MusicVAE and DiffSinger, concluding with a pop song generator project.

The final major section focuses on the sophisticated domain of the Robot Scientist, which involves tackling complex tasks of knowledge representation and reasoning. This segment dedicates significant time to the planning and scheduling of experiments, utilizing structured crash courses and practical assignments. Furthermore, the Robot Scientist must master the process of analyzing experimental results and understanding the state of the art in robotic scientific projects.

---

## 08_Analysing_experimental_results_Reading_1h

# Analysing experimental results
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/hHBQa/analysing-experimental-results

Essential reading: Read the following research articles and pay particular attention to how experimental results were analysed: Williams, K., Bilsland, E., Sparkes, S et al. Cheaper faster drug development validated by the repositioning of drugs against neglected tropical diseases . Journal of the Royal Society Inerface (2015). King, R.D., Rowland, J., Oliver, S.G., Young, M., Aubrey, W., Byrne E., Liakata, M., Markham, M., Pir, P. Soldatova, L.N., Sparkes, A., Whelan, K.E., Clare, A....

---

## 09_Recap_of_Week_19_study_Video_1_min

# Recap of Week 19 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/mrGcQ/recap-of-week-19-study

This course heavily explores the intersection of AI, robotics, and experimental science, specifically focusing on the role of the "Robot Scientist." Central to the curriculum is understanding how to automate and rigorously plan scientific experiments using advanced computational systems.

Experiments carried out by automated robotic systems necessitate meticulous planning, which transforms experimental protocols into a machine-processable form. Planning agents must first evaluate feasibility by confirming the availability of all necessary materials and equipment. A critical element of experimental design involves incorporating controls to properly account for biological variability in the results. Furthermore, robust experimental protocols require measuring the same phenomenon multiple times to ensure statistical reliability.

Robot scientists employ sophisticated machine learning (ML) approaches to analyze the data generated during these automated experiments. The curriculum is structured across various technical domains, including game playing AI and generative systems.

Specifically, the course dedicates multiple weeks to reinforcement learning, covering topics like the formalization of RL and the use of the Deep Q-Network (DQN) agent. Subsequent modules delve into evolutionary computing, utilizing genetic algorithms for automatic design and robot building via platforms like pybullet and URDF files.

The study of generative AI spans topics such as introducing generative systems, generating lyrics with GPT-2, and employing models like MusicVAE and DiffSinger for music composition.

The core modules concerning the Robot Scientist introduce the system's history, perspectives, and associated legal and ethical issues. These sections transition into the practical implementation of the system, covering knowledge representation.

The planning phase of the Robot Scientist is a detailed process, including a walkthrough of the toy planning agent. This phase is coupled with hands-on assignments requiring modification of the planning agent.

The analysis phase focuses on interpreting experimental outcomes, utilizing specialized agents to process the generated data. Practical assignments are provided for both the planning and the analysis modules.

This comprehensive training culminates in understanding the state of the art in various Robot Scientist projects and their future implications. The coursework emphasizes the practical skills needed for designing, executing, and analyzing complex, automated scientific studies.

---

## 10_Self-evaluation_checklist_Part_4_-_Planning_and_analysing_Reading_30_min

# Self-evaluation checklist: Part 4 - Planning and analysing
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/C1gAH/self-evaluation-checklist-part-4-planning-and-analysing

This document functions as a self-evaluation checklist designed to assess a user’s understanding of concepts covered in Week 19 – Part 4: Planning and Analysing. The learning outcomes are structured across three major areas of study.

The first area focuses on comparing and contrasting classical planning problems with real-world planning problems. Learners must be able to define classical planning problems and thoroughly explain their inherent characteristics. Additionally, the assessment requires describing real-world planning scenarios and detailing how they fundamentally differ from the traditional classical approach. A crucial component is the identification of key challenges present in real-world planning, specifically mentioning issues like uncertainty and complex constraints. The overall goal of this section is to provide a comprehensive comparison and contrast between these two types of planning, utilizing relevant examples for illustration.

The second area addresses the critical steps involved in planning scientific experiments using a Robot Scientist. A key concept here is defining the specific role of a Robot Scientist in the field of automating complex scientific experiments. The checklist necessitates outlining the detailed sequence of key steps required when planning an experiment under this automated framework. Furthermore, understanding how hypotheses are successfully formulated and rigorously tested through the mechanism of automated planning is essential knowledge. Learners must also be able to explain how Robot Scientists actively optimize the experimental design to maximize both efficiency and accuracy.

The third area focuses on how the Robot Scientist analyzes the gathered experimental results. Understanding the specific methods employed by Robot Scientists to analyze complex experimental data is a learning objective. The process requires describing how the raw data is properly interpreted to refine existing hypotheses and consequently improve the design of future experiments. A significant technical element involves explaining the vital role that both machine learning and artificial intelligence play in the detailed process of experimental analysis. Finally, competency is measured by the ability to provide a concrete example of how a Robot Scientist utilizes the obtained results to successfully adapt its overarching approach. This checklist serves as a comprehensive guide to mastering advanced planning and analytical techniques.

---

