# 02_MMM_modelling_Video_29_min

# MMM modelling
Video • 29 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/oreUL/mmm-modelling

This transcript provides a detailed lecture on **information modeling for cultural heritage**, specifically focusing on how to represent the complex relationships between creative works, their different versions, and their physical manifestations (like manuscripts or prints).

The discussion moves from high-level conceptual models (inspired by FRBR and adapted for CIDOC CRM) to the practical challenges of implementing these models in a database environment.

Here is a summary of the key concepts:

---

### 1. The Conceptual Hierarchy: Work, Expression, and Manifestation

The lecture establishes a strict hierarchy to categorize artifacts, ensuring that abstract concepts are clearly separated from physical objects:

*   **Work (Abstract Concept):** The underlying, original intellectual creation (e.g., the abstract concept of "Psalm 150," or Beethoven's overall composition).
*   **Expression (Version):** A specific realization or transformation of the work (e.g., the Hebrew version of Psalm 150, or the specific piano duet arrangement).
*   **Manifestation (Physical Item):** The actual, tangible object that embodies the expression (e.g., a specific printed edition, or a unique manuscript).
*   **Singleton:** In the manuscript case, this refers to the unique, singular physical object.

**Key Principle:** The *Work* is realized in an *Expression*, and the *Expression* is embodied in an *actual physical thing* (*Manifestation*).

### 2. Adapting the Model for Events (CIDOC CRM)

The standard FRBR model is adapted using **CIDOC CRM (Conceptual Reference Model)** because it is strongly focused on **events**. In this model, actions are not just static links but explicit *acts of creation* that require tracking:

*   **Agent Tracking:** The model must track *who* performed an act (e.g., "Beethoven made this arrangement," so the agent can be assigned to the creation event).
*   **Event Tracking:** This allows the system to say *when* and *by whom* an expression was turned into a specific manuscript.

### 3. The Core Modeling Challenge: Ownership and Custody

The most complex part of the lecture is addressing the challenges of modeling **provenance and ownership**, using examples from manuscript studies and the Schoenberg database.

*   **The Need for Richness:** Simple models fail because they cannot distinguish between different types of ownership:
    1.  **Collection Ownership:** A manuscript might be part of a large, long-standing **family library** (e.g., the Cecil family), where ownership is diffused over centuries, but the specific acquisition/disposal dates are unknown.
    2.  **Transaction Ownership:** The item may have gone through a clear, documented **sale or transfer of custody** (e.g., a recorded sale in the Schoenberg database).

*   **The Modeling Solution:** To avoid damaging the fidelity of the information, the final model must be **rich** rather than strictly simple.
    *   It must allow for multiple, sometimes overlapping, ways of saying the same information.
    *   For example, the system must be able to record a resource as being *part of a collection* (a general statement) while also maintaining specific *transaction triples* (a detailed event record).

### 4. Conclusion: Fidelity vs. Simplicity

The lecture concludes that while this **rich model** makes data retrieval and querying significantly more complicated, it is a necessary trade-off to preserve the nuances, subtle differences, and complete information integrity found in the source records.

---

### 📚 Context within the Course Material

The supplementary course material confirms that this lecture is part of a larger module dedicated to **Semantic Databases and Linked Data**.

*   **The goal of the project (MMM modelling)** is to move beyond traditional relational tables (RDBMS) to create a semantic, knowledge-graph-based model (like the one discussed in the transcript) capable of handling complex, non-uniform data relationships inherent in cultural heritage.
*   **"Mapping manuscript migrations"** is the practical exercise derived directly from the conceptual problems raised in the lecture—tracking the movement and change of custody (manifestations) over time.

