# Week 9 - CM3020 Artificial Intelligence - Game playing AI: Part 1 - AI game player - Week 1

## 01_Weekly_introduction_Video_1_min

# Weekly introduction
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/s36yC/weekly-introduction

This course is structured around four major areas of advanced artificial intelligence, commencing with Game Playing AI (Weeks 1-5), which covers reinforcement learning and formalizing the DQN agent. This initial phase progresses through tooling, implementation of the DQN agent, and concludes with an ethical review of AI game players (Week 5). Next, the focus shifts to Evolving Artificial Creatures (Weeks 6-10), detailing automatic design via genetic algorithms (GA). Technical aspects include building robots using pybullet and URDF files, establishing genetic encoding schemes, and defining fitness functions for selection.

The curriculum then transitions to Generative and Collaborative AI (Weeks 11-15), exploring systems like GPT-2 for lyric generation and MusicVAE and DiffSinger for music composition. This culminates in integrating these models into a comprehensive pop song generator. A third major block, Weeks 16-20, introduces the concept of a Toy Robot Scientist, examining its history, legal issues, and the technical process of system building. This segment details knowledge representation, the reasoning phase, and planning analysis.

The course includes several practical assignments, quizzes, and culminates in a Mid-term coursework submission and a final exam (Weeks 21-22). Throughout the material, specific technical concepts such as DQN, genetic encoding, pybullet, URDF, GPT-2, MusicVAE, and DiffSinger are highlighted as core learning objectives. These technical deep dives ensure preservation of detailed conceptual knowledge across all modules.

---

## 02_Slides_for_week_9_Reading_30_min

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

## 03_Lesson_introduction_fitness_and_simulation_Reading_10_min

# Lesson introduction: fitness and simulation
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/sK3WN/lesson-introduction-fitness-and-simulation

In this lesson we are going to work on the offline simulation and fitness function. These will allow us to run creatures at high speed offline and to evaluate their performance. Lesson introduction: fitness and simulation In this lesson we are going to work on the offline simulation and fitness function. These will allow us to run creatures at high speed offline and to evaluate their performance. Mark as completed Dislike Report an issue

---

## 04_Evaluating_creatures_the_plan_Video_4_min

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

## 05_Generating_a_random_population_Video_6_min

# Generating a random population
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/4eAKV/generating-a-random-population

This module provides a comprehensive exploration of advanced Artificial Intelligence, structured through four major thematic pillars.

The curriculum begins with the field of Game Playing AI (Weeks 1-5), focusing initially on foundational concepts. Week 2 formalizes reinforcement learning by introducing the Deep Q-Network (DQN) agent, while Week 4 details the specific implementation of this DQN agent. The module also covers AI tooling in Week 3 and concludes this initial phase by addressing the state-of-the-art and ethical considerations in AI game players (Week 5).

Next, the focus shifts to Evolving Artificial Creatures, centered on autonomous design via Genetic Algorithms (GA) (Weeks 6-9). This evolution project begins by detailing automatic design techniques and setting up physical simulation environments using pybullet and defining robot structures via URDF files. A crucial aspect is the implementation of the genetic encoding scheme, followed by developing a robust fitness function. The GA process involves critical management techniques, including generating a random population, utilizing roulette wheel selection, and performing crossover operations. These components enable population management and convergence toward more fit individuals.

The third pillar explores Generative and Collaborative AI (Weeks 10-15), moving from morphology to creativity. Week 10 covers the state of the art in evolving morphology. Subsequently, the module delves into generative systems, learning how to generate content like lyrics using GPT-2. Technical deep dives include exploring MusicVAE for music composition and utilizing DiffSinger. The phase culminates in integrating these systems to create a complete pop song generator.

Finally, the module shifts to practical, reasoning systems with the "A toy Robot Scientist" project (Weeks 16-20). This section addresses the history, legal, and ethical perspectives of robotic systems. Key topics include knowledge representation, building the system, and implementing the robot's reasoning phase. The latter stages involve tackling planning and analyzing complex scenarios, culminating in an assessment of state-of-the-art Robot Scientist projects. Weeks 21 and 22 are dedicated to comprehensive exam preparation and the final assessment.

---

## 06_Running_creatures_in_simulation_Video_22_min

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

## 07_Implement_the_fitness_function_Video_15_min

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

## 08_Multi-process_evaluation_Video_18_min

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

## 09_Code_the_simulation_and_fitness_function_Reading_10_min

# Code the simulation and fitness function
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/y0lCE/code-the-simulation-and-fitness-function

This lab assignment requires coding the simulation and fitness function, utilizing the provided technical resources: the lab worksheet `41110_simulation_v2.pdf` and the starting code contained within the `wk4_start` ZIP File.

---

## 10_Code_from_end_of_lesson_Reading_10_min

# Code from end of lesson
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/nacBL/code-from-end-of-lesson

Please find below the code after the previous worksheet. Note that it includes a no-threads version of the test_simulation code which works on Windows, M1 macs etc. wk4_after_41110_v3 ZIP File Code from end of lesson Please find below the code after the previous worksheet. Note that it includes a no-threads version of the test_simulation code which works on Windows, M1 macs etc. wk4_after_41110_v3 ZIP File Mark as completed Dislike Report an issue

---

## 11_Planning_selection_and_breeding_Video_6_min

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

## 12_Roulette_wheel_selection_Video_10_min

# Roulette wheel selection
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/YFTGX/roulette-wheel-selection

The discussion centers on implementing the Roulette Wheel selection process, a core mechanism for parent selection within a Genetic Algorithm (GA). The overall goal is twofold: generating a fitness map from evaluated individuals and subsequently using this map to select parents.

The concept of a fitness map involves calculating a cumulative sum based on the fitness values of the individuals. For example, given creatures with fitnesses 2.5, 1.2, and 3.4, the fitness map is generated by iteratively accumulating these values. The

---

## 13_Crossover_Video_18_min

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

## 14_Evolution!_Video_15_min

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

## 15_Tweak_the_GA_Video_6_min

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

## 16_Saving_and_viewing_fittest_Video_18_min

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

## 17_Demo_some_fit_individuals_Video_8_min

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

## 18_Implement_the_GA_Reading_30_min

# Implement the GA
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/rETo9/implement-the-ga

This curriculum outlines a comprehensive 22-week program focusing on advanced topics in Artificial Intelligence, moving through game playing, evolutionary computation, generative AI, and robotics. The course begins with the foundational concepts of Game playing AI, covering topics from basic AI game players in Week 1 to formalizing reinforcement learning. Weeks 2 through 4 specifically delve into the Deep Q-Network (DQN) agent, providing a detailed implementation of the DQN agent for game playing AI. Week 5 expands the discussion by addressing the state of the art and critical ethics associated with AI game players.

The curriculum shifts significantly in Week 6, introducing the concept of Evolving Artificial Creatures, starting with automatic design using genetic algorithms. Weeks 7 and 8 transition into applied robotics, focusing on building robots utilizing pybullet and URDF files. Week 9 is dedicated to the core mechanics of Genetic Algorithms (GA), covering the genetic encoding scheme and the crucial definition of the fitness function.

The detailed lessons in the GA section cover robust simulation and evaluation methodologies, including multi-process evaluation for fitness function implementation. Population management is a key technical area, detailed through the implementation of selection techniques, such as Roulette Wheel selection. Furthermore, the process includes teaching genetic operators like Crossover and guiding students through the complete evolutionary cycle. Practical implementation culminates in the module "Implement the GA," referencing a specific lab worksheet for detailed application.

Following the focus on evolutionary computation, Weeks 11 through 15 introduce Generative and Collaborative AI. The focus begins with general generative systems in Week 11 and progresses to specific applications, such as generating lyrics using GPT-2. Further technical dives include music composition via MusicVAE and the utilization of DiffSinger. The module culminates in Week 15 with a comprehensive project on creating a pop song generator, integrating these diverse systems.

The final major phase, Weeks 16 through 20, is dedicated to "A toy Robot Scientist." This section covers the historical perspectives, legal, and ethical issues surrounding AI in robotics. The technical instruction emphasizes system building and robust knowledge representation. The curriculum then focuses on the reasoning phase of the Robot Scientist, covering planning and advanced analytical procedures. The program concludes in Week 21 with dedicated exam preparation, followed by the final exam in Week 22. The overall structure involves continuous assessment through quizzes, practice assignments, and hands-on implementation coding.

---

## 19_GA_solution_code_Reading_10_min

# GA solution code
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/rICMI/ga-solution-code

This comprehensive module curriculum spans various advanced topics in Artificial Intelligence, beginning with AI for game playing. The initial phase introduces Game playing AI, progressing from a basic AI game player in Week 1 to formalizing reinforcement learning in Week 2. Week 3 focuses on general AI game playing tooling, leading into the crucial implementation of the Deep Q-Network (DQN) agent in Week 4. Week 5 examines the state of the art and the ethical considerations surrounding AI game players.

The curriculum then shifts focus to the concept of evolving artificial creatures, beginning in Week 6 with automatic design utilizing genetic algorithms (GA). Weeks 7 and 8 delve into practical robotics, covering the building of robots using tools like pybullet and defining structures via URDF files. Week 9 is dedicated to the implementation and rigorous testing of the GA.

The technical instruction for Week 9 starts with defining the fitness function and simulation mechanics. Students learn to evaluate creatures and implement the fitness function, often utilizing multi-process evaluation for efficiency. Following this, the module addresses population management, concentrating on selection and breeding strategies. Specific technical mechanisms like roulette wheel selection, crossover, and the general evolution process are studied. Several exercises emphasize tweaking the GA and saving/viewing the fittest individuals.

The subsequent weeks introduce modern generative and collaborative AI systems. Week 10 covers the state of the art in evolving morphology, providing a transition into generative systems. Week 11 introduces generative systems, while Week 12 focuses on generating lyrical content using the GPT-2 model. Week 13 explores music composition via MusicVAE, followed by an examination of DiffSinger in Week 14. Week 15 synthesizes these concepts into a comprehensive pop song generator project.

The final major segment explores practical applications through "A toy Robot Scientist" project, starting in Week 16 by discussing introduction, history, perspectives, and legal/ethical issues. Weeks 17 through 20 build the system, addressing knowledge representation, the robot scientist reasoning phase, and planning/analysis. Week 20 concludes this segment by reviewing state-of-the-art Robot Scientist projects. The module concludes with Week 21 dedicated to exam preparation and Week 22 being the exam week. The materials include solutions code for the completed GA code.

---

## 20_Recap_of_week_9_study_Video_2_min

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

## 21_Self-evaluation_checklist_Fitness_function_and_selection_Reading_30_min

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

