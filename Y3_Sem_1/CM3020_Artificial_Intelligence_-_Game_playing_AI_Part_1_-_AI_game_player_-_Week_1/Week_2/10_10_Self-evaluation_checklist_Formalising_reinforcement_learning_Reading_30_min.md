# 10_Self-evaluation_checklist_Formalising_reinforcement_learning_Reading_30_min

# Self-evaluation checklist: Formalising reinforcement learning
Reading • 30 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/supplement/9ynYp/self-evaluation-checklist-formalising-reinforcement-learning

This text serves as a comprehensive self-evaluation checklist for Week 2 of a learning module on Reinforcement Learning (RL), focusing on the formalism of Markov Decision Processes (MDPs), Q-Learning, and Deep Q-Networks (DQN).

The initial learning objective requires a thorough understanding of MDPs, which are the foundational model for sequential decision-making problems in RL. An MDP is defined by several key components: states, actions, transition probabilities, rewards, and discount factors. These components allow a game or decision-making scenario to be accurately represented within the MDP framework. MDPs are crucial because they provide the formal structure necessary for modeling how an agent makes decisions sequentially over time.

The second core concept addressed is Q-Learning and its functional necessity. Q-learning is a specific algorithm designed to learn an optimal action-selection policy by estimating action-value functions (Q-values). It is particularly valuable when the environment’s transition dynamics are unknown, meaning the agent does not know the explicit probabilities of moving between states. A critical element of Q-learning is managing the inherent trade-off between exploration and exploitation. Exploration allows the agent to discover new information, while exploitation maximizes immediate rewards using learned knowledge.

This process is driven by the Bellman equation, which defines the update rule for Q-values over time. The Bellman equation is the core mathematical tool that allows the agent to iteratively refine its estimates of expected future rewards.

The final and most complex topic is the Deep Q-Network (DQN), which addresses the inherent limitations of traditional Q-learning. Traditional methods struggle when the state space is vast, necessitating the use of deep learning to approximate the Q-values. A DQN utilizes a neural network, which acts as the powerful function approximator for the Q-function.

To ensure stable training, DQN incorporates two vital components. The first is experience replay, which stabilizes learning by storing and reusing past experiences. The second is the target network, whose purpose is to reduce instability by providing a fixed target for training. The DQN optimizes its Q-values using a specific loss function. This function quantifies the difference between the predicted Q-values and the target Q-values derived from the Bellman updates. By mitigating the challenges of instability, techniques like experience replay and target networks allow DQN to effectively tackle complex real-world problems.

