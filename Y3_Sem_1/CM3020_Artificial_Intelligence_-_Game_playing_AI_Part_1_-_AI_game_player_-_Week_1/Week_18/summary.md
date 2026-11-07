# Week 18 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

## 02_Reasoning_-_slides_Reading_10_min

# Reasoning - slides
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/kWKLf/reasoning-slides

This course explores four major domains of advanced Artificial Intelligence, beginning with Game Playing AI (Weeks 1-5). The initial phase covers the implementation of AI game players, formalizing reinforcement learning principles, and focusing specifically on the Deep Q-Network (DQN) agent implementation and associated tooling. Moving into the realm of evolution, Weeks 6-10 detail the design of evolving artificial creatures, utilizing genetic algorithms for automatic design and incorporating robotics simulations via pybullet and URDF files. This segment emphasizes crucial concepts such as genetic encoding schemes, fitness function design, and the state of the art in evolving morphology.

The third module (Weeks 11-15) focuses on Generative and Collaborative AI, examining how systems create content. Key topics include the introduction to generative systems, lyric generation using GPT-2, music composition with MusicVAE, and advanced audio synthesis using DiffSinger. The practical application culminates in a sophisticated pop song generator, demonstrating the collaborative power of these generative models.

The fourth major theme, "A Toy Robot Scientist" (Weeks 16-20), delves into complex reasoning and knowledge representation. This module addresses the history, ethical implications, and system construction of a robot designed for scientific inquiry. Central to this phase is a crash course in logic, specifically detailing the generation of hypotheses through abduction and induction. Finally, the curriculum concludes with the integration of these concepts into planning and analysis, leading into preparation for the final exam.

---

## 03_Crash_course_in_logic_Video_15_min

# Crash course in logic
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/nWEGg/crash-course-in-logic

This course is structured around several major AI domains, starting with Game Playing AI, which covers the fundamentals in Weeks 1 through 5. The game playing modules introduce formal reinforcement learning and the implementation of the Deep Q-Network (DQN) agent, alongside examining the state of the art and ethical considerations in AI game players. The focus then shifts to evolving artificial creatures (Weeks 6–10), exploring automatic design using genetic algorithms and building robots via tools like pybullet and URDF files. Specific techniques taught include genetic encoding schemes, defining fitness functions, and state-of-the-art morphology evolution. Weeks 11 through 15 delve into Generative and collaborative AI, showcasing systems like GPT-2 for lyric generation, MusicVAE for composition, and DiffSinger, culminating in a complete pop song generator. The course then transitions to "A Toy Robot Scientist" (Weeks 16–20), covering the system's introduction, knowledge representation, and ethical perspectives. This module heavily emphasizes reasoning, including intensive lessons on logic, hypotheses generation through abduction and induction. Practical exercises include developing a Toy hypotheses generation agent and implementing planning and analysis capabilities for the robot. The curriculum integrates both high-level theoretical understanding and practical system building across all domains. The later weeks wrap up the material, culminating in an exam preparation week and the final assessment. The technical scope covers machine learning agents (DQN), evolutionary computation (Genetic Algorithms), and generative models (GPT-2, MusicVAE). This comprehensive approach covers both theoretical foundations and advanced implementations in AI research.

---

## 04_Crash_course_in_reasoning_Video_5_min

# Crash course in reasoning
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/TC0eT/crash-course-in-reasoning

This mini-lecture provides a detailed examination of the fundamental types of logical reasoning utilized in intelligent systems. It focuses on three core methods: deduction, abduction, and induction.

Deduction operates on the principle that if a rule and a fact are provided, the resulting conclusion is guaranteed to be correct. This form of reasoning is based on the pattern known as Modus Ponens. Specifically, if P implies Q (a condition), and P is asserted, then Q is the necessary conclusion. Deductive reasoning is utilized in standard patterns of inference, allowing chains of conclusions to be derived to reach a goal. Furthermore, Prolog reasoning relies on deduction to verify the truthfulness of logical statements.

Abductive reasoning, conversely, is defined as inferring the most plausible explanation when a rule and an observation are present. Its structure follows: if P implies Q (a condition), and Q is observed, then P is the possible explanation. Unlike deduction, the conclusion derived through abduction is not guaranteed to be correct, requiring an extra step to confirm or reject its truthfulness. The deductive method famously used by Sherlock Holmes is often cited as an example of abductive reasoning, searching for possible explanations.

Induction involves the generalization of facts from observations to form general conclusions. Similar to abduction, induction is not guaranteed to be correct and necessitates a verification step to establish truth. Machine learning is fundamentally based on inductive reasoning, as it processes many facts to generate predictions or general conclusions. This process reflects common sense, such as assuming the sun will rise tomorrow based on past observations.

Beyond these three types, the text notes that other forms of reasoning exist, including qualitative reasoning, case-based reasoning, fuzzy logic, and probabilistic reasoning. All these forms are applicable to intelligent agents to facilitate decision-making and solution searching.

The provided curriculum reinforces these concepts across several advanced AI topics. Modules involve Week 1 and 2 focusing on Game Playing AI and Formalizing Reinforcement Learning using the DQN agent. Week 6 and 7 introduce Evolving Artificial Creatures, utilizing genetic algorithms and Pybullet/URDF files for robot building.

Modules Week 11 through Week 15 cover Generative and Collaborative AI, detailing systems like GPT-2 for lyrics generation and MusicVAE/DiffSinger for music composition. Crucially, Week 16 and 17 introduce the "Toy Robot Scientist," focusing on knowledge representation and system building.

The latter part of the curriculum deeply engages with inference, specifically in Week 18. This module introduces the limits of reasoning and the practical implementation of generating hypotheses. This process includes a "Crash course in logic" and specific assignments for practicing both abduction and induction. The curriculum ultimately ties these logical concepts into a functional "Toy hypotheses generation agent."

---

## 05_Hypotheses_generation_abduction_Video_8_min

# Hypotheses generation: abduction
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/j9Q7v/hypotheses-generation-abduction

This curriculum comprehensively explores advanced concepts in Artificial Intelligence, starting with **Game Playing AI** (Weeks 1-5). Early modules introduce the core concepts of game playing, leading into the formalization of reinforcement learning and the development of the Deep Q-Network (DQN) agent. Following this, the course shifts to **Evolving Artificial Creatures** (Weeks 6-10), focusing on automatic design using genetic algorithms and constructing robots using specialized tools like pybullet and URDF files. Key elements here include establishing genetic encoding schemes, designing fitness functions, and analyzing the state of the art in evolving morphology. The scope expands to **Generative and Collaborative AI** (Weeks 11-15), covering introduction to generative systems, generating lyrics with GPT-2, and advanced music composition via MusicVAE and DiffSinger. This culminates in a pop song generator project, demonstrating collaborative generative capability. The third major focus is **A Toy Robot Scientist** (Weeks 16-20), which details building a system, knowledge representation, and the crucial reasoning phase. This section provides deep dives into logical inference, including crash courses in induction and abduction, and exercises in hypothesis generation. The Robot Scientist module integrates planning and analysis, showcasing how AI agents function in complex, knowledge-based environments. This extensive journey moves from specific agent implementations (DQN) to broad generative systems (MusicVAE) and finally to complex cognitive modeling (Reasoning). Technical foundations include the implementation of DQN, the use of genetic algorithms, and the application of advanced linguistic and musical models like GPT-2 and DiffSinger. The coursework concludes with dedicated preparation and exam weeks, synthesizing knowledge from these diverse AI domains.

---

## 06_Hypotheses_generation_induction_Video_5_min

# Hypotheses generation: induction
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/zqExy/hypotheses-generation-induction

Induction is a crucial mechanism that enables the generalization of specific facts into broader rules for hypothesis generation. This inductive inference, however, is not guaranteed to be correct and necessitates subsequent testing and verification. For instance, observing that Daffy and Tweety are white swans leads to the induced rule that all swans are white, a rule which remains fallible. Our knowledge is inherently imperfect, as evidenced by how Newtonian mechanics was eventually overturned by the theory of relativity. Machine learning is fundamentally based on this inductive reasoning process. ML systems accept multiple data points, identify underlying patterns, and generalize these patterns to predict outcomes for unseen new data. A practical example includes predicting the future sale price of three-bedroom houses in Brighton, which were previously observed to sell for 300K to 350K. While such predictions are often accurate due to stable conditions, they are not absolute, mirroring the limitations of inductive reasoning. Inductive reasoning finds wide application in biomedical research due to the remarkably conservative nature of biology. Main engine functions are often conserved across diverse species, including intelligent humans. Specific genetic facts proven correct in one organism can be inductively generalized to others. For example, if Gene X has function Y in *Saccharomyces cerevisiae* (yeast), and also in *C. elegans*, it can be generalized to have function Y in *Homo sapiens*. The biological study of Sirtuins provides a key example, as these genes have been shown to regulate organismal lifespan. Abundance of certain genes was first reported to increase lifespan in budding yeast, later observed in model organisms like nematodes and fruit flies. Further research utilized zebrafish, where the absence of longevity genes like *sirt1* leads to oxidative injury, chronic inflammation, and reduced lifespan. This line of inquiry illustrates how induction is used to formulate hypotheses about gene functions and potential drug targets in humans. Structurally, the course incorporates a deep dive into these concepts, exemplified by the module "Hypotheses generation: induction." This section includes dedicated content such as a 5-minute video and a 30-minute Induction Practice Assignment. Technical components extend across various AI modules, including "Game playing AI: Part 2" which formalizes reinforcement learning and the DQN agent. Other specialized topics cover evolving artificial creatures, referencing components like Pybullet and URDF files. Generative AI is also explored, utilizing systems like MusicVAE and DiffSinger for creative applications. The curriculum includes the module "A toy Robot Scientist," focusing on knowledge representation and reasoning phases. The overall progression covers topics from Week 1 (AI game player) up to Week 22 (Exam week). The detailed structure ensures thorough learning, ranging from theoretical lectures to hands-on labs, such as the exercise to modify the toy robot hypotheses generation lab.

---

## 07_Reading_articles_Reading_1h

# Reading articles
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/MbUyk/reading-articles

Essential reading: Read the following research articles and pay particular attention to how novel hypotheses were generated: Williams, K., Bilsland, E., Sparkes, S et al. Cheaper faster drug development validated by the repositioning of drugs against neglected tropical diseases . Journal of the Royal Society Inerface (2015). Soldatova, L.N., Rzhetsky, A. (2011) Representation of research hypotheses. Journal of Biomedical Semantics, 2: S9. Available in the Online Library ....

---

## 08_Hypotheses_generation_agent_Video_10_min

# Hypotheses generation agent
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/w6FO4/hypotheses-generation-agent

The curriculum begins with AI Game Playing, covering core concepts from Week 1 to Week 5, focusing heavily on formalizing reinforcement learning and implementing the Deep Q-Network (DQN) agent, while also addressing state-of-the-art and ethical considerations in these systems. Modules 6 through 10 introduce evolving artificial creatures, employing genetic algorithms for automatic design, constructing robots using environments like PyBullet and URDF files, and defining fitness functions and genetic encoding schemes. The Generative and Collaborative AI segment (Weeks 11–15) delves into generative systems, showcasing practical applications such as generating lyrics with GPT-2, composing music using MusicVAE, and exploring advanced techniques like DiffSinger. The "Toy Robot Scientist" module (Weeks 16–20) focuses on building systems for reasoning, encompassing knowledge representation, the reasoning phase, and sophisticated hypothesis generation. Key reasoning skills are separately taught in depth, covering logical crash courses, and specific methodologies like abduction and induction, which are applied within the Toy hypotheses generation agent. This latter phase emphasizes planning, analysis, and reviewing the state of art in complex robot scientist projects. The curriculum structure progresses from foundational AI models (DQN) to evolutionary design (Genetic Algorithms) and finally to advanced knowledge-based reasoning systems. The focus remains highly technical, detailing specific tools, such as PyBullet and URDF files, and specific generative models, such as GPT-2 and MusicVAE. The advanced reasoning components involve critical activities like generating hypotheses via abduction and induction, complemented by extensive logical practice assignments. Overall, the course provides a comprehensive journey from learning how AI agents play games to designing autonomous, reasoning scientific robots.

---

## 09_Recap_of_Week_18_study_Video_1_min

# Recap of Week 18 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/gqGjw/recap-of-week-18-study

The core focus of this curriculum is centered on logic and reasoning, which is considered the essential foundation of Artificial Intelligence (AI). AI agent intelligence is fundamentally dependent on the knowledge they possess and their ability to deploy that knowledge for decision-making. For effective reasoning, knowledge must be structured in a logical format and be capable of machine processing. The curriculum addresses various types of reasoning and inference, emphasizing that not all logical paths lead to correct conclusions. Consequently, verifying and rigorously testing logical conclusions is a crucial undertaking. A robot scientist project utilizes a real laboratory setting to test inferences specifically on real biological systems.

The course structure introduces specialized modules beginning with "Game playing AI: Part 1," "Part 2," "Part 3," and "Part 4." These segments involve formalizing reinforcement learning and implementing the Deep Q-Network (DQN) agent. Module 5 addresses the contemporary state of the art and ethical considerations within AI game players. Subsequent study shifts to "Evolving artificial creatures," beginning with "Part 1: Automatic design using genetic algorithms."

This evolution module continues through "Part 2," which involves building robots using pybullet and Universal Robot Description Format (URDF) files. "Part 3" details the genetic encoding scheme, while "Part 4" focuses on fitness function and selection. "Part 5" concludes the sequence by examining the state of the art in evolving morphology.

The curriculum then delves into "Generative and collaborative AI," starting with "Part 1: Introduction to generative systems." This section progresses to practical applications, such as generating lyrics using GPT-2 (Part 2). Module 3 explores music composition through MusicVAE, and Module 4 covers the DiffSinger system. Part 5 synthesizes these ideas into a comprehensive pop song generator.

A significant portion is dedicated to "A toy Robot Scientist," which is broken into multiple parts. Part 1 covers introduction, history, perspectives, and related legal and ethical issues. Part 2 focuses on building the system and knowledge representation. Part 3 introduces the Robot Scientist reasoning phase. Specific learning paths include a crash course in logic and reasoning, followed by practice assignments in reasoning and abduction.

Module 8 features a detailed deep dive into the Toy hypotheses generation agent, providing exercises to modify the system. The structure also covers advanced topics like planning and analyzing in Part 4, and the state of the art in Robot Scientist projects in Part 5. The final weeks are reserved for exam preparation and assessment.

---

## 10_Self-evaluation_checklist_Part_3_-_Robot_Scientist_reasoning_phase_Reading_30_min

# Self-evaluation checklist: Part 3 - Robot Scientist reasoning phase
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/jeFdi/self-evaluation-checklist-part-3-robot-scientist-reasoning-phase

This text outlines a comprehensive self-evaluation checklist for Week 18, focusing on the introduction to the Robot Scientist Reasoning Phase. The core theme revolves around the critical role of knowledge models in achieving AI-driven scientific discovery. The initial phase requires students to develop a robust argument concerning the necessity and function of knowledge models within scientific contexts. A foundational understanding must be established regarding the definition of a knowledge model and its specific function in driving scientific discovery. Furthermore, students must explain the importance of the reasoning phase utilized by a robot scientist in the context of advanced AI research.

The checklist mandates a critical discussion of the potential benefits and inherent limitations associated with leveraging knowledge models in the process of automating scientific discovery. A key argumentative component involves developing an argument detailing how knowledge models effectively enhance the mechanisms of both hypothesis generation and subsequent hypothesis validation. This section also requires a critical examination of the unique challenges that exist when attempting to implement automated reasoning within complex scientific settings.

The second major section focuses on the rigorous assessment of knowledge models for suitability within AI systems. It is essential to define and clearly differentiate the three primary methods of hypothesis generation: abduction, induction, and deduction. Students must demonstrate an understanding of how a hypotheses generation agent functions within the broader architecture of AI systems. Practical evaluation criteria for knowledge models include assessing their accuracy, completeness, and overall operational efficiency. Furthermore, a critical assessment is required to determine if a given knowledge model is technically suitable for supporting AI-based scientific reasoning. This includes identifying and analyzing inherent limitations in existing knowledge models that could negatively impact AI performance.

The third section addresses the practical implementation and formal representation of knowledge. This involves explaining the concept of machine-processable knowledge representation, ensuring the knowledge can be consumed by a computer. Various technical formats for representing knowledge have been explored, such as logic-based systems, semantic networks, and ontologies. Competency is required to construct a basic knowledge model that logically represents complex scientific concepts. Finally, students must be able to encode these simple knowledge models using precise logical rules or structured data formats. This final step ensures an understanding of how the constructed knowledge model can ultimately be utilized by an AI system for complex reasoning and discovery. The module concludes with a reflection on the confidence and defended understanding of knowledge models' impact on AI research.

---

