# 03_Crash_course_in_planning_and_scheduling_Video_8_min

# Crash course in planning and scheduling
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3020-artificial-intelligence/lecture/UbymE/crash-course-in-planning-and-scheduling

This mini-lecture outlines the complexities of planning and scheduling, addressing both classical and real-world scenarios. Planning is a critical application in fields such as manufacturing and robotics. The field utilizes dedicated languages, such as PDDL (Planning Domain Definition Language), which serves as a primary standard for planning. Classical planning handles observable, deterministic situations and is modeled as a search problem. This involves defining an initial state, possible actions, and the desired goal state. The objective is to find a sequence of actions that successfully transitions the system from the initial state to the goal state. Algorithms employed for searching and planning include breadth-first search, depth-first search, and heuristic search. Deductive reasoning can also be applied by reasoning agents to locate solutions for planning tasks. Actions are typically formalized using a schema that specifies parameters, preconditions, and effects. For instance, a schema for "flying the plane" requires preconditions (e.g., plane at origin, airport access) and defined effects (e.g., plane is no longer at origin).

A classic illustration of this process is the blocks world problem, where a robot arm manipulates blocks on a table. This state is represented using predicate notation, identifying relations like `on(Block, Object)` or `clear(Object)`. The initial state is a list of predicates describing the arrangement of blocks and locations. An action's preconditions specify when it can occur, while its effects list the resulting changes to the system's relationships.

Real-world planning fundamentally differs from classical planning due to environmental uncertainties. Classical planning relies on the closed world assumption, meaning non-explicitly mentioned information is assumed not to exist. In contrast, agents operating in real environments must adhere to the open world assumption, recognizing that undefined information is simply unknown. Real-world agents must often produce contingent plans, which involve conditional branching due to partial observability and non-determinism. Furthermore, dynamic environments necessitate continuous monitoring and potential re-planning if goals or expected outcomes change unexpectedly.

Beyond just sequencing actions, the real world introduces temporal and resource constraints, which form the basis of scheduling problems. Planning typically focuses on *what* actions to perform, while scheduling focuses on *when* and *how long* they take, often requiring separate solutions. Resource constraints involve both reusable resources (like staff) and consumable resources (like chemicals).

Multi-agent planning introduces further complexity by requiring coordination between multiple autonomous agents. Agents may cooperate toward a shared goal, compete, or operate independently. Joint planning generates plans for coordinated actions, and agents may or may not need communication. Ultimately, the scope encompasses finding solutions in environments that are partially observable, non-deterministic, and constrained by resources and agent interactions.

