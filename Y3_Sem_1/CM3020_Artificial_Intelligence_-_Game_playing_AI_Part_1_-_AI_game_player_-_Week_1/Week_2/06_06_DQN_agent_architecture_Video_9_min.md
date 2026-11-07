# 06_DQN_agent_architecture_Video_9_min

# DQN agent architecture
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/q4P2b/dqn-agent-architecture

This summary outlines the architecture and operational principles of the Deep Q-Network (DQN) agent, focusing on the mechanisms of autonomous learning and exploration.

1. An agent is defined as an autonomous entity capable of observing its environment and taking decisions within that world.
2. Its primary goal is to maximize accumulated reward over time.
3. The DQN architecture is designed to solve complex problems where traditional state transition matrices and explicit action policies are unavailable.
4. The core function of the agent is to learn a Q function, which allows it to determine the optimal action in any given state.
5. The overall system comprises the agent itself and the game environment, which interacts with the agent.
6. Data flows from the environment to the agent, providing states and rewards, while the agent sends actions back to the environment.
7. Internally, the agent relies on a Replay Buffer, which acts as a massive memory store for past experiences.
8. The Replay Buffer stores experience tuples, structured as $(S, A, S', R, D)$.
9. $S$ represents the current state, $A$ is the action taken, $S'$ is the subsequent state, $R$ is the immediate reward, and $D$ is a boolean indicating if the game concluded.
10. The other critical component is the Q function, implemented as

