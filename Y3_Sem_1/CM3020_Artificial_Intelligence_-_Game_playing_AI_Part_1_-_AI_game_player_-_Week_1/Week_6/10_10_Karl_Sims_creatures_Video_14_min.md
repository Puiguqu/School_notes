# 10_Karl_Sims_creatures_Video_14_min

# Karl Sims creatures
Video • 14 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/vtByj/karl-sims-creatures

This transcript provides a detailed overview of Karl Sims' seminal 1994 paper, which demonstrates the use of a **Genetic Algorithm** to evolve complex, functioning artificial creatures (morphology and control) within a virtual environment.

Here is a structured summary of the key concepts, methodology, and findings:

---

### 🧬 I. Core Concept and Methodology

*   **Goal:** To evolve morphologies (physical structures) and control systems for virtual creatures by optimizing them against specific fitness tasks.
*   **Approach:** Evolutionary Computation using a Genetic Algorithm.
*   **Simulation Environment:** A dynamic simulation within a virtual three-dimensional world, calculating the movement of creatures based on physical interactions.
*   **Computational Power:** Due to the complexity (population size of 300, complex physics), the simulation was run on a high-performance computing cluster, specifically a **Connection Machine CM-5**, which was a state-of-the-art parallel processor in 1993/1994.

### 🤖 II. Genetic Encoding and Reproduction

Sims encoded both the physical form and the control mechanism as graphs:

1.  **Morphology Encoding:** The creature's body structure was encoded using **directed graph genotypes**.
2.  **Control Encoding:** The creature's neural network or control logic was also represented using a **directed graph**.
3.  **Reproduction:** Offspring were generated from surviving creatures via a process of **copying and combining** the parents' directed graph genotypes (mashing the graphs together).
4.  **Variation (Mutation):** Before offspring were finalized, they underwent **probabilistic variation and mutation**. This involved changes to the graphs, such as increasing recursion or adding new connections between parts.

### 🎯 III. Fitness Functions (Tasks and Selection)

The creatures were optimized for specific tasks, defined by fitness functions:

*   **Task Variations:** Early tasks included swimming toward a light (requiring an added sensor) and competitive behaviors.
*   **Implemented Fitness (Basic):** The primary measure implemented was the **walking fitness measure**—quantifying how far the creature could travel within a given amount of time. This directly measured the efficiency of locomotion.

### 🚀 IV. Results and Conclusion

The evolutionary process yielded surprisingly complex and functional outcomes:

*   **Successful Locomotion:** The creatures evolved not just simple forms, but functional gaits.
*   **Surprising Movement:** The fitness function produced "a surprising number of simple creatures that could shuffle or hobble along at fairly high speeds."
*   **Observed Gaits:** These included lizard-like movements using the corners of their body parts, simply wagging appendages, and rocking back and forth in a manner that propelled them forward.
*   **Significance:** The work is presented as a "classic example of a genetic algorithm being used to evolve forms," demonstrating how computation can drive the creation of functional, novel biological-like morphologies.

