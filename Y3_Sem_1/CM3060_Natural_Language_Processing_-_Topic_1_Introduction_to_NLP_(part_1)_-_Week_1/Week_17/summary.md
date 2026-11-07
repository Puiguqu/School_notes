# Week 17 - CM3060 Natural Language Processing - Topic 1: Introduction to NLP (part 1) - Week 1

## 01_Introduction_and_learning_outcomes_Video_1_min

# Introduction and learning outcomes
Video • 1 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/TxGmJ/introduction-and-learning-outcomes

This course provides a structured progression through Natural Language Processing (NLP) concepts, spanning 22 weeks. The initial phase establishes the foundations in NLP (Weeks 1-2) and develops skills in basic text processing (Weeks 3-4). Students then delve into statistical techniques through Language Modelling (Weeks 5-6), which introduces probability to text generation. Lexical semantics (Weeks 7-8) follows, focusing on the meaning and relationships between individual words. The curriculum progresses to practical applications, starting with Text Categorisation and Sentiment Analysis (Weeks 9-10).

A critical technical focus is placed on grammar and structure, addressed through Syntax and Parsing (Weeks 11-12). The subsequent topic, Information Extraction (Weeks 13-14), details specific techniques like POS tagging and Relation extraction, often utilizing tools like NLTK. This is followed by Information Retrieval (Weeks 15-16), focusing on efficient search and document retrieval systems. The latter stages examine advanced applications, including Chatbots and Dialogue Systems (Weeks 17-18), which handle natural human interaction. Finally, the course culminates in reviewing NLP in practice, summarizing the entire domain, and dedicating time to revision and the final examination (Weeks 19-22).

---

## 02_Properties_of_human_conversation_Video_9_min

# Properties of human conversation
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/CN1S9/properties-of-human-conversation

This comprehensive course spans 22 weeks, beginning with fundamental concepts in NLP (Weeks 1-2). The initial phase focuses on basic text processing (Weeks 3-4), establishing the groundwork for analyzing raw data. Key concepts then progress to Language Modelling (Weeks 5-6) and Lexical Semantics (Weeks 7-8), which define how language structure and meaning are understood. The subsequent modules cover advanced linguistic analysis, including Text Categorization and Sentiment Analysis (Weeks 9-10) and detailed Syntax and Parsing (Weeks 11-12). The course emphasizes knowledge extraction through dedicated sections on Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16). A major focus is placed on interactive systems, detailed across Weeks 17 and 18, covering Chatbots and Dialogue Systems. Furthermore, practical application is reinforced by Week 19, dedicated to "NLP in Practice," and Week 20, serving as the Course Summary. Weeks 21 and 22 are allocated for revision and the final exam. All modules utilize varied learning formats, including video lectures, reading materials, and practice assignments, such as those related to properties of human conversation and speech acts.

---

## 03_Chatbots_Video_10_min

# Chatbots
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/lJU4t/chatbots

Chatbots are categorized as simple dialogue systems, designed primarily for conversation, entertainment, or therapeutic value rather than strictly completing specific tasks. Although early chatbots were highly hyped, they have found functional places in both home and office environments. Examples include Facebook's BlenderBot and Microsoft's Xiaoice. Underlying these systems are two primary classes of architecture: rule-based or data-driven (corpus-based).

The rule-based approach is exemplified by ELIZA, the first-ever chatbot developed by Joseph Weizenbaum in 1966. ELIZA operates as a Rogerian psychotherapist, reflecting the participant's own thoughts without dispensing clinical advice. Functionally, it utilizes rules, often implemented as a Regular Expression (RegEx), which map input patterns to production rules. For instance, the pattern `you love me` might transform into the question, "What makes you think I love you?"

These transformations are linked to specific keywords (e.g., "I," "my"), which are ranked by specificity. This ranking mechanism instantiates Grice's maxims, ensuring the response is as relevant as possible to the user's utterance. Furthermore, ELIZA maintains dialogue coherence by employing a memory or stack of previous transformations, triggered by the keyword "my."

The complementary corpus-based approach is highly data-driven, relying on machine learning paradigms trained on large datasets. These corpora can include call-center transcripts, movie dialogues, or pseudo dialogues derived from sources like Twitter exchanges. When using live usage data for training, confidence metrics must be

---

## 04_Task-based_dialogue_systems_Video_11_min

# Task-based dialogue systems
Video • 11 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/V5lat/task-based-dialogue-systems

This comprehensive course is structured over 22 weeks, designed to provide a deep dive into Natural Language Processing (NLP), starting with an introduction to the field. The initial phase focuses on foundational concepts, covering basic text processing techniques and transitioning into language modeling, which addresses how sequences of words are predicted. Semantic understanding is explored through Lexical Semantics, followed by the practical application of Text Categorisation and Sentiment Analysis. The core structural elements of language are then addressed through Syntax and Parsing, enabling the analysis of grammatical structures. Subsequent topics focus on extracting specific knowledge, covering Information Extraction (Weeks 13-14) and Information Retrieval (Weeks 15-16). A major advanced focus is placed on Chatbots and Dialogue Systems (Weeks 17-18), including detailed study of properties of human conversation, task-based systems, and design/evaluation methodologies. Furthermore, the curriculum integrates these concepts through NLP in Practice (Weeks 19-20), serving as a real-world application context. The course concludes with a Course Summary and a dedicated Revision Week (Week 21). The final week (Week 22) is reserved for the comprehensive examination.

---

## 05_Design_and_evaluation_Video_9_min

# Design and evaluation
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/Fr4vx/design-and-evaluation

Designing dialogue systems is an interactive process that requires drawing upon principles from human-computer interaction (HCI). Consequently, the User-Centered Design process is essential to guide and shape the development of these conversational products. This process requires studying user tasks to develop a deep, evidence-based understanding of who the user is, what their capabilities are, and their context. Following this, simulations and prototypes are iteratively built and then tested directly with users to gather crucial feedback.

A standard framework for this is ISO 9241-210, which dictates identifying the need, specifying the context of use, producing design solutions/prototypes, and finally evaluating them with users. Importantly, the entire design process is iterative, as feedback is used to refine the context of use and requirements, refining the solution until acceptance criteria are met. Another model, Design Council's Double Diamond, frames design as starting with divergent thinking (research), moving to convergent thinking (defining the problem), then design exploration (ideation), and finally delivering a narrowed-down prototype.

Due to the high cost of building and revising complex dialogue systems, researchers frequently employ the Wizard of Oz technique. This method involves inserting a human researcher into the loop to emulate complex behaviors, allowing research and feedback gathering without needing to build the actual, expensive system in advance.

Evaluation in Natural Language Processing (NLP) can be automated, using metrics like BLEU or ROUGE, which are based on patterns of co-occurrence and n-grams in benchmark and test data. However, because generative chat conversations are highly diverse, manual evaluation is typically necessary.

Manual evaluation follows two main approaches: participant evaluation and observer evaluation. In participant evaluation, the user taking part in the dialogue administers an evaluation using questionnaires across eight dimensions, such as fluency, interestingness, and engagingness. Observer evaluation involves third-party annotators assessing a complete conversation, often comparing it via an AB test against a benchmark system on scales like humanness and knowledgeable.

For task-based dialogue systems, evaluation focuses on measuring task success—whether the user completed the task within appropriate time and effort—or user satisfaction via questionnaires. Alternatively, quantitative measures include examining slot error rates, and calculating slot precision, recall, or the F-measure to gauge accuracy.

Finally, ethical considerations are paramount in NLP. Since machine learning systems are trained on data, they inevitably replicate and amplify existing societal biases, including gender stereotypes. Researchers must be aware that these biases can be propagated through the ML approaches, similar to the issues observed with the Microsoft Tay chatbot. Furthermore, safeguarding privacy is critical; dialogue agents may inadvertently capture private information, such as passwords, which should never be used as training data.

---

## 06_Chatbots_and_dialogue_systems_Reading

# Chatbots and dialogue systems
Reading - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/ILRm4/chatbots-and-dialogue-systems

Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Refer to chapter 25 in the provided link. If this link is broken, please let us know via the Student Portal . Chatbots and dialogue systems Jurafsky, D. and J.H. Martin Speech and language processing . (2026; 3rd ed.). Refer to chapter 25 in the provided link. If this link is broken, please let us know via the Student Portal . Mark as completed Dislike Report an issue

---

## 07_Activity_Exploring_speech_acts_Reading_10_min

# Activity: Exploring speech acts
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/supplement/StEif/activity-exploring-speech-acts

This document outlines a communicative exercise requiring the examination and labeling of a conversation using specific speech act categories. These categories include Constatives, which commit the speaker to a proposition like claiming or denying. Directives aim to get the addressee to perform an action, such as asking or inviting. Commissives involve committing to a future course of action, like promising or planning. Finally, Acknowledgements express reactions to an action, such as thanking or greeting.

The conversation begins with C1 stating the need to travel in May. A2 initiates the dialogue by inquiring about the desired day of travel in May. C3 clarifies the necessity of the travel, specifying a required meeting attendance from the 12th to the 15th. A4 then seeks the destination city for the flight. C5 confirms the destination as Seattle.

A6 directs the conversation toward the preferred departure time from Pittsburgh. C7 reports that there are few options available for non-stop travel. A8 counters this by stating that three non-stop options are available for the day. C9 requests the detailed schedule of these options. A10 meticulously lists the three flights. The first departs PGH at 10:00am and arrives in Seattle at an unspecified time. The second option departs PGH at 5:55pm and arrives in Seattle at 8pm. The last flight departs PGH at 8:15pm, arriving in Seattle at 10:28pm.

C11 makes a selection, opting for the "5ish flight on the night before on the 11th." A12 confirms this choice, detailing the specific logistics. This itinerary involves departing at 5:55pm, arriving in Seattle at 8pm, and being assigned as U.S. Air flight 115. C13 provides a simple acknowledgement of this decision.

A14 then verifies the originally stated return date of May 15th. C15 affirms this date, clarifying that the return is "at the end of the day." A16 then notes that there are two non-stops available for the return journey. C17 acts to clarify the calendar logistics, asking for the day of the week corresponding to the 15th. A18 provides the necessary calendar information, confirming that the 15th is a Friday.

C19 then proposes a modification to the travel plan, suggesting a stay extension until Sunday. A20 accepts the suggestion, indicating agreement with the new schedule. The conversation concludes with A20 stating that an activity is planned for Sunday, leaving the planning process incomplete. This exercise demonstrates the practical application of classifying conversational functions within a real-world travel scenario.

---

