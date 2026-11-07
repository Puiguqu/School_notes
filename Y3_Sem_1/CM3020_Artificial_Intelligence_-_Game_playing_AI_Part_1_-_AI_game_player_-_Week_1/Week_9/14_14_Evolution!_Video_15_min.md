# 14_Evolution!_Video_15_min

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

