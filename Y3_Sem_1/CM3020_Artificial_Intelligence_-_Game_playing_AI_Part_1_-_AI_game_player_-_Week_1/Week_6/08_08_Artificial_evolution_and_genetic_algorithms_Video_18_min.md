# 08_Artificial_evolution_and_genetic_algorithms_Video_18_min

# Artificial evolution and genetic algorithms
Video • 18 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/z558P/artificial-evolution-and-genetic-algorithms

This transcript provides a detailed explanation of **Genetic Algorithms (GAs)**, a computational technique inspired by natural evolution.

Here is a structured summary of the core concepts, mechanisms, and the overall process described in the video.

---

## 🧬 Summary of Genetic Algorithms (GAs)

### I. What is a Genetic Algorithm?
A Genetic Algorithm is an optimization technique designed to search through highly complex problem spaces to find efficient or optimal solutions. It works by simulating the process of natural selection, breeding, and mutation.

*   **Credit:** The seminal work on GAs is credited to **John Holland**.
*   **Goal:** To iteratively improve a *population* of potential solutions (genomes) until a highly "fit" solution is found.

### II. The Core Mechanisms (The Two Steps)

The process of generating a new generation relies on two primary genetic operations: Crossover and Mutation.

#### 1. Crossover (Breeding)
Crossover mimics sexual reproduction by combining the genetic material of two "parent" genomes to create a new "child" genotype.

*   **How it works:** The algorithm takes a piece of the genome from one parent and combines it with a piece of the genome from the other parent.
*   **Types:**
    *   **Single-Point Crossover:** A break point is selected (usually randomly) to swap a segment of the two parents.
    *   **Multipoint Crossover:** Multiple break points are selected for complex combinations.
*   **Note on Selection:** The speaker emphasizes that the initial selection pressure (choosing the fittest parents) is applied once; reapplying fitness logic during crossover is usually redundant and simplifies the algorithm if a random point is chosen.
*   **Result:** A new genotype that is a hybrid combination of the two parents.

#### 2. Mutation
Mutation introduces small, random changes to the newly created offspring, ensuring the population doesn't become stagnant.

*   **How it works:** Random points along the new genome are chosen, and the bits at those locations are flipped or changed.
*   **Goal:** To introduce slight, beneficial variation into the population, preventing the algorithm from getting stuck in a sub-optimal solution.

### III. The Iterative Genetic Algorithm Cycle

The Genetic Algorithm is not a single step; it is an ongoing loop that continues until the solutions meet a predefined level of fitness.

1.  **Encoding:** The initial problem is expressed in a standardized format (e.g., a string of bits or numbers, which is the **genotype**).
2.  **Evaluation (Fitness):** Each genome in the population is run, tested, and given a score or measure of how good it is (its **fitness**).
3.  **Selection (The Roulette Wheel):** Parents are selected from the population based on their fitness score (fitter individuals have a higher chance of being chosen).
4.  **Reproduction:** Selected parents undergo **Crossover** to produce offspring.
5.  **Variation:** The offspring undergo **Mutation** to introduce random genetic changes.
6.  **New Generation:** The new, mutated population replaces the old one.
7.  **Repeat:** Steps 2 through 6 are repeated continuously until the population converges on a highly fit solution.

### IV. Why Does It Work? (The Theoretical Basis)

The power of the GA lies in its ability to manage a large population and combine information from successful members:

*   **Population Size:** Unlike simple methods like **Hill Climbing** (which only focuses on finding the single best next step), GAs maintain an entire population, allowing them to explore multiple areas of the search space simultaneously.
*   **The Schema Theorem:** John Holland’s theory explains why this complex, seemingly "weird" process works—it allows the algorithm to efficiently search highly complicated solution spaces and find good solutions that other algorithms might miss.

