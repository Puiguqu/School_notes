# 06_Running_creatures_in_simulation_Video_22_min

# Running creatures in simulation
Video • 22 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/4bjS8/running-creatures-in-simulation

This segment of the video focuses on **completing the simulation loop** by implementing the logic necessary to track and verify that the artificial creature actually moves within the physics engine.

Here is a breakdown of the key steps and concepts covered:

### 1. Implementing Position Tracking in the Creature

The core task was adding an `update_position` function to the `creature` object. This function handles the logic for tracking the creature's starting point versus its current location:

*   **Logic:** The function accepts the creature itself and a new `position`.
*   **State Management:** It initializes two variables: `start_position` and `last_position`.
*   **First Call:** If `start_position` is `None` (meaning it's the first call), the incoming `position` is stored as the **initial position**.
*   **Subsequent Calls:** For every call after the first, the incoming `position` is stored as the **last position**, allowing the program to calculate movement over time.

### 2. Integrating Position Updates into the Simulation

To make the tracking functional, the simulation loop had to be modified:

*   **Position Retrieval:** Every step of the simulation, the program calls the `p.get_a_position_and_orientation()` function from the `pybullet` API. This function is used to get the creature's real-time position from the physics engine, using the creature's ID and the specified physics engine.
*   **Updating the Creature:** This retrieved position is then passed into the `creature.update_position()` method.

### 3. Verification and Testing

The final step was verifying that the simulation was successful—meaning the creature actually moved, confirming the physics engine was functioning correctly.

*   **The Test:** A unit test was written that runs the simulation for a set duration (e.g., 10 seconds).
*   **The Assertion:** The crucial assertion was: `self.assertNotEqual(creature.start_position, creature.last_position)`.
*   **Result:** Because the creature was expected to move randomly (as demonstrated by the simulated "flying"), this assertion passed, proving that the creature's final position was different from its starting position.

### Summary

In essence, this segment moved from *controlling* the creature (setting motor commands) to **measuring** the creature. By implementing `update_position` and using the `pybullet` API to pull real-time coordinates, the program gained the ability to reliably verify that the physics simulation was causing the intended physical movement.

