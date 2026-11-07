# Week 15 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

## 02_Weekly_reading_Reading_1h

# Weekly reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/6Z5Qt/weekly-reading

The provided text lists the weekly reading materials for the AI Creativity lectures, including the introductory lecture slides defining "what is creativity" (`ai-creativity-wk0_what_is_creativity.pdf`) and the comprehensive "putting it together" lecture slides (`ai-creativity-wk5_all_together.pdf`).

---

## 03_Putting_the_system_together_extracting_notes_Video_16_min

# Putting the system together: extracting notes
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/wIqnh/putting-the-system-together-extracting-notes

This curriculum provides a deep exploration into advanced artificial intelligence across several domains, beginning with Game Playing AI (Weeks 1-5). This initial phase introduces the concept of Reinforcement Learning, formalizing it with the DQN agent, culminating in implementation and a discussion of ethical considerations in AI game players. The focus then shifts to Evolving Artificial Creatures (Weeks 6-10), where automatic design utilizes genetic algorithms for building complex robots using tools like PyBullet and URDF files. A critical component of this evolutionary study involves defining genetic encoding schemes and robust fitness functions for selection. The middle section addresses Generative and Collaborative AI (Weeks 11-15), exploring systems designed to create new content. Technical implementations include generating lyrics with GPT-2 and composing music using MusicVAE and DiffSinger, leading to a complete pop song generator. Following the creative focus, the course transitions into advanced robotic intelligence via "A Toy Robot Scientist" (Weeks 16-20). This later module covers system building, knowledge representation, and the complex reasoning phase required for planning and analyzing tasks. Crucially, the curriculum maintains a persistent focus on legal and ethical issues throughout the study of AI agents and creativity. Supplementary materials include weekly videos, dedicated readings, and practical labs for reinforced learning and music generation. The final weeks are dedicated to intensive exam preparation and examination. The overarching theme unites complex systems development, ranging from game theory to autonomous creative generation.

---

## 04_Mixing_the_singing_with_the_backing_Video_7_min

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

## 05_Discussion_of_creativity_Video_12_min

# Discussion of creativity
Video • 12 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/59pA4/discussion-of-creativity

This course is structured across 22 weeks, covering advanced topics in artificial intelligence, divided into distinct modules. The initial phase (Weeks 1-5) focuses on AI Game Playing, starting with basic game player development and progressing to formalizing reinforcement learning using the Deep Q-Network (DQN) agent and implementing this architecture. The middle section (Weeks 6-10) explores Evolving Artificial Creatures, utilizing genetic algorithms for automatic design and building robots using tools like pybullet and URDF files, while focusing on encoding schemes and fitness functions. Weeks 11 through 15 concentrate on Generative and Collaborative AI, introducing generative systems and applying them practically to tasks like generating lyrics with GPT-2, composing music using MusicVAE, and employing DiffSinger for advanced synthesis. The practical implementation culminated in a pop song generator, requiring complex steps like extracting notes and mixing singing with backing tracks. The subsequent module (Weeks 16-20) delves into "A Toy Robot Scientist," covering its history, knowledge representation, the reasoning phase, and planning mechanisms. This latter module emphasizes the state of the art in robot science and associated legal and ethical issues. Overall, the course integrates theoretical concepts with practical tooling, covering areas such as the debate on AI's role in creativity. Assignments involved weekly readings, quizzes, and practical lab work, such as implementing the DQN agent or building generative systems. The curriculum also includes specific focus on ethical considerations, particularly in Week 5 and Week 16. The final weeks (21-22) are dedicated to exam preparation and assessment.

---

## 06_Recap_of_week_15_study_Video_1_min

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

## 07_Self-evaluation_checklist_Part_5_-_Putting_it_all_together_and_pop_song_generator_[_Reading_30_min

# Self-evaluation checklist: Part 5 - Putting it all together and pop song generator [
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/2TZ9W/self-evaluation-checklist-part-5-putting-it-all-together-and-pop-song-generator

This document presents a self-evaluation checklist for the course module "Week 14 - Part 5: Putting it all together and Pop Song Generator 1." Its purpose is to provide a structured approach for students to assess their understanding and technical work. The evaluation is divided into three major areas: theoretical understanding, technical system development, and critical evaluation.

Regarding the understanding of creativity theories, students must first demonstrate a clear explanation of the Skinnerian view. This involves detailing how fundamental behaviourist principles are applicable to creative processes. Secondly, students must clearly explain the Dewian view of creativity. This perspective emphasizes the crucial role of experience, reflection, and continuous development in creative output. A vital component of this section is the ability to compare and contrast these two distinct perspectives. Specifically, the differences in how each view understands creativity must be highlighted. To solidify understanding, students are required to provide real-world or historical examples illustrating both the Skinnerian and Dewian views.

The second major section focuses on developing a complete song generating system. This system requires successful implementation of a lyric generation component. Lyric generation must utilize appropriate techniques, which may include AI models or rule-based systems. Additionally, the system must successfully implement a music generation system capable of creating complex melodies and harmonies. A third critical element is the successful implementation of a singing synthesis system. This synthesizer must effectively transform the generated lyrics into a realistic vocal performance. The system then requires integration, combining the lyric, music, and singing components into one cohesive audio file. Furthermore, the final generated song must adhere to a clear, established structure. This structural requirement includes defining elements such as the verse, chorus, and bridge. Finally, rigorous checks and refinements must be performed on the audio mixing. The goal of mixing is ensuring that all elements—lyrics, music, and singing—sound balanced and professional.

The third section addresses the evaluation of creativity, comparing machines and humans. Students must be able to explain different philosophical and theoretical perspectives on this comparison. This requires referencing examples found in academic literature that specifically discuss creativity within AI-generated content. A critical evaluation component involves assessing the strengths and limitations of AI-generated music and lyrics. This assessment must be compared against the qualities of human-created works. Ultimately, students must articulate their own defined position on the matter of AI creativity. This position addresses whether AI systems can be considered genuinely creative or merely functioning as sophisticated imitators.

Finally, the self-reflection section serves as a meta-cognitive check. Students must assess their confidence in achieving all the learning outcomes for the week. Should there be any identified gaps in their understanding, they must pinpoint specific areas requiring review or improvement. The checklist also confirms the student's ability to clearly explain their work and findings to others, whether in written or peer presentation format. This entire checklist structure functions as a complete mechanism for both self-assessment and comprehensive review of all key concepts and technical implementations.

---

## 08_20.113_AI_creativity_case_study_outro_Video_4_min

# 20.113 AI creativity case study outro
Video • 4 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/5gMgz/20-113-ai-creativity-case-study-outro

This comprehensive syllabus covers a diverse progression through AI applications, starting with Week 1-5 focused on game playing AI. The curriculum formalizes reinforcement learning through the development of the Deep Q-Network (DQN) agent and explores various AI tooling for game environments. Weeks 6-10 shift focus to evolving artificial creatures, utilizing genetic algorithms for automatic design. Specific technical details include building robots using simulation environments like pybullet and defining physical structures via URDF files. The evolutionary process is formalized through genetic encoding schemes, defined fitness functions, and selection mechanisms. The subsequent block (Weeks 11-15) delves into generative and collaborative AI systems. This includes generating lyrics with GPT-2 and composing music using advanced models such as MusicVAE and DiffSinger. The technical goal of this section is synthesizing these components into a complete pop song generator. Weeks 16-20 introduce the "Toy Robot Scientist" concept, examining its history, legal, and ethical dimensions. The Robot Scientist framework involves building a complex system centered on knowledge representation and reasoning phases. Crucial components addressed are planning and analysis capabilities within the robotic agent. Throughout the entire course, learning is reinforced through structured activities including weekly reading, discussion prompts, and practice assignments, culminating in exam preparation.

---

