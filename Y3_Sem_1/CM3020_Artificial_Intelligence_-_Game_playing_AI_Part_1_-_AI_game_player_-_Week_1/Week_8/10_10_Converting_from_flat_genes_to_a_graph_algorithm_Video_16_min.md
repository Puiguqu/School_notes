# 10_Converting_from_flat_genes_to_a_graph_algorithm_Video_16_min

# Converting from flat genes to a graph: algorithm
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/mw91n/converting-from-flat-genes-to-a-graph-algorithm

This transcript details a critical stage in the process of **designing and generating robotic/creature morphologies** using genetic algorithms. The core focus is on converting a simple, abstract genetic description (the "genome" or "flat gene structure") into a fully articulated, physically defined structure (the "expanded graph" and subsequently, a URDF file).

Here is a detailed breakdown of the concepts and processes discussed:

---

### 🧬 1. The Problem: Genome to Graph Conversion
The starting point is a **flat gene structure** (the genome), which describes the parts of a creature or robot but does not explicitly define the hierarchical connections or repeat structures. The goal is to expand this flat structure into a complete, recursive **expanded graph structure** that accurately models the complexity and repetition found in nature.

### ♻️ 2. The Algorithm: Recursive Expansion (`phase2`)
The process relies on a recursive function (labeled `phase2`) to "dig into" the gene structure and ensure every component is mapped and recorded.

*   **Input:** A parent node (e.g., 'a').
*   **Process:**
    1.  Get the immediate **children** of the parent (e.g., 'b').
    2.  Count the **number of recurrences** for these children.
    3.  For each occurrence, the child is added to the `expanded links` array.
    4.  The function then **recursively calls itself** on the child node (e.g., calling `phase2` on 'b' to find its children, 'c').
*   **Output:** The `expanded links` array accumulates every single node, correctly accounting for repetitions and branches.
*   **Result Example:** A simple structure that might have `a -> b` and `b -> c` might be expanded to include multiple entries like `a, a b, a c, a d, a c, a d`, fully mapping the branching pathways.

### ⚙️ 3. The Final Conversion: Expanded Graph to URDF/XML
Once the `expanded links` array is complete, the next step is translating this abstract, expanded graph description into a physical file format that robotics simulation environments (like PyBullet) can understand.

*   **URDF (Unified Robot Description Format):** This XML-based standard is used to describe the structure, geometry, and kinematic properties of robots.
*   **The Mapping:**
    *   Every item in the `expanded links` array converts into a **`link tag`** (a physical component, like a leg segment or arm bone).
    *   For every link, a **`joint tag`** must be created. This tag dictates the parent-child relationship, defining how that specific link connects to its parent (a relationship already determined in Phase 1).

### ➡️ Summary of the Workflow
1.  **Genome/Flat Gene:** (Initial genetic code input) $\rightarrow$
2.  **Phase 1:** (Determining Parent/Child relationships) $\rightarrow$
3.  **Phase 2 (Recursive Algorithm):** (Expanding the structure into the `expanded links` array) $\rightarrow$
4.  **URDF/XML Generation:** (Converting the expanded links into functional, physical robot definitions).

---
### 📚 Course Context
The transcript aligns perfectly with **Week 8: Evolving artificial creatures: Part 3 - Genetic encoding scheme**, focusing specifically on the lessons related to:
*   `Converting from flat genes to a graph: algorithm`
*   `Implement the genome->graph code`
*   `Implement the genome to XML code`

