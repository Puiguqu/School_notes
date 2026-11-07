# 08_Visual_processing_and_states_in_DQN_Video_8_min

# Visual processing and states in DQN
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Z2fbx/visual-processing-and-states-in-dqn

The text details the necessary pre-processing steps required to transform raw data output from an Atari game emulator into a format suitable for training a Deep Q-Network (DQN) agent. These manipulations involve crucial adjustments related to temporal information, artifact removal, and data reduction.

A primary challenge noted is the inherent lack of a sense of time when a neural network processes video input using only a single frame as its state. Because arcade games rely heavily on movement, the AI requires context to predict actions accurately. Standard recurrent systems like LSTM are often used for sequential data, but the DQN architecture employed here is not recurrent. Therefore, the solution involves feeding the network a sequence of frames rather than a single snapshot. Specifically, the state fed into the DQN agent consists of the last three consecutive frames of the game. This three-frame input provides the network with a crucial sense of time, effectively making the state a form of second-order representation.

Furthermore, the raw game frames contain flickering artifacts caused by the hardware limitations of the original Atari 2600 platform. These limitations restricted the number of sprites that could be displayed simultaneously, leading to objects appearing only in alternating even or odd frames. An AI, unlike a human with persistence of vision, registers this flickering as visual instability. To eliminate this, the processing incorporates a compounding technique for each of the three input frames. This technique involves taking the maximum value for

