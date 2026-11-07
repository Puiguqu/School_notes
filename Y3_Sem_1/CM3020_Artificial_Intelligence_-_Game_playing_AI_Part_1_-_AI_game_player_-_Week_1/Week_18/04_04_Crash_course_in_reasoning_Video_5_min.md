# 04_Crash_course_in_reasoning_Video_5_min

# Crash course in reasoning
Video • 5 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/TC0eT/crash-course-in-reasoning

This mini-lecture provides a detailed examination of the fundamental types of logical reasoning utilized in intelligent systems. It focuses on three core methods: deduction, abduction, and induction.

Deduction operates on the principle that if a rule and a fact are provided, the resulting conclusion is guaranteed to be correct. This form of reasoning is based on the pattern known as Modus Ponens. Specifically, if P implies Q (a condition), and P is asserted, then Q is the necessary conclusion. Deductive reasoning is utilized in standard patterns of inference, allowing chains of conclusions to be derived to reach a goal. Furthermore, Prolog reasoning relies on deduction to verify the truthfulness of logical statements.

Abductive reasoning, conversely, is defined as inferring the most plausible explanation when a rule and an observation are present. Its structure follows: if P implies Q (a condition), and Q is observed, then P is the possible explanation. Unlike deduction, the conclusion derived through abduction is not guaranteed to be correct, requiring an extra step to confirm or reject its truthfulness. The deductive method famously used by Sherlock Holmes is often cited as an example of abductive reasoning, searching for possible explanations.

Induction involves the generalization of facts from observations to form general conclusions. Similar to abduction, induction is not guaranteed to be correct and necessitates a verification step to establish truth. Machine learning is fundamentally based on inductive reasoning, as it processes many facts to generate predictions or general conclusions. This process reflects common sense, such as assuming the sun will rise tomorrow based on past observations.

Beyond these three types, the text notes that other forms of reasoning exist, including qualitative reasoning, case-based reasoning, fuzzy logic, and probabilistic reasoning. All these forms are applicable to intelligent agents to facilitate decision-making and solution searching.

The provided curriculum reinforces these concepts across several advanced AI topics. Modules involve Week 1 and 2 focusing on Game Playing AI and Formalizing Reinforcement Learning using the DQN agent. Week 6 and 7 introduce Evolving Artificial Creatures, utilizing genetic algorithms and Pybullet/URDF files for robot building.

Modules Week 11 through Week 15 cover Generative and Collaborative AI, detailing systems like GPT-2 for lyrics generation and MusicVAE/DiffSinger for music composition. Crucially, Week 16 and 17 introduce the "Toy Robot Scientist," focusing on knowledge representation and system building.

The latter part of the curriculum deeply engages with inference, specifically in Week 18. This module introduces the limits of reasoning and the practical implementation of generating hypotheses. This process includes a "Crash course in logic" and specific assignments for practicing both abduction and induction. The curriculum ultimately ties these logical concepts into a functional "Toy hypotheses generation agent."

