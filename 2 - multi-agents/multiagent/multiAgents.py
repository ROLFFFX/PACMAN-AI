# multiAgents.py
# --------------
#   THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING A TUTOR OR CODE WRITTEN BY OTHER STUDENTS
#   - Yuxuan Shi
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        newFood = newFood.asList()

        # to store the positions of the ghosts
        ghostPositions = []
        for ghost in newGhostStates:
            ghostPosition = ghost.getPosition()
            x = ghostPosition[0]
            y = ghostPosition[1]
            ghostCoordinates = (x, y)
            ghostPositions.append(ghostCoordinates)

        # determine whether there is a scared ghost
        scared = min(newScaredTimes) > 0

        # for scared ghost and new position overlaps with it, return -1
        if (not scared) and (newPos in ghostPositions):
            return -1.0

        # for new position overlap with food, return 1
        if newPos in currentGameState.getFood().asList():
            return 1.0

        # calcualte manhattan distance to new position
        def calculateManhattanDistance(position):
            return util.manhattanDistance(position, newPos)

        # find closest food by sorting food list
        closestFoodPositions = sorted(newFood, key=calculateManhattanDistance)

        # similarly find closest gohst by soritng ghost manhattan distnace list
        closestGhostPositions = sorted(
            ghostPositions, key=calculateManhattanDistance)

        # get closest position
        closestFoodPosition = closestFoodPositions[0]
        closestGhostPosition = closestGhostPositions[0]

        # get closest manhattan distance
        foodDistance = calculateManhattanDistance(closestFoodPosition)
        ghostDistance = calculateManhattanDistance(closestGhostPosition)

        def calculate_reciprocal(number):
            if number != 0:
                reciprocal = 1.0 * number / number / number
            else:
                # If the number is zero, its reciprocal is infinity
                reciprocal = float('inf')
            return reciprocal

        reciprocal_food_distance = calculate_reciprocal(foodDistance)
        reciprocal_ghost_distance = calculate_reciprocal(ghostDistance)

        # return difference between the reciprocals
        return reciprocal_food_distance - reciprocal_ghost_distance


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        numberOfAgents = gameState.getNumAgents()
        GhostIndices = []
        for i in range(1, numberOfAgents):
            GhostIndices.append(i)

        # determine if it wins, loss, or reacehd max depth
        def is_terminal_state(state, depth):
            if state.isWin() or state.isLose() or depth == self.depth:
                return True
            else:
                return False

        # returns max value corresponding to player's moves
        def calculate_max_value(state, depth):

            # if the state is terminal, return the evaluation of the state.
            if is_terminal_state(state, depth):
                return self.evaluationFunction(state)

            value = float('-inf')
            for action in state.getLegalActions(0):
                value = max(value, calculate_min_value(
                    state.generateSuccessor(0, action), depth, 1))
            return value

        # returns min value corresponding to ghost's move
        def calculate_min_value(state, depth, ghostIndex):
            # jif the state is terminal, return the evaluation of the state.
            if is_terminal_state(state, depth):
                return self.evaluationFunction(state)
            value = float('inf')
            for action in state.getLegalActions(ghostIndex):
                # if last ghost, calculate max value for next depth
                if ghostIndex == GhostIndices[-1]:
                    value = min(value, calculate_max_value(
                        state.generateSuccessor(ghostIndex, action), depth + 1))
                # else calculate min value for next depth
                else:
                    value = min(value, calculate_min_value(
                        state.generateSuccessor(ghostIndex, action), depth, ghostIndex + 1))
            return value

        action_values = []
        for action in gameState.getLegalActions(0):
            value = calculate_min_value(
                gameState.generateSuccessor(0, action), 0, 1)
            action_values.append((action, value))

        # sort the action-value pairs by value and return the one with highest value
        action_values.sort(key=lambda pair: pair[1])
        return action_values[-1][0]

        # util.raiseNotDefined()


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # get number of agents and populate ghost indices
        numberOfAgents = gameState.getNumAgents()
        GhostIndices = []
        for i in range(0, numberOfAgents):
            GhostIndices.append(i)
        infinity = float('inf')

        def is_terminal_state(state, depth):
            if state.isWin() or state.isLose() or depth == self.depth:
                return True
            else:
                return False

        # returns max value corresponding to player's move
        def calculate_max_value(state, depth, alpha, beta):
            if is_terminal_state(state, depth):
                return self.evaluationFunction(state)

            value = -infinity
            # for all legal action for player, if value is greater than beta, return it. else update alpha
            for action in state.getLegalActions(0):
                value = max(value, calculate_min_value(
                    state.generateSuccessor(0, action), depth, 1, alpha, beta))
                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value

        # returns min value corresponding to ghost move
        def calculate_min_value(state, depth, ghostIndex, alpha, beta):
            if is_terminal_state(state, depth):
                return self.evaluationFunction(state)
            value = infinity

            # for all legal action ghost can take:
            for action in state.getLegalActions(ghostIndex):
                # for last ghost, simply calculate the max value for next depth
                if ghostIndex == GhostIndices[-1]:
                    value = min(value, calculate_max_value(
                        state.generateSuccessor(ghostIndex, action), depth + 1, alpha, beta))
                # else calculate min value for next ghost
                else:
                    value = min(value, calculate_min_value(state.generateSuccessor(
                        ghostIndex, action), depth, ghostIndex + 1, alpha, beta))
                # return value that is less than alpha
                if value < alpha:
                    return value

                # else update beta
                beta = min(beta, value)
            return value

        def alpha_beta_prunning(state):
            value = -infinity
            best_action = None
            alpha = -infinity
            beta = infinity

            # for each legal action player can take:
            for action in state.getLegalActions(0):
                # get min value for next state resulting from current action
                temp_value = calculate_min_value(
                    gameState.generateSuccessor(0, action), 0, 1, alpha, beta)
                # if it's greater than current value, update value to be best action
                if value < temp_value:
                    value = temp_value
                    best_action = action
                # if value is greater than beta, return it
                if value > beta:
                    return value
                alpha = max(alpha, temp_value)
            return best_action
        return alpha_beta_prunning(gameState)
        # util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        numberOfAgents = gameState.getNumAgents()
        GhostIndices = []
        for i in range(1, numberOfAgents):
            GhostIndices.append(i)

        def is_terminal_state(state, depth):
            if state.isWin() or state.isLose() or depth == self.depth:
                return True
            else:
                return False

        # returns the expected value corresponding to the ghost move
        def calculate_expected_value(state, depth, ghostIndex):
            if is_terminal_state(state, depth):
                return self.evaluationFunction(state)

            value = 0
            # calculate probability of each action
            probability = 1 / len(state.getLegalActions(ghostIndex))

            # for all legal actions ghost can take:
            for action in state.getLegalActions(ghostIndex):
                # if last ghost, get max value for next depth
                if ghostIndex == GhostIndices[-1]:
                    value += probability * \
                        calculate_max_value(state.generateSuccessor(
                            ghostIndex, action), depth + 1)
                # else get expected value for next ghost
                else:
                    value += probability * calculate_expected_value(
                        state.generateSuccessor(ghostIndex, action), depth, ghostIndex + 1)
            return value

        def calculate_max_value(state, depth):
            if is_terminal_state(state, depth):
                return self.evaluationFunction(state)
            value = -float('inf')
            for action in state.getLegalActions(0):
                value = max(value, calculate_expected_value(
                    state.generateSuccessor(0, action), depth, 1))
            return value

        playerLegalActions = gameState.getLegalActions(0)
        actionExpectedValuePairs = []
        # for all legal actions for player, calculate and add action and its expected value as a pair to the actionExpectedValuePairs list
        for action in playerLegalActions:
            successorGameState = gameState.generateSuccessor(0, action)
            expectedValue = calculate_expected_value(successorGameState, 0, 1)
            actionExpectedValuePairs.append((action, expectedValue))

        def get_expected_value(pair):
            return pair[1]  # expected value from pair

        # sort by expected value and return pair with highest expected value
        actionExpectedValuePairs.sort(key=get_expected_value)
        return actionExpectedValuePairs[-1][0]

# util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: 
    My approach takes into account of two factors, distance to closest food and current game score.
        1. distance to food: agent will move toward nearest food, and its reciprocal is added to the heuristic.
        2. current state score is added directly to the half of heuristic. State with higher score is preferred.
    In general, the final evaluation is the sum of [reciprocal of distance to closest food] and [current game score]. This
    allows pacman to eat as much food as possible while also considering state score.

    """
    "*** YOUR CODE HERE ***"

    pacmanPosition = currentGameState.getPacmanPosition()
    foods = currentGameState.getFood().asList()
    # initialized as an arbitrary large number
    closestFoodDistance = float('inf')

    if foods:   # if there are foods left
        for food in foods:
            # get manhattan distance from current position to each food
            foodDistance = manhattanDistance(pacmanPosition, food)
            # update minimum distance accordingly
            if foodDistance < closestFoodDistance:
                closestFoodDistance = foodDistance
    else:
        closestFoodDistance = 0.1    # if no foods left

    score = currentGameState.getScore() * 0.5
    heuristic = 1.0 / closestFoodDistance + score
    return heuristic
    # util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction
