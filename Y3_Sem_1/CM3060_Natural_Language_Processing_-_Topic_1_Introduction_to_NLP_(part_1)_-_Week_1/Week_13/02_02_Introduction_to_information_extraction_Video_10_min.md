# 02_Introduction_to_information_extraction_Video_10_min

# Introduction to information extraction
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/RNy0B/introduction-to-information-extraction

Information Extraction (IE) is a fundamental concept in NLP concerned with converting unstructured natural language data, which possesses implicit structure, into explicitly structured data. This process is essentially a transformation, taking raw input strings and aiming to output formalized database entries. Practically, IE allows the construction of applications designed to extract specific semantic content, such as the who, what, when, and where from text. A basic, formulaic example is the automated markup of text, where algorithms identify patterns like dates, phone numbers, and URLs. This simple extraction provides value by enabling interactive features, such as linking a date to a calendar application. More complex applications include building systems that summarize vast amounts of business news, or curating massive scholarly literature to find subtle, valuable relations.

IE involves several distinct subtasks that address the complexity of extracting meaning. The first is Named Entity Recognition (NER), which identifies proper nouns and objects—like people, places, or companies—and resolves them to unique canonical database identifiers. Next is Relation Extraction, which determines how the identified entities relate to one another. For instance, it identifies if "Person A is employed by Organization B" or "Organization B is based in Location C."

Building upon this, Event Extraction identifies specific episodes or events in which those entities participate, which helps construct a coherent timeline. Event Coreference is necessary because linguistic devices often refer back to events using pronouns, and this task resolves these indirect mentions to a unique event instance. Finally, Temporal Event Expression Extraction addresses the "when" by identifying and resolving various expressions of dates, times, and durations related to the events.

The definition of these relations is not universal; it depends heavily on the problem being solved. One example is the ACE evaluation exercise, which proposes a taxonomy of six top-level categories, including "business/lasting personal," "part-whole relations," and "organization affiliation relations," tailored for Newswire reporting. In contrast, the Unified Medical Language System (UMLS) is highly specialized for medicine, dealing with concepts like bodily locations and injuries. Other systems include DBpedia, which systematizes knowledge derived from Wikipedia infoboxes, and WordNet, which defines relations based on hyponym ("is-a") and instance relationships. Ultimately, researchers often employ bespoke systems of relations created specifically to solve a targeted, problem-centric task.

