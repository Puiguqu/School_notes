# 11_Constructing_the_toy_knowledge_model_Video_19_min

# Constructing the toy knowledge model
Video • 19 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/5sn6z/constructing-the-toy-knowledge-model

The mini-lecture focuses on building a knowledge agent within a domain of drug design by encoding conceptual knowledge models into a machine-processable format. This process utilizes the specialized tool Protege, which was developed at Stanford University and is designed to enforce a clean logical structure. The resulting knowledge model is stored in RDF (Resource Description Framework) format because this syntax is highly readable for humans. Within Protege, the knowledge model is structured as a tree-like hierarchy composed of nodes, which are either classes or individuals. Classes represent generic types, such as the root node "thing," while individuals represent concrete instances of these classes.

The process involves defining a hierarchy, starting with classes like "Chemical Entity," and then branching out into more specific types such as "Drug" and "Toxin." Instances, like the specific compound Morphine, are then added as concrete individuals under their relevant classes. To link these nodes, two types of properties are used: object properties

