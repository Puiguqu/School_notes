# 21_Adding_motors_Video_16_min

# Adding motors
Video • 16 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/Dga6h/adding-motors

Based on the transcript, this segment details the successful implementation and initial testing of the motor system within the creature structure.

Here is a summary of the progress made, the technical challenges overcome, and the next steps:

---

### ⚙️ Progress Summary: Implementing Creature Motors

The core objective of this section was to define, incorporate, and test the motors within the creature/graph representation.

#### 1. Motor Implementation
*   **Definition:** A motor (`M`) was defined as an instance linked to a specific link (`l = self.x_link`).
*   **Properties:** Key control properties were accessed from the link object, specifically `l.control_amp` and `l.control_frequency`.
*   **Architecture:** The new motor was successfully appended to the collection of all motors (`self.motors`).
*   **Refinement:** The code was refined to include assertions and conditional logic (`if self.motors is None`) to ensure efficient regeneration and prevent unnecessary recalculations.

#### 2. Testing and Verification
*   **Testing Script:** A test function (`testCMotor`) was created to verify the functionality of the newly added motors.
*   **Verification Logic:** The test checks that the number of motors is exactly one less than the number of expanded links (`len(ls) - 1 == len(ms)`), correctly accounting for the root link.
*   **Debugging:** An initial `AttributeError` (caused by a misplaced dot operator) was encountered and subsequently fixed.
*   **Result:** The test successfully passed, confirming that the motors are correctly generated and produce "sensible output."

#### ⏭️ Next Steps
The implementation phase is complete, and the system is verified. The next steps outlined are:

1.  **Writing a Test Script:** Create a comprehensive test script that generates a random creature, displays it on the screen, and actively moves its motors.
2.  **Algorithmic Implementation:** Use this functional base to implement the actual evolutionary algorithm that will drive the creature's development.

***

### 🔑 Key Takeaway
The creature structure is now robust, with a fully functional, tested, and verifiable motor system, ready to be integrated into a dynamic simulation and genetic algorithm.

