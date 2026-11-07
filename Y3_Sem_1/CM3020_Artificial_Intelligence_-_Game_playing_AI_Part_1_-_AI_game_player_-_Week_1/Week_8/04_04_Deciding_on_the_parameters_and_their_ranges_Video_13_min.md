# 04_Deciding_on_the_parameters_and_their_ranges_Video_13_min

# Deciding on the parameters and their ranges
Video • 13 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/tdTSX/deciding-on-the-parameters-and-their-ranges

The provided transcript segment details a rigorous technical process of **parameterizing and defining the morphology** of an evolving artificial creature or robot. This discussion outlines the requirements for creating a dynamic structure that can be manipulated through a control system.

The course schedule contextually aligns this discussion with **Week 8: Evolving artificial creatures: Part 3 - Genetic encoding scheme**, where the focus is on deciding on parameters and implementing genome-to-graph conversions.

Here is a summary of the key concepts discussed in the transcript:

---

### ⚙️ Morphological Design (Links and Joints)

The creature is built "piece by piece," focusing on the structure of links and joints.

1.  **Incremental Building:** Links are added one at a time. As more links are added, the number of possible connection points increases dynamically (e.g., from 1 option to 2, then 3, and so on).
2.  **Dynamic Parameterization:** To manage this complexity, a dedicated parameter is required for each new link. This parameter dictates *which* of the available connection points the new link will attach to.
3.  **Scaling Requirement:** Crucially, this parameter must be **dynamically scaled** so that it can correctly choose from the entire range of available links as the structure grows.

### 📡 Control System Definition

The system requires specialized **signal generators** to drive the creature's joints. These generators are tied directly to the joints to ensure accurate control.

The control system relies on three primary parameters:

1.  **Waveform:** Determines the signal pattern (must be one of: **Sine, Pulse, or Ramp**).
2.  **Amplitude (0 to 1):** Dictates the speed of the motor. An amplitude of 1 means maximum speed.
3.  **Frequency (0 to 1):** Controls how often the polarity of the motor changes. When the polarity flips (positive $\rightarrow$ negative), the motor reverses direction.

### 📊 Conclusion and Scope

*   **Total Parameters:** The process concludes that a total of **17 parameters** are necessary to completely control and define the morphology of the creatures.
*   **Goal:** The overarching aim is to successfully parameterize the structure (links and joints) and define the input mechanism (the control system) so that the creature's physical shape and movement can be computationally defined.

