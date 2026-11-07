# CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## Table of Contents

- [Week 10](#week_10)
- [Week 11](#week_11)
- [Week 12](#week_12)
- [Week 13](#week_13)
- [Week 14](#week_14)
- [Week 15](#week_15)
- [Week 16](#week_16)
- [Week 17](#week_17)
- [Week 18](#week_18)
- [Week 19](#week_19)
- [Week 20](#week_20)
- [Week 21](#week_21)
- [Week 8](#week_8)
- [Week 9](#week_9)

## Week 10

### 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_Readings_and_slides_for_week_10_Reading_2h

# Readings and slides for week 10
Reading • 2h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/COfwG/readings-and-slides-for-week-10

This document outlines the specialized readings and technical resources for a study module, likely focusing on evolutionary computation and artificial life, as indicated by the recurring themes and paper titles.

The core educational resources include presentation slides titled `ga_state_of_the_art.pdf`, which provide an overview of the state-of-the-art in the field. Additionally, a specific PDF file related to the Molina paper is provided, identified as `OL-CM3020-Molina-1128.pdf`.

The reading list comprises nine distinct research papers spanning the last two decades, covering topics from robotic lifeforms to deep neural network evolution.

The initial technical focus is on automated design, represented by Lipson and Pollack (2000), titled "Automatic design and manufacture of robotic lifeforms," published in *Nature*, 406(6799), pages 974-978.

A related paper by J. Hiller and H. Lipson, from April 2012, details "Automatic Design and Manufacture of Soft Robots" in *IEEE Transactions on Robotics*, vol. 28, no. 2, pages 457-466.

Cheney, MacCurdy, Clune, and Lipson (2014) addressed the topic of evolving soft robots with complex materials and encoding, published in *ACM SIGEVOlution*, 7(1), pages 11-23, under the title "Unshackling evolution."

The application of soft robots to environmental adaptation is explored by Shah et al. (2021), whose research is published in *Nature Machine Intelligence*, 3(1), pages 51-59, detailing "A soft robot that adapts to environments through shape change."

A broader discussion on the field is provided by Lehman et al. (2020) in *Artificial Life*, 26, no. 2, pages 274-306, titled "The surprising creativity of digital evolution."

Computational evolution is addressed specifically through Miikkulainen et al. (2019), whose work, "Evolving deep neural networks," appeared in *Academic Press*, pp. 293-312.

The utility of genetic algorithms for software enhancement is detailed by J. Petke et al. (2018), offering a "Comprehensive Survey" in *IEEE Transactions on Evolutionary Computation*, vol. 22, no. 3, pages 415-432.

Finally, Molina, LaTorre, and Herrera provide a review of optimization, published in *Cognitive Computation* 10.4 (2018): 517-544, offering "An insight into bio-inspired and evolutionary algorithms for global optimization."

The listed materials are designated as available in the Online Library (OL) or the ProQuest Collection, indicating access to these scholarly resources. Administrative notes are provided regarding the location of the slides and the possibility of broken links via the Student Portal.

---

### 03_Going_beyond_Sims_Video_9_min

# Going beyond Sims
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/yPLNy/going-beyond-sims

This overview examines research

---

### 04_Read_the_evolving_soft_robots_paper_Reading_2h

# Read the evolving soft robots paper
Reading • 2h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/GBfmu/read-the-evolving-soft-robots-paper

Read the evolving soft robots paper: Lipson, H., & Pollack, J. B. (2000). Automatic design and manufacture of robotic lifeforms. Nature, 406(6799), 974-978. Here is the Cheney paper about soft body robots: Cheney, N., MacCurdy, R., Clune, J., & Lipson, H. (2014). Unshackling evolution: evolving soft robots with multiple materials and a powerful generative encoding. ACM SIGEVOlution, 7(1), 11-23....

---

### 05_State_of_the_art_for_GAs_Video_8_min

# State of the art for GAs
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/vytHI/state-of-the-art-for-gas

This comprehensive course structure is divided into major thematic blocks, beginning with AI game players, then focusing on evolving artificial creatures, moving into generative systems, and concluding with advanced robotic intelligence.

The initial phase (Weeks 1-5) establishes foundational AI game playing concepts, moving from general AI player development to formalizing reinforcement learning using the Deep Q-Network (DQN) agent. Week 4 specifically details the implementation of the DQN agent, while Week 5 addresses the ethical landscape and state of the art for such game players.

Subsequently, Weeks 6 through 10 delve into the domain of evolving artificial creatures, concentrating on automatic design using Genetic Algorithms (GAs). This includes practical building using robotics frameworks like pybullet and URDF files, defining genetic encoding schemes, and implementing fitness functions and selection processes.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems for content creation. This involves specific technical implementations such as generating lyrics with GPT-2, composing music using MusicVAE, and employing DiffSinger to create sophisticated media.

The final segment introduces advanced robotic intelligence via the "Toy Robot Scientist" (Weeks 16-20). This module covers system building, knowledge representation, the reasoning phase of the Robot Scientist, and complex planning and analysis. Throughout the course, theoretical concepts are supported by deep dives into the State of the Art, covering topics like morphology papers and the ethics of evolving solutions.

---

### 06_Read_the_evolving_ANNs_paper_Reading_1h_30m

# Read the evolving ANNs paper
Reading • 1h 30m - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/rK6em/read-the-evolving-anns-paper

Here is the paper about evolving neural networks: Miikkulainen, Risto, et al. "Evolving deep neural networks." Artificial intelligence in the age of neural networks and brain computing. Academic Press, 2019. 293-312. Read the paper and see if you can make sense of it! What is the fitness function, for example? This reading is available in the Online Library in the ProQuest collection. Read the evolving ANNs paper Here is the paper about evolving neural networks: Miikkulainen, Risto, et al....

---

### 07_Recap_of_week_10_study_Video_2_min

# Recap of week 10 study
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/AY32A/recap-of-week-10-study

This text provides a conclusion to the "Creatures Case Study" and outlines the technical scope of a comprehensive course on advanced artificial intelligence.

The culmination of the study involved a deep dive into the mechanisms of genetic algorithms (GAs) and evolutionary computing. The speaker, who possesses expertise in this field from their PhD and Masters work, emphasized the importance of understanding the underlying "guts" of these systems. Key learning objectives were successfully met, enabling participants to select and explain current state-of-the-art examples of evolutionary computing. Participants gained real insight into how these biological and bio-inspired systems function from scratch.

The course challenges participants to discuss the significant technical challenges facing evolutionary and bio-inspired computer science. A primary focus of current research involves evolving deep networks and tackling heavy computational tasks. These endeavors aim to make existing processes more efficient and nimble. Ultimately, the goal is to determine if these bio-inspired techniques can compete with the dominant "behemoth of deep learning." Such a revolution, if achieved, could fundamentally change how deep learning is executed.

The curriculum progressed through several distinct phases of AI exploration. The initial segment (Weeks 1-5) focused on AI game players, introducing concepts like formalizing reinforcement learning. This phase included the detailed study and implementation of the Deep Q-Network (DQN) agent. Weeks 6 through 10 centered on Evolving artificial creatures using genetic algorithms.

In this evolution segment, technical tools included pybullet and URDF files for building robots. The framework detailed a genetic encoding scheme, followed by defining fitness functions and selection criteria. Week 10 specifically highlighted the state of the art in evolving morphology, referencing papers on evolving soft robots and evolving Artificial Neural Networks (ANNs).

The syllabus then transitioned into the realm of Generative and Collaborative AI (Weeks 11-15). Topics included generative systems, generating lyrics using GPT-2, music composition via MusicVAE, and diffusion modeling using DiffSinger. This segment culminated in a pop song generator project.

The final major module (Weeks 16-20) introduced "A Toy Robot Scientist." This explored foundational AI concepts, including knowledge representation, system building, and the reasoning phase. The curriculum concluded with analyzing state-of-the-art Robot Scientist projects. The course structure also included required readings, quizzes, and practice assignments corresponding to each weekly topic.

---

### 08_Self-evaluation_checklist_State_of_the_art_in_evolving_morphology_Reading_30_min

# Self-evaluation checklist: State of the art in evolving morphology
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/lDnAu/self-evaluation-checklist-state-of-the-art-in-evolving-morphology

This instructional text outlines a detailed self-assessment for mastering the core concepts of automated design and evolving morphologies in advanced robotic systems. The learning outcomes are categorized into three essential areas: Ethical Questions, Field Challenges, and State-of-the-Art Examples.

Regarding Ethical Questions Around Automated Design, learners must first identify and thoroughly explain various ethical concerns inherent in evolving robotic systems. A crucial component involves understanding the potential societal impacts that automated design can generate. These impacts specifically include issues of inherent bias, ensuring system safety, and establishing clear accountability mechanisms. Furthermore, students are required to critically evaluate complex ethical implications. This evaluation must be applied specifically to case studies involving evolving morphologies and sophisticated neural networks. Finally, the curriculum demands that participants articulate well-supported arguments both for and against deploying automated design in sensitive application fields.

The second focus area addresses the complex Challenges in the Field of Evolving Morphologies. Students must be able to precisely describe the primary technical and practical hurdles encountered when designing evolving robotic morphologies. A significant conceptual requirement is understanding the inherent trade-offs between flexibility, adaptability, and overall system complexity within evolutionary design processes. Moreover, the assessment mandates a discussion of crucial constraints. These constraints cover fabrication difficulties, the limitations of real-world testing, and the pervasive challenge of simulation-to-reality transfer. Learners must also demonstrate the ability to compare different methodologies aimed at overcoming these systemic limitations in evolving morphology systems.

The third area, State-of-the-Art Examples in Evolutionary Computing, focuses on practical application knowledge. Participants must identify and provide detailed explanations of at least two current state-of-the-art examples of evolving robot systems. Crucially, they must describe in detail how neural networks are successfully evolved and subsequently applied within these advanced robotic structures. Understanding the fundamental contribution of modern evolutionary algorithms to overall advancements in robotic design is also a key requirement. The learners must be able to effectively present and justify their chosen examples, clearly explaining their specific significance to the broader field.

Finally, a dedicated Reflection segment prompts the self-assessment of confidence and practical readiness. Learners must evaluate their ability to confidently discuss these intricate topics with both peers and instructors. They must also confirm their capacity to apply the concepts learned during the week to new, unseen case studies or research problems. Lastly, the process requires students to proactively identify any gaps remaining in their understanding, indicating where they plan to seek additional resources for mastery.

---

### 09_Automatic_design_outro_Video_5_min

# Automatic design outro
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/4QnUu/automatic-design-outro

This comprehensive course explores advanced topics across multiple domains of Artificial Intelligence, beginning with Game Playing AI. The initial module (Weeks 1-5) focuses on mastering reinforcement learning, specifically detailing the development and implementation of the Deep Q-Network (DQN) agent for AI game players. This is followed by an intensive study of evolving artificial creatures, dedicated to automatic design methodologies (Weeks 6-10). Key technical concepts here include utilizing genetic algorithms (GAs) for automated morphology design, building robots using simulation tools like PyBullet and URDF files, and defining fitness functions for evolution.

The course then transitions to Generative and Collaborative AI systems (Weeks 11-15), covering various deep learning models for creative applications. Specific examples include generating lyrics using GPT-2, composing music with MusicVAE, and utilizing advanced models like DiffSinger. A major shift occurs with the study of cognitive and robotic AI (Weeks 16-20), focusing on the "Robot Scientist" project. This section delves into building complex systems, knowledge representation, and the crucial reasoning and planning phases necessary for robotic decision-making.

The curriculum integrates ethical considerations across all modules, covering both AI game players and the ethics of evolving solutions. Practical skills are reinforced through required assignments, including quizzes and mid-term coursework related to DQN, GAs, and various AI systems. The final weeks are dedicated to preparation for the culminating examination, synthesizing the knowledge acquired in these diverse fields of AI.

---

### 10_Required_knowledge_and_skills_to_complete_Coursework_1_Reading_10_min

# Required knowledge and skills to complete Coursework 1
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/GtEPW/required-knowledge-and-skills-to-complete-coursework-1

Successful completion of Coursework 1 requires knowledge and practical skills spanning two major topics: Game Playing AI and Evolving Creatures with Genetic Algorithms.

**Topic 1: Game Playing AI (Reinforcement Learning)**
This domain focuses heavily on reinforcement learning, deep Q-learning, and the development of AI agents capable of playing games. Historically, the topic examined past game-playing AI systems, such as Deep Blue and AlphaGo, to understand the motivations driving AI research. Games are formalized mathematically using Markov Decision Processes (MDPs), requiring the understanding of state, action, reward, and transition models. Q-learning is essential for reinforcement learning, relying on value functions and the rigorous framework of Bellman equations.

To implement advanced AI, Deep Q-Networks (DQN) are utilized, allowing neural networks to approximate the Q-value function. Key DQN components include the use of experience replay and target networks for stabilization during training. Practically, DQN agents are built and trained using the Keras library, where understanding the specific DQN loss function and optimization techniques is crucial. Game environments are set up and tested using the OpenAI Gym library, allowing for the development of both random and sophisticated game-playing agents. Further learning involves designing and implementing alternative network architectures for performance comparison.

The societal impact of Game Playing AI is analyzed, discussing the push toward General AI. Furthermore, ethical and social considerations are explored, specifically regarding the impact of human-competitive AI players and AI's evolving role in e-sports and human performance augmentation.

**Topic 2: Evolving Creatures with Genetic Algorithms (Evolutionary Computing)**
This second topic focuses on evolutionary computing and automated design, rooted in bio-inspired computing principles and artificial life. Genetic Algorithms (GA) are central to this field, employing operators like selection, mutation, and crossover to solve complex problems. A specialized area involves evolving morphologies, which guides AI-driven design of physical forms. Genetic encoding schemes are necessary for representing organisms and solutions within the optimization framework.

A vital component is the fitness function, which is designed to evaluate solutions and drives the population-based optimization process. Practically, evolutionary simulations are run and analyzed in PyBullet, specifically for the design of robotic systems. To define these complex robot body structures, the URDF file format is utilized. Genetic manipulation involves applying variation and crossbreeding to evolve the population over generations.

The critical analysis of this topic addresses the ethical implications of automated design and artificial evolution. Technical challenges in evolving AI-driven robots and the state of the art in evolutionary computing are also subjects of study. Mastery of both Game Playing AI and Evolutionary Computing knowledge and skills is necessary for successful Coursework 1 completion.

---

## Week 11

### 01_Introduction_to_AI_and_creativity_case_study_Video_8_min

# Introduction to AI and creativity case study
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/LQKwk/introduction-to-ai-and-creativity-case-study

This case study investigates AI creativity by aiming to build a complete system capable of generating a comprehensive piece of music. The overall objective is to create a system that produces lyrics, melody, and singing almost autonomously, pushing the boundaries of current state-of-the-art AI techniques. The curriculum is structured across five distinct weeks, each focusing on a specific generative component.

Week one introduces generative systems by beginning with the fundamental concept of text generation. Students will build a basic text generator from scratch using a Markov model. This initial step provides a foundational grasp of what a generative system is and the process of training such systems.

Week two escalates the complexity by moving to advanced language modeling systems, specifically GPT-2. This model is utilized for generating lyrical content. GPT-2 is highlighted as a practical choice because it can be trained effectively using consumer-grade GPUs, even running on a CPU. This week also covers the principles of transformers, the underlying neural network architecture used by the model.

The third phase focuses on music composition utilizing the Google Magenta Music VAE neural network. This advanced version of the model can generate complete musical pieces, specifically 16 bars, based on a provided chord progression. A critical concept introduced during this week is the latent space, which allows researchers to map and explore a defined space of creative possibilities.

Week four is dedicated to generating highly complex vocal output by employing a voice synthesis model. This system has been adapted to perform singing, generating human-like, in-tune vocals. The model accepts notes and specific lyrics as prompts

---

### 02_Weekly_Introduction_Video_1_min

# Weekly Introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/5l96y/weekly-introduction

This course explores various facets of advanced artificial intelligence, beginning with Game Playing AI, which covers the formalization of reinforcement learning and the implementation of the Deep Q-Network (DQN) agent. The initial modules also focus on AI tooling, state-of-the-art methodologies, and the ethical considerations surrounding AI game players. Next, the curriculum shifts to Evolving Artificial Creatures, detailing automatic design using genetic algorithms, and the construction of robots leveraging platforms like pybullet and URDF files. This segment delves into the core mechanics of evolution, including genetic encoding schemes, fitness function development, and sophisticated selection processes in morphology evolution.

The course then transitions to Generative and Collaborative AI, introducing foundational generative systems and techniques like Markovian text generators. This section further explores advanced generative capabilities through specific models, including using GPT-2 for lyrics generation, MusicVAE for composition, and DiffSinger. The final major module, "A Toy Robot Scientist," focuses on building complex reasoning systems. This involves establishing the system architecture, detailed knowledge representation, and the crucial reasoning and planning phases. The material covers the legal and ethical perspectives of AI systems throughout these applications. Overall, the course progresses from foundational machine learning to sophisticated generative models and autonomous robotic reasoning.

---

### 03_Slides_for_week_11_Reading_30_min

# Slides for week 11
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/1ErwQ/slides-for-week-11

This course structure outlines a progression through various advanced topics in Artificial Intelligence, culminating in exam weeks 21 and 22. The initial module (Weeks 1-5) focuses on Game Playing AI, detailing formal reinforcement learning and the implementation of the DQN agent. The next phase (Weeks 6-10) explores evolving artificial creatures, utilizing genetic algorithms and specific tools like pybullet and URDF files for building robots. Key concepts in this phase include the genetic encoding scheme, fitness function, and state-of-the-art morphology research.

Weeks 11 through 15 are dedicated to Generative and Collaborative AI, starting with an introduction to generative systems, including a worked example. This section includes hands-on coding up a Markovian text generator and training it, followed by advanced applications. These applications feature generating lyrics with GPT-2, music composition using MusicVAE, and employing DiffSinger technology.

The final research module (Weeks 16-20) centers on "A toy Robot Scientist," covering its history, legal, and ethical issues. This involves building the system, knowledge representation, and introducing the robot scientist’s reasoning phase for planning and analysis. The schedule includes extensive supplementary materials like weekly videos, quizzes, and coding challenges, such as the 1-hour Markov model challenge. All key technical areas, from deep reinforcement learning to advanced diffusion models, are covered before the exam preparation begins.

---

### 04_Introduction_to_generative_systems_Video_13_min

# Introduction to generative systems
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Rn9iQ/introduction-to-generative-systems

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 05_Worked_example_of_a_generative_system_Video_9_min

# Worked example of a generative system
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/9MVSq/worked-example-of-a-generative-system

This course provides a comprehensive exploration of advanced AI disciplines, beginning with Game Playing AI (Weeks 1-5). This section formalizes reinforcement learning (RL) and focuses on the development and implementation of the Deep Q-Network (DQN) agent, concluding with an analysis of the state-of-the-art and ethical concerns in AI game players. The curriculum then shifts to evolutionary computing, dedicated to creating and evolving artificial creatures (Weeks 6-10). This involves utilizing genetic algorithms, constructing robots using simulation tools like pybullet and URDF files, and defining rigorous fitness functions and selection criteria.

The next major thematic block focuses on Generative and Collaborative AI (Weeks 11-15). Topics begin with practical applications, such as coding a Markovian text generator, and advance to sophisticated models like GPT-2 for lyric generation. Furthermore, the study covers advanced music composition using models such as MusicVAE and DiffSinger, culminating in a full pop song generator project.

Finally, the course addresses complex problem-solving with the "Robot Scientist" framework (Weeks 16-20). This advanced segment details building the entire system, focusing heavily on knowledge representation, the reasoning phase, and complex planning and analysis. The program concludes with intensive exam preparation (Weeks 21-22), synthesizing the principles of game playing, evolution, generative systems, and robotic intelligence.

---

### 06_Coding_up_a_Markovian_text_generator_and_training_it_Video_13_min

# Coding up a Markovian text generator and training it
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/x92Ii/coding-up-a-markovian-text-generator-and-training-it

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 07_Recap_of_week_11_study_Video_55_sec

# Recap of week 11 study
Video • 55 sec - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/nHJST/recap-of-week-11-study

This course structure spans various advanced topics in Artificial Intelligence, beginning with specialized game-playing AI and formalizing reinforcement learning using the DQN agent. Early modules focus on building AI game players, moving through tooling and implementation, and concluding with a review of the state of the art and ethical considerations in this domain. Next, the curriculum shifts to "Evolving Artificial Creatures," detailing the use of genetic algorithms for automatic design and the construction of robots via pybullet and URDF files. This evolutionary segment elaborates on the genetic encoding scheme, fitness function design, and the current state of evolving morphology.

The focus then transitions to Generative and Collaborative AI, starting with an introduction to generative systems and culminating in the practical coding of a Markovian text generator. This theme deepens into specific generative models, including generating lyrics using GPT-2, composing music with MusicVAE, and employing DiffSinger. The journey concludes with a comprehensive project on a "Toy Robot Scientist," which explores knowledge representation, reasoning phases, planning, and ethical implications. This final section brings together planning and state-of-the-art robot scientist projects, providing a holistic overview of advanced AI applications.

---

### 08_Self-evaluation_checklist_Part_1_-Introduction_to_Generative_Systems_Reading_30_min

# Self-evaluation checklist: Part 1 -Introduction to Generative Systems
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/BJGTB/self-evaluation-checklist-part-1-introduction-to-generative-systems

Use this checklist to assess whether you have met the expected learning outcomes for this week. 1. Understanding the AI and Creativity Case Study ☐ I can describe the overall plan for the AI and creativity case study. ☐ I understand the key steps involved in the case study and how they will build upon each other over the next few weeks. ☐ I can explain how generative systems relate to the case study and what role they play in creative applications. 2....

---

## Week 12

### 01_Weekly_Introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_Slides_for_week_12_Reading_10_min

# Slides for week 12
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/ayKws/slides-for-week-12

This curriculum outlines a comprehensive 22-week journey through advanced AI concepts, starting with specialized domains. The initial phase (Weeks 1-5) focuses on Game Playing AI, progressing from basic game player theory to formalized Reinforcement Learning and the implementation of the DQN agent. The subsequent section (Weeks 6-10) delves into "Evolving Artificial Creatures," covering automatic design using genetic algorithms, building robots with PyBullet and URDF files, and defining fitness functions for evolving morphology. Weeks 11-15 transition into Generative and Collaborative AI, introducing generative systems, exploring the core technology of the Transformer, and focusing heavily on GPT-2 for generating lyrics. This phase includes detailed instruction on working with GPT-2, fine-tuning, and applying these generative models to music composition using MusicVAE and DiffSinger. The final major component (Weeks 16-20) explores a "Toy Robot Scientist," covering its introduction, knowledge representation, reasoning phase, planning/analyzing mechanisms, and state-of-the-art projects. The curriculum concludes with dedicated weeks for exam preparation and the final exam. Key technical concepts covered span DQN, Genetic Algorithms, URDF, MusicVAE, DiffSinger, and the mechanics of the Transformer and GPT-2. The entire sequence progresses from focused agent behavior (DQN) to self-modification (Genetic Algorithms) and finally to creative generation (GPT-2, MusicVAE).

---

### 03_What_is_a_transformer_Video_12_min

# What is a transformer?
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Tdfzb/what-is-a-transformer

This curriculum covers four major areas of advanced AI: Game Playing, Evolution, Generative AI, and Robotic Systems. The initial phase (Weeks 1-5) focuses on Game Playing AI, formally introducing Reinforcement Learning and detailing the implementation of the Deep Q-Network (DQN) agent. The curriculum then shifts to Evolving Artificial Creatures (Weeks 6-10), utilizing genetic algorithms for automatic design and robot building, often involving PyBullet and URDF files for morphological evolution. The Generative and Collaborative AI section (Weeks 11-15) introduces modern systems like transformers, focusing heavily on generating lyrics using GPT-2. Subsequent learning explores advanced generative models, including MusicVAE and DiffSinger, to facilitate music composition and create pop song generators. Weeks 16 through 20 are dedicated to "A Toy Robot Scientist," covering system building, knowledge representation, and advanced reasoning and planning phases for sophisticated robotic agents. The overall program maintains a strong emphasis on technical detail, integrating specific models like DQN, GPT-2, MusicVAE, and DiffSinger. The course consistently addresses the State of the Art, discussing relevant ethics and legal issues across all modules. The structured learning includes dedicated practice assignments, videos explaining concepts like "What is a transformer?", and lab work with GPT-2. The final weeks involve comprehensive review and exam preparation. This comprehensive study offers deep technical dives into how complex systems are designed, trained, and implemented.

---

### 04_GPT-2_Video_11_min

# GPT-2
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/XcZrZ/gpt-2

GPT-2, an advanced language model developed by OpenAI, was initially withheld from public release due to severe societal concerns regarding its malicious potential. In 2019, creators stated they would not release the trained model because of worries about

---

### 05_Fine_tuning_GPT-2_Video_20_min

# Fine tuning GPT-2
Video • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/v20GM/fine-tuning-gpt-2

This course trajectory covers various advanced fields of Artificial Intelligence, beginning with game playing AI and reinforcement learning (RL) in Weeks 1 through 5. The initial phase focuses on formalizing RL and implementing the Deep Q-Network (DQN) agent, alongside an exploration of the state of the art and AI ethics in game players. The curriculum then shifts to evolving artificial creatures (Weeks 6-10), introducing genetic algorithms for automatic design, and building robots using frameworks like Pybullet and defining physical structures with URDF files. The module detailing genetic encoding and fitness functions explores the sophisticated processes required for evolving morphology. A significant block is dedicated to generative and collaborative AI (Weeks 11-15), starting with generative systems and the foundational concepts of transformers. Practical application includes generating lyrics using GPT-2, fine-tuning the model, and exploring advanced music composition with MusicVAE and DiffSinger. Subsequently, the course delves into advanced autonomous systems through the "Toy Robot Scientist" project (Weeks 16-20). This segment covers knowledge representation, building the system, and implementing the sophisticated reasoning and planning phases of the AI. Throughout these modules, specialized topics such as AI tooling, state-of-the-art projects, and legal/ethical issues are addressed. The focus moves from individual agents (DQN) to system-level collaboration (Generative/Collaborative AI). The program culminates with dedicated preparation and exam periods in Weeks 21 and 22.

---

### 06_Recap_week_12_study_Video_1_min

# Recap week 12 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/7gKJd/recap-week-12-study

This curriculum review concludes Week 2, focusing heavily on generative AI models and their practical application in generating creative content, specifically song lyrics. The primary model studied during this week was GPT-2, a significant language model within the realm of transformer networks. Review objectives covered several critical technical concepts relating to modern deep learning architectures. One core objective was detailing how the self-attention mechanism functions within transformer networks. This mechanism is crucial because it allows the model to effectively combine complex contextual and sequential data elements.

A second key objective involved the practical implementation of language generation. Specifically, learners were required to instantiate a pre-trained language generation pipeline utilizing GPT-2 and the Hugging Face API. This process serves as the "nuts and bolts" guide for utilizing advanced, pre-trained models in real-world tasks.

The third essential learning objective centered on the concept of fine-tuning. Students needed to explain the mechanism of fine-tuning and the necessity of this process for pre-trained neural networks such as GPT-2. Fine-tuning adapts the generalized knowledge of the large pre-trained model to specific, desired application domains.

Looking forward, Week 3 shifts the focus from language generation to music generation. The next major model to be explored is the Music VAE (Variational Autoencoder) developed by Google Magenta. This model is designed to generate complete, coherent pieces of music.

The broader curriculum provides a detailed roadmap spanning many weeks, covering various domains of artificial intelligence. Weeks 1 through 5 are dedicated to AI Game Playing, starting with formalizing reinforcement learning and the Deep Q-Network (DQN) agent. Weeks 6 through 10 are dedicated to Evolving Artificial Creatures, addressing automatic design using genetic algorithms. This section progresses into building robots using pybullet and URDF files, and later explores genetic encoding schemes and fitness functions.

The central theme, Generative and Collaborative AI, begins in Week 11. Week 12 serves as a major module, focusing on generating lyrics with GPT-2, alongside theoretical deep dives into what a transformer is. Further technical training during this period includes study on GPT-2 and specialized training on fine-tuning GPT-2.

The curriculum continues its exploration of generative models in Weeks 13 through 15. Week 13 covers Music composition using MusicVAE. Week 14 introduces DiffSinger, another advanced generative system. Week 15 culminates these concepts by integrating them into a comprehensive pop song generator project.

The later stages of the curriculum transition to a complex, multi-faceted project known as "A toy Robot Scientist," spanning Weeks 16 through 20. This project delves into introductory history, perspectives, legal, and ethical issues related to robotics. Subsequent phases cover system building, knowledge representation, and the introduction of the Robot Scientist reasoning phase. The final weeks are dedicated to academic preparation, including Week 21 for exam preparation and Week 22 for the final examination.

---

### 07_Self-Evaluation_Checklist_Part_2_-_Generating_lyrics_with_GPT-2_Reading_30_min

# Self-Evaluation Checklist: Part 2 - Generating lyrics with GPT-2
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/mcg8x/self-evaluation-checklist-part-2-generating-lyrics-with-gpt-2

This document outlines a comprehensive set of learning objectives focusing on advanced Natural Language Processing (NLP) concepts. The core focus is on adapting pre-trained models and understanding the foundational architecture of modern Transformer networks.

A primary concept is fine-tuning in neural networks. Fine-tuning is defined as the process of improving pre-trained models. It plays a crucial role in enabling models to perform highly specific tasks. Specifically, fine-tuning is necessary when adapting a general-purpose language model, such as GPT-2, to generate specific text types, like song lyrics. Learners must understand the trade-offs between modifying a model versus simply using it unmodified. Furthermore, identifying key hyperparameters and settings is critical for optimizing fine-tuning performance.

The practical application utilizes the Hugging Face transformers library for working with GPT-2. Successful implementation requires instantiating a complete text generation pipeline. The Hugging Face API is composed of essential components, including tokenization and model selection. Using GPT-2 involves generating text and manually adjusting parameters to control output quality. Parameters like temperature and max\_length are key controls for output variability. Experimentation with varied prompts helps observe how GPT-2 generates diverse and varied lyrical outputs.

The theoretical underpinning of these models lies in the Transformer network and its self-attention mechanism. Self-attention enables transformers, like GPT-2, to process words while maintaining deep contextual meaning. This mechanism allows the model to weigh the importance of different words in a sentence. The self-attention design differs significantly from traditional sequence-based models like Recurrent Neural Networks (RNNs) and Long Short-Term Memory networks (LSTMs). Transformers are widely recognized as being exceptionally well-suited for complex text generation tasks compared to older architectural models.

Advanced explorations include the practical fine-tuning of GPT-2 using a custom dataset of song lyrics. Users compare the resultant output from a fine-tuned GPT-2 model against the baseline performance of the original base model. This involves comparing performance metrics to assess the model's specialization. Learning also requires experimentation with alternative text-generation models, such as GPT-3, T5, and BERT.

Finally, the entire learning process emphasizes self-evaluation and reflection. This critical stage involves assessing areas of confidence and identifying where further practice is needed. Learners must formulate strategies to deepen their understanding of complex NLP topics and revisit materials to close any identified gaps in knowledge.

---

## Week 13

### 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_Slides_for_week_13_Reading_30_min

# Slides for week 13
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/qnqmd/slides-for-week-13

This text outlines a comprehensive curriculum detailing the progression of topics in Artificial Intelligence, spanning several weeks. The course begins by covering foundational AI topics, dedicating Week 1 to "Game playing AI: Part 1" and Week 2 to "Part 2 - Formalising reinforcement learning and the DQN agent." Subsequent weeks elaborate on AI capabilities, including "Part 3 - Game playing AI tooling" (Week 3) and the "Implementation of the DQN agent" (Week 4).

The curriculum then shifts focus to biological and physical AI in Weeks 6 through 10, exploring "Evolving artificial creatures." This section covers automatic design using genetic algorithms (Week 6), building robots with pybullet and URDF files (Week 7), genetic encoding schemes (Week 8), and fitness function and selection (Week 9). Week 10 provides a state-of-the-art review of evolving morphology.

The course transitions into generative and collaborative AI in Week 11, introducing generative systems. Week 12 focuses on practical generation, specifically "Generating lyrics with GPT-2." Week 13 introduces the core technical topic of music composition using MusicVAE, detailing its history and underlying concepts like latent spaces.

Week 13 includes extensive assignments and resources, such as videos on "Music composition with MusicVAE," "Exploring latent space," and working with MusicVAE and Fluidsynth. Further specialized topics in generative AI include "Generative and collaborative AI: Part 4 - DiffSinger" (Week 14) and "Part 5 - Putting it all together and pop song generator" (Week 15).

The latter half of the schedule dedicates significant time to robotics and ethical considerations. Weeks 16 through 20 delve into "A toy Robot Scientist," covering its introduction, building the system, knowledge representation, reasoning, and planning capabilities. The final weeks are dedicated to practical culmination, with Week 21 for exam preparation and Week 22 being the exam week.

---

### 03_Potted_history_of_automated_music_composition_Video_17_min

# Potted history of automated music composition
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/OEinx/potted-history-of-automated-music-composition

This transcript details a "potted history" of automated music composition using computers, charting the evolution of the field from the 1950s into the 2020s. The talk emphasizes the shift from simple algorithmic composition to complex, interactive, and generative AI systems.

Here is a detailed summary of the key movements and technological advancements discussed:

---

### 🎼 Core Thesis: Evolution from Algorithm to Collaborator

The central theme is the progression of computer music systems: they have moved from being simple tools that run a predetermined algorithm to becoming sophisticated, real-time interactive collaborators capable of understanding, mimicking, and generating complex musical structures.

### 🎷 Key Movements and Milestones

The speaker breaks down the history by different contributing schools of thought and eras:

#### 1. Interactive Improvisation and Jazz (The 2000s)
*   **Key Figure:** **Jorge Lewis** (a jazz performer and computer scientist).
*   **Technology:** The **Voyager** system.
*   **Significance:** This system represents a major leap because it was not simply *composing*; it engaged in a **real-time dialogue** with human improvisers. A computer program analyzed the performers' actions instantly to guide an automatic composition, acting as a true collaborator.

#### 2. Popular Electronic and Rhythm Music (1980s & 1990s)
*   **Focus:** Applying algorithms to genres often excluded from classical academia, such as techno, house, and drum and bass.
*   **Key Figure:** **Nick Collins**.
*   **Significance:** Collins focused on modeling complex rhythmic patterns, specifically attempting to recreate the intricate, chopped **break beat patterns** found in artists like Aphex Twin and Square Pressure. This demonstrated the application of algorithms to the unique science of electronic rhythm.

#### 3. Stylistic Modeling and Composition (The Mid-Range Development)
*   **Key Figure:** **François Pasha** (and his work at Brio and Panache).
*   **Significance:** Research here focused on **analyzing musical style** and building models that could then compose *in the style of* a given artist or genre. This laid the groundwork for modern generative AI.

#### 4. The Deep Learning Revolution: Raw Audio Generation (The 2010s & 2020s)
*   **Key System:** **OpenAI Jukebox**.
*   **Significance:** This represents the most radical shift. Instead of generating sheet music or musical scores that are then rendered, Jukebox works with **raw audio** at the sample or frequency frame level. It can generate complex audio—for instance, singing and lyrics in the style of Frank Sinatra—after being trained on massive datasets of music using huge farms of GPUs.

### 💡 Current State and Open Challenges

Despite the rapid advancements, the speaker stresses that the field is not complete. Current research faces several **open challenges**:

1.  **Control:** Maintaining precise control over the output.
2.  **Structure:** Ensuring the generated music has cohesive, long-term architectural integrity.
3.  **Creativity:** Moving beyond replication to genuine, novel innovation.
4.  **Interactivity:** Developing systems that fluidly and intelligently respond to external human input.

### ➡️ Conclusion

The talk serves as a comprehensive overview of computer music composition, illustrating that the field has successfully integrated diverse streams—jazz, dance culture, and cutting-edge machine learning—to create powerful, evolving tools for musical creation.

---

### 04_Introduction_to_latent_spaces_Video_12_min

# Introduction to latent spaces
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/8oVeH/introduction-to-latent-spaces

The curriculum begins with an intense focus on AI game playing, starting with an overview in Week 1 and progressing to the formalization of reinforcement learning and the implementation of the Deep Q-Network (DQN) agent in Week 2 and 4. Week 3 introduces critical tooling for game playing AI, followed by a discussion of the state of the art and ethical considerations in AI game players during Week 5. The focus then shifts to evolving artificial creatures, dedicating several weeks to autonomous design via genetic algorithms (Week 6).

In the evolutionary robotics segment, specific technical aspects are covered, including building robots using pybullet and URDF files (Week 7), the development of a genetic encoding scheme (Week 8), and defining the fitness function and selection methods (Week 9). Weeks 10 and 11 explore the state of the art in evolving morphology and introduce the foundational concepts of generative systems.

The third major unit, Generative and Collaborative AI, begins in Week 12, exploring lyric generation using GPT-2. A deep dive into music composition follows in Week 13, focusing specifically on MusicVAE and its mechanisms. This week involves multiple associated resources, including videos on latent spaces, MusicVAE functionality, and rendering audio with fluidsynth.

Weeks 14 and 15 continue the generative theme, examining advanced systems like DiffSinger and synthesizing the knowledge into a complete pop song generator. The final major segment is dedicated to "A Toy Robot Scientist," starting with an introduction to its history, legal, and ethical issues (Week 16).

The subsequent weeks detail the construction of the system, knowledge representation, and the Robot Scientist’s reasoning and planning phases (Weeks 17-19). Week 20 presents a survey of state-of-the-art Robot Scientist projects, leading into Week 21 for exam preparation and Week 22 for the exam itself. A preliminary topic, 'Introduction to latent spaces,' also appears as a supplemental module.

---

### 05_What_is_Music-VAE_Video_13_min

# What is Music-VAE?
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/xjrPg/what-is-music-vae

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 06_Javascript_and_promises_Video_7_min

# Javascript and promises
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/aU3tD/javascript-and-promises

The course is structured across multiple modules, beginning with Game Playing AI (Weeks 1-5), which covers foundational concepts and advanced implementations. Early modules introduce reinforcement learning and formally develop the Deep Q-Network (DQN) agent, culminating in practical implementation and analysis of state-of-the-art AI game players and their ethical implications. The second major theme, Evolving Artificial Creatures (Weeks 6-10), focuses on automatic design through genetic algorithms. This section details the use of pybullet and URDF files for robotic implementation, establishing a genetic encoding scheme, and defining fitness functions for morphology evolution. The Generative and Collaborative AI module (Weeks 11-15) explores systems designed to create novel content. Specific applications include generating lyrics using GPT-2 and advanced music composition using MusicVAE. The MusicVAE section provides deep technical dives, including explorations of latent spaces, rendering audio via fluidsynth, and the use of DiffSinger. The final module, "A Toy Robot Scientist" (Weeks 16-20), addresses complex reasoning and autonomous system construction. This module covers knowledge representation, the system's reasoning phase, and sophisticated planning and analysis capabilities. The curriculum concludes with dedicated weeks for exam preparation and the final exam.

---

### 07_Working_with_MusicVAE_Video_8_min

# Working with MusicVAE
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/tdvx2/working-with-musicvae

This technical summary details the workflow for utilizing MusicVAE, a generative musical library, demonstrating the steps from environment setup to latent space sampling and output analysis.

The process begins with preparation, requiring the installation of necessary node modules via `npm install`, which serves as the dependency manager, analogous to `pip install` in Python. Following this, a local web server must be initialized, as the MusicVAE JavaScript library depends on serving its models from a web source. This local server, often running on port 8080, allows the model files—which can include complex multi-track models (e.g., 8/16 part models with bass, drums, and melody)—to be downloaded.

The core workflow involves loading a specific MusicVAE model, such as a one-bar or 16-bar model, into the script environment. The model is instantiated and requires a URL pointing to the newly created local web server for access.

---

### 08_Rendering_audio_with_MusicVAE_and_fluidsynth_Video_15_min

# Rendering audio with MusicVAE and fluidsynth
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/mlF83/rendering-audio-with-musicvae-and-fluidsynth

This curriculum outlines a comprehensive study across four major areas of artificial intelligence: Game Playing, Evolutionary Design, Generative Systems, and Embodied Robotics.

The initial focus covers Game Playing AI, beginning with Week 1, followed by Week 2, which formalizes reinforcement learning and introduces the Deep Q-Network (DQN) agent. Weeks 3 and 4 detail the necessary tooling and implementation of the DQN agent, concluding the section with Week 5, which addresses the state of the art and ethical considerations of AI game players.

The second major pillar is Evolving Artificial Creatures, a section spanning Weeks 6 through 10. This includes automatic design using genetic algorithms (GA), robot construction utilizing Pybullet and URDF files, and defining the genetic encoding scheme. Weeks 9 and 10 focus specifically on optimizing the fitness function and examining the state of the art in evolving morphology.

The study then transitions to Generative and Collaborative AI (Weeks 11-15). Week 12 explores generating lyrics using GPT-2, while Week 13 dives deep into music composition using MusicVAE. This module includes extensive materials covering latent spaces, working with MusicVAE, rendering audio with Fluidsynth, and various practice assignments.

The advanced generative section continues in Week 14 with DiffSinger, and Week 15 synthesizes these tools into a complete pop song generator.

Finally, the course introduces the concepts of a Toy Robot Scientist (Weeks 16-20). This area covers the system's history, legal and ethical issues, and the crucial task of building the system and defining knowledge representation. The latter weeks focus on introducing the Robot Scientist reasoning phase, planning, and analyzing complex scenarios.

The program culminates in Week 21 for exam preparation and Week 22 for the final examination.

---

### 09_Exploring_latent_space_Video_12_min

# Exploring latent space
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/8l1lb/exploring-latent-space

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 10_Recap_of_week_13_study_Video_1_min

# Recap of week 13 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/ldOyP/recap-of-week-13-study

This curriculum spans various advanced domains of Artificial Intelligence, beginning with Game Playing AI. Weeks 1 through 5 focus on the development and formalization of reinforcement learning (RL) agents. This segment details the application of the DQN agent, covering its theoretical formalization and subsequent practical implementation. Additional topics in this phase include dedicated study on game playing AI tooling and the ethical considerations surrounding AI game players. The focus then shifts to evolving artificial creatures, commencing in Week 6. Weeks 6 through 10 concentrate on automatic design using genetic algorithms (GAs). Specific technical details involve building robots using frameworks like pybullet and implementing URDF files. The subsequent focus covers the genetic encoding scheme, fitness function definition, and selection processes in evolutionary computation. Generative and collaborative AI forms the next major block, spanning Weeks 11 through 15. The course introduces generative systems and explores lyrics generation using GPT-2. A significant portion is dedicated to music composition using MusicVAE, which involves understanding latent spaces. Weekly Week 13 resources provide comprehensive study materials, including a 1-minute introduction video and a 30-minute reading on the history of automated music composition. Practical assignments include quizzes and working with MusicVAE, rendering audio via fluidsynth, and exploring the latent space. Week 14 introduces DiffSinger as a major generative model. The module concludes by integrating all concepts into a pop song generator. Finally, the course addresses sophisticated autonomous agents through the "A toy Robot Scientist" module (Weeks 16-20). This covers the system's introduction, knowledge representation, reasoning phase, and planning/analyzing capabilities. The program culminates in Week 21 as exam preparation and Week 22 as the final exam period.

---

### 11_Self-evaluation_checklist_Part_3_-_Music_composition_with_MusicVAE_Reading_30_min

# Self-evaluation checklist: Part 3 - Music composition with MusicVAE
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/GdtcT/self-evaluation-checklist-part-3-music-composition-with-musicvae

This self-evaluation checklist assesses the learning outcomes for Week 13, Part 3, focusing on Music Composition using MusicVAE. The central focus involves understanding and applying advanced machine learning models for creative music generation.

**Outcome 1: Practical Implementation of MusicVAE**
The first outcome covers the practical use of the MusicVAE model in Google Magenta. Specifically, the learner must demonstrate the ability to successfully load a pre-trained MusicVAE model. A key skill involves using this model to generate multi-track MIDI files. Furthermore, the learner must be proficient in modifying various parameters to influence and steer the characteristics of the generated musical output. The process includes saving and exporting the generated MIDI files for external use. Finally, a critical practical step involves applying sound fonts to convert the generated MIDI files into audible sound, making the composition playable.

**Outcome 2: Understanding the Latent Space**
The second outcome centers on describing the critical concept of a latent space within machine learning. A latent space is defined as a compressed, abstract representation of data. In the context of music generation, this space effectively represents all possible variations and styles within the musical dataset. Exploring this latent space allows for significant creative flexibility. Crucially, the ability to manipulate this latent space enables interpolation between two distinct musical styles, leading to novel compositions. Learners must demonstrate practical methods for manipulating this space to create entirely new music.

**Outcome 3: Exploring Variational Auto-encoders (VAEs)**
The third outcome requires a thorough explanation of the Variational Auto-encoder (VAE). Learners must be able to describe the unique structure and function of a VAE. It is important to understand the fundamental differences between a standard auto-encoder and a VAE. VAEs are prized for creative applications because they inherently model the probability distribution of the data. This probabilistic nature makes them ideal for generating creative outputs like music. Beyond music, the learner must provide examples of real-world applications of VAEs in other domains.

**Synthesis and Reflection**
This comprehensive checklist serves as a mechanism to gauge the learner's understanding and identify areas needing further practice. Reflective questions encourage deeper critical thinking regarding the process. These questions include analyzing challenges faced during MusicVAE generation and detailing solutions implemented. They also prompt consideration of how VAEs and latent spaces can be applied to non-musical fields, such as visual art or text generation. Finally, the reflection encourages identifying specific improvements to the MIDI generation process to achieve higher musical quality.

---

## Week 14

### 01_Weekly_introduction_Video_2_min

# Weekly introduction
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/UamSO/weekly-introduction

This course structure covers a broad spectrum of advanced AI topics, beginning with Game Playing AI, formalizing concepts like Reinforcement Learning and the DQN agent (Weeks 2-4). The initial modules introduce tooling for Game Playing AI and focus on the implementation of the Deep Q-Network (DQN) agent. Following this foundation, the curriculum transitions into the study of Evolving Artificial Creatures (Weeks 6-10). These segments explore automatic design using genetic algorithms and build sophisticated robots utilizing PyBullet and URDF files.

The later phase focuses on Generative and Collaborative AI, establishing the groundwork with generative systems (Week 11). Key techniques introduced include generating lyrics using GPT-2 and performing music composition via MusicVAE. The most advanced area covered is speech and vocal synthesis, highlighted in Week 14. The Week 4 content introduces a challenging, state-of-the-art speech synthesis model, current for 2021-2022 research.

Learning objectives for this week include providing historical examples of speech synthesis systems, such as the singing generated by HAL 9000 from *2001*. Furthermore, students must gain an insight into the substantial complexity of modern speech synthesis research. The practical focus involves using a pre-trained speech synthesis model coupled with pitch correction technology. This process generates singing voices from specific inputs: a list of desired lyrics and corresponding musical notes.

The output of this system is a rendered audio file, which can be visualized as a spectral spectrogram. A major technical model discussed in this area is DiffSinger. The course is highly comprehensive, progressing to include a "Pop Song Generator" in Week 15. Subsequent weeks cover specialized AI applications, including a "Toy Robot Scientist" module (Weeks 16-20). This final segment delves into knowledge representation, system building, reasoning, and planning within robotic systems. Throughout the course, students engage with complex assignments, including experiments with DiffSinger and self-evaluation checklists.

---

### 02_Slides_for_week_14_Reading_30_min

# Slides for week 14
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/0fw1u/slides-for-week-14

This document outlines a 22-week course progression spanning major areas of Artificial Intelligence. The initial phase, Weeks 1 through 5, focuses on Game Playing AI, beginning with general AI player concepts and formalizing Reinforcement Learning. Key technical development in this section involves the Deep Q-Network (DQN) agent, which is studied in detail across Weeks 2, 3, and 4. The program then shifts to Evolving Artificial Creatures (Weeks 6-10), exploring automatic design using genetic algorithms. This phase includes detailed studies on genetic encoding schemes, fitness functions, and applying concepts to build robots using tools like Pybullet and URDF files. The focus subsequently transitions to Generative and Collaborative AI, starting with introductory generative systems in Week 11. Weeks 12 and 13 cover specialized generative tasks, such as generating lyrics with GPT-2 and music composition using MusicVAE. A major deep dive occurs in Week 14, which is dedicated to DiffSinger, an advanced topic involving weekly video lectures, readings, and multiple practice assignments. The course continues Generative AI in Week 15 by putting concepts together to create a pop song generator. The final major thematic block, Weeks 16 through 20, is dedicated to "A Toy Robot Scientist." This segment covers the introduction, history, legal, and ethical issues of robotics, and details the system's knowledge representation and reasoning phases. The syllabus concludes with Week 21 as an exam preparation week, followed by Exam Week 22.

---

### 03_Speech_and_vocal_synthesis_Video_12_min

# Speech and vocal synthesis
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Untn2/speech-and-vocal-synthesis

This course spans several major AI domains, starting with game playing AI (Weeks 1-5). Initially, it covers general AI game players, progressing to the formalization of reinforcement learning and the specific implementation of the Deep Q-Network (DQN) agent (Weeks 2-4). The focus then shifts to evolution and morphology, exploring how automatic design is achieved using genetic algorithms and how robots are built using tools like pybullet and URDF files (Weeks 6-10). The subsequent section explores generative and collaborative AI, introducing generative systems, generating lyrics using GPT-2, and composing music with MusicVAE (Weeks 11-13). A major technical focus is placed on DiffSinger, covering its models and practical application, including experiments with singing results (Week 14). The curriculum then tackles the "A Toy Robot Scientist" project, detailing system building, knowledge representation, and the AI reasoning and planning phases (Weeks 16-19). Further state-of-the-art projects and ethical considerations are addressed throughout the specialized modules (Weeks 5, 10, 20). The course culminates in a comprehensive review and examination preparation period (Week 21-22).

---

### 04_Background_for_diffsinger_Video_10_min

# Background for diffsinger
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/uqKYi/background-for-diffsinger

This video provides an essential background on DiffSinger, an advanced system in the field of speech and vocal synthesis. The core function of DiffSinger is to generate singing audio based on user input. Specifically, a user provides the lyrics as a property, along with the precise musical notes and the desired duration. This input allows the system to generate a sung rendition of the provided words.

The scope of this work places speech synthesis among the most complex machine learning tasks. This complexity stems from its multi-domain nature, integrating language, musical, and synthesis domains, along with issues of expressiveness. The field is highly technical, requiring deep engagement with state-of-the-art (SOTA) research from 2022.

The presenter outlines a challenging process to make the SOTA singing synthesis model cross-platform and functional. This process involved extensive reading of research papers to identify the state of the art. Subsequently, the presenter had to search for and test various source code repositories to determine their viability. A major technical hurdle was obtaining code written with older versions of TensorFlow and various libraries, making successful installation difficult.

To address these challenges, a specific working implementation was located, built upon various complex systems. Key technical concepts must be understood to grasp the system's operation. An "embedding" is defined as a method to reduce high-dimensional data into a meaningful, more exploratory space. "Convolutional networks" are filters trained to process signal data, such as images, video, and sound. "Transformers," noted in

---

### 05_Diffsinger_models_Video_12_min

# Diffsinger models
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Aqg9o/diffsinger-models

This curriculum covers four major domains of advanced AI, beginning with Game Playing AI (Weeks 1-5). Early focus involves formalizing reinforcement learning and implementing the Deep Q-Network (DQN) agent to build sophisticated game players. The next major block, Evolving Artificial Creatures (Weeks 6-10), explores automatic design using genetic algorithms to build functional robots. This involves specific technical tools like pybullet and URDF files, focusing on genetic encoding schemes and fitness functions for evolving morphology.

Generative and Collaborative AI takes center stage from Week 11, introducing systems like GPT-2 for lyric generation and MusicVAE for music composition. A significant portion is dedicated to DiffSinger (Weeks 13-15), covering its models, working principles, and applications in speech and vocal synthesis. This module includes extensive practice assignments and experiments with the DiffSinger lab.

The study then shifts to complex reasoning with "A toy Robot Scientist" (Weeks 16-20). This module examines knowledge representation, system building, and the specialized reasoning and planning phases of intelligent robots. The entire course culminates in dedicated exam preparation and the final examination week.

---

### 06_Working_with_diffsinger_Video_12_min

# Working with diffsinger
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/PJ6jn/working-with-diffsinger

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 07_Recap_of_week_14_study_Video_2_min

# Recap of week 14 study
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Ne2ZT/recap-of-week-14-study

This curriculum progresses through several advanced areas of artificial intelligence, starting with AI game playing (Weeks 1-5). Initial focus covers the development of AI game players, transitioning to the formalization of reinforcement learning and the implementation of the Deep Q-Network (DQN) agent. The study then shifts to evolving artificial creatures (Weeks 6-10), utilizing genetic algorithms for automatic design and building robots via pybullet and URDF files, while defining fitness functions and selection schemes. Weeks 11 through 15 focus on generative and collaborative AI, introducing systems like GPT-2 for generating lyrics and MusicVAE for music composition. A detailed module on DiffSinger is covered extensively, including specific videos on models, working with DiffSinger, and a practical lab experiment for singing results. The curriculum then tackles "A toy Robot Scientist" (Weeks 16-20), exploring its history, legal and ethical issues, knowledge representation, and the subsequent reasoning and planning phases. The final week (Week 21) is dedicated to exam preparation, culminating in the examination during Week 22.

---

### 08_Self-evaluation_checklist_Part_4_-_DiffSinger_Reading_30_min

# Self-evaluation checklist: Part 4 - DiffSinger
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/fKLiS/self-evaluation-checklist-part-4-diffsinger

This self-evaluation checklist is structured to assess a user’s comprehension of Week 14, Part 4, focusing specifically on the DiffSinger model and the broader field of AI voice synthesis. The primary function of this checklist is to enable a critical self-assessment of progress against defined learning outcomes.

Learning Outcome 1 focuses heavily on the conceptual discussion of creativity within the field of AI-generated audio. Specifically, learners must be able to explain various aspects of creativity as applied to AI-generated singing and voice synthesis. Furthermore, proficiency requires referencing and discussing relevant academic literature concerning creativity in AI and music synthesis. A crucial element is the ability to critically analyze how AI-based voice synthesis fundamentally challenges traditional human notions of creativity. This outcome also necessitates a comparative analysis between human and AI-generated creativity within vocal performance.

Learning Outcome 2 addresses the technical complexity of modern speech synthesis models. The learner must be able to thoroughly explain the specific architecture and operational workflow of advanced systems, notably DiffSinger. This objective highlights the critical role that diffusion-based models play in achieving high-quality synthesized singing voices. Technical comprehension requires describing the function of machine learning techniques, such as deep neural networks (DNNs), within the process of speech synthesis. Finally, the assessment demands the learner compare the complexity and overall performance between various modern speech synthesis systems.

Learning Outcome 3 shifts focus to historical context and technological evolution. Learners are required to describe early speech synthesis systems and techniques, such as the Voder and the Vocoder, along with other foundational methods. This section mandates an explanation of how both text-to-speech (TTS) and singing synthesis systems have progressed and evolved over time. A core requirement involves comparing historical and modern approaches to voice synthesis across criteria like quality, realism, and usability. Moreover, the learner must be able to provide concrete examples detailing how previous speech synthesis techniques continue to influence contemporary model development.

In addition to the technical knowledge checks, the module includes a reflective component designed for metacognitive learning. This reflection encourages the user to identify the areas of the subject matter that they found most challenging and to articulate the reasons for that difficulty. It also prompts the learner to identify any additional resources required to deepen their understanding of the complex topics. Lastly, the reflection guides the learner toward practical or creative applications of the knowledge gained. Overall, the checklist serves as a comprehensive tool ensuring the user can critically assess their grasp of both theoretical and technical aspects of DiffSinger and voice synthesis.

---

## Week 15

### 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_Weekly_reading_Reading_1h

# Weekly reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/6Z5Qt/weekly-reading

The provided text lists the weekly reading materials for the AI Creativity lectures, including the introductory lecture slides defining "what is creativity" (`ai-creativity-wk0_what_is_creativity.pdf`) and the comprehensive "putting it together" lecture slides (`ai-creativity-wk5_all_together.pdf`).

---

### 03_Putting_the_system_together_extracting_notes_Video_16_min

# Putting the system together: extracting notes
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/wIqnh/putting-the-system-together-extracting-notes

This curriculum provides a deep exploration into advanced artificial intelligence across several domains, beginning with Game Playing AI (Weeks 1-5). This initial phase introduces the concept of Reinforcement Learning, formalizing it with the DQN agent, culminating in implementation and a discussion of ethical considerations in AI game players. The focus then shifts to Evolving Artificial Creatures (Weeks 6-10), where automatic design utilizes genetic algorithms for building complex robots using tools like PyBullet and URDF files. A critical component of this evolutionary study involves defining genetic encoding schemes and robust fitness functions for selection. The middle section addresses Generative and Collaborative AI (Weeks 11-15), exploring systems designed to create new content. Technical implementations include generating lyrics with GPT-2 and composing music using MusicVAE and DiffSinger, leading to a complete pop song generator. Following the creative focus, the course transitions into advanced robotic intelligence via "A Toy Robot Scientist" (Weeks 16-20). This later module covers system building, knowledge representation, and the complex reasoning phase required for planning and analyzing tasks. Crucially, the curriculum maintains a persistent focus on legal and ethical issues throughout the study of AI agents and creativity. Supplementary materials include weekly videos, dedicated readings, and practical labs for reinforced learning and music generation. The final weeks are dedicated to intensive exam preparation and examination. The overarching theme unites complex systems development, ranging from game theory to autonomous creative generation.

---

### 04_Mixing_the_singing_with_the_backing_Video_7_min

# Mixing the singing with the backing
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/97uw4/mixing-the-singing-with-the-backing

The primary focus of this video segment is demonstrating the final step of music production: mixing a backing track with vocal recordings using three distinct methodologies. These methods include leveraging graphical audio applications (Reaper and Audacity) and implementing a code-based workflow using Python and the Librosa library.

Reaper, a multi-track commercial application created by Justin Frankel (also the creator of Winamp), offers a powerful environment for this mixing task. The process in Reaper involves loading the tracks (e.g., `skippy.wav`) onto a blank slate and carefully adjusting levels to prevent distortion, ensuring the audio does not clip into the red zone. Since the initial singing was too fast, the workflow required substituting the original track with a pre-rendered, slower version (`skippy slow`). The slow vocal track is then manually dragged and lined up against the backing track to achieve proper synchronization.

Audacity, presented as an open-source graphical alternative suitable for various platforms, performs the same mixing task. In Audacity, tracks are also dragged and dropped into a multi-track setup. The crucial step here utilizes the "Time Shift Tool," which allows the user to visually pull and align the vocal track accurately with the accompanying music. Volume balance is then fine-tuned using the dedicated controls on the respective track channels.

The third, and most technical, method involves implementing the mix using code, relying heavily on Librosa for audio processing. The coding workflow requires several specific steps: loading the input files (singing and music), and normalizing them to maximize the available audio levels. The shorter track must then be padded with zeros at the beginning to match the length of the longer track—a programmatic equivalent of dragging the track in the graphical tools.

This padding prepares the tracks for addition using NumPy's `NumPy add` function, after which the combined audio is written out to disk as a final mixed file. The implementation script specifies the filenames, checks for their existence, and sets a sample rate, commonly 44100, for high quality. The script utilizes a pad function, essentially calling `np.pad` with appropriate parameters, which handles length differences by either padding or truncating the end of the longer track.

Overall, this video successfully demonstrated how simple track mixing can be achieved both through intuitive GUI tools like Reaper and Audacity, and through rigorous mathematical processing using Python and Librosa. While the finished composition is noted as being functional for pop music, the presenter acknowledges that achieving a polished, "big" sound requires advanced AI techniques that were beyond the scope of this basic mixing demonstration. Furthermore, the surrounding course material references broader AI topics, including genetic algorithms for creature evolution, DQN agents for game playing, and generative models like MusicVAE and DiffSinger for advanced music composition.

---

### 05_Discussion_of_creativity_Video_12_min

# Discussion of creativity
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/59pA4/discussion-of-creativity

This course is structured across 22 weeks, covering advanced topics in artificial intelligence, divided into distinct modules. The initial phase (Weeks 1-5) focuses on AI Game Playing, starting with basic game player development and progressing to formalizing reinforcement learning using the Deep Q-Network (DQN) agent and implementing this architecture. The middle section (Weeks 6-10) explores Evolving Artificial Creatures, utilizing genetic algorithms for automatic design and building robots using tools like pybullet and URDF files, while focusing on encoding schemes and fitness functions. Weeks 11 through 15 concentrate on Generative and Collaborative AI, introducing generative systems and applying them practically to tasks like generating lyrics with GPT-2, composing music using MusicVAE, and employing DiffSinger for advanced synthesis. The practical implementation culminated in a pop song generator, requiring complex steps like extracting notes and mixing singing with backing tracks. The subsequent module (Weeks 16-20) delves into "A Toy Robot Scientist," covering its history, knowledge representation, the reasoning phase, and planning mechanisms. This latter module emphasizes the state of the art in robot science and associated legal and ethical issues. Overall, the course integrates theoretical concepts with practical tooling, covering areas such as the debate on AI's role in creativity. Assignments involved weekly readings, quizzes, and practical lab work, such as implementing the DQN agent or building generative systems. The curriculum also includes specific focus on ethical considerations, particularly in Week 5 and Week 16. The final weeks (21-22) are dedicated to exam preparation and assessment.

---

### 06_Recap_of_week_15_study_Video_1_min

# Recap of week 15 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/zizuQ/recap-of-week-15-study

This detailed review summarizes the course structure, technical progression, and key conceptual findings across the curriculum.

The initial modules covered Game Playing AI, beginning with Part 1 and Part 2. Week 2 focused on formalizing reinforcement learning (RL), specifically detailing the Deep Q-Network (DQN) agent. Week 3 provided tooling for game playing AI, which was followed by the implementation of the DQN agent in Week 4. Week 5 concluded the AI game players unit by examining the state of the art and ethical considerations in this field.

Subsequently, the course transitioned to Evolving Artificial Creatures across five weeks. Weeks 6 through 10 introduced automatic design using genetic algorithms. Building robots utilized specific tools, including pybullet and URDF files, for physical realization. The curriculum detailed the genetic encoding scheme in Week 8. Furthermore, Week 9 focused on implementing the fitness function and subsequent selection processes for evolution.

The mid-course phase, weeks 11 through 15, focused on Generative and Collaborative AI systems. Week 11 provided an introduction to generative systems in general. The progression moved to specific generative tasks, such as generating lyrics using the GPT-2 model in Week 12. Music composition was covered in Week 13, leveraging MusicVAE.

A key focus in generative AI was the advanced music synthesis, demonstrated through DiffSinger in Week 14. Week 15 brought all these elements together into a culminating project: the pop song generator. This final generation phase involved putting the system together and mixing the singing with the backing audio file.

The subsequent section, weeks 16 through 20, explored the role of the Toy Robot Scientist. Week 16 addressed the history, legal, and ethical issues surrounding robotic intelligence. Weeks 17 and 18 focused on system building and introducing the Robot Scientist's reasoning phase. Planning and analyzing capabilities were covered in Week 19, which was followed by a state of the art review in Week 20.

The curriculum concluded with Week 21 designated for exam preparation, leading into Week 22, the dedicated exam week. Conceptual reviews also occurred, notably a Recap of week 15 study.

The transcript confirmed that by the end of Week 5, students should be able to complete a full AI package. This includes generating both music and singing, and then successfully mixing these components into a final audio file. Critically, students were expected to use literature examples to discuss different aspects of creativity. A deeper objective was the ability to differentiate between the Skinnerian and Dewian views on creativity, including the concept of godlike or natural creativity. The entire course structure provided hands-on experience with diverse AI methodologies, from DQN and genetic algorithms to GPT-2 and DiffSinger.

---

### 07_Self-evaluation_checklist_Part_5_-_Putting_it_all_together_and_pop_song_generator_[_Reading_30_min

# Self-evaluation checklist: Part 5 - Putting it all together and pop song generator [
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/2TZ9W/self-evaluation-checklist-part-5-putting-it-all-together-and-pop-song-generator

This document presents a self-evaluation checklist for the course module "Week 14 - Part 5: Putting it all together and Pop Song Generator 1." Its purpose is to provide a structured approach for students to assess their understanding and technical work. The evaluation is divided into three major areas: theoretical understanding, technical system development, and critical evaluation.

Regarding the understanding of creativity theories, students must first demonstrate a clear explanation of the Skinnerian view. This involves detailing how fundamental behaviourist principles are applicable to creative processes. Secondly, students must clearly explain the Dewian view of creativity. This perspective emphasizes the crucial role of experience, reflection, and continuous development in creative output. A vital component of this section is the ability to compare and contrast these two distinct perspectives. Specifically, the differences in how each view understands creativity must be highlighted. To solidify understanding, students are required to provide real-world or historical examples illustrating both the Skinnerian and Dewian views.

The second major section focuses on developing a complete song generating system. This system requires successful implementation of a lyric generation component. Lyric generation must utilize appropriate techniques, which may include AI models or rule-based systems. Additionally, the system must successfully implement a music generation system capable of creating complex melodies and harmonies. A third critical element is the successful implementation of a singing synthesis system. This synthesizer must effectively transform the generated lyrics into a realistic vocal performance. The system then requires integration, combining the lyric, music, and singing components into one cohesive audio file. Furthermore, the final generated song must adhere to a clear, established structure. This structural requirement includes defining elements such as the verse, chorus, and bridge. Finally, rigorous checks and refinements must be performed on the audio mixing. The goal of mixing is ensuring that all elements—lyrics, music, and singing—sound balanced and professional.

The third section addresses the evaluation of creativity, comparing machines and humans. Students must be able to explain different philosophical and theoretical perspectives on this comparison. This requires referencing examples found in academic literature that specifically discuss creativity within AI-generated content. A critical evaluation component involves assessing the strengths and limitations of AI-generated music and lyrics. This assessment must be compared against the qualities of human-created works. Ultimately, students must articulate their own defined position on the matter of AI creativity. This position addresses whether AI systems can be considered genuinely creative or merely functioning as sophisticated imitators.

Finally, the self-reflection section serves as a meta-cognitive check. Students must assess their confidence in achieving all the learning outcomes for the week. Should there be any identified gaps in their understanding, they must pinpoint specific areas requiring review or improvement. The checklist also confirms the student's ability to clearly explain their work and findings to others, whether in written or peer presentation format. This entire checklist structure functions as a complete mechanism for both self-assessment and comprehensive review of all key concepts and technical implementations.

---

### 08_20.113_AI_creativity_case_study_outro_Video_4_min

# 20.113 AI creativity case study outro
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/5gMgz/20-113-ai-creativity-case-study-outro

This comprehensive syllabus covers a diverse progression through AI applications, starting with Week 1-5 focused on game playing AI. The curriculum formalizes reinforcement learning through the development of the Deep Q-Network (DQN) agent and explores various AI tooling for game environments. Weeks 6-10 shift focus to evolving artificial creatures, utilizing genetic algorithms for automatic design. Specific technical details include building robots using simulation environments like pybullet and defining physical structures via URDF files. The evolutionary process is formalized through genetic encoding schemes, defined fitness functions, and selection mechanisms. The subsequent block (Weeks 11-15) delves into generative and collaborative AI systems. This includes generating lyrics with GPT-2 and composing music using advanced models such as MusicVAE and DiffSinger. The technical goal of this section is synthesizing these components into a complete pop song generator. Weeks 16-20 introduce the "Toy Robot Scientist" concept, examining its history, legal, and ethical dimensions. The Robot Scientist framework involves building a complex system centered on knowledge representation and reasoning phases. Crucial components addressed are planning and analysis capabilities within the robotic agent. Throughout the entire course, learning is reinforced through structured activities including weekly reading, discussion prompts, and practice assignments, culminating in exam preparation.

---

## Week 16

### 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_Weekly_reading_Reading_10_min

# Weekly reading
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/ESOPm/weekly-reading

The central theme of these readings is the ambitious concept of the automation of science, detailed extensively in King, R.D. et al.'s 2009 paper, "The Automation of Science" (Science 324: 85-89). This field explores how robotic systems can move beyond mere data processing to actively participate in the cycle of scientific discovery. The foundational work also includes the specific exploration of the 'Robot Scientist Adam,' discussed in "The Robot Scientist Adam" (Computer 42/8: 46-54). Fundamentally, the automation requires robust mechanisms for causal explanation and model induction, a focus addressed by Langley, P. (2019) in *Mind & Society, 18*, 43-56.

Early proof of concept for autonomous systems was seen in Zutkow L.M. et al.'s 1990 work on "Automated discovery in a chemistry laboratory" (Proceedings of the Eighth National Conference on Artificial Intelligence). More recently, sophisticated systems have successfully been applied to complex biological problems. For instance, Todorovski, L. et al. (1998) demonstrated equation discovery in modeling and predicting phytoplankton growth, published in *Ecological Modelling, 113*, 71-81.

The tangible realization of these systems includes the development of advanced physical robots. Burger, B. et al. reported on "A mobile robotic chemist," detailing a sophisticated mobile platform (Nature 583, 237–241, 2020). Ross King’s work further showcases industrial implementation, such as the "Maholo" biomedical experiment robot. In the highly specialized field of drug discovery, robotic automation has shown immense promise. Williams, K. et al. validated the efficiency of drug repositioning against neglected tropical diseases in the *Journal of the Royal Society Interface* (2015).

Specific successes have been noted, such as the robot scientist discovering a potential malaria drug, as reported by A. Extance in *Scientific American* (2015). The capability of these systems is bolstered by automated statistical methods, addressed by Steinruecken, C. et al. in "The Automatic Statistician" (Automated Machine Learning, 2019). The underlying computational goal is encapsulated in Kitano, H.'s 2021 exploration of the "Nobel Turing Challenge: creating the engine for scientific discovery" (NPJ Syst Biol Appl 2021 Jun 18;7(1):29).

However, the pursuit of automated science is not purely technical; it carries significant philosophical and social weight. King, R.D. et al. investigate the "Philosophical and social dimensions" of this automation (IEEE Technology and Society Magazine, 37, pp 40-46). The ethical implications of these autonomous agents are captured in the provided link: https://medcraveonline.com/IRATJ/ethics-in-robotics-and-automation-a-general-view.html. The debate touches upon the nature of the "socially distant robot scientist," as noted by BBC News. In summary, the field presents a comprehensive model, spanning from fundamental AI principles and equation discovery to real-world applications in chemistry and biomedicine, all while demanding careful consideration of ethical guidelines.

---

### 03_Introduction_to_Robot_Scientist;_history,_perspectives,_legal_and_ethical_issues_-_slides_Reading_10_min

# Introduction to Robot Scientist; history, perspectives, legal and ethical issues - slides
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/q8voI/introduction-to-robot-scientist-history-perspectives-legal-and-ethical-issues

This comprehensive curriculum introduces students to diverse frontiers of Artificial Intelligence, spanning game playing, evolutionary design, generative systems, and advanced robotics. The study of Game Playing AI begins by formalizing reinforcement learning and implementing the powerful Deep Q-Network (DQN) agent, alongside examining related tooling and the ethics of AI players. Evolutionary artificial creatures are explored using genetic algorithms, with a technical focus on building robots via pybullet and URDF files. Key concepts in this area include the genetic encoding scheme, defining fitness functions, and utilizing selection mechanisms for evolving morphology. The curriculum progresses to Generative and Collaborative AI, introducing foundational generative systems. Specific practical applications include generating lyrics using GPT-2 and composing music with models such as MusicVAE and DiffSinger. The later module focuses on an integrated "Toy Robot Scientist," covering its core history, perspectives, and critical legal and ethical issues. The system itself involves detailed steps, including knowledge representation, the reasoning phase, and sophisticated planning and analyzing capabilities. Weekly study also emphasizes discovery science, providing both practice assignments and in-depth video lectures on the Robot Scientist system. Throughout the course, a consistent thread is the examination of ethical and legal issues in robotics and lab automation. The initial weeks cover foundational topics, while later modules delve into advanced practical implementation and state-of-the-art projects. The course structure is rigorous, dedicating weeks to both reading materials and practical assignments for self-evaluation. Ultimately, the syllabus guides students from foundational machine learning models to complex, self-designing, reasoning autonomous systems.

---

### 04_Discovery_science_and_the_Robot_Scientist_system_Video_3_min

# Discovery science and the Robot Scientist system
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/eDz25/discovery-science-and-the-robot-scientist-system

This course provides a comprehensive exploration of advanced AI, spanning six core areas from game theory to robotic discovery science. The initial weeks focus on AI game playing, detailing the evolution from basic AI agents to formalizing reinforcement learning, particularly through the implementation of the DQN agent. Subsequent modules delve into the mechanics of evolving artificial creatures, utilizing genetic algorithms for automatic design and optimization. Technical details include building robots using PyBullet and URDF files, and establishing specialized genetic encoding schemes and fitness functions. The course then transitions into Generative and Collaborative AI, showcasing systems that create content, such as generating lyrics with GPT-2 and composing music via MusicVAE and DiffSinger. The curriculum culminates in "A toy Robot Scientist," which introduces the concept of discovery science and the foundational history, perspectives, and ethical debates surrounding lab automation. The later weeks detail the structural components of the Robot Scientist system, focusing on knowledge representation and the complex reasoning phase. Finally, the sequence outlines the planning and analysis capabilities of the system, culminating in a review of state-of-the-art projects. The entire structure progresses from specific AI implementations (DQN) to broad systems design (Robot Scientist), demonstrating modern AI applications across various domains. Key elements include understanding legal and ethical issues in robotics alongside technical development. The course culminates in a dedicated exam preparation and examination period.

---

### 05_The_concept_of_Robot_Scientist_Video_7_min

# The concept of Robot Scientist
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/camcJ/the-concept-of-robot-scientist

The concept of a Robot Scientist introduces AI systems designed for automated scientific discovery and experimentation. This idea originated in 2004 with Professor Skin, currently working at Chalmers University of Technology in Sweden. His colleagues successfully developed a system named Adam, demonstrating the feasibility of automating scientific processes. A Robot Scientist is an AI system capable of generating its own experiments, physically executing them, interpreting the results, and repeating the entire cycle. These systems rely on a knowledge base that contains established knowledge and data pertinent to a specific domain. From this knowledge base, the Robot Scientist infers novel scientific hypotheses that are not yet included in the current knowledge.

The system further includes the possible explanations for existing data and phenomena, allowing for deeper analysis. To verify these inferred explanations, the Robot Scientist designs specific experiments to test the hypotheses. Crucially, this is a physically implemented system, incorporating robotic equipment for conducting the generated experiments. It possesses the capability to perform multiple experiments in parallel while simultaneously analyzing the resulting data. The knowledge component evaluates whether the hypotheses were confirmed, subsequently updating its knowledge base with new experimental data and conclusions. This loop allows the cycle to be repeated thousands of times until further refinement is reached.

The Robot Scientist represents a technological implementation of the hypothetical-deductive method of scientific discovery. This method constructs a scientific theory by accounting for results from direct observation and experimentation, which is then verified through inference and empirical evidence. While not all sciences involve physical experimentation—computer and social sciences, for instance, involve competition and surveys—many do. The field of automated scientific discovery is still nascent but holds immense potential for accelerating technological progress and improving quality of life.

The necessity for Robot Scientists arises for two primary reasons: first, it helps in understanding the nature of science itself, echoing Richard Feynman's idea that "what I cannot create, I do not understand." Second, human production of data significantly outpaces human capacity for knowledge production. Robot Scientists promise to increase scientific productivity by working faster, cheaper, more accurately, and for longer durations than humans.

Positive aspects include the ability to record and share every step of scientific discovery, promoting open science. Furthermore, since educating a new human scientist takes several years, these robots can be easily multiplied and constructed within months, though they remain expensive due to current non-mass production. While human scientists excel at deep understanding and conceptual leaps, they require assistance in processing vast datasets and making unbiased, accurate logical inferences. The overall scope of this technological advancement is still limited to specific scientific areas. Related modules delve into specific technical implementations, such as game playing AI, formalizing reinforcement learning and the DQN agent, and building evolving creatures using pybullet and URDF files. The learning trajectory also addresses legal and ethical issues in robotics and lab automation.

---

### 06_Robot_scientists_Reading_1h

# Robot scientists
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/0scrd/robot-scientists

Now read these articles about Robot Scientists: King, R.D., Rowland, J., Oliver, S.G., Young, M., Aubrey, W., Byrne E., Liakata, M., Markham, M., Pir, P. Soldatova, L.N., Sparkes, A., Whelan, K.E., Clare, A. (2009) The Automation of Science. Science 324: 85-89. OL-CM3020-King_et_al.pdf PDF File Williams, K., Bilsland, E., Sparkes, S et al. Cheaper faster drug development validated by the repositioning of drugs against neglected tropical diseases . Journal of the Royal Society Inerface (2015)....

---

### 07_History_of_Robot_Scientists_and_future_trends_Video_14_min

# History of Robot Scientists and future trends
Video • 14 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/hOTBF/history-of-robot-scientists-and-future-trends

This curriculum extensively covers advanced topics in artificial intelligence, structured into distinct functional areas across multiple weeks. The initial phase (Weeks 1-5) focuses on AI game playing, detailing the formalization of reinforcement learning and the implementation of the Deep Q-Network (DQN) agent. Subsequent modules explore autonomous systems via evolution, dedicating Weeks 6-10 to the design of artificial creatures using genetic algorithms. This evolutionary segment also involves building robots using technical specifications like pybullet and URDF files, requiring specific genetic encoding and fitness function design. Weeks 11-15 delve into Generative and Collaborative AI, exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. These generative techniques culminate in a comprehensive pop song generator project. The final, extensive module (Weeks 16-20) introduces "A toy Robot Scientist," addressing its history, legal, and ethical considerations in robotics. The Robot Scientist system focuses on knowledge representation and developing a reasoning phase. It systematically covers planning, analysis, and reviewing the state of the art in robot science projects. This practical application contrasts sharply with the preceding AI modules by focusing on scientific discovery and automation. The entire course structure is reinforced by weekly study materials, including specific video and reading assignments. The program concludes with dedicated weeks for exam preparation and assessment.

---

### 08_Reading_articles_Reading_1h

# Reading articles
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/gK59R/reading-articles

Now read: Ross King: Automating Science using Robot Scientists Langley, P. (2019). Scientific discovery, causal explanation, and process model induction. Mind & Society, 18, 43-56. This article is available in the Online Library . Pat Langley and Adam Arvay Scientific Discovery, Process Models, and the Social Sciences Todorovski, L., Dˇzeroski, S., & Kompare, B. (1998). Modeling and prediction of phytoplankton growth with equation discovery. Ecological Modelling, 113, 71-81....

---

### 09_Legal_and_ethical_issues_in_robotics_and_lab_automation_Video_11_min

# Legal and ethical issues in robotics and lab automation
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/IgsyX/legal-and-ethical-issues-in-robotics-and-lab-automation

This lecture addresses critical ethical and legal issues in developing and deploying AI, specifically focusing on the context of robot scientists and laboratory automation. The study of these moral dimensions is termed "roboethics," which examines questions such as robot rights, how robots should treat humans, and who holds responsibility when automated systems cause harm. Developers are fundamentally responsible for ensuring the ethical design of AI systems and overseeing their usage.

The text acknowledges widespread criticism regarding job displacement, noting that robots are taking over human tasks, from Amazon product handling to bar service. While labor automation threatens certain human roles, the speaker asserts that in laboratory automation, the primary goal is mitigating danger and automating repetitive tasks. For example, autonomous laboratories allow experiments to proceed remotely, bypassing dangers posed by travel or social distancing, particularly during pandemics.

It is crucial to understand the distinct advantages of both AI systems and human operators. AI excels in processing large datasets, reasoning, and performing parallel tasks non-stop. Conversely, humans retain superiority in high-level planning and making decisions within uncertain, non-deterministic environments. The ultimate target for advanced systems should be human-robot collaboration and co-creation, mirroring findings that AI combined with humans outperforms individual teams.

A significant ethical concern is AI bias, which can be inbuilt by design, often stemming from biased datasets (e.g., medical datasets lacking data from minority groups). Mitigation requires awareness of bias, using stratification to compensate for it, and rigorously checking AI decisions. Furthermore, AI systems can technically make mistakes, necessitating highly consistent experimental replication, as seen in the robot scientist project.

Existing legal frameworks are unprepared for AI, highlighted by the copyright law preventing Robot Scientist Adam from being listed as a co-author because he could not sign the agreement. Debates continue regarding whether robots should possess legal rights. Safety is paramount; systems like Robot Scientist Eve utilize sensors to automatically shut down if human proximity to dangerous equipment is detected.

In terms of technical depth, the associated curriculum covers diverse AI methods, including reinforcement learning applied to game playing AI via the DQN agent. Other technical explorations include automatic design of evolving artificial creatures using genetic algorithms, modeled with pybullet and URDF files. Generative AI modules detail systems like GPT-2 for lyrics and MusicVAE/DiffSinger for music composition. The Robot Scientist project itself is detailed across several modules, focusing on its history, knowledge representation, and reasoning phases. The overall study spans weeks 16 through 22, culminating in an examination of these legal and ethical issues in robotics.

---

### 10_Reading_articles_Reading_1h

# Reading articles
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/SVJaA/reading-articles

Roboethics King, R.D., Schuler Costa, V., Mellingwood, C. & Soldatova, L.N. Automating sciences: Philosophical and social dimensions IEEE Technology and Society Magazine, 37, pp 40-46. If these links are broken, please let us know via the Student Portal . Reading articles Roboethics King, R.D., Schuler Costa, V., Mellingwood, C. & Soldatova, L.N. Automating sciences: Philosophical and social dimensions IEEE Technology and Society Magazine, 37, pp 40-46....

---

### 11_Recap_of_week_16_study_Video_1_min

# Recap of week 16 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/OFywP/recap-of-week-16-study

The curriculum begins by exploring AI game playing, starting with fundamental AI player concepts and transitioning into formalizing reinforcement learning. This early stage focuses on implementing the Deep Q-Network (DQN) agent, examining its mechanics and then assessing the state of the art and ethical considerations within AI game players. The focus subsequently shifts to evolving artificial creatures, beginning with automated design using genetic algorithms. This section delves into practical implementation, including building robots using pybullet and URDF files, detailing the genetic encoding scheme, and designing fitness functions and selection mechanisms. A third major theme, Generative and Collaborative AI, is covered next, introducing general generative systems. Specific technical applications include generating lyrics with GPT-2 and exploring music composition using MusicVAE and DiffSinger. This generative exploration culminates in integrating these systems to create a pop song generator. Following these broad AI topics, the study introduces the specialized area of the "Toy Robot Scientist," addressing its history, perspectives, and critical legal and ethical issues. The module then progresses to building the system itself, focusing on knowledge representation. Subsequent parts introduce the Robot Scientist's reasoning phase, culminating in modules dedicated to planning and analyzing scientific discovery. The course concludes by reviewing the state of the art in Robot Scientist projects, providing a comprehensive perspective on automated discovery science. The entire program is structured with weekly learning components, including videos, reading assignments, and practical assignments. Overall, the curriculum offers a comprehensive survey of advanced topics, spanning from reinforcement learning and genetic evolution to generative modeling and autonomous robotics.

---

### 12_Self-evaluation_checklist_Part_1_-_introduction,_history,_perspectives,_legal_and_ethical_issues_Reading_30_min

# Self-evaluation checklist: Part 1 - introduction, history, perspectives, legal and ethical issues
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/KK7FY/self-evaluation-checklist-part-1-introduction-history-perspectives-legal-and

This text outlines a comprehensive self-evaluation checklist designed to assess a student's understanding and progress by the end of Week 16. The primary focus of this assessment revolves around the advanced concepts of Automated Scientific Discovery. Learners are expected to demonstrate mastery across five distinct, interconnected areas.

The first area covers the Understanding of Scientific Discovery Systems. Students must be capable of describing various scientific discovery systems. Furthermore, they must trace the historical development of these systems to understand their evolution. A critical component of this section requires the learner to compare and contrast diverse examples of these systems. This comparison must explicitly highlight the specific strengths and inherent limitations of each model.

The second area addresses Perspectives on Automated Scientific Discovery. Here, the goal is to explain the various differing viewpoints on the role of automation in modern scientific research. Students must move beyond simple understanding to develop a clear, defensible argument. This argument must convincingly support the potential of automated scientific discovery. Such an argument requires supporting evidence and relevant, real-world examples.

The third area focuses on Robot Scientists: Features and Components. Learners must first identify the key features that define these advanced robotic entities. They must also specify the essential components that comprise the Robot Scientist systems. Crucially, the learner must explain how these robots contribute actively to the scientific process. This contribution spans three critical stages: hypothesis generation, experimentation, and detailed data analysis.

The fourth area delves deeply into Legal and Ethical Considerations. Students are required to discuss the complex legal implications stemming from automated scientific discovery. Specific legal concerns include addressing intellectual property issues and navigating regulatory challenges. Ethically, the analysis must focus on several key challenges related to automated research. These ethical challenges specifically involve ensuring transparency, maintaining accountability, and defining the appropriate role of human oversight.

The final domain is dedicated to Critical Thinking and Reflection. This requires the student to critically evaluate the broad impact of automated scientific discovery. The evaluation must be conducted against the backdrop of traditional scientific methods. Furthermore, learners must articulate their own synthesized perspective on the future of scientific discovery. This personal outlook must integrate the concepts of automation, legal structures, and ethical mandates. Achieving success means having checked all or most of these detailed learning outcomes. If uncertainty remains in any area, the text advises revisiting lectures, readings, and class discussions for necessary clarification.

---

## Week 17

### 01_Weekly_introduction_Video_2_min

# Weekly introduction
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/UamSO/weekly-introduction

This course structure covers a broad spectrum of advanced AI topics, beginning with Game Playing AI, formalizing concepts like Reinforcement Learning and the DQN agent (Weeks 2-4). The initial modules introduce tooling for Game Playing AI and focus on the implementation of the Deep Q-Network (DQN) agent. Following this foundation, the curriculum transitions into the study of Evolving Artificial Creatures (Weeks 6-10). These segments explore automatic design using genetic algorithms and build sophisticated robots utilizing PyBullet and URDF files.

The later phase focuses on Generative and Collaborative AI, establishing the groundwork with generative systems (Week 11). Key techniques introduced include generating lyrics using GPT-2 and performing music composition via MusicVAE. The most advanced area covered is speech and vocal synthesis, highlighted in Week 14. The Week 4 content introduces a challenging, state-of-the-art speech synthesis model, current for 2021-2022 research.

Learning objectives for this week include providing historical examples of speech synthesis systems, such as the singing generated by HAL 9000 from *2001*. Furthermore, students must gain an insight into the substantial complexity of modern speech synthesis research. The practical focus involves using a pre-trained speech synthesis model coupled with pitch correction technology. This process generates singing voices from specific inputs: a list of desired lyrics and corresponding musical notes.

The output of this system is a rendered audio file, which can be visualized as a spectral spectrogram. A major technical model discussed in this area is DiffSinger. The course is highly comprehensive, progressing to include a "Pop Song Generator" in Week 15. Subsequent weeks cover specialized AI applications, including a "Toy Robot Scientist" module (Weeks 16-20). This final segment delves into knowledge representation, system building, reasoning, and planning within robotic systems. Throughout the course, students engage with complex assignments, including experiments with DiffSinger and self-evaluation checklists.

---

### 02_Building_the_system_-_slides_Reading_10_min

# Building the system - slides
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/yCa5Y/building-the-system-slides

This extensive module outlines a curriculum spanning AI game playing, evolutionary computation, generative models, and advanced robotic systems. The initial focus covers AI game playing, starting with basic AI players and formalizing reinforcement learning principles. Key technical concepts include the development and implementation of the Deep Q-Network (DQN) agent and an examination of the ethical implications in AI game players. The course then shifts to evolving artificial creatures, utilizing genetic algorithms for automatic design and morphology. Technical components of this phase involve building robots using specialized tools like pybullet and defining structures via URDF files. Genetic encoding schemes, fitness functions, and selection mechanisms are detailed to guide the evolution of complex artificial entities. The curriculum next explores Generative and collaborative AI, covering diverse creative systems. Specific generative models studied include GPT-2 for lyric generation and MusicVAE and DiffSinger for advanced music composition. This phase culminates in a practical project: creating a comprehensive pop song generator. Modules transition to "A toy Robot Scientist," introducing the foundational concepts of rational agents and multi-agent environments. A critical technical emphasis is placed on knowledge representation, involving the construction of a Toy Knowledge Base (KB). Students engage in deep practical work, including constructing the toy knowledge model in Python and modifying the system in labs. This robotic framework progresses into complex cognitive abilities, specifically tackling the Robot Scientist's reasoning and subsequent planning phases. The material covers the overview of the toy system's components and their intricate interactions with the environment. The learning structure integrates structured videos, readings, and practice assignments to reinforce technical understanding. Throughout the modules, the state of the art in AI projects and associated legal and ethical issues are continuously addressed. The journey concludes with a dedicated exam preparation week, leading into the final examination period.

---

### 03_Introduction_to_rational_agents_Video_6_min

# Introduction to rational agents
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/HriFf/introduction-to-rational-agents

This course explores various advanced domains of Artificial Intelligence through a structured, multi-week progression. The initial phase focuses on AI game playing, covering foundational concepts (Week 1) and formally introducing Reinforcement Learning and the Deep Q-Network (DQN) agent in Week 2. Week 3 details specialized AI game playing tooling, while Week 4 focuses on the practical implementation of the DQN agent itself. The curriculum then addresses the ethical and technical state of art in AI game players in Week 5. Next, the focus shifts to evolving artificial creatures, beginning in Week 6 with automatic design using genetic algorithms. Weeks 7, 8, and 9 build upon this by addressing robotics implementation using pybullet and URDF files, detailing the genetic encoding scheme, and defining fitness functions and selection processes. Week 10 reviews the state of the art in evolving morphology.

The program then transitions to Generative and Collaborative AI, starting with a general introduction to generative systems in Week 11. Key technical applications include generating lyrics using GPT-2 (Week 12) and employing MusicVAE for music composition (Week 13). Further exploration of generative models includes DiffSinger (Week 14) and culminating in a comprehensive pop song generator project (Week 15). The final major section introduces the "Toy Robot Scientist," covering history, perspectives, and associated legal and ethical issues (Week 16).

Week 17 delves deeply into building the system, specifically focusing on knowledge representation through extensive related videos, practice assignments, and the construction of the toy knowledge model in Python. The subsequent weeks structure the reasoning phase, starting with an introduction to the Robot Scientist reasoning phase (Week 18). Weeks 19 and 20 concentrate on planning, analysis, and reviewing the state of the art in Robot Scientist projects, respectively. The program concludes with Week 21 dedicated to exam preparation and Week 22 for the final examination.

---

### 04_Further_reading_Reading_1h

# Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/aN2yA/further-reading

Seminara, L. et al. Active Haptic Perception in Robots: A Review . Front. Neurorobot, 17 July 2019. Please note that because these are supplemental readings, we are unable to guarantee they are available in our Online Library. Further reading Seminara, L. et al. Active Haptic Perception in Robots: A Review . Front. Neurorobot, 17 July 2019. Please note that because these are supplemental readings, we are unable to guarantee they are available in our Online Library....

---

### 05_Introduction_to_multi-agent_environments_Video_8_min

# Introduction to multi-agent environments
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/rjkiz/introduction-to-multi-agent-environments

This lecture explores multi-agent environments (MAEs), where each agent must consider the actions and effects generated by other participating agents. Specifically, it examines competitive environments where the goals of the agents are inherently in conflict. The discussion begins with deterministic observable environments, where agents act alternately and the utility values of the agents are always equal and opposite. A foundational example used to illustrate the complexity of MAEs is the classic Prisoner's Dilemma. This game was introduced by American mathematicians Merrill Flood and Melvin Dresher in the 1950s and demonstrates tendencies in corporate behavior. In the Prisoner's Dilemma scenario, two prisoners, A and B, are offered a bargain: they can either cooperate (remain silent) or betray the other (testify). If both cooperate, both receive a minimal penalty of one year in prison. However, the optimal strategy for each individual agent is to betray the partner, as this action yields a greater personal reward than cooperation.

While human behavior often exhibits a bias towards cooperative behavior in similar scenarios, the Prisoner's Dilemma highlights the fundamental conflict inherent in competitive systems. A more complex example of a dynamic MAE is RoboCop, a robotic soccer tournament introduced by Professor Hioroaki Kitano. Unlike AI game research, which often focuses on abstract games due to representation simplicity, physical games are prioritized because their complex description and wider range of possible actions offer deeper insights. RoboCop involves many agents, some cooperating within a team, and others competing against different teams. The Robot World Cup initiative aims to foster intelligent robotics research by providing a standard problem that integrates design principles like autonomous agents, collaboration, and real-time reasoning.

The progression of AI game playing is evidenced by significant breakthroughs in classic games. Long before, Deep Blue defeated the Russian chess master Garry Kasparov, and Watson challenged in Jeopardy. However, the most impressive example mentioned is the triumph of AlphaGo in 2016. AlphaGo defeated the Human European Go champion, a game historically considered immensely challenging due to its enormous state space and the difficulty in evaluating board positions. Beyond competitive strategy, advanced research includes implementing deep reinforcement learning agents, such as the DQN agent, for solving game theory problems.

The broader course context reveals sophisticated techniques being employed in AI design. Concepts range from building evolving artificial creatures using genetic algorithms to creating sophisticated robots modeled via pybullet and URDF files. Furthermore, generative and collaborative AI systems are studied, including technologies for generating lyrics with GPT-2, music composition using MusicVAE, and DiffSinger. Technical focus areas also cover advanced knowledge representation, as detailed in modules concerning the "Toy Robot Scientist." These techniques underscore a comprehensive approach to AI that spans classical game theory, dynamic robotics, and state-of-the-art generative models.

---

### 06_Further_reading_Reading_10_min

# Further reading
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/y5gIG/further-reading

When you have completed this topic, if you would like to read in more depth about any of the content covered, we recommend the following texts. Please note that because these are supplemental readings, we are unable to guarantee they are available in our Online Library. Kitano, H., M. Asada, Y. Kuniyoshi et al. ‘RoboCup: The Robot World Cup Initiative’ , AGENTS '97: Proceedings of the first international conference on Autonomous agents, pp.340–47. YouTube: Robot Soccer Goes Big Time ....

---

### 07_Overview_of_the_toy_system_components_and_their_interactions_Video_10_min

# Overview of the toy system: components and their interactions
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/SyWyM/overview-of-the-toy-system-components-and-their-interactions

This comprehensive curriculum explores various domains within modern artificial intelligence, beginning with foundational AI game playing. Weeks 1 through 5 focus on Game Playing AI, progressing from basic player concepts to formalizing reinforcement learning using the Deep Q-Network (DQN) agent. Implementation of the DQN agent is detailed in Week 4, while Week 5 addresses the current state of the art and ethical considerations surrounding AI game players. The next major theme, Weeks 6 through 10, investigates evolving artificial creatures through genetic algorithms. This module covers automatic design, building robots using tools like PyBullet and URDF files, and establishing genetic encoding schemes, fitness functions, and selection methods. The focus then shifts to Generative and Collaborative AI in Weeks 11 through 15. Key systems covered include generating lyrics using GPT-2, composing music with MusicVAE, and leveraging DiffSinger. The curriculum culminates with the "Toy Robot Scientist" module, which starts in Week 16 by examining rational agents, legal, and ethical issues. Week 17 extensively covers building the system, delving into knowledge representation concepts through various videos and lab exercises. Further complexity is introduced in Weeks 18 through 20, focusing on the robot scientist's reasoning phase, planning, and analyzing processes. These modules provide a deep dive into agent-based systems and the construction of a functioning knowledge model. The schedule concludes with Week 21 designated for exam preparation, followed by the formal exam week in Week 22. Overall, the training integrates high-level AI concepts, such as deep learning, genetic evolution, natural language generation, and advanced symbolic reasoning.

---

### 08_The_agent-based_systems_Reading_1h

# The agent-based systems
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/p16Ad/the-agent-based-systems

Here are some interesting readings on agent-based systems: Donald L. DeAngelis and Stephanie G. Diaz (2019) Decision-Making in Agent-Based Modeling: A Current Review and Future Prospectus. Frontiers in Ecology and Evolution. Adenuga, O.T et al (2019) Agent-based Control System: A Review and Platform for Reconfigurable Bending Press Machine. Procedia Manufacturing. Bonabeau, E. (2002) Agent-based modeling: Methods and techniques for simulating human systems....

---

### 09_Crash_course_in_knowledge_representation_Video_11_min

# Crash course in knowledge representation
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/hUSYs/crash-course-in-knowledge-representation

Knowledge-based agents require a systematic, machine-processable method to represent and encode knowledge, moving beyond direct encoding in conventional languages like Java or Python. This necessity stems from the fact that the true power of knowledge resides in logical inference and reasoning. To enable logical inference, knowledge must be formalized into a logical structure. Various logical systems exist, including propositional, first order logic (FOL), temporal, and modal logics. Each logic presents a trade-off between expressive power and the complexity of its reasoning problems.

Two specific logics discussed are FOL and Description Logic (DL). DL is notably preferred in certain applications because, unlike some FOL problems, its core reasoning problems are typically decidable, guaranteeing that an inference agent can reach a conclusion. Key knowledge representation languages used for encoding statements within these logics include Prolog and RDF (Resource Description Framework). The aim is to create a knowledge model or knowledge graph that the agent can utilize.

The RDF model represents resources, which are defined as any object uniquely identifiable by a Uniform Resource Identifier (URI). These objects, such as a student or a module, become resources within the model. Resources are connected through properties, which can link them to other resources (relationships) or to simple values like text strings (data properties). Fundamentally, RDF structures knowledge into triplets: Resource X, Property Y, Resource Z, exemplified by (student, raises, query). The logic supporting RDF is Description Logic, enabling reasoners to easily process the models and infer new facts.

To elaborate on RDF structure, the Resource Description Framework Schema (RDFS) is utilized, often leveraging the human-readable Turtle syntax. Classes define categories of resources, and an instance of a class is identified using the predicate `rdf:type`. For example, AI can be defined as a subclass of the general module class. RDFS properties are used to establish the relations and attributes between these defined classes.

A major advantage of knowledge models is their inherent extensibility and ability to integrate with other knowledge models. Integration is achieved by explicitly linking entities defined across different knowledge bases, for instance, linking to a pre-existing ontology like FOAF. These global definitions contrast sharply with local definitions in traditional programming languages. This capability allows the system to combine disparate knowledge, such as linking a university program to events in a specific city.

This architecture enables the development of sophisticated agents, such as those that classify academic versus non-academic queries. Such agents can then advise students on the appropriate contact and monitor the query's progress. Ultimately, knowledge representation allows not only for understanding the domain but also for continuous learning and improving communication processes.

---

### 10_Toy_KB_Video_10_min

# Toy KB
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/WMAdn/toy-kb

This comprehensive curriculum explores four major fields of advanced artificial intelligence. The first module focuses on AI game playing, starting with foundational concepts of AI players. It formally introduces Reinforcement Learning (RL) in Week 2, dedicating Week 4 to the practical implementation of the Deep Q-Network (DQN) agent. Key topics include AI game tooling and concluding with a critical discussion on the state of the art and ethical considerations in game AI.

The second major section addresses evolving artificial creatures, which utilizes Genetic Algorithms (GA) for automatic design. Students learn about implementing robots using specialized tools like PyBullet and utilizing URDF files for physical modeling. This module emphasizes the technical details of the GA, specifically covering the genetic encoding scheme, fitness function design, and selection methods. The goal is to achieve a state-of-the-art understanding of evolving morphology.

The third area concentrates on Generative and Collaborative AI, demonstrating systems capable of creative output. Introduction to generative systems is followed by practical applications, such as generating lyrics using GPT-2. The curriculum expands into music composition, covering technologies like MusicVAE and DiffSinger. The module culminates in a project involving the creation of a comprehensive pop song generator.

The final, detailed section is dedicated to the "Toy Robot Scientist" system, focusing heavily on rational agents and knowledge representation. Week 17 involves building the system, covering rational agents, multi-agent environments, and constructing a toy knowledge base (KB) in Python. Subsequent weeks delve into the robot's reasoning phase, covering planning and analysis. The course concludes with an examination, cementing the theoretical and practical understanding of advanced AI concepts.

---

### 11_Constructing_the_toy_knowledge_model_Video_19_min

# Constructing the toy knowledge model
Video • 19 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/5sn6z/constructing-the-toy-knowledge-model

The mini-lecture focuses on building a knowledge agent within a domain of drug design by encoding conceptual knowledge models into a machine-processable format. This process utilizes the specialized tool Protege, which was developed at Stanford University and is designed to enforce a clean logical structure. The resulting knowledge model is stored in RDF (Resource Description Framework) format because this syntax is highly readable for humans. Within Protege, the knowledge model is structured as a tree-like hierarchy composed of nodes, which are either classes or individuals. Classes represent generic types, such as the root node "thing," while individuals represent concrete instances of these classes.

The process involves defining a hierarchy, starting with classes like "Chemical Entity," and then branching out into more specific types such as "Drug" and "Toxin." Instances, like the specific compound Morphine, are then added as concrete individuals under their relevant classes. To link these nodes, two types of properties are used: object properties

---

### 12_Constructing_the_toy_knowledge_model_in_Python_Video_10_min

# Constructing the toy knowledge model in Python
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/FMURG/constructing-the-toy-knowledge-model-in-python

The curriculum progresses through several distinct areas of advanced Artificial Intelligence, beginning with AI Game Playing. The first module focuses on formalizing Reinforcement Learning and implementing the DQN agent, exploring the concepts of competitive game playing, tooling, and ethical considerations. Following this, the course transitions to the evolution of artificial creatures. This section utilizes genetic algorithms for automatic design and examines building robots using platforms like pybullet and URDF files. Key technical concepts covered include the genetic encoding scheme, developing fitness functions, and understanding the state of the art in evolving morphology. Next, the focus shifts to Generative and Collaborative AI systems. This involves introductions to generative systems and practical applications such as generating lyrics using GPT-2. Further advanced studies include music composition utilizing MusicVAE and the DiffSinger framework. The generative capabilities are consolidated by creating a comprehensive pop song generator. The final major theme centers on "A Toy Robot Scientist," which introduces concepts of rational agents and their applications. The system construction emphasizes knowledge representation, including the development of a toy Knowledge Base (KB). This learning path deepens into multi-agent environments and the overall overview of the toy system's components and interactions. Subsequent modules cover the robot scientist's reasoning phase and specialized planning and analyzing abilities. The curriculum concludes with a state-of-the-art survey of Robot Scientist projects, leading into comprehensive exam preparation and the final assessment week.

---

### 13_Constructing_real_knowledge_model_Video_13_min

# Constructing real knowledge model
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/f09GE/constructing-real-knowledge-model

This lecture addresses how data and knowledge are incorporated into real AI systems, focusing specifically on drug design applications. The speaker introduces the necessity of using external data and knowledge representations for the "robot scientist" agent. The demonstration begins with a simple toy domain model containing chemical entities and basic biological properties, acknowledging that real-world sources are significantly more complex.

A primary external resource discussed is CHEMBL, described as an ontology of chemical entities of biological interest containing over 150,000 classes. CHEMBL allows users to retrieve extensive information on specific compounds, such as morphine, including synonyms, various names, and molecular properties. The use of Unique Resource Identifiers (IDs) is critical to ensure that diverse resources accurately refer to the same chemical entity.

Another vital source is DrugBank, which functions as a comprehensive database rather than an ontology. DrugBank provides detailed information on substances, including brand names, genetic names, mechanism of action, volume of distribution, and adverse effects. It also contains critical data regarding potential drug-drug and food interactions, such as interactions involving alcohol.

CHEMBL is highlighted as especially relevant to the drug design case study because it is a collaborative database populated by researchers analyzing scientific literature. For compounds like morphine, CHEMBL provides data on clinical trial stages, approved uses, synonyms, and structural information.

Crucially, CHEMBL incorporates molecular features, such as the Lipinski rules (or Rule of Five), which help assess whether a small molecule is likely to be a drug. CHEMBL thus provides extensive experimental and clinical data used by the robotic agent.

In the project, the toy robot scientist extensively utilized these external sources, combining its own derived data with information from resources like CHEMBL. The process of integrating data and knowledge from diverse resources is referred to as knowledge and data integration, a difficult task due to inconsistent or varied textual information.

This integrated data is then unified into a machine-accessible, structured format, represented by the lab project's internal ontologies. These ontologies were largely imported from other sources, particularly those related to systems biology and biological entities. The architecture ensures that all necessary entities and information are consolidated for the robot scientist to reason over.

The underlying structure utilizes an upper-level ontology, which is foundational in systems biology and ensures essential interoperability between different data sets. This unified structure is characteristic of how real knowledge models are constructed. Although some external sources possess strict logical structures, this effort is challenging because all available information must be combined, harmonized, and encoded. The final goal is to provide a logically consistent dataset that the AI system can effectively reason with.

---

### 14_Recap_of_week_17_study_Video_1_min

# Recap of week 17 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/8C9zM/recap-of-week-17-study

This curriculum explores advanced topics across Artificial Intelligence, beginning with foundational Game Playing AI (Weeks 1-5). The initial focus involves developing AI game players, formally utilizing Reinforcement Learning principles and implementing the Deep Q-Network (DQN) agent for practical performance. Following this, the curriculum shifts to Evolving Artificial Creatures (Weeks 6-10), introducing automatic design via Genetic Algorithms. These studies involve building robots using specific tools like pybullet and incorporating URDF files, utilizing genetic encoding schemes, and defining fitness functions and selection processes to study evolving morphology.

The focus then transitions to Generative and Collaborative AI (Weeks 11-15), which explores generative systems broadly. Key technical deep dives include generating text with GPT-2 and composing music using specialized models such as MusicVAE and DiffSinger. These modules culminate in putting together integrated systems, such as a pop song generator.

The later phases center on "A Toy Robot Scientist," addressing historical, legal, and ethical perspectives on rational agents (Weeks 16-17). The system's core involves detailed knowledge representation, constructing both toy and real knowledge models in Python. Subsequent modules cover the design of the reasoning phase, planning, and analysis capabilities of the robot scientist. Furthermore, the curriculum delves into complex multi-agent environments and reviewing the state-of-the-art in Robot Scientist projects.

The final weeks are dedicated to consolidation, including exam preparation (Week 21) and final review (Week 22). This structured progression moves from trained behavioral systems (DQN) to evolving morphological systems (Genetic Algorithms) to creative output systems (Generative AI), and finally to complex reasoning and planning systems (Rational Agents/Robot Scientist).

---

### 15_Self-evaluation_checklist_Part_2_-_Building_the_system;_Knowledge_representation_Reading_30_min

# Self-evaluation checklist: Part 2 - Building the system; Knowledge representation
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/M9qdO/self-evaluation-checklist-part-2-building-the-system-knowledge-representation

This educational module establishes a comprehensive framework for understanding, implementing, and evaluating knowledge models within the context of Artificial Intelligence (AI) systems.

The first critical learning objective focuses on the comprehensive assessment of AI knowledge models. Students are required to identify and thoroughly explain various types of knowledge models employed in AI applications. Furthermore, a deep critical evaluation must be performed, examining the specific strengths and inherent limitations of these different knowledge structures when deployed in practical AI environments. A key component of this assessment is the ability to accurately determine the suitability of specific knowledge models for diverse AI-driven tasks and specialized domains.

The module also explores the profound potential of knowledge models concerning scientific discovery and research. Participants must be able to articulate precisely how these models contribute to advancing scientific understanding and research endeavors. This involves developing a well-supported argument that balances the significant advantages of using knowledge models in scientific contexts against the inherent challenges they present. Real-world case studies are required to exemplify how these knowledge models have successfully facilitated major scientific breakthroughs.

The third major area focuses on the practical development and implementation of knowledge models in a machine-processable format. Learners must be able to design and logically structure a simple knowledge model that effectively represents complex information. A crucial technical skill involves encoding this designed knowledge model using industry-standard machine-processable formats. These formats include Resource Description Framework (RDF), Web Ontology Language (OWL), Extensible Markup Language (XML), and JavaScript Object Notation (JSON).

Finally, the process of model development extends beyond simple encoding; learners must be able to rigorously test and refine their knowledge models. This refinement process ensures that the model functions correctly and predictably within a target AI system. Reflective practice guides students to identify personal learning challenges, specify areas requiring further review, and plan the practical application of acquired knowledge in future AI or scientific research projects.

---

## Week 18

### 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_Reasoning_-_slides_Reading_10_min

# Reasoning - slides
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/kWKLf/reasoning-slides

This course explores four major domains of advanced Artificial Intelligence, beginning with Game Playing AI (Weeks 1-5). The initial phase covers the implementation of AI game players, formalizing reinforcement learning principles, and focusing specifically on the Deep Q-Network (DQN) agent implementation and associated tooling. Moving into the realm of evolution, Weeks 6-10 detail the design of evolving artificial creatures, utilizing genetic algorithms for automatic design and incorporating robotics simulations via pybullet and URDF files. This segment emphasizes crucial concepts such as genetic encoding schemes, fitness function design, and the state of the art in evolving morphology.

The third module (Weeks 11-15) focuses on Generative and Collaborative AI, examining how systems create content. Key topics include the introduction to generative systems, lyric generation using GPT-2, music composition with MusicVAE, and advanced audio synthesis using DiffSinger. The practical application culminates in a sophisticated pop song generator, demonstrating the collaborative power of these generative models.

The fourth major theme, "A Toy Robot Scientist" (Weeks 16-20), delves into complex reasoning and knowledge representation. This module addresses the history, ethical implications, and system construction of a robot designed for scientific inquiry. Central to this phase is a crash course in logic, specifically detailing the generation of hypotheses through abduction and induction. Finally, the curriculum concludes with the integration of these concepts into planning and analysis, leading into preparation for the final exam.

---

### 03_Crash_course_in_logic_Video_15_min

# Crash course in logic
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/nWEGg/crash-course-in-logic

This course is structured around several major AI domains, starting with Game Playing AI, which covers the fundamentals in Weeks 1 through 5. The game playing modules introduce formal reinforcement learning and the implementation of the Deep Q-Network (DQN) agent, alongside examining the state of the art and ethical considerations in AI game players. The focus then shifts to evolving artificial creatures (Weeks 6–10), exploring automatic design using genetic algorithms and building robots via tools like pybullet and URDF files. Specific techniques taught include genetic encoding schemes, defining fitness functions, and state-of-the-art morphology evolution. Weeks 11 through 15 delve into Generative and collaborative AI, showcasing systems like GPT-2 for lyric generation, MusicVAE for composition, and DiffSinger, culminating in a complete pop song generator. The course then transitions to "A Toy Robot Scientist" (Weeks 16–20), covering the system's introduction, knowledge representation, and ethical perspectives. This module heavily emphasizes reasoning, including intensive lessons on logic, hypotheses generation through abduction and induction. Practical exercises include developing a Toy hypotheses generation agent and implementing planning and analysis capabilities for the robot. The curriculum integrates both high-level theoretical understanding and practical system building across all domains. The later weeks wrap up the material, culminating in an exam preparation week and the final assessment. The technical scope covers machine learning agents (DQN), evolutionary computation (Genetic Algorithms), and generative models (GPT-2, MusicVAE). This comprehensive approach covers both theoretical foundations and advanced implementations in AI research.

---

### 04_Crash_course_in_reasoning_Video_5_min

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

### 05_Hypotheses_generation_abduction_Video_8_min

# Hypotheses generation: abduction
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/j9Q7v/hypotheses-generation-abduction

This curriculum comprehensively explores advanced concepts in Artificial Intelligence, starting with **Game Playing AI** (Weeks 1-5). Early modules introduce the core concepts of game playing, leading into the formalization of reinforcement learning and the development of the Deep Q-Network (DQN) agent. Following this, the course shifts to **Evolving Artificial Creatures** (Weeks 6-10), focusing on automatic design using genetic algorithms and constructing robots using specialized tools like pybullet and URDF files. Key elements here include establishing genetic encoding schemes, designing fitness functions, and analyzing the state of the art in evolving morphology. The scope expands to **Generative and Collaborative AI** (Weeks 11-15), covering introduction to generative systems, generating lyrics with GPT-2, and advanced music composition via MusicVAE and DiffSinger. This culminates in a pop song generator project, demonstrating collaborative generative capability. The third major focus is **A Toy Robot Scientist** (Weeks 16-20), which details building a system, knowledge representation, and the crucial reasoning phase. This section provides deep dives into logical inference, including crash courses in induction and abduction, and exercises in hypothesis generation. The Robot Scientist module integrates planning and analysis, showcasing how AI agents function in complex, knowledge-based environments. This extensive journey moves from specific agent implementations (DQN) to broad generative systems (MusicVAE) and finally to complex cognitive modeling (Reasoning). Technical foundations include the implementation of DQN, the use of genetic algorithms, and the application of advanced linguistic and musical models like GPT-2 and DiffSinger. The coursework concludes with dedicated preparation and exam weeks, synthesizing knowledge from these diverse AI domains.

---

### 06_Hypotheses_generation_induction_Video_5_min

# Hypotheses generation: induction
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/zqExy/hypotheses-generation-induction

Induction is a crucial mechanism that enables the generalization of specific facts into broader rules for hypothesis generation. This inductive inference, however, is not guaranteed to be correct and necessitates subsequent testing and verification. For instance, observing that Daffy and Tweety are white swans leads to the induced rule that all swans are white, a rule which remains fallible. Our knowledge is inherently imperfect, as evidenced by how Newtonian mechanics was eventually overturned by the theory of relativity. Machine learning is fundamentally based on this inductive reasoning process. ML systems accept multiple data points, identify underlying patterns, and generalize these patterns to predict outcomes for unseen new data. A practical example includes predicting the future sale price of three-bedroom houses in Brighton, which were previously observed to sell for 300K to 350K. While such predictions are often accurate due to stable conditions, they are not absolute, mirroring the limitations of inductive reasoning. Inductive reasoning finds wide application in biomedical research due to the remarkably conservative nature of biology. Main engine functions are often conserved across diverse species, including intelligent humans. Specific genetic facts proven correct in one organism can be inductively generalized to others. For example, if Gene X has function Y in *Saccharomyces cerevisiae* (yeast), and also in *C. elegans*, it can be generalized to have function Y in *Homo sapiens*. The biological study of Sirtuins provides a key example, as these genes have been shown to regulate organismal lifespan. Abundance of certain genes was first reported to increase lifespan in budding yeast, later observed in model organisms like nematodes and fruit flies. Further research utilized zebrafish, where the absence of longevity genes like *sirt1* leads to oxidative injury, chronic inflammation, and reduced lifespan. This line of inquiry illustrates how induction is used to formulate hypotheses about gene functions and potential drug targets in humans. Structurally, the course incorporates a deep dive into these concepts, exemplified by the module "Hypotheses generation: induction." This section includes dedicated content such as a 5-minute video and a 30-minute Induction Practice Assignment. Technical components extend across various AI modules, including "Game playing AI: Part 2" which formalizes reinforcement learning and the DQN agent. Other specialized topics cover evolving artificial creatures, referencing components like Pybullet and URDF files. Generative AI is also explored, utilizing systems like MusicVAE and DiffSinger for creative applications. The curriculum includes the module "A toy Robot Scientist," focusing on knowledge representation and reasoning phases. The overall progression covers topics from Week 1 (AI game player) up to Week 22 (Exam week). The detailed structure ensures thorough learning, ranging from theoretical lectures to hands-on labs, such as the exercise to modify the toy robot hypotheses generation lab.

---

### 07_Reading_articles_Reading_1h

# Reading articles
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/MbUyk/reading-articles

Essential reading: Read the following research articles and pay particular attention to how novel hypotheses were generated: Williams, K., Bilsland, E., Sparkes, S et al. Cheaper faster drug development validated by the repositioning of drugs against neglected tropical diseases . Journal of the Royal Society Inerface (2015). Soldatova, L.N., Rzhetsky, A. (2011) Representation of research hypotheses. Journal of Biomedical Semantics, 2: S9. Available in the Online Library ....

---

### 08_Hypotheses_generation_agent_Video_10_min

# Hypotheses generation agent
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/w6FO4/hypotheses-generation-agent

The curriculum begins with AI Game Playing, covering core concepts from Week 1 to Week 5, focusing heavily on formalizing reinforcement learning and implementing the Deep Q-Network (DQN) agent, while also addressing state-of-the-art and ethical considerations in these systems. Modules 6 through 10 introduce evolving artificial creatures, employing genetic algorithms for automatic design, constructing robots using environments like PyBullet and URDF files, and defining fitness functions and genetic encoding schemes. The Generative and Collaborative AI segment (Weeks 11–15) delves into generative systems, showcasing practical applications such as generating lyrics with GPT-2, composing music using MusicVAE, and exploring advanced techniques like DiffSinger. The "Toy Robot Scientist" module (Weeks 16–20) focuses on building systems for reasoning, encompassing knowledge representation, the reasoning phase, and sophisticated hypothesis generation. Key reasoning skills are separately taught in depth, covering logical crash courses, and specific methodologies like abduction and induction, which are applied within the Toy hypotheses generation agent. This latter phase emphasizes planning, analysis, and reviewing the state of art in complex robot scientist projects. The curriculum structure progresses from foundational AI models (DQN) to evolutionary design (Genetic Algorithms) and finally to advanced knowledge-based reasoning systems. The focus remains highly technical, detailing specific tools, such as PyBullet and URDF files, and specific generative models, such as GPT-2 and MusicVAE. The advanced reasoning components involve critical activities like generating hypotheses via abduction and induction, complemented by extensive logical practice assignments. Overall, the course provides a comprehensive journey from learning how AI agents play games to designing autonomous, reasoning scientific robots.

---

### 09_Recap_of_Week_18_study_Video_1_min

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

### 10_Self-evaluation_checklist_Part_3_-_Robot_Scientist_reasoning_phase_Reading_30_min

# Self-evaluation checklist: Part 3 - Robot Scientist reasoning phase
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/jeFdi/self-evaluation-checklist-part-3-robot-scientist-reasoning-phase

This text outlines a comprehensive self-evaluation checklist for Week 18, focusing on the introduction to the Robot Scientist Reasoning Phase. The core theme revolves around the critical role of knowledge models in achieving AI-driven scientific discovery. The initial phase requires students to develop a robust argument concerning the necessity and function of knowledge models within scientific contexts. A foundational understanding must be established regarding the definition of a knowledge model and its specific function in driving scientific discovery. Furthermore, students must explain the importance of the reasoning phase utilized by a robot scientist in the context of advanced AI research.

The checklist mandates a critical discussion of the potential benefits and inherent limitations associated with leveraging knowledge models in the process of automating scientific discovery. A key argumentative component involves developing an argument detailing how knowledge models effectively enhance the mechanisms of both hypothesis generation and subsequent hypothesis validation. This section also requires a critical examination of the unique challenges that exist when attempting to implement automated reasoning within complex scientific settings.

The second major section focuses on the rigorous assessment of knowledge models for suitability within AI systems. It is essential to define and clearly differentiate the three primary methods of hypothesis generation: abduction, induction, and deduction. Students must demonstrate an understanding of how a hypotheses generation agent functions within the broader architecture of AI systems. Practical evaluation criteria for knowledge models include assessing their accuracy, completeness, and overall operational efficiency. Furthermore, a critical assessment is required to determine if a given knowledge model is technically suitable for supporting AI-based scientific reasoning. This includes identifying and analyzing inherent limitations in existing knowledge models that could negatively impact AI performance.

The third section addresses the practical implementation and formal representation of knowledge. This involves explaining the concept of machine-processable knowledge representation, ensuring the knowledge can be consumed by a computer. Various technical formats for representing knowledge have been explored, such as logic-based systems, semantic networks, and ontologies. Competency is required to construct a basic knowledge model that logically represents complex scientific concepts. Finally, students must be able to encode these simple knowledge models using precise logical rules or structured data formats. This final step ensures an understanding of how the constructed knowledge model can ultimately be utilized by an AI system for complex reasoning and discovery. The module concludes with a reflection on the confidence and defended understanding of knowledge models' impact on AI research.

---

## Week 19

### 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_New_Reading_Reading_10_min

# New Reading
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/2Dyvv/new-reading

This curriculum progresses through several advanced topics in artificial intelligence, beginning with AI Game Playing. The early phase (Weeks 1-5) introduces foundational AI players, culminating in the implementation of the Deep Q-Network (DQN) agent, covering concepts like formal reinforcement learning and ethical considerations in AI game players. The focus then shifts to evolving artificial creatures (Weeks 6-10), exploring automatic design through genetic algorithms and the construction of robots using tools like pybullet and URDF files. Key elements in this segment include genetic encoding schemes and the development of robust fitness functions and selection processes for evolving morphology. Following this, the module delves into Generative and Collaborative AI (Weeks 11-15), examining systems from introductory concepts to practical applications. Specific projects feature generating lyrics using GPT-2, composing music with MusicVAE, and utilizing advanced models like DiffSinger, ultimately culminating in a complete pop song generator. The final major theme is "A Toy Robot Scientist" (Weeks 16-20), which focuses on building a complex reasoning system. This includes knowledge representation, introducing the Robot Scientist reasoning phase, and mastering planning and scheduling of experiments. The practical exercises involve analyzing experimental results and modifying the planning and analysis agents. The entire program concludes with a comprehensive preparation phase and subsequent exam week.

---

### 03_Crash_course_in_planning_and_scheduling_Video_8_min

# Crash course in planning and scheduling
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/UbymE/crash-course-in-planning-and-scheduling

This mini-lecture outlines the complexities of planning and scheduling, addressing both classical and real-world scenarios. Planning is a critical application in fields such as manufacturing and robotics. The field utilizes dedicated languages, such as PDDL (Planning Domain Definition Language), which serves as a primary standard for planning. Classical planning handles observable, deterministic situations and is modeled as a search problem. This involves defining an initial state, possible actions, and the desired goal state. The objective is to find a sequence of actions that successfully transitions the system from the initial state to the goal state. Algorithms employed for searching and planning include breadth-first search, depth-first search, and heuristic search. Deductive reasoning can also be applied by reasoning agents to locate solutions for planning tasks. Actions are typically formalized using a schema that specifies parameters, preconditions, and effects. For instance, a schema for "flying the plane" requires preconditions (e.g., plane at origin, airport access) and defined effects (e.g., plane is no longer at origin).

A classic illustration of this process is the blocks world problem, where a robot arm manipulates blocks on a table. This state is represented using predicate notation, identifying relations like `on(Block, Object)` or `clear(Object)`. The initial state is a list of predicates describing the arrangement of blocks and locations. An action's preconditions specify when it can occur, while its effects list the resulting changes to the system's relationships.

Real-world planning fundamentally differs from classical planning due to environmental uncertainties. Classical planning relies on the closed world assumption, meaning non-explicitly mentioned information is assumed not to exist. In contrast, agents operating in real environments must adhere to the open world assumption, recognizing that undefined information is simply unknown. Real-world agents must often produce contingent plans, which involve conditional branching due to partial observability and non-determinism. Furthermore, dynamic environments necessitate continuous monitoring and potential re-planning if goals or expected outcomes change unexpectedly.

Beyond just sequencing actions, the real world introduces temporal and resource constraints, which form the basis of scheduling problems. Planning typically focuses on *what* actions to perform, while scheduling focuses on *when* and *how long* they take, often requiring separate solutions. Resource constraints involve both reusable resources (like staff) and consumable resources (like chemicals).

Multi-agent planning introduces further complexity by requiring coordination between multiple autonomous agents. Agents may cooperate toward a shared goal, compete, or operate independently. Joint planning generates plans for coordinated actions, and agents may or may not need communication. Ultimately, the scope encompasses finding solutions in environments that are partially observable, non-deterministic, and constrained by resources and agent interactions.

---

### 04_Planning_and_scheduling_experiments_by_the_Robot_Scientists_Video_12_min

# Planning and scheduling experiments by the Robot Scientists
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Lohom/planning-and-scheduling-experiments-by-the-robot-scientists

This curriculum is structured across various advanced AI disciplines, beginning with game playing AI. The first phase covers AI game players, detailing the progression from foundational AI concepts (Weeks 1-3) to formalizing reinforcement learning and implementing the Deep Q-Network (DQN) agent (Weeks 2-4). Further exploration into this domain addresses state-of-the-art techniques and ethical considerations regarding AI game players (Week 5).

Next, the focus shifts to evolving artificial creatures, introducing automatic design methods using genetic algorithms (Week 6). This segment also covers the practical construction of robots using specific tools like pybullet and URDF files (Week 7), alongside detailed technical components such as genetic encoding schemes and fitness function selection (Weeks 8-9). The study concludes this module by reviewing the state of the art in evolving morphology (Week 10).

The third major block explores generative and collaborative AI, starting with an introduction to generative systems (Week 11). Technical implementations include generating lyrics using GPT-2 (Week 12), composing music with MusicVAE (Week 13), and examining advanced models like DiffSinger (Week 14), culminating in a comprehensive pop song generator project (Week 15).

The final and most extensive section introduces "A Toy Robot Scientist," covering its foundational history, perspectives, and legal/ethical issues (Week 16). The system development progresses through knowledge representation (Week 17), the core reasoning phase (Week 18), and planning and analyzing experimental results (Weeks 19-20). Week 19 specifically details crash courses in planning, scheduling, and system analysis, which are essential for the robot's operation, before concluding with state-of-the-art Robot Scientist projects in Week 20.

---

### 05_Planning_and_scheduling_Reading_1h

# Planning and scheduling
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/wFAmo/planning-and-scheduling

Essential reading: Read the following research articles and pay particular attention to how experiments were planned: Williams, K., Bilsland, E., Sparkes, S et al. Cheaper faster drug development validated by the repositioning of drugs against neglected tropical diseases . Journal of the Royal Society Inerface (2015). King, R.D., Rowland, J., Oliver, S.G., Young, M., Aubrey, W., Byrne E., Liakata, M., Markham, M., Pir, P. Soldatova, L.N., Sparkes, A., Whelan, K.E., Clare, A....

---

### 06_Walkthrough_the_toy_planning_agent_Video_20_min

# Walkthrough the toy planning agent
Video • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/wKlGo/walkthrough-the-toy-planning-agent

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

### 07_Analysing_experimental_results_by_the_Robot_Scientists_Video_8_min

# Analysing experimental results by the Robot Scientists
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/KQjyV/analysing-experimental-results-by-the-robot-scientists

This curriculum explores three major areas of modern artificial intelligence: Game Playing, Evolutionary Design, and Generative Systems, culminating in the advanced topic of autonomous scientific reasoning. The study of Game Playing AI begins with foundational concepts, transitioning into formal Reinforcement Learning and the implementation of the Deep Q-Network (DQN) agent. Key technical details include understanding the state of the art, ethical considerations in AI game players, and the full implementation cycle of the DQN agent.

The curriculum then shifts to Evolving Artificial Creatures, focusing on automatic design using Genetic Algorithms. This section details the construction of robots utilizing environments like PyBullet and specific structural definitions through URDF files. Core concepts involve establishing a genetic encoding scheme and defining robust fitness functions for selection processes, leading to an examination of evolving morphology.

Next, Generative and Collaborative AI is covered, introducing various generative systems. Specific projects include generating lyrics with GPT-2 and composing music using MusicVAE and DiffSinger, concluding with a pop song generator project.

The final major section focuses on the sophisticated domain of the Robot Scientist, which involves tackling complex tasks of knowledge representation and reasoning. This segment dedicates significant time to the planning and scheduling of experiments, utilizing structured crash courses and practical assignments. Furthermore, the Robot Scientist must master the process of analyzing experimental results and understanding the state of the art in robotic scientific projects.

---

### 08_Analysing_experimental_results_Reading_1h

# Analysing experimental results
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/hHBQa/analysing-experimental-results

Essential reading: Read the following research articles and pay particular attention to how experimental results were analysed: Williams, K., Bilsland, E., Sparkes, S et al. Cheaper faster drug development validated by the repositioning of drugs against neglected tropical diseases . Journal of the Royal Society Inerface (2015). King, R.D., Rowland, J., Oliver, S.G., Young, M., Aubrey, W., Byrne E., Liakata, M., Markham, M., Pir, P. Soldatova, L.N., Sparkes, A., Whelan, K.E., Clare, A....

---

### 09_Recap_of_Week_19_study_Video_1_min

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

### 10_Self-evaluation_checklist_Part_4_-_Planning_and_analysing_Reading_30_min

# Self-evaluation checklist: Part 4 - Planning and analysing
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/C1gAH/self-evaluation-checklist-part-4-planning-and-analysing

This document functions as a self-evaluation checklist designed to assess a user’s understanding of concepts covered in Week 19 – Part 4: Planning and Analysing. The learning outcomes are structured across three major areas of study.

The first area focuses on comparing and contrasting classical planning problems with real-world planning problems. Learners must be able to define classical planning problems and thoroughly explain their inherent characteristics. Additionally, the assessment requires describing real-world planning scenarios and detailing how they fundamentally differ from the traditional classical approach. A crucial component is the identification of key challenges present in real-world planning, specifically mentioning issues like uncertainty and complex constraints. The overall goal of this section is to provide a comprehensive comparison and contrast between these two types of planning, utilizing relevant examples for illustration.

The second area addresses the critical steps involved in planning scientific experiments using a Robot Scientist. A key concept here is defining the specific role of a Robot Scientist in the field of automating complex scientific experiments. The checklist necessitates outlining the detailed sequence of key steps required when planning an experiment under this automated framework. Furthermore, understanding how hypotheses are successfully formulated and rigorously tested through the mechanism of automated planning is essential knowledge. Learners must also be able to explain how Robot Scientists actively optimize the experimental design to maximize both efficiency and accuracy.

The third area focuses on how the Robot Scientist analyzes the gathered experimental results. Understanding the specific methods employed by Robot Scientists to analyze complex experimental data is a learning objective. The process requires describing how the raw data is properly interpreted to refine existing hypotheses and consequently improve the design of future experiments. A significant technical element involves explaining the vital role that both machine learning and artificial intelligence play in the detailed process of experimental analysis. Finally, competency is measured by the ability to provide a concrete example of how a Robot Scientist utilizes the obtained results to successfully adapt its overarching approach. This checklist serves as a comprehensive guide to mastering advanced planning and analytical techniques.

---

## Week 20

### 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_State_of_the_art_-_slides_Reading_10_min

# State of the art - slides
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/RtgkX/state-of-the-art-slides

This curriculum progression begins with Game Playing AI, covering topics from basic AI game players (Week 1) to formalizing reinforcement learning and the DQN agent (Week 2-4), culminating in a "State of the Art and Ethics" review (Week 5). The focus then shifts to Evolving Artificial Creatures (Week 6-10), detailing automatic design using genetic algorithms, robot construction with pybullet and URDF files, genetic encoding, and fitness function analysis. Generative and Collaborative AI follows (Week 11-15), exploring systems such as generating lyrics with GPT-2, music composition with MusicVAE, and advanced models like DiffSinger. Weeks 16-20 are dedicated to "A Toy Robot Scientist," which encompasses introduction, knowledge representation, the Robot Scientist reasoning phase, planning, and analysis. The latter portion of the course emphasizes advanced applications, including meta-analysis and multi-agent communication systems. Specific technical tools utilized include pybullet, URDF files, DQN agents, genetic algorithms, GPT-2, and MusicVAE. The study structure incorporates various learning modalities, including videos, detailed readings, and practical assignments to reinforce theoretical concepts. The final weeks are dedicated to exam preparation and a comprehensive review of the State of the Art in the field. Overall, the module culminates in an understanding of complex AI system design, from game-playing agents to sophisticated robot scientists.

---

### 03_Meta-analysis_agent_Video_10_min

# Meta-analysis agent
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/41Cx2/meta-analysis-agent

The robot scientist utilizes a core set of agents to execute a full scientific investigation cycle. These agents include the Knowledge Agent, which encodes underpinning knowledge for the robot scientists. Following this, the Hypothesis Generation Agent formulates new hypotheses to be tested. The Planning Agent then produces an experimental protocol based on these hypotheses. Next, the Automated Robotic Lab Agent executes this protocol and meticulously records all experimental results. Finally, the Experimental Results Analysis Agent determines whether the initial hypothesis was confronted or refuted. To enhance the performance of these scientists, additional agents, such as a Meta Analysis Agent, are utilized. A Meta Analysis Agent collects information about all previous experimental rounds and results. It also compares the performance of various agents, determining under what specific situations they function optimally. For instance, it can advise on which methods the Hypothesis Generation Agent should employ. The specific implementation of such an agent for the robot scientists utilized a method called disk method cosine. The core technique powering this advanced capability is meta learning, or "learning to learn." Meta machine learning is a powerful approach that learns about machine learning algorithms and their parameters. Specifically, it determines which algorithms perform best on certain datasets. The robot scientist Yves applies this technique through Meta-QSAR learning to predict chemical compounds based on their structure and activity. This work is detailed in the open access paper, *Meta-QSAR, a large-scale application of meta learning to drug design and discover*. The detailed methodology is also available in the Journal of machine learning. The QSAR task involves giving a target, typically a protein, and a set of chemical compounds, also known as small molecules. These compounds are associated by their activity, such as inhibiting the target. The fundamental principle underlying Meta-QSAR is the "no free lunch theorem." This theorem posits that no single, universal machine learning algorithm performs best across all possible datasets. Therefore, meta learning seeks to understand which learning method is better suited for specific scenarios. The motivation was to understand the performance characteristics of baseline machine learning methods in QSAR learning. The Meta-QSAR goal was to select the best combination of QSAR and molecular representations for any given problem. Researchers considered over 8,000 QSAR datasets for this analysis. These datasets featured various characteristics, including number of examples and mutual information. Eighteen base-level learning algorithms were evaluated, including linear regression, support vector machines, neural networks, regression trees, and random forests. Before the meta-learning stage, nearly 3,000 drug targets were extracted from ChEMBL, a curated public database. Each chemical compound was represented by binary fingerprints showing presence or absence. Initial baseline learning showed that Random Forest was the best performer, achieving high accuracy in more than 1,000 targets. However, Random Forest was not superior in over 50 percent of cases, necessitating the meta-learning approach. To facilitate meta-learning, comprehensive meta-datasets were constructed using key features. These features, or meta-features, included dataset characteristics and drug target properties. These meta-features were organized using the Meta-QSAR ontology. This ontology described properties like the number of compounds and mutual information. The final meta-dataset contained over 2,000 meta-features spanning more than 8,000 datasets. After training the meta-QSAR learner, performance was evaluated against a default Random Forest baseline. The results demonstrated that most algorithms suggested by the meta-QSAR learner performed better than the initial random forest default. This confirms that meta-learning successfully optimizes algorithm selection for specific QSAR tasks. Furthermore, this meta-analysis agent framework can be generalized to solve other complex learning problems beyond QSAR.

---

### 04_Communication_in_multi-agent_systems_Video_20_min

# Communication in multi-agent systems
Video • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/o9CXA/communication-in-multi-agent-systems

This comprehensive curriculum covers four major areas of advanced artificial intelligence, beginning with AI game playing. The game playing module formalizes Reinforcement Learning (RL), specifically detailing the implementation and state-of-the-art applications of the Deep Q-Networks (DQN) agent, alongside ethical considerations in AI. Next, the course delves into evolving artificial creatures through Genetic Algorithms (GA), focusing on automatic design, genetic encoding schemes, and fitness function optimization. Practical robotic development is addressed by building physical simulations using specialized tools like Pybullet and URDF files. The generative AI segment introduces systems for creative output, utilizing models such as GPT-2 for lyric generation, MusicVAE and DiffSinger for sophisticated music composition, culminating in a pop song generator. A significant portion is dedicated to the "Toy Robot Scientist" project, exploring systems that involve knowledge representation, advanced reasoning phases, and complex planning capabilities. This module also addresses the legal and ethical perspectives inherent in designing sophisticated artificial agents. Finally, the curriculum synthesizes these concepts by examining meta-analysis agents and the dynamics of communication within multi-agent systems, preparing students for final examination.

---

### 05_Reading_articles_Reading_1h

# Reading articles
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/UkC4o/reading-articles

...

---

### 06_Robot_Scientist_new_projects_Video_17_min

# Robot Scientist: new projects
Video • 17 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/BpwGy/robot-scientist-new-projects

The lecture introduces two cutting-edge projects leveraging robotic scientists: "Action on Cancer" and "AMBITION."

The first project, Action on Cancer, is a decision support system aimed at designing personalized cancer treatments. This initiative is a collaboration involving the University of Cambridge and Goldsmiths College, funded by the Research Council UK (EPSRC) with a budget of £1.4 million over four years. The core objective is to develop an AI prototype capable of recommending personalized drug cocktails for cancer patients.

Cancer is identified as a critical global health threat, with estimates pointing to 13 million deaths and 20 million new cases annually by 2025. Traditional single-drug chemotherapy is insufficient because cancer easily develops resistance mechanisms, necessitating a more complex approach.

Action focuses specifically on combinations of multiple drugs, typically recommending between six and twelve agents. This

---

### 07_Recap_of_week_20_study_Video_1_min

# Recap of week 20 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/LLPvV/recap-of-week-20-study

This curriculum explores diverse domains of advanced AI, starting with Weeks 1-5, which focus on Game Playing AI through the formalization of Reinforcement Learning and the implementation of the Deep Q-Network (DQN) agent, alongside an examination of related ethical considerations. The focus shifts in Weeks 6-10 to Evolving Artificial Creatures, where genetic algorithms are utilized for automatic design and building robots using simulation tools like Pybullet and URDF files, underpinned by specific genetic encoding schemes and fitness functions. Weeks 11-15 delve into Generative and Collaborative AI, introducing systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition, culminating in integrated projects like pop song generators. The latter half of the course is dedicated to the "Toy Robot Scientist" (Weeks 16-20), a sophisticated system involving knowledge representation, specialized reasoning phases, planning, and the analysis of multi-agent systems. Key components of the Robot Scientist include meta-analysis agents and structured frameworks for state-of-the-art projects. Technical coverage spans from discrete reinforcement learning techniques to continuous system modeling and complex multi-agent communication. The module emphasizes practical implementation, as seen in the construction of the DQN agent and the building of evolving robotic systems. Throughout the curriculum, significant time is allocated to understanding the legal and ethical issues surrounding AI systems and advanced automated design. The course concludes with extensive preparation and examination weeks (Weeks 21-22) to synthesize the vast range of AI concepts and findings.

---

### 08_Self-evaluation_checklist_Part_5_-_State_of_the_art_Robot_Scientist_projects_Reading_30_min

# Self-evaluation checklist: Part 5 - State of the art Robot Scientist projects
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/nXsMP/self-evaluation-checklist-part-5-state-of-the-art-robot-scientist-projects

Use this checklist to assess whether you have met the expected learning outcomes for this week. 1. Critical Assessment of Automated Scientific Discovery ☐ I can explain the concept of automated scientific discovery and its significance. ☐ I can describe the Robot Scientist project and its contributions to this field. ☐ I have critically assessed the current state of research on Robot Scientists, including strengths and limitations....

---

## Week 21

### 01_Key_concepts_review_Reading_30_min

# Key concepts review
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/i4xYn/key-concepts-review

This module provides a foundational review of key concepts across four major areas of Artificial Intelligence (AI). Topic 1 focuses on Game Playing AI using Reinforcement Learning (RL), a machine learning type where an agent learns decisions through rewards or penalties. Q-Learning is a core RL algorithm that determines an optimal action-selection policy utilizing a Q-table. Deep Q-Network (DQN) elevates this by integrating Q-learning with neural networks for complex decision-making in games. The mathematical modeling of these decisions is provided by the Markov Decision Process (MDP), which frameworks situations with partly random outcomes. Developing and comparing these algorithms is facilitated by the OpenAI Gym toolkit, while Keras serves as an open-source deep learning API for building networks. Neural Networks are computational models inspired by the human brain, used for advanced pattern recognition and learning. Fundamentally, a Loss Function is a mathematical tool evaluating how closely a model’s predictions align with actual outcomes. Finally, AI concepts differentiate between General AI, capable of any human intellectual task, and Human-Competitive AI, which matches or surpasses human performance.

Topic 2 explores Evolving Creatures via Genetic Algorithms (GA), an optimization technique inspired by natural selection to evolve solutions. This field belongs to Bio-Inspired Computing, which leverages biological processes for computational methods. Artificial Life Systems simulate natural life forms and evolution using computational models. A Morphology Evolving System is specifically designed to evolve physical or structural traits over iterations. URDF (Unified Robot Description Format) defines the structure and properties of robots, often utilized with the PyBullet physics simulation engine. The process involves Genetic Encoding, which digitally represents potential solutions as "genes." A Fitness Function critically evaluates the performance of any given solution within the genetic algorithm. Variation is introduced through Genetic Manipulation techniques, such as mutation and crossover, driving Evolutionary Computing to solve complex optimization problems.

Topic 3 covers Creative AI Generative Models, which are AI designed to create new data resembling existing datasets. Generative models can be improved through Fine-Tuning, adjusting a pre-trained model for specific datasets. GPT-2 is a noted generative AI model developed by OpenAI, specializing in natural language processing. Transformers leverage the Self-Attention Mechanism, a component that allows AI to weigh different parts of an input sequence. Latent Space is a mathematical representation where complex data is compressed for generation. The Variational Autoencoder (VAE) is a generative model that learns latent representations for generating novel samples. Creativity can be viewed Skinnerianly, based on reinforcement and learned behavior, or Dewianly, emphasizing experience and dynamic interaction. Practical applications include Speech Synthesis for human-like speech and Multi-Track MIDI Generation for AI music compositions.

Topic 4 focuses on Robot Scientists and Knowledge Representation, the method of structuring information for AI reasoning. This pursuit leads to Automated Scientific Discovery, where AI autonomously generates new scientific knowledge. A Robot Scientist is an AI system designed specifically to conduct experiments and make scientific breakthroughs. Structured data that AI can interpret is termed Machine-Processable Knowledge. Planning Techniques encompass AI strategies for developing and executing action sequences. Experiment Planning is the specific process where AI determines the optimal experimental setups required. Meta-Machine Learning describes a learning approach where AI models continually adapt and improve based on accumulated experience. This research advances State-of-the-Art AI, contrasting theoretical Classical Planning with practical Real-World Planning. The future holds significant potential for Robot Scientists in furthering scientific research.

---

### 02_Mock_exam_Reading_10_min

# Mock exam
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/wqpiM/mock-exam

Please find below a mock exam. This only contains PART B, the long answer questions. The real exam will include a multiple choice quiz section which you will take on the exams platform as per other exams. uolww_exam_long_answer.pdf PDF File Mock exam Please find below a mock exam. This only contains PART B, the long answer questions. The real exam will include a multiple choice quiz section which you will take on the exams platform as per other exams....

---

## Week 8

### 01_Weekly_introduction_Video_2_min

# Weekly introduction
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/UamSO/weekly-introduction

This course structure covers a broad spectrum of advanced AI topics, beginning with Game Playing AI, formalizing concepts like Reinforcement Learning and the DQN agent (Weeks 2-4). The initial modules introduce tooling for Game Playing AI and focus on the implementation of the Deep Q-Network (DQN) agent. Following this foundation, the curriculum transitions into the study of Evolving Artificial Creatures (Weeks 6-10). These segments explore automatic design using genetic algorithms and build sophisticated robots utilizing PyBullet and URDF files.

The later phase focuses on Generative and Collaborative AI, establishing the groundwork with generative systems (Week 11). Key techniques introduced include generating lyrics using GPT-2 and performing music composition via MusicVAE. The most advanced area covered is speech and vocal synthesis, highlighted in Week 14. The Week 4 content introduces a challenging, state-of-the-art speech synthesis model, current for 2021-2022 research.

Learning objectives for this week include providing historical examples of speech synthesis systems, such as the singing generated by HAL 9000 from *2001*. Furthermore, students must gain an insight into the substantial complexity of modern speech synthesis research. The practical focus involves using a pre-trained speech synthesis model coupled with pitch correction technology. This process generates singing voices from specific inputs: a list of desired lyrics and corresponding musical notes.

The output of this system is a rendered audio file, which can be visualized as a spectral spectrogram. A major technical model discussed in this area is DiffSinger. The course is highly comprehensive, progressing to include a "Pop Song Generator" in Week 15. Subsequent weeks cover specialized AI applications, including a "Toy Robot Scientist" module (Weeks 16-20). This final segment delves into knowledge representation, system building, reasoning, and planning within robotic systems. Throughout the course, students engage with complex assignments, including experiments with DiffSinger and self-evaluation checklists.

---

### 02_Slides_for_week_8_Reading_30_min

# Slides for week 8
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/BJFJn/slides-for-week-8

The provided materials for Week 8, covering AI-2 Genetic Encoding, include two PDF slides: `ai-2-genetic-encoding-theory.pdf` and `ai-2-genetic-encoding-practice.pdf`.

---

### 03_Genetic_encoding_problem_overview_Video_12_min

# Genetic encoding problem overview
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/oNfw2/genetic-encoding-problem-overview

This course examines various advanced topics in Artificial Intelligence, starting with sophisticated methods for AI game players. Weeks 1 through 5 focus on game playing AI, detailing the formalization of reinforcement learning and the implementation of the Deep Q-Network (DQN) agent. A key technical element is the implementation of the DQN agent itself, complemented by an analysis of the current state of the art and the associated ethical considerations in AI game players. The course then transitions to evolving artificial creatures, emphasizing automatic design using Genetic Algorithms (GA) in Weeks 6 and 7. Week 7 specifically covers building robots using the pybullet simulator and defining robot structures via URDF files.

Week 8 provides an in-depth technical dive into Genetic Encoding, detailing the process from genome generation to a graph structure. This module mandates converting flat genes into a graph algorithm and then mapping the resulting genome into XML code. Further technical topics in Week 8 include geometric fixes for robot children and integrating motors into the structure. The evolutionary segment continues in Weeks 9 and 10, focusing on the essential concepts of the fitness function and selection methods crucial for evolving morphology.

The curriculum subsequently shifts to Generative and Collaborative AI, exploring systems that create novel content. Weeks 12 through 15 are dedicated to specific generative models, such as generating lyrics using GPT-2 and composing music with MusicVAE. The program also covers advanced synthesis techniques, including DiffSinger, culminating in a comprehensive pop song generator project.

The latter portion of the course introduces "A Toy Robot Scientist," an application-focused study. Weeks 16 through 20 cover the history, perspectives, legal, and ethical issues surrounding robots. Technical aspects include building the system, knowledge representation, the reasoning phase, planning, and analyzing complex tasks. The modules conclude by reviewing the state-of-the-art in Robot Scientist projects, followed by dedicated exam preparation and the final exam week. All modules provide detailed video and reading materials, guiding students through practical implementation, quiz assignments, and self-evaluation checklists.

---

### 04_Deciding_on_the_parameters_and_their_ranges_Video_13_min

# Deciding on the parameters and their ranges
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/tdTSX/deciding-on-the-parameters-and-their-ranges

The provided transcript segment details a rigorous technical process of **parameterizing and defining the morphology** of an evolving artificial creature or robot. This discussion outlines the requirements for creating a dynamic structure that can be manipulated through a control system.

The course schedule contextually aligns this discussion with **Week 8: Evolving artificial creatures: Part 3 - Genetic encoding scheme**, where the focus is on deciding on parameters and implementing genome-to-graph conversions.

Here is a summary of the key concepts discussed in the transcript:

---

### ⚙️ Morphological Design (Links and Joints)

The creature is built "piece by piece," focusing on the structure of links and joints.

1.  **Incremental Building:** Links are added one at a time. As more links are added, the number of possible connection points increases dynamically (e.g., from 1 option to 2, then 3, and so on).
2.  **Dynamic Parameterization:** To manage this complexity, a dedicated parameter is required for each new link. This parameter dictates *which* of the available connection points the new link will attach to.
3.  **Scaling Requirement:** Crucially, this parameter must be **dynamically scaled** so that it can correctly choose from the entire range of available links as the structure grows.

### 📡 Control System Definition

The system requires specialized **signal generators** to drive the creature's joints. These generators are tied directly to the joints to ensure accurate control.

The control system relies on three primary parameters:

1.  **Waveform:** Determines the signal pattern (must be one of: **Sine, Pulse, or Ramp**).
2.  **Amplitude (0 to 1):** Dictates the speed of the motor. An amplitude of 1 means maximum speed.
3.  **Frequency (0 to 1):** Controls how often the polarity of the motor changes. When the polarity flips (positive $\rightarrow$ negative), the motor reverses direction.

### 📊 Conclusion and Scope

*   **Total Parameters:** The process concludes that a total of **17 parameters** are necessary to completely control and define the morphology of the creatures.
*   **Goal:** The overarching aim is to successfully parameterize the structure (links and joints) and define the input mechanism (the control system) so that the creature's physical shape and movement can be computationally defined.

---

### 05_Lesson_introduction_Reading_10_min

# Lesson introduction
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/uO2yi/lesson-introduction

This lesson introduces the codebase for implementing the genetic algorithm. The core subject matter involves dealing with a substantial volume of specialized code. The primary focus of this coding lesson is the mechanisms required to encode and interpret structural information. Specifically, attention is placed on how to manage the directed graph structure that serves as the basis for the creature model. This directed graph structure is the foundational element defining the creature's architecture. The instructional videos accompanying the code are necessarily lengthy. This extended duration is because the instructor provides an extremely detailed explanation of nearly every line of code. Learners are encouraged to speed up the playback of these videos to facilitate a faster completion rate.

---

### 06_Test_driven_approach_Video_9_min

# Test driven approach
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/4dM8w/test-driven-approach

This curriculum comprehensively outlines 22 weeks of study in advanced Artificial Intelligence, structured across several key domains. Weeks 1 through 5 focus on Game Playing AI, beginning with the development of AI game players. This section progresses by formally tackling reinforcement learning and introducing the Deep Q-Network (DQN) agent in Week 2. Game playing AI tooling is examined in Week 3, followed by the implementation of the DQN agent itself in Week 4. The study concludes the AI game playing module by exploring the state of the art and the associated ethical issues in Week 5.

The curriculum shifts dramatically in Week 6 to the topic of Evolving Artificial Creatures, starting with automatic design using genetic algorithms. Week 7 integrates physical simulation by building robots using pybullet and URDF files, providing a practical environment for evolution. Week 8 details the critical genetic encoding scheme, which involves extensive implementation. This implementation starts with generating a genome, followed by converting the flat gene structure into a graph.

Further technical depth in Week 8 involves converting flat genes to a graph algorithm, a process reinforced through multiple coding activities and quizzes. The material then advances to implementing the genome to XML code, requiring the interpretation of the genome specification. This leads to defining a `Creature class` and implementing the `toXML` function to represent the creature structure. The final phases of Week 8 cover crucial mechanical aspects, including geometry fixing and adding motors, finalizing the full decoding process.

Weeks 9 and 10 continue the study of evolving artificial creatures, focusing specifically on the fitness function, selection methods, and the state of the art in evolving morphology. The scope then broadens to Generative and Collaborative AI, starting in Week 11 with an introduction to generative systems. This segment includes practical applications like generating lyrics using GPT-2 in Week 12.

Technical generation continues in Week 13 with music composition using MusicVAE, followed by the investigation of DiffSinger in Week 14. Week 15 consolidates these generative skills by building a pop song generator, demonstrating the synthesis of various models. The final major theme, Weeks 16 through 20, introduces the "Toy Robot Scientist." This module covers the history, legal, and ethical issues of robotics in Week 16. Subsequent weeks focus on building the system, knowledge representation, and introducing the Robot Scientist reasoning phase. The course culminates in the detailed study of planning, analysis, and the state of the art in Robot Scientist projects. Weeks 21 and 22 are dedicated to final exam preparation and the exam itself.

---

### 07_Generate_a_genome_Video_16_min

# Generate a genome
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/fNmBh/generate-a-genome

The provided transcript details a focused coding session centered on **Test-Driven Development (TDD)** for implementing the core algorithms of **Genetic Encoding**, specifically the process of generating random genomes and genes.

Here is a summary of the key activities and progress made:

### 🧬 Core Goals & Methodology
The primary objective is to build the underlying logic to create random, functional genomes. This is achieved strictly through the TDD methodology: writing a test that fails, implementing the minimum code required to pass the test, and repeating the cycle.

### ⚙️ Progress Summary

#### 1. Genome and Gene Generation (`get_random_gene` and `get_random_genome`)
*   **Initial Debugging:** The session began by fixing an initial assert error where the code was returning a Python list when the test expected a NumPy array, requiring a simple conversion (`np.array`).
*   **Implementing Gene Generation:** The speaker implemented a function (`genome.get_random_gene`) to generate a single gene, first realizing it needed to be wrapped as a static method on the `genome` class.
*   **Refinement:** They improved the calculation of the gene count using a Python list comprehension.
*   **Successful Implementation:** By addressing the requirement for a `gene_length` positional argument, the code was successfully tested, allowing the system to generate random genes.

#### 2. Genome Specification (`GenomeSpec`)
*   **Testing the Spec:** The next step was implementing the genome specification (`genome.get_gene_spec`).
*   **Implementation:** The initial test failed because the method did not exist. The speaker implemented a static method `def get_gene_spec()` that returns a dictionary to satisfy the test.
*   **Scope:** While the test was passed, the speaker noted that they would dive deeper into the complexity of the `gene_spec` in a subsequent video, as the current implementation only involved generating a list of random numbers.

### ✅ Conclusion
The session concludes successfully, having built the fundamental, tested algorithms necessary to **generate a random genome** and define its structure (`gene_spec`), establishing a strong, functional foundation for the subsequent phases of genetic evolution.

---

### 08_Genome_spec_Video_12_min

# Genome spec
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/YnOpa/genome-spec

This course delves into advanced artificial intelligence systems across several specialized domains.

The initial phase (Weeks 1-5) focuses on AI game players, beginning with general AI concepts in Week 1. Weeks 2 and 4 formalize reinforcement learning, specifically detailing the implementation of the Deep Q-Network (DQN) agent, which is a core technical subject. Week 3 covers essential game playing AI tooling, while Week 5 examines the state of the art and the ethical considerations surrounding these AI game players.

Transitioning to evolutionary systems, Weeks 6-10 explore evolving artificial creatures and morphology. Week 6 introduces automatic design using genetic algorithms. Weeks 7 and 8 focus heavily on construction and encoding, specifically building robots utilizing PyBullet and URDF files. Week 8 is highly technical, dedicating major portions to the genetic encoding scheme, encompassing the generation of genomes and the conversion of flat genes into structural graphs. Further development in Week 8 involves implementing XML coding and handling geometrical fixes and motors for the creatures. Weeks 9 and 10 then build upon this foundation, covering the necessary fitness function and selection methods, alongside the state of the art in evolving morphology.

The mid-course segment (Weeks 11-15) shifts focus to Generative and Collaborative AI systems. Week 11 introduces the fundamental concepts of generative systems, which are then explored practically in Week 12 by generating lyrics using GPT-2. Week 13 introduces music composition through MusicVAE, while Week 14 delves into the DiffSinger model. The sequence concludes with Week 15, combining these elements into a pop song generator.

The final major theme (Weeks 16-20) centers on the "Toy Robot Scientist," focusing on complex autonomous reasoning. Week 16 establishes the foundational context, including history, perspectives, and critical legal and ethical issues. Weeks 17 through 19 detail the system building process, covering knowledge representation, the introduction to the robot scientist's reasoning phase, and planning and analysis. Week 20 summarizes the state of the art projects in this field.

The program concludes with Week 21 dedicated to comprehensive exam preparation and Week 22 being the designated exam week. The entire curriculum emphasizes a blend of theory and practical implementation, driven by specific technical milestones such as the DQN agent implementation and the graph-based genetic encoding scheme.

---

### 09_Genome_generating_code_Reading_10_min

# Genome generating code
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/dpIHZ/genome-generating-code

This curriculum covers a comprehensive progression through advanced Artificial Intelligence, moving from game playing to evolutionary design, generative modeling, and robotics.

The initial phase (Weeks 1-5) focuses on Game Playing AI, beginning with basic game player concepts. This transitions into formalizing reinforcement learning, specifically detailing the Deep Q-Network (DQN) agent. Week 3 addresses AI game player tooling, followed by the implementation of the DQN agent in Week 4. The curriculum concludes this segment with an analysis of the state-of-the-art and ethical considerations in AI game players (Week 5).

Weeks 6 through 10 pivot to Evolving Artificial Creatures, starting with automatic design through genetic algorithms. Week 7 involves building robots using technical frameworks like pybullet and URDF files. Week 8 is a detailed module on "Genome generating code," focusing heavily on the genetic encoding scheme.

The technical process in Week 8 begins by addressing the fundamental genetic encoding problem, including decisions on parameter ranges. The core task involves implementing the `genome->graph` code, requiring converting flat genes into a complex graph structure. This process utilizes a defined gene-to-graph algorithm, which is heavily tested through practice assignments.

Subsequently, the system is designed to implement the `genome to XML` code, necessitating the interpretation of the genome specification and defining a `Creature class`. This module finishes by handling the physical aspects, including geometry fixes and the addition of motors. The entire decoding process integrates these steps to produce a functional structure.

Following the evolutionary phase, Weeks 11-15 delve into Generative and collaborative AI systems. The focus includes introducing generative systems, generating lyrics using GPT-2, and applying MusicVAE for music composition. The progression continues with studies on DiffSinger and culminates in a complete pop song generator.

Finally, Weeks 16 through 20 explore a "Toy Robot Scientist," addressing its history, perspectives, and the legal and ethical issues surrounding robotics. This segment focuses on system building, knowledge representation, and the intricate steps of the Robot Scientist reasoning phase. The final weeks (21 and 22) are dedicated to exam preparation and the final examination.

---

### 10_Converting_from_flat_genes_to_a_graph_algorithm_Video_16_min

# Converting from flat genes to a graph: algorithm
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/mw91n/converting-from-flat-genes-to-a-graph-algorithm

This transcript details a critical stage in the process of **designing and generating robotic/creature morphologies** using genetic algorithms. The core focus is on converting a simple, abstract genetic description (the "genome" or "flat gene structure") into a fully articulated, physically defined structure (the "expanded graph" and subsequently, a URDF file).

Here is a detailed breakdown of the concepts and processes discussed:

---

### 🧬 1. The Problem: Genome to Graph Conversion
The starting point is a **flat gene structure** (the genome), which describes the parts of a creature or robot but does not explicitly define the hierarchical connections or repeat structures. The goal is to expand this flat structure into a complete, recursive **expanded graph structure** that accurately models the complexity and repetition found in nature.

### ♻️ 2. The Algorithm: Recursive Expansion (`phase2`)
The process relies on a recursive function (labeled `phase2`) to "dig into" the gene structure and ensure every component is mapped and recorded.

*   **Input:** A parent node (e.g., 'a').
*   **Process:**
    1.  Get the immediate **children** of the parent (e.g., 'b').
    2.  Count the **number of recurrences** for these children.
    3.  For each occurrence, the child is added to the `expanded links` array.
    4.  The function then **recursively calls itself** on the child node (e.g., calling `phase2` on 'b' to find its children, 'c').
*   **Output:** The `expanded links` array accumulates every single node, correctly accounting for repetitions and branches.
*   **Result Example:** A simple structure that might have `a -> b` and `b -> c` might be expanded to include multiple entries like `a, a b, a c, a d, a c, a d`, fully mapping the branching pathways.

### ⚙️ 3. The Final Conversion: Expanded Graph to URDF/XML
Once the `expanded links` array is complete, the next step is translating this abstract, expanded graph description into a physical file format that robotics simulation environments (like PyBullet) can understand.

*   **URDF (Unified Robot Description Format):** This XML-based standard is used to describe the structure, geometry, and kinematic properties of robots.
*   **The Mapping:**
    *   Every item in the `expanded links` array converts into a **`link tag`** (a physical component, like a leg segment or arm bone).
    *   For every link, a **`joint tag`** must be created. This tag dictates the parent-child relationship, defining how that specific link connects to its parent (a relationship already determined in Phase 1).

### ➡️ Summary of the Workflow
1.  **Genome/Flat Gene:** (Initial genetic code input) $\rightarrow$
2.  **Phase 1:** (Determining Parent/Child relationships) $\rightarrow$
3.  **Phase 2 (Recursive Algorithm):** (Expanding the structure into the `expanded links` array) $\rightarrow$
4.  **URDF/XML Generation:** (Converting the expanded links into functional, physical robot definitions).

---
### 📚 Course Context
The transcript aligns perfectly with **Week 8: Evolving artificial creatures: Part 3 - Genetic encoding scheme**, focusing specifically on the lessons related to:
*   `Converting from flat genes to a graph: algorithm`
*   `Implement the genome->graph code`
*   `Implement the genome to XML code`

---

### 11_Activity_expand_some_flat_graphs_Reading_10_min

# Activity: expand some flat graphs
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/75oSQ/activity-expand-some-flat-graphs

This curriculum outlines a comprehensive study spanning several advanced fields of artificial intelligence, from game theory and evolutionary computing to generative systems and robotics.

The initial phase, spanning Weeks 1 through 5, is dedicated to Game playing AI. This section introduces the foundational concepts of AI game players. Week 2 delves into the formalization of reinforcement learning and specifically examines the implementation of the Deep Q-Network (DQN) agent. Week 3 focuses on Game playing AI tooling, while Weeks 4 and 5 address the practical implementation and the critical discussion surrounding the state of the art and ethics in AI game players.

A major focus shifts in Weeks 6 through 10 to Evolving artificial creatures and genetic algorithms. Week 7 specifically covers building robots using technical standards such as pybullet and URDF files. Weeks 6 and 8 concentrate on the Automatic design process using genetic algorithms. Week 8 is heavily detailed, focusing on the "Genetic encoding scheme."

The encoding process includes several technical components, such as generating a genome, defining gene specs, and the critical step of converting from flat genes to a graph. Students engage in the "Activity: expand some flat graphs," and complete the "Gene to graph - implementation" exercise. Further decoding involves implementing the genome to XML code, utilizing a "Creature class," and applying a "Geometry fix and motors" to the generated structure.

The progression continues into Week 9 and Week 10, where the focus shifts to the critical concepts of the Fitness function and selection, concluding the module on evolving morphology.

Weeks 11 through 15 are dedicated to Generative and collaborative AI systems. The study begins with an introduction to generative systems in Week 11. Week 12 explores content creation by generating lyrics using GPT-2. The focus then transitions to music composition with MusicVAE in Week 13, followed by the examination of DiffSinger in Week 14. The final week of this module synthesizes these concepts by developing a pop song generator.

Weeks 16 through 20 introduce "A toy Robot Scientist." This module covers the initial historical perspectives, legal, and ethical issues associated with robotics in Week 16. Subsequent weeks focus on technical implementation, starting with system building and knowledge representation (Week 17). The core of the module involves the Robot Scientist reasoning phase (Week 18), followed by the analysis and planning capabilities (Week 19). The series concludes with a review of the state of the art in Robot Scientist projects.

Finally, the curriculum allocates Week 21 for exam preparation, leading into the designated Exam week in Week 22. Additional resources, including the lab worksheet "32075\_expand\_a\_graph\_20210929.pdf," support the practical application of these complex topics throughout the course.

---

### 12_Gene_to_graph_-_implementation_Video_20_min

# Gene to graph - implementation
Video • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/IpBfj/gene-to-graph-implementation

This comprehensive curriculum covers advanced topics across game playing AI, evolutionary design, and generative artificial intelligence. The initial module (Weeks 1-5) focuses on Game Playing AI, starting with the fundamentals of AI game players. This progression leads to the formalization of reinforcement learning (RL) and the development of the Deep Q-Network (DQN) agent. Specific tooling is introduced for AI game development, followed by practical implementation of the DQN agent. The module concludes by examining the state of the art and essential ethical considerations within the field of AI game players.

Shifting focus, the curriculum addresses Evolving Artificial Creatures, beginning with the concept of automatic design using genetic algorithms (Weeks 6-8). Week 8 is heavily dedicated to mastering the complex process of genetic encoding. This process involves defining parameters, establishing ranges, and translating a flat genome representation into a navigable graph structure. A key technical focus is the implementation of the `genome->graph` code, which involves a test-driven approach.

Furthermore, the implementation includes converting the genome structure into XML format using a custom `Creature` class and `toXML` process. The physical realization of these creatures is achieved through geometry fixes and motor integration. This detailed decoding process culminates in the physical build of robots using simulation frameworks like Pybullet and standard robot descriptions (URDF files).

The latter half of the course dives into sophisticated AI architectures, covering Generative and Collaborative AI (Weeks 11-15). This section explores systems designed for creative output, beginning with a general introduction to generative systems. Practical applications include generating lyrics using GPT-2 and creating music compositions via specialized models like MusicVAE and DiffSinger. The final generative component focuses on synthesizing complex outputs, such as a pop song generator.

The course then pivots to advanced robotic reasoning in the "Toy Robot Scientist" series (Weeks 16-20). This module addresses the history, legal, and ethical issues of robotics before building the core system. Emphasis is placed on knowledge representation, followed by the introduction to the Robot Scientist's reasoning phase. The curriculum details planning, analytical capabilities, and reviewing the state of the art in complex robot scientist projects. The final weeks prepare students for the comprehensive exam, solidifying understanding across all major domains.

---

### 13_Code_the_Graph_expansion_Reading_10_min

# Code the Graph expansion
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/EVeHd/code-the-graph-expansion

This is a procedural instruction set for a lab assignment titled "Code the Graph expansion," providing the required lab worksheet, `32100_code_graph_expansion_20210929.pdf`, and supplementary starter code, `wk3_pre_32100` (ZIP File), for participants to complete the task.

---

### 14_Lesson_introduction_genome_to_XML_Reading_10_min

# Lesson introduction: genome to XML
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/CKwGn/lesson-introduction-genome-to-xml

In this lesson we are going to push on with the implementation of the genetic encoding scheme. At the end we will be able to convert a random genome into URDF XML and load it into pybullet. So we will see our first creatures! Here is a preview of the first creature Lesson introduction: genome to XML In this lesson we are going to push on with the implementation of the genetic encoding scheme. At the end we will be able to convert a random genome into URDF XML and load it into pybullet....

---

### 15_Interpret_the_genome_spec_Video_21_min

# Interpret the genome spec
Video • 21 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/aQugU/interpret-the-genome-spec

Based on the provided transcript and the context of the course material (Week 8: Genetic encoding scheme), here is a detailed summary of the technical progress and the core concepts discussed.

---

## 🧬 Technical Summary: Genome Parsing and URDFLink Construction

The video segment focuses on the critical intermediate step in the project: **transforming low-level, raw genetic data (the "genome") into structured, usable properties for a physical robot model (`URDFLink` objects)**. This process bridges the theoretical genetic algorithm with the practical application of robotics (URDF/XML generation).

### I. Key Achievements Demonstrated

1.  **Structural Link Validation (Topology):**
    *   The initial phase successfully validated the method for establishing the hierarchical relationships between the robot's links.
    *   The speaker confirmed that the code correctly appended the link name to the `parent_names` list, ensuring that each newly generated link is correctly indexed and integrated into the overall structural tree of the robot.
    *   This confirms the successful parsing of the graph structure from the genome.

2.  **Expanding the Data Model (`URDFLink` Class Update):**
    *   The primary goal moving forward is to enrich the `URDFLink` class by incorporating *all* necessary physical and geometric properties defined in the genome dictionary.
    *   The speaker demonstrated the implementation process by adding a new property, such as **`link_length`**, to the `URDFLink` class. This showcases how the code is being adapted to handle various data types from the genome (not just numerical ones).

3.  **Data Mapping Implementation:**
    *   The code structure is being refined to allow for concise assignment of these properties:
        ```python
        # Conceptual example from the video
        link_length = genome_dict["link_length"]
        # ... and passing it into the URDFLink constructor
        ```
    *   This process moves the data away from being just "floating point values" in the genome dictionary and converts it into explicit, usable attributes of the robot component.

### II. Conceptual Significance (The "Why")

The entire effort is geared toward the final output stage of the project:

*   **Goal:** To take abstract genetic instructions (the genome) and translate them into a deterministic, machine-readable representation (the URDF file, which is XML).
*   **Function:** The `URDFLink` object acts as the crucial bridge. It holds the concrete parameters (mass, length, shape, etc.) derived from the genome, which the subsequent XML writer will consume.
*   **Progress Context:** This directly relates to the steps outlined in **Week 8 (Gene to graph - implementation, Code the Graph expansion)**, where the raw gene data is being formalized into the tangible, indexed graph structure required for robot definition.

### III. Roadmap and Next Steps

The speaker outlines the immediate next steps:

1.  **Completion of Property Mapping:** Finish adding all remaining properties (e.g., for shape, mass, joint specifications) from the genome dictionary into the `URDFLink` object.
2.  **XML Generation:** After the structure is fully defined in Python objects, the process will move to the final stage: taking the complete set of `URDFLink` objects and generating the corresponding `.urdf` (XML) file.

---

### 16_Creature_class_Video_21_min

# Creature class
Video • 21 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/mWl3n/creature-class

This course provides an extensive exploration of modern artificial intelligence across four distinct domains: game playing, evolving creatures, generative systems, and robotics.

The study begins with Game Playing AI, focusing on formalizing reinforcement learning (RL) in Week 2. This section introduces the Deep Q-Network (DQN) agent and covers necessary AI tooling in Week 3. Subsequent weeks detail the implementation of the DQN agent, culminating in an analysis of the state of the art and associated ethics in AI game players.

The focus then shifts to Evolving Artificial Creatures, starting with automatic design using genetic algorithms (GA). Week 7 introduces physical system building using industry standards like pybullet and URDF files. Week 8 dives deeply into the technical process of genetic encoding schemes, requiring participants to determine parameter ranges.

The core technical challenge of Week 8 involves implementing the complex genome-to-graph code. This process begins by generating a genome, followed by converting flat genes into a functional graph. Further implementation requires translating the genome into an XML format. Crucially, this includes geometry fixing and the addition of motors to ensure physical feasibility.

Weeks 9 and 10 expand on evolutionary principles, detailing the application of fitness functions and selection mechanisms for evolving morphology.

Next, the curriculum explores Generative and Collaborative AI systems (Weeks 11-15). Introduction to generative systems leads into specific applications, such as generating lyrics using GPT-2. The system also covers complex music composition methods, including MusicVAE and DiffSinger.

The final major theme is the development of a Toy Robot Scientist (Weeks 16-20). This involves understanding the historical and ethical landscape of robotics. The system architecture requires knowledge representation, followed by a rigorous introduction to the robot's reasoning phase. Subsequent weeks cover planning, analysis, and surveying current state-of-the-art projects in the field.

Throughout the course, foundational concepts range from the specific algorithms like "Gene to graph algorithm" to the integration of complex systems like "The full decoding process."

The curriculum concludes with dedicated weeks for exam preparation and examination.

---

### 17_toXML_Video_22_min

# toXML
Video • 22 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/LaYIA/toxml

This content covers the practical implementation phase of creating and simulating artificial, genetically evolved creatures and robots. The overall theme is moving from abstract genetic parameters (the genome) to a functional, physics-simulated robot model.

Here is a detailed summary, broken down by the major concepts presented in the video transcript and the associated syllabus modules.

---

## 🤖 Core Topic: Evolving Artificial Creatures (Weeks 6, 7, 8)

The central goal is to use Genetic Algorithms (GA) to generate novel creature designs, encode those designs, and then simulate them in a physics engine (PyBullet).

### 🧬 Phase 1: Genetic Encoding (The Genome)
*   **Concept:** How to represent a physical object (a robot) using a set of raw, inheritable numbers (the genome).
*   **Process (Week 8):**
    *   **Parameterization:** Defining the structural components (e.g., number of joints, link sizes) and setting their allowable ranges.
    *   **Genome Structure:** The genome starts as a flat list of random numbers.
    *   **Genome $\rightarrow$ Graph Conversion:** This critical step involves turning the flat array of genes into a structured, hierarchical graph, defining how the body parts connect.
    *   **Fitness:** (Introduced in Week 9) The mechanism by which the GA judges how "good" a generated design is (e.g., stability, speed).

### 🏗️ Phase 2: Model Generation (Genome $\rightarrow$ XML/URDF)
*   **Concept:** Translating the abstract graph structure into a format that a computer physics engine can understand.
*   **The Role of URDF:** The **Unified Robot Description Format (URDF)** is the standard XML schema used to describe a robot's physical structure, geometry, and kinematic joints.
*   **The `toXML` Process:**
    1.  The Python `Creature` class takes the graph structure.
    2.  It iterates through the structure, calculating positions and relative dimensions (Geometry Fix).
    3.  It generates the required XML tags, describing each link (part) and joint.
    4.  The result is an XML file (specifically, a URDF file) that defines the robot's morphology.
*   **Implementation Detail (Transcript):** The code uses functions like `p.loadURDF` to load the generated XML file into the PyBullet simulator.

### 🕹️ Phase 3: Simulation and Interaction (PyBullet)
*   **Concept:** Bringing the model to life within a physics simulation environment.
*   **Setup:** The simulation is run in real time, and the robot model is loaded into the physics engine (PyBullet).
*   **Control:** Once loaded, the robot is controllable:
    *   **Joint Control:** Using functions like `p.setJointMotorControl2`, the system can override physics and manually set the desired position of specific joints, demonstrating the robot's kinematic movement.
*   **Iteration:** The entire cycle (Random Genome $\rightarrow$ XML $\rightarrow$ Simulation $\rightarrow$ Fitness Evaluation) is repeated to evolve better designs.

---

## 🗺️ Course Progression Overview (Syllabus)

The material follows a clear path from theoretical AI to applied robotics:

| Weeks | Focus Area | Key Concepts | Outcome |
| :--- | :--- | :--- | :--- |
| **6–8** | **Evolutionary Morphology** | Genetic Algorithms, Genome Encoding, URDF/XML, PyBullet. | Automatic design of novel, functional robots. |
| **9–10** | **Selection & Fitness** | Fitness functions, Selection strategies. | Determining which designs are "good" for the evolutionary loop. |
| **11–15** | **Generative AI** | GPT-2, MusicVAE, DiffSinger. | Exploring generative systems outside of morphology (e.g., text, music). |
| **16–20** | **The Robot Scientist** | Knowledge representation, Planning, Reasoning, Ethics. | Developing a high-level AI system capable of abstract problem-solving and planning. |

### 🚀 Transcript Summary Focus (Video Content)

The video serves as a practical demonstration of **Week 8: Implementing the Genome $\rightarrow$ XML Code**.

*   **Action:** Loading a randomly generated robot (`p.loadURDF 102.urdf`).
*   **Demonstration:** Showing the robot's structural complexity and demonstrating motor control by forcing specific joints to move to a predefined position using `p.POSITION_CONTROL`.
*   **Conclusion:** The current work successfully automates the entire pipeline from raw genetic numbers to a runnable, simulated robot, setting the stage for future improvements (like refining geometry and getting motors to react dynamically).

---

### 18_Generating_XML_from_a_genome_Reading_10_min

# Generating XML from a genome
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/Qjvhl/generating-xml-from-a-genome

This lab focuses on the concept of "Generating XML from a genome," providing students with the required worksheet, 32170\_to\_xml\_20210929.pdf, and preparatory starter code, wk3\_pre\_3217 ZIP File, for completing the exercise.

---

### 19_Lesson_introduction_geometry_fix_and_motors_Reading_10_min

# Lesson introduction: geometry fix and motors
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/IruMV/lesson-introduction-geometry-fix-and-motors

The core objective of this lesson is to advance the coding process by implementing movement within the creatures. A secondary, but crucial, task is applying a necessary fix to the existing creature geometry. The main technical goal is completing the full genetic encoding pipeline. This completed pipeline allows the system to generate a creature randomly. Ultimately, this entire system enables the creature to be run in a real-time simulation with functional movement.

---

### 20_Fixing_positions_of_children_Video_8_min

# Fixing positions of children
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/xGtZ6/fixing-positions-of-children

The course begins by focusing on Game Playing AI, spanning Weeks 1 through 5. Initial concepts involve formalizing reinforcement learning (RL) and developing the Deep Q-Network (DQN) agent. Further study delves into Game Playing AI tooling and culminates in the implementation of the DQN agent. The curriculum also addresses the state of the art in AI game players and associated ethical considerations.

The subsequent section introduces Evolving Artificial Creatures, beginning in Week 6. This module utilizes genetic algorithms for automatic design and evolution. Week 7 details the construction of robots using tools like pybullet and URDF files.

Week 8 is dedicated to mastering the genetic encoding scheme, which forms the core of the evolutionary process. This involves defining parameterization, ranging, and implementing the critical genome-to-graph code. Specific technical processes include using a test-driven approach, generating a genome, and defining the gene specification. A major technical detail is converting flat genes into a graph structure via a defined algorithm.

The process continues with implementing the genome-to-XML code, detailing how to interpret the genome specification and construct the `Creature` class. The final stages of Week 8 cover geometry fixes and the addition of motors, detailing the full decoding process. Weeks 9 and 10 complete the evolutionary phase, focusing on the fitness function, selection methods, and the state of the art in evolving morphology.

The course then pivots to Generative and Collaborative AI in Weeks 11 through 15. Week 12 illustrates generative capabilities by generating lyrics using GPT-2. Music generation is covered in Week 13 using MusicVAE, followed by the advanced topic DiffSinger in Week 14. This section concludes by integrating these concepts into a pop song generator.

The final major technical module is "A Toy Robot Scientist," spanning Weeks 16 through 20. Week 17 focuses on system building and essential knowledge representation. The subsequent weeks detail the robot's reasoning phase, its planning capabilities, and how it analyzes information. The curriculum finishes with an examination of state-of-the-art Robot Scientist projects. Weeks 21 and 22 are allocated for exam preparation and the final examination.

---

### 21_Adding_motors_Video_16_min

# Adding motors
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Dga6h/adding-motors

Based on the transcript, this segment details the successful implementation and initial testing of the motor system within the creature structure.

Here is a summary of the progress made, the technical challenges overcome, and the next steps:

---

### ⚙️ Progress Summary: Implementing Creature Motors

The core objective of this section was to define, incorporate, and test the motors within the creature/graph representation.

#### 1. Motor Implementation
*   **Definition:** A motor (`M`) was defined as an instance linked to a specific link (`l = self.x_link`).
*   **Properties:** Key control properties were accessed from the link object, specifically `l.control_amp` and `l.control_frequency`.
*   **Architecture:** The new motor was successfully appended to the collection of all motors (`self.motors`).
*   **Refinement:** The code was refined to include assertions and conditional logic (`if self.motors is None`) to ensure efficient regeneration and prevent unnecessary recalculations.

#### 2. Testing and Verification
*   **Testing Script:** A test function (`testCMotor`) was created to verify the functionality of the newly added motors.
*   **Verification Logic:** The test checks that the number of motors is exactly one less than the number of expanded links (`len(ls) - 1 == len(ms)`), correctly accounting for the root link.
*   **Debugging:** An initial `AttributeError` (caused by a misplaced dot operator) was encountered and subsequently fixed.
*   **Result:** The test successfully passed, confirming that the motors are correctly generated and produce "sensible output."

#### ⏭️ Next Steps
The implementation phase is complete, and the system is verified. The next steps outlined are:

1.  **Writing a Test Script:** Create a comprehensive test script that generates a random creature, displays it on the screen, and actively moves its motors.
2.  **Algorithmic Implementation:** Use this functional base to implement the actual evolutionary algorithm that will drive the creature's development.

***

### 🔑 Key Takeaway
The creature structure is now robust, with a fully functional, tested, and verifiable motor system, ready to be integrated into a dynamic simulation and genetic algorithm.

---

### 22_Motor_test_script_Video_9_min

# Motor test script
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/ubtZ9/motor-test-script

This curriculum outlines a comprehensive study spanning AI, Reinforcement Learning (RL), Evolutionary Algorithms, and Generative Systems. The initial module, Weeks 1-5, focuses on Game Playing AI. Week 2 formalizes reinforcement learning and introduces the Deep Q-Network (DQN) agent. Week 4 involves the practical implementation of the DQN agent, which is essential for AI game players. Week 5 examines the state of the art and the critical ethical considerations within AI game players.

The course then transitions to evolving artificial creatures (Weeks 6-8), centering on automatic design using genetic algorithms (GAs). Week 7 specifically addresses building robots utilizing tools like PyBullet and URDF files. Week 8 delves deeply into the genetic encoding scheme and its implementation.

This highly detailed segment covers the necessary steps to transform genetic data into functional hardware definitions. The process involves implementing the `genome->graph` code, converting flat genes into a graph structure. Key technical deliverables include defining genome and gene specifications and implementing algorithms for gene-to-graph conversion. Further development involves implementing `genome to XML code` and establishing the `Creature class` to structure the resulting machine definition. The final stages of Week 8 address critical mechanical aspects, including geometry fixes and the addition of motors, culminating in a full decoding process.

Following creature design, Weeks 9 and 10 cover the essential next steps for evolutionary systems: defining the fitness function and selection mechanisms, and exploring the state of the art in evolving morphology.

The curriculum then shifts focus to Generative and Collaborative AI (Weeks 11-15). Week 12 focuses on generating lyrics using GPT-2, while Week 13 explores music composition through MusicVAE. Week 14 introduces DiffSinger, and Week 15 culminates by integrating these elements into a pop song generator.

The subsequent block examines robotic intelligence under "A toy Robot Scientist" (Weeks 16-20). Week 17 details system building and knowledge representation, followed by the introduction to the Robot Scientist reasoning phase in Week 18. Weeks 19 and 20 focus specifically on planning, analysis, and surveying the state of the art in Robot Scientist projects. The course concludes with exam preparation (Week 21) and examination (Week 22).

---

### 23_The_full_decoding_process_Reading_10_min

# The full decoding process
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/M3HVV/the-full-decoding-process

The available resources related to the full decoding process include the lab worksheet file `32220_full_decoding_process_20210929.pdf` and associated starter code provided in the `wk3_pre_32220 ZIP File` for completing the previous lab.

---

### 24_End_of_week_code_Reading_10_min

# End of week code
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/PMDP1/end-of-week-code

The curriculum progresses through several advanced domains of artificial intelligence, starting with AI game playing. Weeks 1 through 5 cover Game playing AI, moving from basic AI player concepts to formalizing reinforcement learning. A significant technical focus in this phase is the Deep Q-Network (DQN) agent, which is formally studied and subsequently implemented across Week 4. Week 5 transitions the discussion to the contemporary state of the art and ethical considerations surrounding AI game players.

The study then shifts dramatically in Weeks 6 through 8 to evolving artificial creatures, centering on automatic design using genetic algorithms. Week 7 specifically addresses building robots utilizing external tools like pybullet and URDF files. Week 8 dives deeply into genetic encoding schemes, which is the foundational mechanism for evolutionary design.

The technical implementation in Week 8 is highly detailed, covering the conversion process from flat genes to a functional graph structure. Key modules include generating a genome, specifying the genome and gene structure, and implementing the algorithm that converts the flat genes into a graph. Furthermore, the system development includes translating the genome into XML code, which is essential for interpreting the creature's specifications. This process requires defining a `Creature class` and implementing functions like `toXML` to complete the full decoding process. Additional technical topics cover geometry fixes and the addition of motors to the evolving structures.

Following this, Weeks 9 and 10 focus on the mechanics of evolution, specifically introducing the fitness function and selection methods in the context of evolving morphology. The curriculum moves into generative and collaborative AI during Weeks 11 through 15.

Generative AI is introduced in Week 11, followed by applications in Week 12 using GPT-2 for generating lyrics. The focus then broadens to different generative models, including MusicVAE in Week 13 for music composition and DiffSinger in Week 14. Week 15 synthesizes these concepts by creating a comprehensive pop song generator.

The final major section is dedicated to the "Toy Robot Scientist" across Weeks 16 through 20. This segment covers the history, ethical issues, and knowledge representation necessary for building the system. The learning culminates with detailed coverage of the Robot Scientist's reasoning phase and subsequent planning and analysis capabilities. Week 21 is dedicated to exam preparation, and Week 22 marks the examination week. Throughout the course, weekly code releases are provided, such as the `wk3_end ZIP File` and the final code, ensuring practical implementation alongside theoretical learning.

---

### 25_Recap_of_week_8_study_Video_1_min

# Recap of week 8 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/cGGiL/recap-of-week-8-study

The course has heavily focused on utilizing genetic encoding schemes to express complex problem solutions. Specifically, the focus has been on building a genetic encoding scheme capable of capturing the characteristics of a robot. This system is designed around a free-dimensional graph structure, drawing inspiration from projects such as that of Karl Sims. Furthermore, the instructional material included the implementation of evolvable motor controls within this framework. This foundational knowledge is crucial, as it will provide students with the insight needed to analyze and compare state-of-the-art systems later in the curriculum.

The progression through Week 3 of the "Creatures case study" culminates the development of this genetic encoding scheme. In the subsequent week, the focus shifts from theoretical design to practical application. The curriculum plans to implement the simulation for real and complete the full genetic algorithm implementation. This will allow the students to observe the evolution of their artificial creatures.

The detailed study of genetic encoding, particularly in Week 8, involves numerous technical stages. The process begins with understanding the genetic encoding problem overview and deciding on critical parameter ranges. A central technical challenge addressed is converting flat genes into a functional graph structure.

Implementation steps include generating a genome and defining a robust gene specification. A key algorithmic component involves the conversion from flat genes to a graph, which is detailed through specific video lessons. Following graph generation, the system must be able to interpret the genome spec and map it into a Creature class.

Another major technical development is the transition from the internal genome structure to external formats, specifically using a `toXML` mechanism. The complexity of the robot body requires geometrical fixes, such as fixing the positions of children within the structure. Finally, the system is augmented by adding complex motor controls.

Beyond creature evolution, the course outlines several future advanced topics. Early modules cover Game Playing AI, including formalizing reinforcement learning and implementing a Deep Q-Network (DQN) agent. Subsequent sections explore advanced evolution concepts, such as building robots using PyBullet and URDF files.

The course later shifts focus to Generative and Collaborative AI systems. This includes topics like generating lyrics using GPT-2 and composing music with MusicVAE and DiffSinger. The final modules transition into the domain of A Toy Robot Scientist. These topics cover system building, knowledge representation, reasoning phases, and planning. The curriculum moves from theoretical encoding to fully functional, complex AI systems across diverse fields.

---

### 26_Self-evaluation_checklist_Genetic_encoding_scheme_Reading_30_min

# Self-evaluation checklist: Genetic encoding scheme
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/U0byh/self-evaluation-checklist-genetic-encoding-scheme

This text serves as a comprehensive self-assessment checklist outlining the learning outcomes for a module focused on Genetic Encoding Schemes (GES). The core objective is to ensure a thorough understanding of how encoding transforms complex problems into numerical representations suitable for evolutionary algorithms. The assessment is divided into three distinct areas: comparison of methods, implementation of schemes, and theoretical explanation of solution representation.

First, the learner must demonstrate the ability to compare and contrast various genetic encoding methods. Specifically, this requires describing at least two distinct approaches, such as direct encoding and indirect encoding. Furthermore, the evaluation demands understanding the inherent advantages and disadvantages of different encoding schemes. This understanding must be specifically applied to representing complex structures, such as robots and their intricate control systems. The assessment also requires explaining how these varying encoding methods significantly impact the overall evolvability and adaptability of the resulting solutions. Practical examples are necessary to demonstrate where each specific encoding method would be most suitable in real-world applications.

Second, the module requires the successful implementation of a genetic encoding scheme in functional code. This implementation must allow for the representation of a complex system, specifically a robot and its corresponding control system, using a simple list of numbers. A crucial component is incorporating a developmental process, which acts as a translator, converting the abstract genetic encoding into a functional, operational representation. The testing phase necessitates verification that these encoded individuals can be properly decoded and successfully executed. Finally, the implementation must include rigorous debugging and optimization to ensure the code is both highly efficient and clearly structured.

Third, the conceptual understanding of how potential solutions are represented via a genetic encoding scheme is paramount. The learner must articulate how the GES fundamentally transforms a problem’s expansive solution space into a discrete numerical representation. It is necessary to explain precisely how the chosen encoding scheme enables standard evolutionary algorithm operations, specifically mutation and crossover. The summary must describe the correlation between the resulting encoded list of numbers and the meaningful physical and functional characteristics of the robot and its control system. Discussing the implications of the chosen encoding scheme on the overall search space geometry and the potential final solution quality is also a requirement.

The final section involves a critical self-reflection on the entire process. This reflection challenges the learner to identify specific technical challenges encountered during the implementation of the encoding scheme. Furthermore, they must articulate the strategies used to successfully overcome these encountered difficulties. The assessment concludes by prompting the learner to suggest potential improvements or modifications to the encoding scheme for future implementations. This checklist serves as a vital guide to ensure all technical and conceptual learning outcomes have been successfully achieved.

---

## Week 9

### 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

### 02_Slides_for_week_9_Reading_30_min

# Slides for week 9
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/XNKII/slides-for-week-9

This curriculum outlines a comprehensive study of advanced Artificial Intelligence, progressing from game-playing agents to complex generative and robotic systems.

The foundational module covered initial topics like Game Playing AI, detailing the formalization of Reinforcement Learning and the deployment of the Deep Q-Network (DQN) agent. This early phase also introduced AI game player tooling and focused on the implementation of the DQN agent itself. Subsequently, the course transitioned to evolving artificial creatures, initiating discussions on automatic design through genetic algorithms (GA). Technical foundations were laid by building robots using environments like PyBullet and defining their structure via URDF files. The scheme for genetic encoding, which dictates how traits are represented, was covered in preparation for the core optimization phase.

Week 9 specifically focuses on the crucial concepts of the fitness function and selection within the GA framework. The process begins with generating a random initial population of artificial creatures. These creatures are then subjected to simulation, a critical step that requires implementing the fitness function to evaluate their performance. To maintain computational efficiency, the simulation and fitness function evaluation utilize a multi-process architecture. The next major stage is population management and the planning of selection and breeding cycles.

Specific selection algorithms detailed include Roulette Wheel selection, which guides the preferential selection of high-performing individuals. Reproduction is achieved through crossover, a genetic mechanism that combines traits from successful parents to generate offspring. The overall process is cyclical, allowing for the tweaking of GA parameters to optimize evolutionary outcomes. The ultimate goal of this phase is the successful implementation of the GA, culminating in the ability to save and view the fittest individuals in CSV format.

Following this deep dive into evolution, the course expands its focus to different AI modalities. Week 10 addresses the advanced topic of state of the art in evolving morphology. The curriculum then moves into Generative and Collaborative AI, beginning with an introduction to generative systems. Technical examples include generating lyrics using GPT-2 and composing music utilizing models like MusicVAE and DiffSinger. These generative techniques are integrated by the end of the module into a functional pop song generator.

The final major component is dedicated to "A Toy Robot Scientist." This segment is highly technical, focusing on the initial introduction, history, and the legal and ethical implications surrounding such systems. The robot scientist system is built incrementally, starting with knowledge representation and advancing to the system's reasoning phase. Subsequent weeks detail the robot scientist’s planning and analytical capabilities, concluding with an analysis of state-of-the-art robot scientist projects. The final weeks are reserved for comprehensive exam preparation and review.

---

### 03_Lesson_introduction_fitness_and_simulation_Reading_10_min

# Lesson introduction: fitness and simulation
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/sK3WN/lesson-introduction-fitness-and-simulation

In this lesson we are going to work on the offline simulation and fitness function. These will allow us to run creatures at high speed offline and to evaluate their performance. Lesson introduction: fitness and simulation In this lesson we are going to work on the offline simulation and fitness function. These will allow us to run creatures at high speed offline and to evaluate their performance. Mark as completed Dislike Report an issue

---

### 04_Evaluating_creatures_the_plan_Video_4_min

# Evaluating creatures: the plan
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/wgUk8/evaluating-creatures-the-plan

This text outlines the implementation plan for the next stage of a genetic algorithm (GA) designed for evolving artificial creatures. The process involves three main technical phases: population generation, simulation, and fitness evaluation. The GA itself involves a fundamental cycle: starting with a varied, random population, moving through a selection phase, and finally generating new variations from individuals that scored highly.

To initiate the process, a random population must be generated in a straightforward manner. This involves creating multiple random genomes and encapsulating them within a designated `Creature` class. This simple structure forms the initial pool for the GA.

The next critical phase is running these individuals within a simulation environment. This requires the creation of a dedicated `Simulation` class, separate from the initial `Population` class. This class will manage the dynamic interaction between the creatures and the environment.

A key technical decision is the use of `pybullet` in **direct mode**, as opposed to the standard GUI mode. Running the simulation in direct mode is essential because it operates offline and does not attempt real-time rendering. This significantly increases speed.

This high speed is necessary because the GA requires quickly evaluating numerous individuals to complete the evolutionary cycle in a reasonable amount of time. The simulation process involves instantiating an individual within the environment and then stepping through time. During this step-through, motors must be continuously updated to ensure the creature moves correctly as programmed.

At the conclusion of the simulation, the system must accurately assess the creature's performance. This requires modifying the `Creature` class to include internal variables that monitor its actions. Specifically, the system must track the creature's starting position and its final end position.

The resultant distance traveled between the start and end positions serves as the core fitness function. The concept dictates that the further an individual moves during the simulation, the higher its fitness score, making it more likely to propagate genetic material.

In summary, the implementation plan focuses on using an offline simulation to evaluate a random population. The goal is to monitor movement accurately and use that movement data—derived from the start and end positions—to define fitness. This structured approach sets the stage for subsequent evolutionary steps, including the planning of selection and breeding processes. Future work will focus on implementing methods like roulette wheel selection and crossover to drive the evolution.

---

### 05_Generating_a_random_population_Video_6_min

# Generating a random population
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/4eAKV/generating-a-random-population

This module provides a comprehensive exploration of advanced Artificial Intelligence, structured through four major thematic pillars.

The curriculum begins with the field of Game Playing AI (Weeks 1-5), focusing initially on foundational concepts. Week 2 formalizes reinforcement learning by introducing the Deep Q-Network (DQN) agent, while Week 4 details the specific implementation of this DQN agent. The module also covers AI tooling in Week 3 and concludes this initial phase by addressing the state-of-the-art and ethical considerations in AI game players (Week 5).

Next, the focus shifts to Evolving Artificial Creatures, centered on autonomous design via Genetic Algorithms (GA) (Weeks 6-9). This evolution project begins by detailing automatic design techniques and setting up physical simulation environments using pybullet and defining robot structures via URDF files. A crucial aspect is the implementation of the genetic encoding scheme, followed by developing a robust fitness function. The GA process involves critical management techniques, including generating a random population, utilizing roulette wheel selection, and performing crossover operations. These components enable population management and convergence toward more fit individuals.

The third pillar explores Generative and Collaborative AI (Weeks 10-15), moving from morphology to creativity. Week 10 covers the state of the art in evolving morphology. Subsequently, the module delves into generative systems, learning how to generate content like lyrics using GPT-2. Technical deep dives include exploring MusicVAE for music composition and utilizing DiffSinger. The phase culminates in integrating these systems to create a complete pop song generator.

Finally, the module shifts to practical, reasoning systems with the "A toy Robot Scientist" project (Weeks 16-20). This section addresses the history, legal, and ethical perspectives of robotic systems. Key topics include knowledge representation, building the system, and implementing the robot's reasoning phase. The latter stages involve tackling planning and analyzing complex scenarios, culminating in an assessment of state-of-the-art Robot Scientist projects. Weeks 21 and 22 are dedicated to comprehensive exam preparation and the final assessment.

---

### 06_Running_creatures_in_simulation_Video_22_min

# Running creatures in simulation
Video • 22 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/4bjS8/running-creatures-in-simulation

This segment of the video focuses on **completing the simulation loop** by implementing the logic necessary to track and verify that the artificial creature actually moves within the physics engine.

Here is a breakdown of the key steps and concepts covered:

### 1. Implementing Position Tracking in the Creature

The core task was adding an `update_position` function to the `creature` object. This function handles the logic for tracking the creature's starting point versus its current location:

*   **Logic:** The function accepts the creature itself and a new `position`.
*   **State Management:** It initializes two variables: `start_position` and `last_position`.
*   **First Call:** If `start_position` is `None` (meaning it's the first call), the incoming `position` is stored as the **initial position**.
*   **Subsequent Calls:** For every call after the first, the incoming `position` is stored as the **last position**, allowing the program to calculate movement over time.

### 2. Integrating Position Updates into the Simulation

To make the tracking functional, the simulation loop had to be modified:

*   **Position Retrieval:** Every step of the simulation, the program calls the `p.get_a_position_and_orientation()` function from the `pybullet` API. This function is used to get the creature's real-time position from the physics engine, using the creature's ID and the specified physics engine.
*   **Updating the Creature:** This retrieved position is then passed into the `creature.update_position()` method.

### 3. Verification and Testing

The final step was verifying that the simulation was successful—meaning the creature actually moved, confirming the physics engine was functioning correctly.

*   **The Test:** A unit test was written that runs the simulation for a set duration (e.g., 10 seconds).
*   **The Assertion:** The crucial assertion was: `self.assertNotEqual(creature.start_position, creature.last_position)`.
*   **Result:** Because the creature was expected to move randomly (as demonstrated by the simulated "flying"), this assertion passed, proving that the creature's final position was different from its starting position.

### Summary

In essence, this segment moved from *controlling* the creature (setting motor commands) to **measuring** the creature. By implementing `update_position` and using the `pybullet` API to pull real-time coordinates, the program gained the ability to reliably verify that the physics simulation was causing the intended physical movement.

---

### 07_Implement_the_fitness_function_Video_15_min

# Implement the fitness function
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/d09lD/implement-the-fitness-function

The curriculum is structured into several thematic modules, beginning with Game Playing AI. Weeks 1 through 5 focus on the core concepts of AI game players, formalizing reinforcement learning and detailing the Deep Q-Network (DQN) agent. This includes the implementation and practical application of the DQN agent, culminating in an examination of the state of the art and ethical considerations in AI game players.

The next major module, covering Weeks 6 through 9, shifts focus to the evolution of artificial creatures. This section explores automatic design using genetic algorithms (GA) and the practical construction of robots, utilizing tools like pybullet and URDF files. Week 9 provides a deep technical dive into the mechanics of the GA.

The core of the GA study revolves around the fitness function and simulation, where initial processes involve generating a random population and running these creatures in simulation. Essential technical steps involve implementing the fitness function, which is subsequently evaluated using multi-process evaluation techniques.

Subsequently, the module addresses population management and convergence through selection and breeding strategies. Key operational processes include implementing Roulette wheel selection and Crossover mechanisms. The learning progression then involves tweaking the GA parameters and saving the fittest individuals.

Weeks 10 through 15 transition into the domain of Generative and Collaborative AI. The course begins with an introduction to generative systems, progressing to practical examples such as generating lyrics using GPT-2. The focus then expands to advanced generative models, including MusicVAE for music composition and DiffSinger. This segment culminates in a project applying all concepts to create a pop song generator.

The final substantive module, spanning Weeks 16 through 20, is dedicated to the concept of a Toy Robot Scientist. This unit covers the historical perspectives, legal, and ethical issues surrounding robotic systems. The implementation phase involves building the system, focusing heavily on knowledge representation and the Robot Scientist's reasoning phase.

The latter part of the Robot Scientist module concentrates on planning, analysis, and reviewing the state of the art in robotic projects. Weeks 21 and 22 are dedicated to final exam preparation and the exam week. Throughout the course, concepts such as DQN, URDF, Genetic Algorithms, and large generative models (GPT-2, DiffSinger) serve as the foundational technical pillars.

---

### 08_Multi-process_evaluation_Video_18_min

# Multi-process evaluation
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/w4AGd/multi-process-evaluation

This video serves as a practical guide on optimizing a Genetic Algorithm (GA) by implementing **multi-process parallel evaluation**, which drastically accelerates the fitness testing phase of the evolutionary process.

Here is a detailed summary of the content, methods, and results:

---

### 🔬 Summary of Content

The main objective of the lesson is to transform the simulation—which involves running and evaluating multiple creatures—from a sequential, single-threaded process into a parallel, multiprocessor capable system. This allows the Genetic Algorithm to evaluate a much larger number of creatures in a much shorter amount of time.

#### ⚙️ The Implementation Method (Multi-Process Evaluation)

1.  **Data Structure Preparation:** An empty list, `new_creatures`, is initialized to hold the creatures that are evaluated in the current generation.
2.  **Parallel Processing:** The code iterates over the population's argument sets. For each set, a Python `Pool` object is created. The `Pool` is the mechanism that allows the code to manage multiple parallel processes.
3.  **Task Distribution (`starmap`):** The critical step is using the `pool.starmap()` function. This function automatically takes the arguments for each creature and distributes them to the defined fitness evaluation function, `static_run_creatures`, allowing all creatures to be evaluated simultaneously across available CPU cores.
4.  **Data Aggregation:** The `static_run_creatures` function returns the evaluated creatures. These results are collected and appended to the `new_creatures` list.
5.  **Population Update:** Once all parallel evaluations are complete, the original population is replaced with the newly evaluated, fittest set of creatures.

#### 🚀 Testing and Performance Analysis

A dedicated test script (`testProc`) is created to benchmark the speed difference between the old sequential method and the new parallel method.

*   **Non-Threaded Run (Sequential):** The initial test runs the simulation sequentially.
*   **Threaded Run (Parallel):** The simulation is run using the `Pool` with an initial size (e.g., 4).

**Key Findings:**

*   **Massive Speedup:** The threaded (multi-process) version of the simulation was shown to be **significantly faster** than the non-threaded version.
*   **Scalability:** By increasing the pool size (e.g., from 4 to 8), the speedup continued to increase dramatically.
*   **Viability for Large Searches:** The conclusion emphasizes that this acceleration makes it "viable to run thousands of these overnight." This capability allows researchers to conduct much deeper and more extensive searches of the fitness space.

#### 💡 Conclusion

The lesson successfully demonstrates how to use Python's built-in multi-processing features to accelerate computationally intensive tasks like genetic algorithm simulations. By enabling parallel evaluation, the speed of the genetic algorithm is multiplied several times over, transforming a slow, academic simulation into a powerful tool for large-scale evolutionary design.

---

### 09_Code_the_simulation_and_fitness_function_Reading_10_min

# Code the simulation and fitness function
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/y0lCE/code-the-simulation-and-fitness-function

This lab assignment requires coding the simulation and fitness function, utilizing the provided technical resources: the lab worksheet `41110_simulation_v2.pdf` and the starting code contained within the `wk4_start` ZIP File.

---

### 10_Code_from_end_of_lesson_Reading_10_min

# Code from end of lesson
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/nacBL/code-from-end-of-lesson

Please find below the code after the previous worksheet. Note that it includes a no-threads version of the test_simulation code which works on Windows, M1 macs etc. wk4_after_41110_v3 ZIP File Code from end of lesson Please find below the code after the previous worksheet. Note that it includes a no-threads version of the test_simulation code which works on Windows, M1 macs etc. wk4_after_41110_v3 ZIP File Mark as completed Dislike Report an issue

---

### 11_Planning_selection_and_breeding_Video_6_min

# Planning selection and breeding
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/SOpjC/planning-selection-and-breeding

This course covers diverse aspects of artificial intelligence, starting with game playing AI. Weeks 1 through 5 focus on the development and analysis of AI game players. Key topics include formalizing reinforcement learning and implementing the Deep Q-Network (DQN) agent. Dedicated sessions explore game playing AI tooling and conclude with an examination of the state of the art and associated ethical concerns.

The curriculum shifts significantly to evolving artificial creatures in Week 6. This phase begins by focusing on automatic design utilizing genetic algorithms (GA). Week 7 details the construction of robots, leveraging simulation tools such as pybullet and incorporating Universal Robot Description Format (URDF) files. A core focus in Week 8 is defining the genetic encoding scheme for these creatures.

Week 9 dives deep into the practical implementation and management of GA. Crucial concepts covered include defining the fitness function and designing comprehensive simulation plans. Specific practical exercises involve generating a random population and successfully running creatures in simulation environments.

The module extensively details the implementation of the fitness function, including multi-process evaluation for efficient assessment. Population management and convergence are addressed through detailed planning of selection and breeding. Technical mechanisms taught include Roulette Wheel Selection and the process of Crossover. The final segment involves visualizing results, specifically through saving and viewing fittest individuals via CSVs.

The focus moves to advanced AI in Weeks 10 through 15, covering state-of-the-art in evolving morphology. This section introduces generative systems, beginning with generating lyrics using GPT-2. Music composition is explored using MusicVAE, and specialized deep learning models like DiffSinger are studied. These topics culminate in creating a complex pop song generator.

The latter third of the course is dedicated to robotics and intelligent systems. Weeks 16 through 20 detail the "Toy Robot Scientist." This module covers the system's history, legal, and ethical issues, moving into knowledge representation. Subsequent weeks examine the crucial Robot Scientist reasoning phase, followed by dedicated sessions on planning and analysis. The final weeks are reserved for Exam preparation and the formal Examination period.

---

### 12_Roulette_wheel_selection_Video_10_min

# Roulette wheel selection
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/YFTGX/roulette-wheel-selection

The discussion centers on implementing the Roulette Wheel selection process, a core mechanism for parent selection within a Genetic Algorithm (GA). The overall goal is twofold: generating a fitness map from evaluated individuals and subsequently using this map to select parents.

The concept of a fitness map involves calculating a cumulative sum based on the fitness values of the individuals. For example, given creatures with fitnesses 2.5, 1.2, and 3.4, the fitness map is generated by iteratively accumulating these values. The

---

### 13_Crossover_Video_18_min

# Crossover
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/iDNzA/crossover

The curriculum is structured into several major modules, beginning with Week 1 focusing on basic AI game playing techniques. Weeks 2 through 5 dive deeply into reinforcement learning, formalizing the process and implementing the Deep Q-Network (DQN) agent for advanced game players. The progression from foundational concepts to the DQN agent's implementation, followed by an examination of state-of-the-art practices and AI ethics, concludes this initial module.

The focus then shifts drastically in Week 6, initiating the exploration of evolving artificial creatures using automatic design principles. Weeks 7 through 9 detail the construction and optimization of these creatures, utilizing pybullet and URDF files for robotic system building. The genetic encoding scheme defines how creature parameters are managed, leading into the critical task of defining the fitness function and selection strategies.

The intensive material covering fitness and simulation involves generating random populations and running creatures within the simulation environment. Key processes taught include implementing the fitness function, utilizing multi-process evaluation, and coding the integrated simulation logic. Population management then focuses on genetic algorithms, specifically planning selection and breeding methods.

Technical methods for genetic evolution include implementing Roulette Wheel selection and executing Crossover operations to drive optimization. The course culminates this module by detailing the process of tuning the Genetic Algorithm (GA), saving the fittest individuals, and analyzing their characteristics.

The curriculum moves into generative and collaborative AI from Week 10 onward. Week 11 introduces generative systems, leading to specific applications in generating lyrics using GPT-2. Musical creativity is explored in Week 13 with MusicVAE, and advanced synthesis techniques are covered via DiffSinger in Week 14. The module concludes with integrating these technologies into a complete pop song generator.

The final major theme, "A Toy Robot Scientist," commences in Week 16, addressing the historical, legal, and ethical perspectives of robotic systems. Weeks 17 through 19 detail the practical build-up, focusing on knowledge representation, the reasoning phase of the system, and sophisticated planning and analysis. The final weeks showcase a state-of-the-art review of Robot Scientist projects. Weeks 21 and 22 are dedicated to final exam preparation and examination week, completing the comprehensive program.

---

### 14_Evolution!_Video_15_min

# Evolution!
Video • 15 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/N3qAI/evolution

This transcript details the successful implementation and first execution of an **Iterated Genetic Algorithm (GA)** designed to evolve artificial creatures. The speaker focuses heavily on solving a technical hurdle in Python while building the core evolutionary loop.

Here is a summary of the process and key concepts:

### ⚙️ Addressing Technical Challenges (The `set_dna` Solution)

The speaker initially faces the problem of not being able to "overload" a constructor in Python. To avoid implementing poor practices like module control coupling (using flags in constructors), they adopt a cleaner design:

1.  **Basic Constructor:** The `creature` is initialized using a basic constructor which generates random DNA initially.
2.  **`set_dna` Function:** A separate method, `set_dna(self, dna)`, is implemented. When this function is called, it overwrites the creature's DNA (`self.dna = dna`) and, crucially, forces the creature to perform all the necessary internal setup that the constructor normally handles (regeneration of links, joints, motors, and resetting position).
3.  **Process:** The mutant or crossed-over DNA is passed to this function, effectively updating the creature mid-lifecycle.

### 🔁 Implementing the Iterated Genetic Algorithm

The creation of a single creature is formalized into a complete evolutionary cycle:

1.  **Initialization:** A new creature is created, and its DNA is updated using `set_dna()` with the current best mutant/crossed-over DNA.
2.  **Population Update:** The new creature is added to the `new_gen` list.
3.  **The Iteration Loop:** This entire process is placed inside a `for generation in range(10):` loop, ensuring the GA runs for 10 cycles.
4.  **Population Replacement:** After each generation, the old population is completely replaced by the `new_gen` list (`pop.creatures = new_gen`), defining the "iterated" nature of the algorithm.
5.  **Evaluation and Stats:** The code is configured to import `numpy` and track key metrics after each evaluation, including the generation number, the highest achieved fitness, and the mean fitness.

### ✅ Conclusion and Current Status

The GA is now fully implemented and running. The first tests show that the creatures are jumping around in the simulation, and the fitness values are fluctuating. The speaker concludes that while the fitness is not yet steadily increasing, the fundamental architecture of the genetic algorithm is complete, and future work will focus on fine-tuning the parameters to improve convergence.

---

### 15_Tweak_the_GA_Video_6_min

# Tweak the GA
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/6hnKN/tweak-the-ga

This module series is structured across several major AI domains, beginning with the foundational principles of game-playing AI. Weeks 1 through 5 establish the groundwork for AI agents, starting with general game playing and progressing to formalizing reinforcement learning. The central technical focus in this phase is the Deep Q-Network (DQN) agent. Week 4 is dedicated to the practical implementation of the DQN agent, building upon the theoretical framework established in Week 2. Furthermore, Week 5 addresses the contemporary state of the art and the critical ethical considerations inherent in AI game players.

The curriculum then transitions to the topic of evolving artificial creatures, commencing in Week 6. This section begins with automatic design using genetic algorithms. Week 7 focuses on practical robotic implementation, utilizing tools like pybullet and specific hardware descriptions via URDF files. Week 8 details the necessary genetic encoding scheme for these evolving systems. Crucial to the process, Week 9 covers the fitness function and selection mechanisms.

A deep dive into the Genetic Algorithm (GA) process is achieved through focused learning modules. Key components include developing a robust fitness function and handling simulation, which involves multi-process evaluation. Population management is another critical concept, detailing selection and breeding strategies. Specific GA techniques covered include roulette wheel selection and the crossover mechanism. The final weeks of this segment involve implementing the GA, observing evolution, and saving the fittest individuals.

Following the evolutionary phase, the course shifts to Generative and Collaborative AI, spanning Weeks 10 through 15. Week 11 introduces the core concepts of generative systems. The practical application begins in Week 12 with generating lyrics using GPT-2. Week 13 explores music composition through MusicVAE, demonstrating generative capability in complex media.

The technical detail is further advanced in Week 14, focusing on the DiffSinger model. Week 15 synthesizes these concepts, culminating in a pop song generator, bringing various generative technologies together.

The latter half of the course is dedicated to the "Toy Robot Scientist" project, starting in Week 16. This section provides context by discussing the introduction, history, and the legal and ethical issues surrounding robot systems. Week 17 focuses on building the system and defining knowledge representation. Week 18 details the introduction to the Robot Scientist reasoning phase. Week 19 concentrates on the complexities of planning and analysis within the system. Week 20 reviews the state of the art in various Robot Scientist projects.

The module concludes with Week 21 serving as a dedicated exam preparation week, leading into the final examinations in Week 22.

---

### 16_Saving_and_viewing_fittest_Video_18_min

# Saving and viewing fittest
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Vim3I/saving-and-viewing-fittest

This transcript documents the final steps of implementing a working Genetic Algorithm (GA): **saving the results of the evolution** and **using those saved genomes to run in a real-time simulation.**

Here is a structured summary of the process:

---

### 💾 Part 1: Saving Elite Genomes (Persistence)

The first goal was to implement code that allows the system to save the fittest individuals (the elite) after each generation of evolution.

**1. Implementation:**
*   A series of **CSV files** was created, with one file generated for each evolution iteration.
*   A dynamic filename was created based on the generation number: `generation_[elite].csv`.
*   **Result:** The code successfully generated and saved these files. The content of the file represented the genome of the elite individual for that specific generation.
*   **Observation:** The elite genome remained remarkably consistent across generations, showing only sensible, slight variations (e.g., a mutation from a value of 7 down to 6).

### 🏃 Part 2: Running Simulations with Evolved Genomes (Testing)

The second and final major step was to load one of the saved genomes and run it in the physics simulation to observe its behavior.

**1. Modifying the Code:**
*   The existing "Test Motor" script was copied and renamed to `run_genome.py`.
*   The core functionality was changed: Instead of generating a completely random creature, the script was modified to **load the creature's DNA** directly from the saved CSV file (e.g., `DNA = genome.genome.from_csv('Elite_Elite.csv')`).

**2. Execution and Results:**
*   The simulation was run using the elite genome from the GA.
*   **Observation:** The resulting creature successfully moved in the simulation, exhibiting a "shoving motion," which the presenter deemed "pretty good."

### 🎯 Conclusion and Next Steps

The code has successfully been upgraded to a fully functional genetic algorithm:

*   **Capability:** The system can now **store** fit individuals and **reload** them for real-time testing in the simulation environment.
*   **Current Status:** The GA is now ready for large-scale evolution runs.
*   **Future Work:** The next video will explore running the GA with a much bigger initial population and many more iterations to discover what truly optimized and fit individuals look like.

---

### 17_Demo_some_fit_individuals_Video_8_min

# Demo some fit individuals
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Wfw87/demo-some-fit-individuals

This module explores advanced topics across artificial intelligence, focusing sequentially on game playing, evolutionary design, generative systems, and robotic reasoning.

The initial phase focuses on AI game players, beginning with general AI concepts in Week 1. Week 2 formalizes reinforcement learning by introducing the Deep Q-Network (DQN) agent. AI tooling is covered in Week 3, followed by a practical implementation of the DQN agent in Week 4. The course concludes the game playing segment in Week 5 by addressing the state of the art and critical ethical implications of AI game players.

The program then transitions to evolving artificial creatures, starting in Week 6 with automatic design using genetic algorithms (GA). Week 7 details the construction of robots, utilizing specialized simulation environments like Pybullet and defining structures via URDF files. Genetic encoding is formally addressed in Week 8, providing the blueprint for the evolutionary process. Week 9 concentrates on the core mechanisms of evolution, specifically the fitness function and selection processes.

Detailed GA practices include defining the fitness function and running creatures in simulation, often using multi-process evaluation for efficiency. Population management involves careful planning of selection and breeding, utilizing techniques such as roulette wheel selection. Further evolutionary mechanisms covered include crossover and the overall "Evolution!" process. Practical GA implementation requires tweaking the algorithm and saving/viewing the fittest individuals.

The next major phase covers Generative and Collaborative AI, beginning in Week 10 by reviewing the state of the art in evolving morphology. Week 11 introduces the principles of generative systems, while Week 12 demonstrates text generation through models like GPT-2. Generative music composition is explored in Week 13 using MusicVAE, followed by advanced music synthesis methods like DiffSinger in Week 14. The module synthesizes these concepts by building a complete pop song generator in Week 15.

The final core section, beginning in Week 16, introduces the "Toy Robot Scientist" framework. This section covers the system's history, perspectives, and crucial legal and ethical issues. Knowledge representation is built in Week 17, followed by the introduction of the Robot Scientist reasoning phase in Week 18. Weeks 19 and 20 concentrate on advanced planning and analysis capabilities within the framework, examining the state of the art in Robot Scientist projects. Week 21 is dedicated to exam preparation, culminating in the final exam week of Week 22.

---

### 18_Implement_the_GA_Reading_30_min

# Implement the GA
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/rETo9/implement-the-ga

This curriculum outlines a comprehensive 22-week program focusing on advanced topics in Artificial Intelligence, moving through game playing, evolutionary computation, generative AI, and robotics. The course begins with the foundational concepts of Game playing AI, covering topics from basic AI game players in Week 1 to formalizing reinforcement learning. Weeks 2 through 4 specifically delve into the Deep Q-Network (DQN) agent, providing a detailed implementation of the DQN agent for game playing AI. Week 5 expands the discussion by addressing the state of the art and critical ethics associated with AI game players.

The curriculum shifts significantly in Week 6, introducing the concept of Evolving Artificial Creatures, starting with automatic design using genetic algorithms. Weeks 7 and 8 transition into applied robotics, focusing on building robots utilizing pybullet and URDF files. Week 9 is dedicated to the core mechanics of Genetic Algorithms (GA), covering the genetic encoding scheme and the crucial definition of the fitness function.

The detailed lessons in the GA section cover robust simulation and evaluation methodologies, including multi-process evaluation for fitness function implementation. Population management is a key technical area, detailed through the implementation of selection techniques, such as Roulette Wheel selection. Furthermore, the process includes teaching genetic operators like Crossover and guiding students through the complete evolutionary cycle. Practical implementation culminates in the module "Implement the GA," referencing a specific lab worksheet for detailed application.

Following the focus on evolutionary computation, Weeks 11 through 15 introduce Generative and Collaborative AI. The focus begins with general generative systems in Week 11 and progresses to specific applications, such as generating lyrics using GPT-2. Further technical dives include music composition via MusicVAE and the utilization of DiffSinger. The module culminates in Week 15 with a comprehensive project on creating a pop song generator, integrating these diverse systems.

The final major phase, Weeks 16 through 20, is dedicated to "A toy Robot Scientist." This section covers the historical perspectives, legal, and ethical issues surrounding AI in robotics. The technical instruction emphasizes system building and robust knowledge representation. The curriculum then focuses on the reasoning phase of the Robot Scientist, covering planning and advanced analytical procedures. The program concludes in Week 21 with dedicated exam preparation, followed by the final exam in Week 22. The overall structure involves continuous assessment through quizzes, practice assignments, and hands-on implementation coding.

---

### 19_GA_solution_code_Reading_10_min

# GA solution code
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/rICMI/ga-solution-code

This comprehensive module curriculum spans various advanced topics in Artificial Intelligence, beginning with AI for game playing. The initial phase introduces Game playing AI, progressing from a basic AI game player in Week 1 to formalizing reinforcement learning in Week 2. Week 3 focuses on general AI game playing tooling, leading into the crucial implementation of the Deep Q-Network (DQN) agent in Week 4. Week 5 examines the state of the art and the ethical considerations surrounding AI game players.

The curriculum then shifts focus to the concept of evolving artificial creatures, beginning in Week 6 with automatic design utilizing genetic algorithms (GA). Weeks 7 and 8 delve into practical robotics, covering the building of robots using tools like pybullet and defining structures via URDF files. Week 9 is dedicated to the implementation and rigorous testing of the GA.

The technical instruction for Week 9 starts with defining the fitness function and simulation mechanics. Students learn to evaluate creatures and implement the fitness function, often utilizing multi-process evaluation for efficiency. Following this, the module addresses population management, concentrating on selection and breeding strategies. Specific technical mechanisms like roulette wheel selection, crossover, and the general evolution process are studied. Several exercises emphasize tweaking the GA and saving/viewing the fittest individuals.

The subsequent weeks introduce modern generative and collaborative AI systems. Week 10 covers the state of the art in evolving morphology, providing a transition into generative systems. Week 11 introduces generative systems, while Week 12 focuses on generating lyrical content using the GPT-2 model. Week 13 explores music composition via MusicVAE, followed by an examination of DiffSinger in Week 14. Week 15 synthesizes these concepts into a comprehensive pop song generator project.

The final major segment explores practical applications through "A toy Robot Scientist" project, starting in Week 16 by discussing introduction, history, perspectives, and legal/ethical issues. Weeks 17 through 20 build the system, addressing knowledge representation, the robot scientist reasoning phase, and planning/analysis. Week 20 concludes this segment by reviewing state-of-the-art Robot Scientist projects. The module concludes with Week 21 dedicated to exam preparation and Week 22 being the exam week. The materials include solutions code for the completed GA code.

---

### 20_Recap_of_week_9_study_Video_2_min

# Recap of week 9 study
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/r6zwp/recap-of-week-9-study

The instructional materials chronicle the successful implementation and expansion of Artificial Intelligence concepts, culminating in a fully functioning Genetic Algorithm (GA) by the end of Week 4. This achievement mirrors the work done by Karl Sims in his 1994 thinking machine systems, signifying a major technical milestone.

The course establishes that a robust GA allows for the evolution of creatures or solutions to optimize a defined set of problems. Central to this process are two key concepts: the fitness function and the population model. Learners acquire the ability to explain how these components are utilized in genetic algorithms to achieve optimization. Specifically, the population model facilitates sampling across the search space by maintaining a diverse collection of different solutions simultaneously.

A critical skill developed is the construction and implementation of a fitness function from scratch. While the initial implementation was simple, the instruction encourages further investigation into more elaborate fitness functions for enhanced control over creature evolution. The GA employs several genetic manipulation techniques to alter and interbreed solutions. These operators include grow mutations, shrink mutations, crossover, and point mutation. These techniques enable the core capability of the GA: multiplying the sampling ability across the search space.

The curriculum structure shows an initial focus on Game Playing AI, covering DQN agent formalization and implementation in Weeks 2, 3, and 4. Weeks 6 through 9 are dedicated entirely to Evolving Artificial Creatures using genetic algorithms. Week 9 delves into the fine mechanics of GA convergence and selection. Key processes include using roulette wheel selection and performing crossover operations.

Furthermore, the course progresses into advanced robotics, detailed in Week 7, which utilizes Pybullet and URDF files for building evolving robots. The genetic encoding scheme is a major focus in Week 8, directly supporting the fitness function and selection process. Subsequent modules shift focus dramatically to modern AI paradigms. Weeks 11 through 15 explore Generative and Collaborative AI. This section covers state-of-the-art systems such as GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition.

The course concludes by addressing the intersection of AI and human interaction via the "Toy Robot Scientist" modules (Weeks 16-20). These modules examine knowledge representation, reasoning phases, planning, and the associated legal and ethical issues of sophisticated AI systems. Ultimately, the material provides a comprehensive overview spanning foundational GA implementation to cutting-edge generative models and ethical robotics.

---

### 21_Self-evaluation_checklist_Fitness_function_and_selection_Reading_30_min

# Self-evaluation checklist: Fitness function and selection
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/g4LhG/self-evaluation-checklist-fitness-function-and-selection

This text presents a detailed self-evaluation checklist outlining the critical learning outcomes associated with the implementation and understanding of Genetic Algorithms (GAs). The core focus is on leveraging biological concepts, such as genetic manipulation, to optimize complex problem solutions.

Firstly, understanding genetic manipulation techniques is fundamental to creating necessary variation within a population. This process involves implementing specific methods to introduce diversity into the evolving system. These techniques include crossover, which combines genetic material from selected individuals, and mutation, which introduces novel diversity into the population. The successful generation of new individuals through these methods is crucial, and this variation ultimately contributes significantly to the overall effectiveness of an evolving system.

Secondly, the development and application of a robust fitness function are paramount to guiding the optimization process. A fitness function defines the purpose of the evolutionary algorithm by quantitatively evaluating potential solutions within the population. It must be meticulously designed to effectively differentiate between individuals that are better and those that are worse at solving the target problem. The fitness function is then utilized to rank individuals, allowing for precise selection. Furthermore, the ability to adjust the fitness function is necessary to continually refine the selection process and move toward optimal solutions.

Thirdly, the synergy between fitness functions and population models governs the entire optimization cycle within genetic algorithms. The fitness function dictates the direction and speed of the population's evolution. Understanding different population models, such as the steady-state model and the generational model, is essential, as each impacts the selection dynamics and overall evolutionary trajectory differently.

The mechanism of selection is a pivotal element, directly influencing which individuals are chosen to reproduce and propagate their genetic material. Specific selection mechanisms studied include tournament selection and roulette wheel selection. Both these processes ensure that superior individuals are more likely to be selected.

Overall, the genetic algorithm achieves optimization over multiple generations by balancing the forces of selection, crossover, and mutation. The fitness function influences the evolution, while selection mechanisms drive the propagation of advantageous traits. Final competency requires the ability to analyze and interpret the system's performance by meticulously observing the changes in population fitness over successive generations. If these concepts are mastered, the implementation of the GA is considered successful and on track.

---

