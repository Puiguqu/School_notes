# 02_Slides_for_week_9_Reading_30_min

# Slides for week 9
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/XNKII/slides-for-week-9

This curriculum outlines a comprehensive study of advanced Artificial Intelligence, progressing from game-playing agents to complex generative and robotic systems.

The foundational module covered initial topics like Game Playing AI, detailing the formalization of Reinforcement Learning and the deployment of the Deep Q-Network (DQN) agent. This early phase also introduced AI game player tooling and focused on the implementation of the DQN agent itself. Subsequently, the course transitioned to evolving artificial creatures, initiating discussions on automatic design through genetic algorithms (GA). Technical foundations were laid by building robots using environments like PyBullet and defining their structure via URDF files. The scheme for genetic encoding, which dictates how traits are represented, was covered in preparation for the core optimization phase.

Week 9 specifically focuses on the crucial concepts of the fitness function and selection within the GA framework. The process begins with generating a random initial population of artificial creatures. These creatures are then subjected to simulation, a critical step that requires implementing the fitness function to evaluate their performance. To maintain computational efficiency, the simulation and fitness function evaluation utilize a multi-process architecture. The next major stage is population management and the planning of selection and breeding cycles.

Specific selection algorithms detailed include Roulette Wheel selection, which guides the preferential selection of high-performing individuals. Reproduction is achieved through crossover, a genetic mechanism that combines traits from successful parents to generate offspring. The overall process is cyclical, allowing for the tweaking of GA parameters to optimize evolutionary outcomes. The ultimate goal of this phase is the successful implementation of the GA, culminating in the ability to save and view the fittest individuals in CSV format.

Following this deep dive into evolution, the course expands its focus to different AI modalities. Week 10 addresses the advanced topic of state of the art in evolving morphology. The curriculum then moves into Generative and Collaborative AI, beginning with an introduction to generative systems. Technical examples include generating lyrics using GPT-2 and composing music utilizing models like MusicVAE and DiffSinger. These generative techniques are integrated by the end of the module into a functional pop song generator.

The final major component is dedicated to "A Toy Robot Scientist." This segment is highly technical, focusing on the initial introduction, history, and the legal and ethical implications surrounding such systems. The robot scientist system is built incrementally, starting with knowledge representation and advancing to the system's reasoning phase. Subsequent weeks detail the robot scientist’s planning and analytical capabilities, concluding with an analysis of state-of-the-art robot scientist projects. The final weeks are reserved for comprehensive exam preparation and review.

