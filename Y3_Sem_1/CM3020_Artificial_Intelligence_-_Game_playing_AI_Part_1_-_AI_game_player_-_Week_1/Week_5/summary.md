# Week 5 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/oG2EA/weekly-introduction

This course systematically covers four major themes in advanced Artificial Intelligence. Initially (Weeks 1-5), the focus is on Game playing AI, formalizing reinforcement learning and implementing the DQN agent, while also discussing state-of-the-art applications and ethics. The curriculum then transitions to "Evolving artificial creatures" (Weeks 6-10), exploring automatic design using genetic algorithms, building robots with pybullet and URDF files, and refining genetic encoding schemes and fitness functions. Subsequently, Weeks 11-15 delve into Generative and collaborative AI, covering introduction to generative systems, and practical applications like generating lyrics with GPT-2, composing music using MusicVAE and DiffSinger, and creating pop songs. The final major section (Weeks 16-20) is dedicated to "A toy Robot Scientist," addressing historical perspectives, knowledge representation, the reasoning phase, and planning. Key technical details covered include the implementation of the DQN agent, the use of pybullet and URDF for robot building, and specific models like GPT-2, MusicVAE, and DiffSinger. The program prepares students for assessment through Week 21 exam preparation and Week 22 examination. This comprehensive structure spans from fundamental game theory and RL to advanced evolutionary computing, generative modeling, and complex robotics.

---

## 02_Reading_and_slides_for_week_5_Reading_2h

# Reading and slides for week 5
Reading • 2h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/tpQUi/reading-and-slides-for-week-5

This text provides a comprehensive reading list and slide material for Week 5, focusing on the advanced study of AI game players. The primary reading material includes the file `ai-game-player-wk5.pdf`.

A major technical analysis is presented in "Alphastar: An evolutionary computation perspective." This work, by Arulkumaran, K., A. Cully, and J. Togelius (2019), details the use of evolutionary computation principles in game AI. The field of human/AI game competitions is also examined through the lens of fairness. Canaan, M., C. Salge, J. Togelius, and A. Nealen (2019) introduced "The six dimensions of fairness in human/AI games competitions" in their arXiv preprint, arXiv:1903.07008. This paper addresses the challenge of "leveling the playing field" in benchmarks.

Historically, the competitive nature of AI was documented in the reflective piece "The Mario AI championship 2009–2012." This article, authored by Togelius, J. et al. (2013), appears in *AI Magazine* and covers specific benchmarks of human vs. AI skill.

The curriculum also explores various state-of-the-art Deep Reinforcement Learning (DRL) agents tailored for Atari. The Rainbow Atari player was introduced by Hessel, M. et al. (2018) in the Thirty-second AAAI Conference on Artificial Intelligence. This agent is notable for its strategy of "combining improvements in deep reinforcement learning."

Another highly advanced agent is the DreamerV2 Atari player. Hafner, D. et al. (2020) documented this player in arXiv preprint arXiv:2010.02193, highlighting its capacity for "Mastering Atari with discrete world models." The R2D2 Atari player, detailed by Kapturowski, S. et al. (2018), focuses specifically on using "Recurrent experience replay in distributed reinforcement learning."

Finally, Agent57 serves as a benchmark for human comparison. Badia, A.P. et al. (2020) presented Agent57, which was shown to be "Outperforming the Atari human benchmark." All listed papers and materials are noted to be available in the Online Library. A disclaimer is provided regarding potential link failures: "If these links are broken, please let us know via the Student Portal." This rigorous structure encapsulates all provided technical details and references.

---

## 03_State_of_the_art_game_players_Video_8_min

# State of the art game players
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/dqMpF/state-of-the-art-game-players

This summary reviews the critical milestones and developments in AI game playing that occurred subsequent to the publication of the seminal Deep Q-Network (DQN) agent paper in 2015.

The discussion first outlines the key technical elements one must analyze in post-DQN systems, including the agent's general runtime, how experiences are gathered and the state transition matrix is built (beyond the DQN replay buffer), required exploratory behavior (beyond $\epsilon$-nets or greedy approaches), neural network architecture advancements, and the crucial loss function computation. Specifically, the ground truth in DQN is derived by combining an older network version with the immediate reward plus a prediction of future reward.

Following the DQN success, significant progress was made in Atari game playing with the invention of Double DQN, which led to the development of the advanced Rainbow system. Other notable Atari agents reviewed are Dreamer v2 and R2D2.

The field reached a massive milestone in 2020 with DeepMind's development of Agent 57. This agent surpassed most professional game players across a benchmark set of 57 Atari games. Agent 57 demonstrates the ability to play highly complicated games, even those requiring extremely long exploration periods before a reward is achieved.

Turning to complex strategy games, StarCraft 2 was highlighted as a title considerably more challenging than Go. DeepMind's AlphaStar system, developed in 2019, aimed to be a general-purpose AI capable of mastering diverse games. AlphaStar succeeded, reaching a level that matched and exceeded that of professional players in the demanding StarCraft environment. This advanced system integrates deep learning, reinforcement learning, game theory, and evolutionary computation.

The development extended to DotaII, a multi-player team-based strategy game. In 2019, an AI system managed to defeat professional World Champion players, notably the team OG, in back-to-back matches. Crucially, this AI was put online in 2019, engaging in real-time competitive games. Against human players, the AI consistently won 7,215 games while only registering 42 losses.

In contrast, the Mario AI competition predates these major advances, tracing its roots to around 2013 in the original Arcade learning environment. This older community was focused on playing a wide range of games, rather than simply mastering a single title entirely.

---

## 04_Ethics_of_game_playing_AI_Video_11_min

# Ethics of game playing AI
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/IZh0Y/ethics-of-game-playing-ai

This curriculum covers several distinct areas of artificial intelligence, beginning with Game Playing AI (Weeks 1-5), which focuses on developing AI agents and formally implementing reinforcement learning concepts. Key technical elements include the implementation of the Deep Q-Network (DQN) agent, emphasizing state-of-the-art techniques and the ethical implications of AI game players. The course then transitions to Evolving Artificial Creatures (Weeks 6-10), exploring automatic design using genetic algorithms and practical robot building using frameworks like pybullet and URDF files, concentrating on genetic encoding and fitness functions. Next, the focus shifts to Generative and Collaborative AI (Weeks 11-15), covering systems for generating complex content, exemplified by tasks such as generating lyrics using GPT-2, composing music with MusicVAE, and employing DiffSinger. The latter portion, Weeks 16-20, introduces a project based on "A Toy Robot Scientist," detailing system construction, knowledge representation, and advanced reasoning and planning phases. This sequence provides a comprehensive overview from basic AI agents to complex generative models and embodied intelligent systems. The entire structure culminates in exam preparation, reinforcing theoretical knowledge across diverse AI domains.

---

## 05_Recap_of_week_5_study_Video_53_sec

# Recap of week 5 study
Video • 53 sec - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/o3o1P/recap-of-week-5-study

This comprehensive course provides a deep dive into various state-of-the-art concepts in Artificial Intelligence. The curriculum is structured across multiple weeks, progressing from fundamental AI mechanics to highly complex generative and robotic systems. Initially, the focus during Weeks 1 through 5 is dedicated to AI game players. These early modules cover formalizing reinforcement learning and the implementation of the DQN agent, a key technical detail. Weeks 3 and 4 specifically address the tooling and practical implementation phases of the DQN agent. Week 5 then transitions the focus to the state of the art in AI game players and, crucially, the associated ethical considerations.

The learning objectives achieved by the end of Week 5 require students to present examples of AI game player capacities. Furthermore, the course demands reasoning about the ethical impact of human competitive AI and justifying the trend toward general AI's societal influence. Following the game AI module, Weeks 6 through 10 explore evolving artificial creatures. This segment involves practical automatic design using genetic algorithms, specifically utilizing tools like Pybullet and URDF files. Key concepts here include the genetic encoding scheme, fitness function, and selection processes in morphological evolution.

The course shifts significantly in Weeks 11 through 15 to generative and collaborative AI systems. This advanced section covers various models, including generating lyrics with GPT-2 and music composition using MusicVAE. Further technical studies involve DiffSinger and the development of a comprehensive pop song generator. The program continues its progression into robotics and scientific reasoning during Weeks 16 through 20. The module "A Toy Robot Scientist" explores knowledge representation, the system building phase, and advanced reasoning.

This final robotic phase integrates planning, analytical abilities, and critical examination of legal and ethical issues surrounding autonomous agents. The entire course structure is designed to build from foundational game AI to sophisticated, reasoning robotic systems. The concluding weeks, 21 and 22, are reserved for final exam preparation and the examination period. This detailed outline demonstrates the breadth of modern AI fields covered, from formal reinforcement learning to complex generative and physical robotic applications. The course ensures a robust understanding of both the technological capabilities and the ethical implications of advanced AI.

---

## 06_Self-evaluation_checklist_State_of_the_art_and_ethics_in_AI_Game_Players_Reading_30_min

# Self-evaluation checklist: State of the art and ethics in AI Game Players
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/SsnWu/self-evaluation-checklist-state-of-the-art-and-ethics-in-ai-game-players

Use this checklist to assess whether you have successfully achieved the learning outcomes for Week 5. 1. General AI and Its Societal Impact ☐ I can explain the key reasons behind the trend toward general AI. ☐ I can discuss the potential societal impacts of general AI, including benefits and risks. ☐ I can critically evaluate ethical considerations related to general AI. 2....

---

## 07_Game_player_case_study_outro_Video_1_min

# Game player case study outro
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/IuTr8/game-player-case-study-outro

This curriculum outlines an advanced study of contemporary AI, beginning with Game Playing AI (Weeks 1-5). The first phase focuses on formalizing reinforcement learning and implementing the Deep Q-Network (DQN) agent, concluding with an examination of state-of-the-art systems and ethical implications. The program then transitions to Evolving Artificial Creatures (Weeks 6-10), where techniques like genetic algorithms are utilized for automatic design, building robots using Pybullet and URDF files, and defining appropriate fitness functions. Next, the focus shifts to Generative and Collaborative AI (Weeks 11-15), exploring systems such as GPT-2 for lyric generation and MusicVAE and DiffSinger for sophisticated music composition and pop song creation. The final major block, "A Toy Robot Scientist" (Weeks 16-20), delves into practical system building, knowledge representation, and complex reasoning phases. This segment covers the legal and ethical issues surrounding intelligent agents, alongside advanced topics in planning and system analysis. The course is structured with extensive resources, including dedicated videos, reading materials, quizzes, and case studies for each module. The study culminates with dedicated preparation and examination weeks (Weeks 21-22).

---

