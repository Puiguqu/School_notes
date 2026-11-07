# 03_Chatbots_Video_10_min

# Chatbots
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/lJU4t/chatbots

Chatbots are categorized as simple dialogue systems, designed primarily for conversation, entertainment, or therapeutic value rather than strictly completing specific tasks. Although early chatbots were highly hyped, they have found functional places in both home and office environments. Examples include Facebook's BlenderBot and Microsoft's Xiaoice. Underlying these systems are two primary classes of architecture: rule-based or data-driven (corpus-based).

The rule-based approach is exemplified by ELIZA, the first-ever chatbot developed by Joseph Weizenbaum in 1966. ELIZA operates as a Rogerian psychotherapist, reflecting the participant's own thoughts without dispensing clinical advice. Functionally, it utilizes rules, often implemented as a Regular Expression (RegEx), which map input patterns to production rules. For instance, the pattern `you love me` might transform into the question, "What makes you think I love you?"

These transformations are linked to specific keywords (e.g., "I," "my"), which are ranked by specificity. This ranking mechanism instantiates Grice's maxims, ensuring the response is as relevant as possible to the user's utterance. Furthermore, ELIZA maintains dialogue coherence by employing a memory or stack of previous transformations, triggered by the keyword "my."

The complementary corpus-based approach is highly data-driven, relying on machine learning paradigms trained on large datasets. These corpora can include call-center transcripts, movie dialogues, or pseudo dialogues derived from sources like Twitter exchanges. When using live usage data for training, confidence metrics must be

