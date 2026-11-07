# 03_Formalising_the_problem_Video_7_min

# Formalising the problem
Video • 7 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Z9TPX/formalising-the-problem

This text outlines the formalization of AI game playing using the framework of a Markov Decision Process (MDP). The fundamental process in most games involves an iterated cycle of observation and action. Key components must be identified: states, actions, and rewards. A state ($S$) is defined as the current view of the game, such as the pixel configuration in a game like Breakout. The actions ($A$) are the moves the AI can take, such as moving left, moving right, or staying still. A reward ($R$) is a result associated with an action, providing positive or negative feedback.

For example, in Breakout, hitting a brick yields a positive reward (e.g., +1 point), while missing the ball may result in a heavy negative reward leading to game over. The interaction flow involves the player observing state $S$, taking action $A$, and subsequently observing the next state, $S'$.

Crucially, this transition is often probabilistic, meaning the same action in the same state may lead to multiple possible next states. This probabilistic relationship is formally expressed as the probability of state prime given state and action, $P(S'|S, A)$. This mathematical representation constitutes the state transition matrix.

The reward function, $R(S, A, S')$, dictates the gain or loss associated with the transition from state $S$ via action $A$ to $S'$. Rewards can be positive (points gained), negative (penalties or loss of life), or zero (for inaction in a given frame).

The combination of the probabilistic state transition matrix and the reward function formalizes the problem as a Markov Decision Process (MDP). An MDP is defined as a mechanism for formalizing a stochastic sequential decision problem. The term "stochastic" refers to the inherent probabilistic element determined by the state transition matrix.

The process is "sequential" because the AI must make a continuous series of decisions, determining an action for each frame observed in the game sequence. Finally, it is a "decision problem" because the goal is to determine the optimal sequence of actions.

The curriculum further extends these basic concepts to advanced reinforcement learning techniques. Key topics include the action policy and Q-learning. The program also addresses formalized reinforcement learning using agents like Deep Q-Networks

