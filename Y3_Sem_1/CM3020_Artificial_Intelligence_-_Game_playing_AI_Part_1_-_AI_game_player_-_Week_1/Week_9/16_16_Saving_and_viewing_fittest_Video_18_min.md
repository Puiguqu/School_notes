# 16_Saving_and_viewing_fittest_Video_18_min

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

