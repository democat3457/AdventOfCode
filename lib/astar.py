from __future__ import annotations
from typing import Callable, Generic, TypeVar

# Credit for this: Nicholas Swift
# as found at https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
from warnings import warn
import heapq

from .coords import Coor
from .grid import Grid

__all__ = ["Node", "astar"]

T = TypeVar("T")

class Node(Generic[T]):
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent: Node[T]|None=None, position: T=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other: Node):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other: Node):
      return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other: Node):
      return self.f > other.f

def return_path(current_node: Node[T]) -> list[T]:
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(
    maze: Grid,
    start: Coor,
    end: Coor,
    adjacency_check: Callable[[Coor, Coor], bool] = (lambda _,_a: True),
    heuristic_func: Callable[[Coor, Coor], int] = (lambda x, y: (x - y).hypot()),
    *,
    check_diagonals: bool = False,
) -> list[Coor] | None:
    """
    Runs the A* path-planning algorithm on a given maze using the provided functions to customize its behavior.
    :param maze:    The grid / maze
    :param start:   The starting coordinate
    :param end:     The ending coordinate
    :param adjacency_check:     Returns whether a possible location is valid. First parameter is the current coordinate, second parameter is the tentative coordinate
    :param heuristic_func:      Returns the heuristic value for a node. First parameter is the current coordinate, second parameter is the end coordinate. Return 0 for Djikstra's
    :return:        None if a path cannot be found, or a list of coordinates as a path from start to end (inclusive) in the maze
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list: list[Node[Coor]] = []
    closed_list: list[Node[Coor]] = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (maze.height * maze.width * 3)

    # what squares do we search
    adjacent_squares = Grid.adjacent()
    if check_diagonals:
        adjacent_squares = Grid.adjacent_diagonal()

    # Loop until you find the end
    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
            # if we hit this point return the path such as it is
            # it will not contain the destination
            warn("giving up on pathfinding too many iterations")
            return return_path(current_node)       

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children: list[Node[Coor]] = []

        for new_position in adjacent_squares: # Adjacent squares

            # Get node position
            node_position = current_node.position + new_position

            # Make sure within range
            if node_position not in maze:
                # print('out range')
                continue

            # Make sure walkable terrain
            if not adjacency_check(current_node.position, node_position):
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = heuristic_func(child.position, end_node.position)
            child.f = child.g + child.h

            # Child is already in the open list
            if any(map(lambda open_node: child.position == open_node.position and child.g > open_node.g, open_list)):
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    warn("Couldn't get a path to destination")
    return None
