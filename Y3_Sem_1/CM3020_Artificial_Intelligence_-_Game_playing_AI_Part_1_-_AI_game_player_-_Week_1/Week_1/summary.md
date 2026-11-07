# Week 1 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Welcome_and_introduction_to_the_course_Video_3_min_Get_started

# Welcome and introduction to the course
Video • 3 min
Get started - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/dH6Rp/welcome-and-introduction-to-the-course

This BSC AI course adopts a unique approach to teaching artificial intelligence, focusing on four deep-dive case studies that demonstrate how real-world AI systems are deployed. The module is co-developed with Larisa Soldatova, a leader in Data Science at Goldsmiths College, University of London, who brings over 20 years of AI experience. The curriculum aims to provide students with insight into the entire ecosystem of an AI project, not just the underlying algorithms.

The four core case studies are: The Robot Scientist, Evolving Creatures in Simulation, AI Game Player, and Creative Applications of Artificial Intelligence. Larisa Soldatova introduces the Robot Scientist, an pioneering system that achieved fully automated scientific discovery. The Evolving Creatures case study recreates a famous 1990s research paper by Karl Sims, focusing on automated design using genetic algorithms. The AI Game Player module examines a 2015 DeepMind paper, detailing an AI agent capable of playing Atari video games at human-level standards. Finally, the Creative AI study explores building collaboration models where an AI acts as a creative collaborator.

The subsequent syllabus provides a comprehensive technical roadmap across several specialized modules. Weeks 1 through 5 focus on the AI Game Player, covering reinforcement learning and the practical implementation of the Deep Q-Network (DQN) agent. Week 2 introduces the formalization of reinforcement learning, while Week 4 focuses specifically on the implementation of the DQN agent. Weeks 6 through 10 are dedicated to Evolving Artificial Creatures, focusing on automatic design via genetic algorithms. This module involves building robots using technical formats like Pybullet and URDF files, and implementing the genetic encoding scheme and fitness function.

The Generative and Collaborative AI topics cover Weeks 11 through 15. This section introduces generative systems and includes specific case studies on generating lyrics with GPT-2, music composition using MusicVAE, and applying DiffSinger. Weeks 16 through 20 provide an in-depth exploration of the Toy Robot Scientist. This sequence covers system introduction, knowledge representation, the critical reasoning phase, planning and analysis, and the current state of art in Robot Scientist projects. This structured journey guides students from basic algorithms to complex, integrated, and ethically considered AI deployments.

---

## 02_Module_syllabus_Reading_20_min

# Module syllabus
Reading • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/SnnoU/module-syllabus

This course, CM3020, introduces students to the broad and long-standing field of Artificial Intelligence (AI). AI remains a key area of research within computer science. The module is designed to build upon and complement several other related modules within the programme structure. The core focus of this course centers on specific Artificial Intelligence techniques. These techniques encompass crucial topics such as symbolic representations, modeling, task learning, and game playing. Students will gain an understanding of the historical development of AI. This history includes foundational concepts such as search, vision, and planning. Furthermore, the course familiarizes participants with the foundations of agent-based approaches. These approaches relate directly to software design, decision making, and advanced problem solving. A critical element covered is the ability to solve problems under uncertainty. Students will have practical opportunities to apply these AI techniques to real-world problems. This practical focus specifically includes scenarios involving game playing and complex decision making. Upon successful completion, students will be able to describe and discuss key issues across a range of AI branches. They will also be able to describe and outline effective strategies for artificial agents in game playing scenarios. These strategies must utilize appropriate representations of the scenario data. A vital objective is learning how to select appropriate AI algorithms for particular scenarios. Students must also evaluate the adequacy and efficiency of these chosen algorithms using proper techniques. Furthermore, students are required to create working computer programs that successfully implement specific AI techniques. Finally, they will learn how information can be represented within an artificial intelligence system. This includes the ability to select the most appropriate representations for diverse types of information. Specific readings for each week are provided within the designated Readings pages for detailed study.

---

## 03_Getting_started_on_this_module_Reading_20_min

# Getting started on this module
Reading • 20 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/4AdJK/getting-started-on-this-module

This module begins by welcoming students and advising them to start by reviewing the syllabus and watching the introduction video. Students must review the module's learning outcomes to identify key knowledge and skills, and examine the assessment section to understand how to pass. For those new to the Coursera platform, an Orientation course is recommended to deepen understanding and discover tools for success. Three vital communication tools will be used throughout the program: discussion forums, Slack, and Zoom. Students should familiarize themselves with these tools within the Orientation course. An initial step is to introduce oneself to classmates in the dedicated 'Getting to know each other' discussion forum. Before participating, students must review the guidelines and follow the essential rules for using discussion forums, which are found in the Orientation course. The Orientation course also provides information on live webinars and the function of the Online Library.

The University is piloting Studiosity, a new online service, which offers academic writing support and refresher assistance in various topics. The University of London Careers Service assists all students regardless of their professional status. This service caters to those who are a career starter, a career developer, or a career changer. Aligning studies with career goals is emphasized as a method to maintain motivation and success. Resources for career enhancement include the Careers Connect platform and scheduled live targeted BSc Computer Science careers webinars. Specific career starter resources, including a video detailing how to develop work experience, are also available.

Independent research activities require students to conduct investigations using both general internet sources and the Online Library. Students are advised to use the research checklist to identify appropriate internet resources. Furthermore, they can visit the Online Library's specific page on the effective searching of databases. The Online Library tutorial, titled "Computer Science Information Skills," guides effective usage of this rich resource. Accessing the Online Library requires logging in using the part of the Portal username before the '@' symbol (e.g., entering `ab123` if the username is `ab123@london.ac.uk`).

Finally, students are encouraged to create a non-assessed study journal, which can be traditional pen and paper or electronic. The journal serves to collate information, monitor progress, and organize notes for future coursework or revision. While pen and paper is an option, electronic documents are preferable because they are easily searchable and can store links. Suggested electronic formats include live Word documents, Google Docs, OneNote, or Evernote. Journal entries should include links to websites, personal reflections, responses to case studies, and notes on readings and videos. Students are instructed to start a journal and then post an entry detailing how they will record reflective practice and which journal tool they will use.

---

## 04_Complete_reading_list_Reading_10_min

# Complete reading list
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/c9JDR/complete-reading-list

This is an extremely detailed and well-curated list of references spanning the major subfields of Artificial Intelligence: **Game AI (Deep Reinforcement Learning), Computational Creativity, Generative Models, and Foundational/Theoretical AI.**

To make this information maximally useful, I have categorized the entries by theme, highlighting the key contribution of each paper or book.

---

## 🤖 I. Game AI & Deep Reinforcement Learning (DRL)
*(This section covers the paradigm shift of AI moving from traditional programming to learning through interaction and competition.)*

### 🧠 Landmark Achievements & Benchmark Games
These papers represent breakthroughs where AI achieved human-level or superhuman performance in complex, real-world games.

*   **Go (2017):** Silver, D. et al. *Mastering the game of go without human knowledge.* (Demonstrated the power of self-play and neural networks on a complex board game.)
*   **Poker (2018):** Brown, N. and T. Sandholm. *Superhuman AI for heads-up no-limit poker: Libratus beats top professionals.* (Showcased AI achieving expert/superhuman performance in complex strategic games.)
*   **Atari (2015):** Mnih, V. et al. *Human-level control through deep reinforcement learning.* (The foundational paper that popularized DRL in computer vision/game playing.)
*   **Scrabble (2002):** B. 'World-championship-caliber Scrabble'. (An early example of advanced AI performance in word games.)
*   **Mario AI (2013):** Togelius, J. et al. *The Mario AI championship 2009–2012.* (A reflective look at the competitive AI landscape in platformer games.)
*   **Dota II (2019):** Raiman, J., S. Zhang and F. Wolski. *Long-term planning and situational awareness in OpenAI five.* (Demonstrates applying AI to extremely complex, large-scale strategy games.)

### 🛠️ DRL Techniques & Architecture
These papers focus on the algorithms, architectures, and methodologies used to improve AI performance.

*   **Early DQN (2013):** Mnih, Volodymyr, et al. *Playing atari with deep reinforcement learning.* (The open-access version of the groundbreaking DQN paper.)
*   **Rainbow Atari Player (2018):** Hessel, M. et al. *Rainbow: combining improvements in deep reinforcement learning.* (An advancement over standard DQN, combining multiple improvements for better performance.)
*   **DreamerV2 (2020):** Hafner, D. et al. *Mastering atari with discrete world models.* (Utilizes world models, a sophisticated method allowing AI to predict future states internally, improving efficiency.)
*   **R2D2 Atari Player (2018):** Kapturowski, S. et al. *Recurrent experience replay in distributed reinforcement learning.* (Focuses on improving memory and processing in distributed learning environments.)
*   **Agent57 Atari Player (2020):** Badia, A.P. et al. *Agent57: Outperforming the atari human benchmark.* (A benchmark study showing AI surpassing human performance across various Atari games.)
*   **Alphastar (2019):** Arulkumaran, K., A. Cully and J. Togelius. *Alphastar: An evolutionary computation perspective.* (Presents an evolutionary approach to solving complex game problems.)
*   **Methodology:** Markov Decision Process toolbox (General resource for modeling and solving state-based problems.)

### ⚖️ Ethical and Competitive Considerations
*   **Fairness in Games (2019):** Canaan, M., C. Salge, J. Togelius and A. Nealen. *Leveling the playing field-fairness in ai versus human game benchmarks.* (Addresses the critical issue of ensuring competition is fair when AI dramatically outperforms human benchmarks.)

---

## 🎨 II. Computational Creativity (CC)
*(This section explores the philosophy and mechanism of how machines can generate novel or creative output.)*

### 💡 Foundational Theories & Philosophy
These references provide the philosophical basis and history of the concept of creativity applied to machines.

*   **Boden, Margaret A. (2009):** *Computer models of creativity.* (A seminal work discussing the different types of creativity—like combinatorial, extrapolative, and syncretic—and how AI might model them.)
*   **Still, Arthur, and Mark d'Inverno (2

---

## 05_Introduction_to_case_study_1_Video_9_min

# Introduction to case study 1
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/mBTj9/introduction-to-case-study-1

This course begins with an extensive exploration of AI game playing in Week 1, covering foundational material, case studies on video game AI, and the conceptual introduction to reinforcement learning. Weeks 2, 3, and 4 formally transition into the technical application of game-playing AI, focusing specifically on the theoretical formalization of reinforcement learning. A major technical milestone is reached in Week 4 with the detailed implementation of the DQN agent (Deep Q-Network). Week 5 expands the scope to the current state of the art and the ethical considerations surrounding AI game players.

The curriculum then shifts focus to autonomous design through evolving artificial creatures, beginning in Week 6. Weeks 7 through 10 concentrate on genetic algorithms (GA), detailing the building of robots using frameworks like pybullet and URDF files. Key technical elements include mastering the genetic encoding scheme in Week 8 and optimizing the fitness function and selection processes in Week 9.

Weeks 11 through 15 are dedicated to the expansive field of generative and collaborative AI. The course explores diverse generative systems, including the ability to generate lyrics using GPT-2. Specialized topics include music composition utilizing MusicVAE and advanced audio generation with DiffSinger. This section culminates in a practical project involving a pop song generator.

The latter half of the course introduces highly complex systems in Weeks 16 through 20 via "A toy Robot Scientist." This module covers the system's history, perspectives, and ethical issues. Crucially, the coursework delves into knowledge representation and the system's reasoning phase. Further topics involve detailed planning and analysis capabilities within the Robot Scientist framework.

Finally, Week 21 serves as dedicated exam preparation, followed by the examination week in Week 22. This structured progression guides students through the foundational concepts of AI to highly advanced applications in robotics and generative modeling.

---

## 06_Breakdown_of_case_study_1_Reading_5_min

# Breakdown of case study 1
Reading • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/CtpGp/breakdown-of-case-study-1

This five-week case study examines AIs that play video games using reinforcement learning, formalizing the Deep Q Network (DQN) agent in Week 2. The curriculum covers tooling—specifically `openAI gym`, `keras`, and convolutional neural networks—followed by the agent's implementation (Week 4), culminating in a discussion of the state of the art and ethics in AI game players (Week 5).

---

## 07_Slides_used_in_the_video_lectures_in_week_1_Reading_10_min

# Slides used in the video lectures in week 1
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/tAt8I/slides-used-in-the-video-lectures-in-week-1

This course is a comprehensive study spanning 22 weeks, focusing on various advanced topics in artificial intelligence, particularly how AI agents interact with games, environments, and creative systems. The initial phase, Weeks 1 through 5, introduces the concepts of game-playing AI and the principles of Reinforcement Learning (RL). Week 1 provides a foundational overview of AI game players, followed by an exploration of how to formally build such an agent.

The major technical focus of this initial phase is establishing the Deep Q-Network (DQN) agent, which is thoroughly covered in Week 2, Week 4, and Week 5. This deep dive into DQN examines the formalization of reinforcement learning and the practical implementation of the agent. Following the game-playing module, Weeks 6 through 10 shift focus to the design and evolution of artificial creatures using genetic algorithms.

These later weeks detail the processes of automatic design, including the use of pybullet and URDF files for robot building. Key concepts covered include the genetic encoding scheme, the necessity of defining a fitness function, and methods for selection to optimize morphology.

The curriculum then transitions to Generative and Collaborative AI across Weeks 11 through 15, exploring systems that can create content. This section examines the introduction to generative systems and practical applications like generating lyrics using GPT-2. Further topics include music composition using MusicVAE and the analysis of DiffSinger.

The final major module, Weeks 16 through 20, is dedicated to the concept of a "Toy Robot Scientist." This involves exploring the history, legal, and ethical issues related to such systems. The coursework details building the system, focusing on knowledge representation, and the sophisticated reasoning and planning phases of the agent.

The concluding weeks, 21 and 22, are dedicated to exam preparation and the final examination, completing the detailed study of AI systems and advanced agent design. The course structure comprehensively moves from foundational RL concepts to advanced generative models and complex robotic reasoning.

---

## 08_Introduction_to_week_1_study_Video_1_min

# Introduction to week 1 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/a3wQB/introduction-to-week-1-study

This course provides a comprehensive case study on the history and implementation of Game Playing Artificial Intelligence (AI). The introductory module outlines three key learning objectives: describing historic examples of game-playing AIs, evaluating the motivations for researching these systems, and considering methods for implementing such an AI. The course begins by reviewing historical milestones, contrasting the classic Deep Blue achievement in chess with modern video game AIs, such as those developed for Atari. The core focus shifts quickly to the methodology underlying these systems: Reinforcement Learning.

Week 1 establishes the theoretical foundation for how a game-playing AI might be built, introducing the concepts of AI game player milestones. Subsequent studies move into formalizing reinforcement learning, specifically detailing the development of the Deep Q-Network (DQN) agent in Weeks 2 and 4. These weeks address the practical implementation of the DQN agent, building upon the theoretical background.

The course then transitions from traditional game playing to evolutionary design in Weeks 6 through 10. This phase explores the use of genetic algorithms for automatic design, employing tools like pybullet and utilizing URDF files for robotic modeling. The goal is to study fitness functions and selection mechanisms in the context of evolving artificial creatures.

The program subsequently dedicates several modules to Generative and Collaborative AI in Weeks 11 through 15. These weeks showcase applications such as generating lyrics using GPT-2 and composing music with specialized models like MusicVAE and DiffSinger. This section demonstrates AI's capability in creative domains beyond competitive play.

The final major segment (Weeks 16 through 20) is centered on the complex framework known as the Robot Scientist. This segment examines knowledge representation, planning, and reasoning phases to construct intelligent, problem-solving robotic systems. The curriculum concludes with exam preparation in Week 21 and examination in Week 22, summarizing a wide range of advanced AI disciplines.

---

## 09_Recommended_readings_on_AIs_that_play_video_games_Reading_2h

# Recommended readings on AIs that play video games
Reading • 2h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/62LgJ/recommended-readings-on-ais-that-play-video-games

This document provides recommended readings detailing the progress of Artificial Intelligence in playing various games, spanning from the 1950s into the modern era. The initial recommended starting article covering the work from the 1950s to 2000 is Schaeffer, J.'A gamut of games' in *AI Magazine 22*(3) 2001, pp.29–29, available in the Online Library. Subsequent readings are supplemental and optional.

Early milestones began in 1950 with Shannon, C.'Programming a computer for playing chess' published in *Philosophical Magazine 41*(4) 1950, pp.256–75. In 1952, Strachey, C. explored logical or non-mathematical programmes for Checkers/Drafts, detailed in the *Proceedings of the Association for Computing Machinery Meeting*, pp.46–49. The field advanced significantly by 1979 with Berliner, H.'Backgammon computer program beats world champion' published in *Artificial Intelligence 14*(2) 1980, pp.205–20.

A major development in chess occurred in 1992, when Schaeffer, J. et al. presented 'A world championship caliber checkers program' in *Artificial Intelligence –3 1992*, pp.273–89. The landmark 1997 Deep Blue chess victory was documented by Campbell, M.A., J. Hoane Jr and Feng-hsiung Hsu in 'Deep blue' in *Artificial Intelligence 134*(1–2) 2002, pp.57–83. Furthermore, world-championship-caliber Scrabble was achieved by B. Sheppard in 2002, documented in *Artificial Intelligence 134*(1–2) 2002, pp.241–75.

More recent developments included the Mario AI competition in 2013, documented by Togelius, J. et al. as 'The Mario AI championship 2009–2012' in *AI Magazine 34*(3) 2013, pp.89–92. A major conceptual shift occurred in 2015 when Mnih, V. et al. detailed 'Human-level control through deep reinforcement learning' for Atari in *Nature 518*(7540) 2015, pp.529–33.

The application of AI reached new heights in 2016 with Silver, D. et al.'Mastering the game of go without human knowledge' published in *Nature 550*(7676) 2017, pp.354–59. In 2018, the capabilities of AI for complex strategy games were demonstrated by Brown, N. and T. Sandholm with 'Superhuman AI for heads-up no-limit poker: Libratus beats top professionals' in *Science 359*(6374) 2018, pp.418–24.

The focus broadened further in 2019, as Raiman, J., S. Zhang and F. Wolski explored 'Long-term planning and situational awareness in OpenAI five' for Dota II, published as an arXiv preprint arXiv:1912.06721. A subsequent advancement in Atari was reported in 2020 by Badia, A.P. et al., demonstrating 'Agent57: Outperforming the atari human benchmark' at the International Conference on Machine Learning. All listed articles include specific publication links, including OL-CO3020-Shannon.pdf and OL-CM3020-Schaeffer-7038.pdf.

---

## 10_Overview_playing_games_with_AI_Video_14_min

# Overview: playing games with AI
Video • 14 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/NNLqB/overview-playing-games-with-ai

This course provides a comprehensive overview of advanced artificial intelligence applications, beginning with fundamental concepts of game-playing AI in Week 1. The initial modules introduce the course syllabus, prompt self-reflection through discussion prompts, and establish the background of AIs that play video games. Key concepts in early studies involve milestones in AI game players and the practical application of learning theory.

The central technical focus shifts in Week 2 and Week 4 to Reinforcement Learning and the implementation of the Deep Q-Network (DQN) agent, which is essential for building effective game-playing AI systems. Week 3 details the necessary tooling for these game-playing AI architectures.

The curriculum expands into evolutionary computing starting in Week 6, detailing the use of genetic algorithms for automatic design. This is further explored through the use of environments like PyBullet and the structure defined by URDF files in Week 7. Weeks 8 and 9 focus specifically on the technical components of evolutionary systems: genetic encoding schemes and fitness function selection.

The thematic scope widens significantly in the Generative and Collaborative AI modules (Weeks 11–15). These weeks explore various generative systems, including generating lyrics using GPT-2, composition with MusicVAE, and specialized models like DiffSinger. The final phase of this section culminates in a sophisticated pop song generator.

The later modules shift focus to complex robotics and knowledge representation in the "A toy Robot Scientist" segment (Weeks 16–20). This involves building the system, defining knowledge representation, and addressing the planning and reasoning phases of the robotic agent. Throughout the entire course structure, dedicated time is allocated for assignments, self-evaluation, and final exam preparation (Week 21 and Week 22).

---

## 11_AI_game_player_milestones_Video_13_min

# AI game player milestones
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/ad5CC/ai-game-player-milestones

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## 12_How_might_we_build_a_game_playing_AI_Video_9_min

# How might we build a game playing AI?
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/0Ne4k/how-might-we-build-a-game-playing-ai

This comprehensive course progresses through various domains of artificial intelligence, beginning with the foundational principles of AI game playing. Week 1 introduces the core concepts, establishing the background of AIs that play video games and setting the stage for game-playing milestones. Week 2 and 3 focus on the formalization of reinforcement learning, preparing for the technical deep dive into AI agent construction. Weeks 4 and 5 involve the practical implementation and state-of-the-art examination of the DQN agent, a key technical model in modern game AI.

The curriculum then shifts dramatically in Week 6, focusing on evolving artificial creatures through the application of genetic algorithms. Weeks 7 through 10 explore the development of robotic systems, including building robots using pybullet and URDF files, and understanding the crucial components of genetic encoding schemes and fitness functions.

The course next transitions into Generative and Collaborative AI, beginning in Week 11 with an introduction to generative systems. The technical focus deepens in Weeks 12 through 14, examining specific models, such as generating lyrics with GPT-2, music composition with MusicVAE, and the application of DiffSinger. Week 15 culminates this section by integrating these concepts into a pop song generator.

The final major thematic block, spanning Weeks 16 through 20, addresses the sophisticated field of a Toy Robot Scientist. This segment covers its history, legal and ethical considerations, knowledge representation, and the critical reasoning and planning phases of the system. These final weeks conclude with Week 21 dedicated to exam preparation, leading into Week 22, the examination week. The overall course provides a detailed overview of how AIs are built, from foundational Reinforcement Learning principles to complex, generative, and autonomous systems.

---

## 13_Activity_Experiment_with_some_games_Reading_1h

# Activity: Experiment with some games
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/Ua3by/activity-experiment-with-some-games

Now that you have encountered some of the previous work and the basic concepts of game playing with reinforcement learning, it is time to experiment. online for a simple arcade-style video game and play it. It is not often you will be instructed to do that, unless you are a games tester by trade! You can find browser-based versions of various games....

---

## 14_Recap_of_week_1_study_Video_50_sec

# Recap of week 1 study
Video • 50 sec - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/MVWrI/recap-of-week-1-study

The course concluded Week 1 of the game-playing AI case study, marking a significant learning checkpoint for participants. Upon completion of Week 1, students are expected to be capable of describing historical examples of game-playing AIs. Furthermore, they should be able to evaluate the underlying motivations for researchers investigating game-playing AI systems. Participants also started the crucial process of considering how one might practically implement a game-playing AI.

The immediate progression for Week 2 involves a deep dive into formally describing game-playing and game-playing systems. This formalization is a prerequisite step that enables the later development of a complete, working system.

The curriculum then progresses through highly technical stages, starting with the formalization of reinforcement learning in Week 2. Week 3 focuses specifically on introducing tooling essential for developing game-playing AI systems. The core technical implementation begins in Week 4 with a detailed look at the implementation of the Deep Q-Network (DQN) agent.

Following the practical AI agent implementation, Week 5 shifts focus to the state of the art and ethical considerations surrounding AI game players. The later modules then explore evolutionary computing, beginning in Week 6. Weeks 7, 8, and 9 focus on building robots using specific platforms like pybullet and URDF files. Week 8 specifically introduces the essential genetic encoding scheme.

These evolutionary themes continue in Week 10, examining the state of the art in evolving morphology. The focus then broadens to generative and collaborative AI systems starting in Week 11. Week 12 applies this theme by generating lyrics using the GPT-2 model.

The course further explores complex generative processes with MusicVAE in Week 13, specifically addressing music composition. Week 14 examines the DiffSinger model, demonstrating advanced generative techniques. Week 15 culminates the generative section by creating a pop song generator.

The module then shifts into a focus on embodied intelligence with "A Toy Robot Scientist" beginning in Week 16. Week 17 addresses the foundational aspects of building the system, including knowledge representation. Week 18 details the introduction to the Robot Scientist’s reasoning phase. This is followed by Weeks 19 and 20, which cover planning, analyzing, and the state of the art in Robot Scientist projects. The final weeks include a dedicated Week 21 for exam preparation and Week 22 for the official examination.

---

## 15_Self-evaluation_checklist_Game-Playing_AI_Reading_30_min

# Self-evaluation checklist: Game-Playing AI
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/eHIRn/self-evaluation-checklist-game-playing-ai

This text presents a comprehensive self-evaluation checklist designed to assess mastery of the key concepts covered in Week 1 concerning Game-Playing Artificial Intelligence (AI). The fundamental premise is that achieving confidence in all listed statements signifies that the learner has met the expected learning outcomes. Should a learner be unsure of any specific topic, they are advised to review the relevant materials immediately.

The first major conceptual area is focused on understanding historical examples of Game-Playing AIs. A core requirement is the ability to describe at least two pivotal historical examples of this field. These examples specifically include Deep Blue and AlphaGo. It is crucial to understand the deep significance of these AIs within the broader context of artificial intelligence development. Furthermore, learners must be able to explain how these groundbreaking AIs functioned at a high level. This explanation must incorporate the specific techniques they employed. These techniques often include brute-force search methods and advanced reinforcement learning algorithms.

The second area of evaluation focuses on understanding the motivational drivers for game-playing AI research. Researchers must be able to articulate the primary reasons for studying game-playing AIs. This includes understanding their overall importance to the advancement of AI research. A critical concept here is realizing how games provide inherently structured environments. These environments are perfect for rigorously testing the capabilities of complex AI systems. Moreover, the understanding must extend to discussing how advancements derived from game-playing AI contribute to broader AI applications. These applications often extend significantly beyond the boundaries of gaming itself.

The final area details how one might approach the implementation of a Game-Playing AI. Learners must be able to identify the foundational, key components of such an AI system. These indispensable components include effective game state representation and accurate move evaluation. A basic technical understanding of core principles is required. This involves grasping search algorithms, heuristics, and reinforcement learning as they apply to the gameplay context. Furthermore, the learner should be capable of outlining a simple, practical approach. This approach is designed for building a basic AI agent specifically tailored for a turn-based game. Ultimately, this self-assessment guides the student toward targeted review of any underdeveloped topics.

---

