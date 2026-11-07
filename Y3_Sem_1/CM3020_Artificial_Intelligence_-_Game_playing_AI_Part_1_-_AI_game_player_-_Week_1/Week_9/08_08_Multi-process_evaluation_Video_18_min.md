# 08_Multi-process_evaluation_Video_18_min

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

