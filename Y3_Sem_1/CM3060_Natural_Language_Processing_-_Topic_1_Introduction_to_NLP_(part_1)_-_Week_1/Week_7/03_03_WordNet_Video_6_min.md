# 03_WordNet_Video_6_min

# WordNet
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Rr7NY/wordnet

This summary focuses exclusively on the technical concepts and findings presented in the transcript, adhering to the 25-sentence limit while preserving all core information.

1. The discussion introduces WordNet, a lexical resource, utilizing it within a Jupyter Notebook environment by importing it as `WN` from `nltk.corpus`.
2. A fundamental concept in WordNet is the synset, which conceptually groups words into sets of synonyms.
3. Accessing these groups is performed by calling the method `WN.synsets` on a given term, such as "motorcar."
4. The result for "motorcar" is an indexed synset, exemplified by `car.n.01`, signifying the primary noun sense of the word "car."
5. In contrast, the term "spell" is shown to be far more complex, possessing numerous synsets (approximately 10 or 11), illustrating semantic ambiguity.
6. Drilling into a specific synset, like `car.n.01`, reveals its members—five synonyms in this case—which collectively form that synset.
7. WordNet is noted not to be indexed on individual terms, but rather on abstract concepts.
8. This abstract concept can be explicitly defined using a definition method, such as the definition for `car.n.01` ("a motor vehicle four wheels, usually propelled by an internal combustion engine").
9. The set of all individual members belonging to a synset are referred to as its lemmas.
10. Lemmas represent a linguistically principled process, similar to lemmatization, reducing various tokens to a common root.
11. The demonstration of "car" highlights that multiple senses correspond to multiple synsets; for example, five different synsets exist for the word "car."
12. By iterating through these senses, the transcript shows distinct meanings, including "wheeled vehicle," "railway car," "gondola," "elevator car," and "cable car."
13. The text then shifts focus to traversing the hierarchy within WordNet, exploring hyponyms (child terms) and hypernyms (parent terms).
14. By instantiating `motorcar` with the `car.n.01` sense, the hyponyms for that synset (`types_of_motorcar`) can be retrieved.
15. Conversely, retrieving the hypernym allows the user to move upward from the synset to its parent term.
16. The concept of polyhierarchy is introduced, explaining that a single concept can be defined in multiple ways, thus having multiple parents.
17. This complexity is demonstrated by using the `hypernym_paths` method, which reveals two distinct lineage paths for "motorcar."
18. The first parent path runs from `car.n.01` up through "wheeled vehicle" and "container."
19. The second parent path from "car" follows a different lineage, passing through "conveyance vehicle" before reaching the common parent "entity."
20. This illustrates that different ancestral paths lead up to a shared root node.
21. Key concepts introduced include the hierarchy of WordNet, the crucial role of synsets as conceptual representations, and the methods for navigating this structure.
22. The process of walking up and down the hierarchy enables the discovery of parent and child relationships within the lexicon.
23. The provided course outline shows that WordNet usage culminates in calculating semantic similarity in subsequent modules.
24. Further learning paths involve topics like Basic text processing, Language modelling, and Lexical semantics.
25. These tools provide the foundational knowledge necessary for advanced NLP tasks, such as Text categorisation and Information extraction.

