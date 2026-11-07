# 04_Evaluating_creatures_the_plan_Video_4_min

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

