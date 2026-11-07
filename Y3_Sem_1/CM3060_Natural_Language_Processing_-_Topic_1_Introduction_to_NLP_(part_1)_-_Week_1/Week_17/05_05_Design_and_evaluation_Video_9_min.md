# 05_Design_and_evaluation_Video_9_min

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

