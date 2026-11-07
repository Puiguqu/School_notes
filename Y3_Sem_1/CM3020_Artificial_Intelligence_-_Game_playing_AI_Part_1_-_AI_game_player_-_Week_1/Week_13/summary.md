# Week 13 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

## 02_Slides_for_week_13_Reading_30_min

# Slides for week 13
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/qnqmd/slides-for-week-13

This text outlines a comprehensive curriculum detailing the progression of topics in Artificial Intelligence, spanning several weeks. The course begins by covering foundational AI topics, dedicating Week 1 to "Game playing AI: Part 1" and Week 2 to "Part 2 - Formalising reinforcement learning and the DQN agent." Subsequent weeks elaborate on AI capabilities, including "Part 3 - Game playing AI tooling" (Week 3) and the "Implementation of the DQN agent" (Week 4).

The curriculum then shifts focus to biological and physical AI in Weeks 6 through 10, exploring "Evolving artificial creatures." This section covers automatic design using genetic algorithms (Week 6), building robots with pybullet and URDF files (Week 7), genetic encoding schemes (Week 8), and fitness function and selection (Week 9). Week 10 provides a state-of-the-art review of evolving morphology.

The course transitions into generative and collaborative AI in Week 11, introducing generative systems. Week 12 focuses on practical generation, specifically "Generating lyrics with GPT-2." Week 13 introduces the core technical topic of music composition using MusicVAE, detailing its history and underlying concepts like latent spaces.

Week 13 includes extensive assignments and resources, such as videos on "Music composition with MusicVAE," "Exploring latent space," and working with MusicVAE and Fluidsynth. Further specialized topics in generative AI include "Generative and collaborative AI: Part 4 - DiffSinger" (Week 14) and "Part 5 - Putting it all together and pop song generator" (Week 15).

The latter half of the schedule dedicates significant time to robotics and ethical considerations. Weeks 16 through 20 delve into "A toy Robot Scientist," covering its introduction, building the system, knowledge representation, reasoning, and planning capabilities. The final weeks are dedicated to practical culmination, with Week 21 for exam preparation and Week 22 being the exam week.

---

## 03_Potted_history_of_automated_music_composition_Video_17_min

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

## 04_Introduction_to_latent_spaces_Video_12_min

# Introduction to latent spaces
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/8oVeH/introduction-to-latent-spaces

The curriculum begins with an intense focus on AI game playing, starting with an overview in Week 1 and progressing to the formalization of reinforcement learning and the implementation of the Deep Q-Network (DQN) agent in Week 2 and 4. Week 3 introduces critical tooling for game playing AI, followed by a discussion of the state of the art and ethical considerations in AI game players during Week 5. The focus then shifts to evolving artificial creatures, dedicating several weeks to autonomous design via genetic algorithms (Week 6).

In the evolutionary robotics segment, specific technical aspects are covered, including building robots using pybullet and URDF files (Week 7), the development of a genetic encoding scheme (Week 8), and defining the fitness function and selection methods (Week 9). Weeks 10 and 11 explore the state of the art in evolving morphology and introduce the foundational concepts of generative systems.

The third major unit, Generative and Collaborative AI, begins in Week 12, exploring lyric generation using GPT-2. A deep dive into music composition follows in Week 13, focusing specifically on MusicVAE and its mechanisms. This week involves multiple associated resources, including videos on latent spaces, MusicVAE functionality, and rendering audio with fluidsynth.

Weeks 14 and 15 continue the generative theme, examining advanced systems like DiffSinger and synthesizing the knowledge into a complete pop song generator. The final major segment is dedicated to "A Toy Robot Scientist," starting with an introduction to its history, legal, and ethical issues (Week 16).

The subsequent weeks detail the construction of the system, knowledge representation, and the Robot Scientist’s reasoning and planning phases (Weeks 17-19). Week 20 presents a survey of state-of-the-art Robot Scientist projects, leading into Week 21 for exam preparation and Week 22 for the exam itself. A preliminary topic, 'Introduction to latent spaces,' also appears as a supplemental module.

---

## 05_What_is_Music-VAE_Video_13_min

# What is Music-VAE?
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/xjrPg/what-is-music-vae

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## 06_Javascript_and_promises_Video_7_min

# Javascript and promises
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/aU3tD/javascript-and-promises

The course is structured across multiple modules, beginning with Game Playing AI (Weeks 1-5), which covers foundational concepts and advanced implementations. Early modules introduce reinforcement learning and formally develop the Deep Q-Network (DQN) agent, culminating in practical implementation and analysis of state-of-the-art AI game players and their ethical implications. The second major theme, Evolving Artificial Creatures (Weeks 6-10), focuses on automatic design through genetic algorithms. This section details the use of pybullet and URDF files for robotic implementation, establishing a genetic encoding scheme, and defining fitness functions for morphology evolution. The Generative and Collaborative AI module (Weeks 11-15) explores systems designed to create novel content. Specific applications include generating lyrics using GPT-2 and advanced music composition using MusicVAE. The MusicVAE section provides deep technical dives, including explorations of latent spaces, rendering audio via fluidsynth, and the use of DiffSinger. The final module, "A Toy Robot Scientist" (Weeks 16-20), addresses complex reasoning and autonomous system construction. This module covers knowledge representation, the system's reasoning phase, and sophisticated planning and analysis capabilities. The curriculum concludes with dedicated weeks for exam preparation and the final exam.

---

## 07_Working_with_MusicVAE_Video_8_min

# Working with MusicVAE
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/tdvx2/working-with-musicvae

This technical summary details the workflow for utilizing MusicVAE, a generative musical library, demonstrating the steps from environment setup to latent space sampling and output analysis.

The process begins with preparation, requiring the installation of necessary node modules via `npm install`, which serves as the dependency manager, analogous to `pip install` in Python. Following this, a local web server must be initialized, as the MusicVAE JavaScript library depends on serving its models from a web source. This local server, often running on port 8080, allows the model files—which can include complex multi-track models (e.g., 8/16 part models with bass, drums, and melody)—to be downloaded.

The core workflow involves loading a specific MusicVAE model, such as a one-bar or 16-bar model, into the script environment. The model is instantiated and requires a URL pointing to the newly created local web server for access.

---

## 08_Rendering_audio_with_MusicVAE_and_fluidsynth_Video_15_min

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

## 09_Exploring_latent_space_Video_12_min

# Exploring latent space
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/8l1lb/exploring-latent-space

## VIDEO TRANSCRIPT ## You may navigate through the transcript using tab. To save a note for a section of text press CTRL + S. To expand your selection you may use CTRL + arrow key. You may contract your selection using shift + CTRL + arrow key. For screen readers that are incompatible with using arrow keys for shortcuts, you can replace them with the H J K L keys....

---

## 10_Recap_of_week_13_study_Video_1_min

# Recap of week 13 study
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/ldOyP/recap-of-week-13-study

This curriculum spans various advanced domains of Artificial Intelligence, beginning with Game Playing AI. Weeks 1 through 5 focus on the development and formalization of reinforcement learning (RL) agents. This segment details the application of the DQN agent, covering its theoretical formalization and subsequent practical implementation. Additional topics in this phase include dedicated study on game playing AI tooling and the ethical considerations surrounding AI game players. The focus then shifts to evolving artificial creatures, commencing in Week 6. Weeks 6 through 10 concentrate on automatic design using genetic algorithms (GAs). Specific technical details involve building robots using frameworks like pybullet and implementing URDF files. The subsequent focus covers the genetic encoding scheme, fitness function definition, and selection processes in evolutionary computation. Generative and collaborative AI forms the next major block, spanning Weeks 11 through 15. The course introduces generative systems and explores lyrics generation using GPT-2. A significant portion is dedicated to music composition using MusicVAE, which involves understanding latent spaces. Weekly Week 13 resources provide comprehensive study materials, including a 1-minute introduction video and a 30-minute reading on the history of automated music composition. Practical assignments include quizzes and working with MusicVAE, rendering audio via fluidsynth, and exploring the latent space. Week 14 introduces DiffSinger as a major generative model. The module concludes by integrating all concepts into a pop song generator. Finally, the course addresses sophisticated autonomous agents through the "A toy Robot Scientist" module (Weeks 16-20). This covers the system's introduction, knowledge representation, reasoning phase, and planning/analyzing capabilities. The program culminates in Week 21 as exam preparation and Week 22 as the final exam period.

---

## 11_Self-evaluation_checklist_Part_3_-_Music_composition_with_MusicVAE_Reading_30_min

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

