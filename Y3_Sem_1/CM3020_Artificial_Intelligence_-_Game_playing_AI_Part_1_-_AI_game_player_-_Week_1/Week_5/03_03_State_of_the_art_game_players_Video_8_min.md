# 03_State_of_the_art_game_players_Video_8_min

# State of the art game players
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/dqMpF/state-of-the-art-game-players

This summary reviews the critical milestones and developments in AI game playing that occurred subsequent to the publication of the seminal Deep Q-Network (DQN) agent paper in 2015.

The discussion first outlines the key technical elements one must analyze in post-DQN systems, including the agent's general runtime, how experiences are gathered and the state transition matrix is built (beyond the DQN replay buffer), required exploratory behavior (beyond $\epsilon$-nets or greedy approaches), neural network architecture advancements, and the crucial loss function computation. Specifically, the ground truth in DQN is derived by combining an older network version with the immediate reward plus a prediction of future reward.

Following the DQN success, significant progress was made in Atari game playing with the invention of Double DQN, which led to the development of the advanced Rainbow system. Other notable Atari agents reviewed are Dreamer v2 and R2D2.

The field reached a massive milestone in 2020 with DeepMind's development of Agent 57. This agent surpassed most professional game players across a benchmark set of 57 Atari games. Agent 57 demonstrates the ability to play highly complicated games, even those requiring extremely long exploration periods before a reward is achieved.

Turning to complex strategy games, StarCraft 2 was highlighted as a title considerably more challenging than Go. DeepMind's AlphaStar system, developed in 2019, aimed to be a general-purpose AI capable of mastering diverse games. AlphaStar succeeded, reaching a level that matched and exceeded that of professional players in the demanding StarCraft environment. This advanced system integrates deep learning, reinforcement learning, game theory, and evolutionary computation.

The development extended to DotaII, a multi-player team-based strategy game. In 2019, an AI system managed to defeat professional World Champion players, notably the team OG, in back-to-back matches. Crucially, this AI was put online in 2019, engaging in real-time competitive games. Against human players, the AI consistently won 7,215 games while only registering 42 losses.

In contrast, the Mario AI competition predates these major advances, tracing its roots to around 2013 in the original Arcade learning environment. This older community was focused on playing a wide range of games, rather than simply mastering a single title entirely.

