from stack import Stack
from queue_1 import Queue
from node import Node


def dfs(initial, goal_test, successors):
    """
    Find the goal state using depth-first search.
    :param initial: Initial state.
    :param goal_test: Callable for checking if the goal is met.
    :param successors: Callable for generating a list of successor states.
    :return: A node representing the goal state, else none if goal was not found.
    """
    frontier = Stack()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


def bfs(initial, goal_test, successors):
    """
    Find the goal state using breadth-first search.
    :param initial: Initial state.
    :param goal_test: Callable for checking if the goal is met.
    :param successors: Callable for generating a list of successors states.
    :return: A node representing the goal state, else None if goal was not found.
    """
    frontier = Queue()
    frontier.push(Node(initial, None))
    explored = {initial}
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def node_to_path(node):
    """
    Generate a list of states that lead from the initial state to the goal state.
    :param node: A generic node.
    :return: A list of states.
    """
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
