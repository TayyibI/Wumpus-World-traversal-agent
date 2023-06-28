# Wumpus-World-traversal-agent
An Agent to traverse the Wumpus world using predicate logic, location of wumpus, pit and gold is random


# # Introduction:

The Wumpus World is a classic problem in artificial intelligence that
requires designing an agent capable of exploring a maze-like
environment inhabited by a Wumpus, pits, and gold. 
The goal of the agent is to collect the gold and return to the starting location without
falling into pits or being eaten by the Wumpus. This report details a
project that implements a Wumpus World agent that navigates through
the environment, collects the gold, and returns to the starting location.

# #  Implementation:

The project consists of four Python files that work together to simulate
the Wumpus World. The first file, runagent.py, is responsible for running
the simulation by importing the agent and world1 modules and invoking
the simulation function.

The second file, world1.py, defines the environment and its
characteristics. The Wumpus World environment is represented as a grid
with a size of 5 by 5. The environment contains pits, gold, and a Wumpus,
which are randomly located. The agent starts at the location (1,1) and
the gold is located at (2,4). The pits and Wumpus are generated
randomly with one pit and one Wumpus. The environment is
represented as a set of blocks, which includes the boundaries and
obstacles such as pits and Wumpus.

The third file, wumpus.py, implements the agent that navigates through
the environment using the fourth file, agent.py. The agent is initialized
with a starting location, the location of the Wumpus, the location of the
pits, and the location of the gold. The agent has a has_arrow attribute
that is set to true, which means that it can kill the Wumpus with the
arrow. The agent has a get_action function that returns the action to be
taken based on the current state of the environment. The agent also has
a give_senses function that is called by the environment to provide the
agent with the senses of the current square.

The agent navigates through the environment by implementing a depthfirst search algorithm to explore the environment. The agent uses a stack
data structure to keep track of the visited squares and the possible
moves. The agent marks the squares that it has visited and marks the
squares that it knows are safe. The agent avoids squares that are known
to be unsafe, such as those adjacent to pits and the Wumpus. When the
agent collects the gold, it uses the same algorithm to return to the
starting location.

# #  Results:

The Wumpus World agent successfully navigates through the environment, collects the gold, and returns to the starting location. 
The agent avoids squares that are known to be unsafe, such as those adjacent
to pits and the Wumpus. The agent uses the top down algorithm to
explore the environment and mark the squares that it has visited and the
squares that it knows are safe. The agent uses the same algorithm to
return to the starting location after collecting the gold.

# #  Conclusion:

The Wumpus World agent project successfully implements an agent that
navigates through the environment, collects the gold, and returns to the
starting location. The project uses the depth-first search algorithm to
explore the environment and avoid squares that are known to be unsafe.
The project demonstrates the use of Python programming language to
solve classic problems in artificial intelligence. The project can be
improved by implementing other algorithms such as the A* algorithm
and by adding more complex environments.


Initial state:
<img width="145" alt="image" src="https://github.com/TayyibI/Wumpus-World-traversal-agent/assets/94107654/bdcd97c7-ac8e-4446-8f95-1c1df031f79d">

Final state:
<img width="124" alt="image" src="https://github.com/TayyibI/Wumpus-World-traversal-agent/assets/94107654/f8fcbc85-5b26-4f40-9992-f050de73122f">

