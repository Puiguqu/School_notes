# 09_Crash_course_in_knowledge_representation_Video_11_min

# Crash course in knowledge representation
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/hUSYs/crash-course-in-knowledge-representation

Knowledge-based agents require a systematic, machine-processable method to represent and encode knowledge, moving beyond direct encoding in conventional languages like Java or Python. This necessity stems from the fact that the true power of knowledge resides in logical inference and reasoning. To enable logical inference, knowledge must be formalized into a logical structure. Various logical systems exist, including propositional, first order logic (FOL), temporal, and modal logics. Each logic presents a trade-off between expressive power and the complexity of its reasoning problems.

Two specific logics discussed are FOL and Description Logic (DL). DL is notably preferred in certain applications because, unlike some FOL problems, its core reasoning problems are typically decidable, guaranteeing that an inference agent can reach a conclusion. Key knowledge representation languages used for encoding statements within these logics include Prolog and RDF (Resource Description Framework). The aim is to create a knowledge model or knowledge graph that the agent can utilize.

The RDF model represents resources, which are defined as any object uniquely identifiable by a Uniform Resource Identifier (URI). These objects, such as a student or a module, become resources within the model. Resources are connected through properties, which can link them to other resources (relationships) or to simple values like text strings (data properties). Fundamentally, RDF structures knowledge into triplets: Resource X, Property Y, Resource Z, exemplified by (student, raises, query). The logic supporting RDF is Description Logic, enabling reasoners to easily process the models and infer new facts.

To elaborate on RDF structure, the Resource Description Framework Schema (RDFS) is utilized, often leveraging the human-readable Turtle syntax. Classes define categories of resources, and an instance of a class is identified using the predicate `rdf:type`. For example, AI can be defined as a subclass of the general module class. RDFS properties are used to establish the relations and attributes between these defined classes.

A major advantage of knowledge models is their inherent extensibility and ability to integrate with other knowledge models. Integration is achieved by explicitly linking entities defined across different knowledge bases, for instance, linking to a pre-existing ontology like FOAF. These global definitions contrast sharply with local definitions in traditional programming languages. This capability allows the system to combine disparate knowledge, such as linking a university program to events in a specific city.

This architecture enables the development of sophisticated agents, such as those that classify academic versus non-academic queries. Such agents can then advise students on the appropriate contact and monitor the query's progress. Ultimately, knowledge representation allows not only for understanding the domain but also for continuous learning and improving communication processes.

