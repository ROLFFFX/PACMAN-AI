# Pac-Man AI Projects

This repository contains my implementations for the Pac-Man AI projects from UCB CS188 Intro to Artificial Intelligence course. These projects cover a range of AI concepts, from search algorithms to reinforcement learning.

## Project Overview
### Projects Index
[Search Algorithms](#1-search-algorithms)<br/>
[Multi-Agents Pacman](#2-multi-agent-pac-man)<br/>
[GhostBusters](#3-ghostbusters)<br/>
[Reinforcement Learning](#4-reinforcement-learning)<br/>

### 1. Search Algorithms

#### Introduction
In the "Search in Pac-Man" project, classic search algorithms are applied to navigate Pac-Man through various mazes. The objective is to understand and implement search strategies for pathfinding, food collection, and ghost avoidance in a dynamic maze environment.

#### Key Concepts
- **Search Algorithms**: Implementation of Depth-First Search (DFS), Breadth-First Search (BFS), Uniform-Cost Search (UCS), and A* Search.
- **Pathfinding**: Techniques for efficient maze navigation, reaching specific locations, and food collection.
- **State Space Representation**: Effective representation of the game state for search algorithms.

#### Implementation Details
- **Core Files**:
  - `search.py`: Contains the search algorithms to be implemented.
  - `searchAgents.py`: Features agents using search algorithms in the Pac-Man world.
- **Supportive Files**:
  - `pacman.py`: Runs Pac-Man games and manages game states.
  - `game.py`: Handles game logic, including agent states, directions, and grids.
  - `util.py`: Offers data structures for search algorithms (e.g., stacks, queues).
- **Graphics and User Interface**:
  - Graphical display of Pac-Man, ghosts, and the maze.
  - Command-line options for testing different agents and maze layouts.

#### Running the Project
- Basic game execution: `python pacman.py`
- Testing specific agents and mazes:
  - GoWestAgent example: `python pacman.py --layout testMaze --pacman GoWestAgent`
  - Depth-First Search test: `python pacman.py -l tinyMaze -p SearchAgent`
  - Breadth-First Search test: `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`

#### Challenges and Objectives
- Understanding and coding different search algorithms in the context of a maze.
- Choosing appropriate data structures for each search algorithm's implementation.
- Comparing the efficiency and optimality of various search strategies.
- Developing heuristics for complex problems like the shortest path for food collection.

#### Autograder Evaluation
- General autograder test: `python autograder.py`
- Specific question test, e.g., question 2: `python autograder.py -q q2`

---

### 2. Multi-Agent Pac-Man

#### Introduction
"Fightin' Pac-Man" is the second project where you will enhance Pac-Man with the ability to contend with ghosts using minimax, expectimax, and evaluation function design. This project focuses on developing agents for the classic version of Pac-Man, introducing adversarial search concepts.

#### Key Concepts
- **Adversarial Search**: Implementing minimax and expectimax search algorithms in a multi-agent context.
- **Evaluation Function Design**: Creating functions that effectively evaluate game states considering both Pac-Man and ghosts.
- **Generalization**: Extending algorithms to handle any number of ghosts.

#### Implementation Details
- **Core Files to Edit**:
  - `multiAgents.py`: Contains all multi-agent search agents.
- **Supportive Files**:
  - `pacman.py`: Runs Pac-Man games and manages GameState.
  - `game.py`: Contains game logic, including AgentState and Grid.
  - `util.py`: Provides data structures for implementing search algorithms.
- **Files to Ignore**:
  - Various files related to graphics, ghost agents, layout parsing, and testing framework.
- **What to Submit**: You will only need to submit the `multiAgents.py` file.

#### Running the Project
- To play a classic game of Pac-Man: `python pacman.py`
- To test the provided ReflexAgent: `python pacman.py -p ReflexAgent`
- For testing different layouts and ghost numbers: `python pacman.py --frameTime 0 -p ReflexAgent -k [number_of_ghosts]`

#### Tasks and Questions
- **Reflex Agent Improvement (Question 1)**: Enhance the ReflexAgent to play effectively on the `testClassic` layout.
- **Minimax Agent (Question 2)**: Implement the MinimaxAgent class to perform minimax search considering multiple ghosts and depth-limited search.
- **Alpha-Beta Pruning (Question 3)**: Improve the MinimaxAgent with alpha-beta pruning for efficiency.
- **Expectimax Agent (Question 4)**: Implement the ExpectimaxAgent, which considers the probabilistic behavior of ghosts rather than the worst-case scenario.
- **Better Evaluation Function (Question 5)**: Develop a more sophisticated evaluation function for the ExpectimaxAgent to perform well in complex scenarios.

#### Additional Challenges
- **Mini Contest**: Implement an ApproximateSearchAgent that finds a short path in the `bigSearch` layout. The top agents will be awarded extra credit points.

#### Hints and Observations
- The evaluation function should consider various features of the game state.
- Agents should be optimized to run within reasonable time limits, especially for deeper searches.
- Understanding the difference in agent behavior between minimax and expectimax is key.

#### Autograder Evaluation
- The project includes an autograder for evaluating answers: `python autograder.py`
- It can be run for specific questions, e.g., `python autograder.py -q q2`
- For testing specific test cases: `python autograder.py -t test_cases/q2/0-small-tree`

---

### 3. Ghostbusters

#### Introduction
"Ghostbusters" is a project where Pacman, equipped with sensors, locates and eats invisible ghosts. In this project, you'll advance from locating stationary ghosts to hunting multiple moving ghosts with Bayes' Nets and particle filters.

#### Key Concepts
- **Bayesian Networks**: Utilizing Bayes' Nets for probabilistic reasoning and ghost tracking.
- **Particle Filtering**: Implementing particle filters to manage and update beliefs about ghost positions.
- **Sensory Information**: Using noisy distance readings to infer the position of invisible ghosts.

#### Implementation Details
- **Core Files to Edit**:
  - `busterAgents.py`: Agents for the Ghostbusters variant of Pacman.
  - `inference.py`: Code for tracking ghosts over time using their sounds.
- **Supportive Files**:
  - `busters.py`: Main entry for Ghostbusters, replacing `pacman.py`.
  - `bustersGhostAgents.py`, `ghostAgents.py`: New ghost agents for Ghostbusters.
  - `distanceCalculator.py`, `game.py`: Computes maze distances and inner workings for Pacman.
- **Files to Ignore**: 
  - Files related to graphics, keyboard interfaces, and layout parsing.
- **What to Submit**: 
  - Submit edited `bustersAgents.py` and `inference.py` files.

#### Evaluation
- **Autograder**: Your code will be evaluated for technical correctness using `python autograder.py`.
- **Correctness**: The correctness of your implementation will be the final judge of your score.

#### Tasks and Questions
- **Discrete Distribution (Question 0)**: Implement the DiscreteDistribution class in `inference.py`.
- **Observation Probability (Question 1)**: Implement the `getObservationProb` method in `inference.py`.
- **Exact Inference Observation (Question 2)**: Implement `observeUpdate` in the ExactInference class.
- **Exact Inference with Time Elapse (Question 3)**: Update beliefs in the ExactInference class after time elapses.
- **Full Test with Exact Inference (Question 4)**: Integrate observation and time elapse updates in ExactInference.
- **Approximate Inference Initialization (Question 5)**: Initialize particle filters in `ParticleFilter` class.
- **Approximate Inference Observation (Question 6)**: Implement `observeUpdate` in the `ParticleFilter` class.
- **Approximate Inference with Time Elapse (Question 7)**: Update particle filter after time elapse.
- **Joint Particle Filter Observation (Extra Credit Question 8)**: Implement particle filtering for multiple ghosts.
- **Joint Particle Filter with Elapse Time (Extra Credit Question 9 & 10)**: Resample particles in `JointParticleFilter` considering ghost movements.

#### Running the Project
- To play Ghostbusters: `python busters.py`
- For autograder tests: `python autograder.py -q [question_number]`

#### Autograder Evaluation
- Use `python autograder.py` to evaluate your solutions. 
- Specific question tests, e.g., `python autograder.py -q q2`.
- Single test run, e.g., `python autograder.py -t test_cases/q1/1-ExactObserve`.

*Note*: Patience may be required as some autograder tests can take time to run. The autograder's judgment may not always align with the correctness of your implementation, and individual assignments will be reviewed to ensure fair credit.

---

### 4. Reinforcement Learning

#### Introduction
In the Reinforcement Learning project, you will implement value iteration and Q-learning. You will apply your agents to Gridworld, a Crawler robot, and Pacman scenarios. This project focuses on enabling Pacman to learn policies through trial and error interactions with the environment.

#### Key Concepts
- **Value Iteration**: Implementing an agent that solves known Markov Decision Processes (MDPs).
- **Q-Learning**: Developing Q-learning agents for Gridworld, Crawler, and Pacman.
- **Feature Extraction**: Utilizing features of state-action pairs for approximate Q-learning.

#### Implementation Details
- **Core Files to Edit**:
  - `valueIterationAgents.py`: A value iteration agent for solving known MDPs.
  - `qlearningAgents.py`: Q-learning agents.
  - `analysis.py`: Contains answers to project questions.
- **Supportive Files**:
  - `mdp.py`, `learningAgents.py`: General MDP methods and base classes for agents.
  - `util.py`, `gridworld.py`: Utilities and the Gridworld implementation.
  - `featureExtractor.py`: Feature extraction for state-action pairs.

#### Evaluation
- **Autograder**: Your code will be assessed for technical correctness using `python autograder.py`.
- **Correctness**: The final judgment of your score will be based on the correctness of your implementation.

#### Tasks and Questions
- **Value Iteration (Question 1)**: Implement a value iteration agent in `valueIterationAgents.py`.
- **Bridge Crossing Analysis (Question 2)**: Analyze policies in `BridgeGrid` under varying conditions.
- **Policies (Question 3)**: Experiment with different policies on the `DiscountGrid` layout.
- **Asynchronous Value Iteration (Question 4)**: Implement asynchronous value iteration.
- **Prioritized Sweeping Value Iteration (Question 5)**: Prioritize state updates in value iteration.
- **Q-Learning (Question 6)**: Develop a Q-learning agent.
- **Epsilon Greedy (Question 7)**: Implement epsilon-greedy action selection.
- **Bridge Crossing Revisited (Question 8)**: Explore Q-learning in `BridgeGrid`.
- **Q-Learning and Pacman (Question 9)**: Apply Q-learning to Pacman.
- **Approximate Q-Learning (Question 10)**: Implement an approximate Q-learning agent.

#### Running the Project
- For Gridworld: `python gridworld.py -m`
- For specific questions: `python autograder.py -q q1`

#### Autograder Evaluation
- Use `python autograder.py` to evaluate solutions.
- Specific question tests, e.g., `python autograder.py -q q1`.

*Note*: Patience may be required as some autograder tests can take time to run. The autograder's judgment may not always align with the correctness of your implementation, and individual assignments will be reviewed to ensure fair credit.

---

## Technologies Used
- Python
- AI algorithms and principles as outlined in the UC Berkeley CS188 course.

## Installation and Usage
- Clone this repository.
- Navigate to the directory of each project.
- Run the Pac-Man games with AI strategies using commands provided in each project folder.

## License
This project is for educational purposes and is not for commercial use. The Pac-Man projects and associated teaching materials are property of UC Berkeley.

## Acknowledgments
Special thanks to the UC Berkeley CS188 course staff for providing the framework and guidance for these projects.

## Contact
For any inquiries or feedback, please contact me at yshi373@emory.edu
