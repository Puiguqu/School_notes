# 06_Dependency_parsing_in_practice_Video_5_min

# Dependency parsing in practice
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/R82VA/dependency-parsing-in-practice

This text provides a detailed comparative analysis of two software libraries, NLTK and spaCy, used for performing dependency parsing in Natural Language Processing (NLP). The core demonstration revolves around analyzing the sentence: "I shot an elephant in my pajamas."

The process begins by exploring dependency parsing, which operates similarly to context-free grammar (CFG) formalism but focuses on directional relationships between words. Using NLTK, a dependency grammar is instantiated, mirroring a process used for CFGs, starting from a defined string. This process results in a projective dependency parser application. When applied to the sample sentence, the parser produces parse trees that illustrate a crucial finding: prepositional phrase attachment ambiguity.

This ambiguity shows two interpretations: one where "the elephant is in the pajamas," represented by a deeply nested cascade bracketing structure. The second interpretation shows that the "in my pajamas" relation attaches to the subject ("I") rather than the direct object ("elephant"). This demonstrates that dependency relations effectively represent the same ambiguity present in constituency structures.

A similar analysis is performed using spaCy, another widely recognized NLP toolkit. To execute spaCy, the library requires downloading and loading a specific model, namely `en_core_web_assembly`, which creates an active NLP object. This object is then applied to the sentence to yield structured results within a document object.

SpaCy’s output is presented by iterating through the tokens, displaying the text, the token's dependency label, and a corresponding explanation. For example, "I" is labeled as the nominal subject, and "shot" is identified as the sentence root. Tokens like "an" (determiner), "elephant" (direct object), "in" (preposition), "my" (possessive/possession modifier), and "pajamas" (propositional object) are precisely categorized.

While the first view shows the token and its dependency label, the second view focuses on structural relationships. The system allows for visualizing ancestors, such as the ancestor of "I" being "shot" (though the root "shot" has no ancestor). Conversely, it can show children, detailing the terms linked to each head word.

Finally, the text explores a composite structure visualization called the subtree for each term. This subtree representation illustrates the full dependency structure radiating from a specific word. For instance, the subtree for "elephant" maps onto itself, showing its connections to "an," "in," and "my pajamas." These practical examples in NLTK and spaCy highlight how dependency parsing provides useful, informative, and accurate insights into direct word relations within a sentence structure.

