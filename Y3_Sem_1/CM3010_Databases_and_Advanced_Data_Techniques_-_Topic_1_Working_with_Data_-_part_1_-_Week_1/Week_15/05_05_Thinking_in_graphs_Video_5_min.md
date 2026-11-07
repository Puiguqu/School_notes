# 05_Thinking_in_graphs_Video_5_min

# Thinking in graphs
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/WeWqh/thinking-in-graphs

The discussion centers on the nature and complexity of working with graphs and graph diagrams in modeling abstract concepts. Some individuals find this abstract modeling liberating, while others find it intimidating due to its lack of concrete structure. Modeling begins by selecting a point in a semantic space, which is typically marked with a circle and a name. Initial simple relationships, such as "Film has cast member actor," are often oversimplified for complex real-world data. For instance, merely attaching a role to an actor's URI only provides a list of roles without connecting them to the specific film. A more complex structure is required, such as "Film has a role which is a character" and "That character is played by an actor." Furthermore, complex systems require even greater intricacy, such as differentiating between a young and an old version of the same character. A general rule advises utilizing existing structures developed by others, provided they are adopted critically.

Graphs differ fundamentally from structures like JSON and XML, which inherently possess a hierarchical tree structure. Crucially, graphs lack an inherent, fixed order. This lack of order is especially important in a web environment where graph components may arrive unpredictably from different servers or URLs. In graph theory, any combination of a circle, an arrow, and another circle constitutes exactly one triple. Once a graph is drawn, it can be easily translated into RDF serialization, which effectively stores all data. Extracting data involves counting the cycles and areas within the finalized graph structure.

Beyond the graph concept, the course structure details a comprehensive exploration of database models. Topics progress from Week 1 (Working with Data - part 1) through Week 6 (Reliable databases: Data Integrity and Security - part 2). This leads into Week 11 and Week 12, which focus on Distributed databases and alternative database models. A major shift occurs in Weeks 13 through 15, dedicated to Semantic databases and Linked Data.

Specifically, Section 8.0 introduces Linked Data and the Semantic Web, referencing Tim Berners-Lee's foundational proposal. Section 8.1 focuses on RDF, detailing the model and its various serializations, reinforced by activities like "Thinking in graphs." Finally, Section 8.2 delves into Semantics in Linked Data via Web ontologies. This area includes practical assignments on choosing, designing, and drawing ontologies, demonstrating the technical application of semantic web concepts.

