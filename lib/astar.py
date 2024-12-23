from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

# Credit for this: Nicholas Swift
# as found at https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
from warnings import warn
import heapq

from .coords import Coor
from .grid import Grid

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

    @property
    def f(self):
        return self.g + self.h

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

def _return_path(current_node: Node[T]) -> list[T]:
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


@dataclass
class MazeState(Generic[T]):
    cur_pos: Coor
    cur_val: T
    adj_pos: Coor
    adj_val: T
    start_pos: Coor
    start_val: T
    end_pos: Coor
    end_val: T


def adj_valid_if_not(obstacle: T):
    def is_adj_valid(maze_state: MazeState[T]):
        return maze_state.adj_val != obstacle
    return is_adj_valid

def heur_dijkstras():
    def heuristic_func(adj_coor: Coor, end_coor: Coor):
        return 0
    return heuristic_func

def heur_hypot():
    def heuristic_func(adj_coor: Coor, end_coor: Coor):
        return (end_coor - adj_coor).hypot()
    return heuristic_func

def heur_manhattan():
    def heuristic_func(adj_coor: Coor, end_coor: Coor):
        diff = abs(end_coor - adj_coor)
        return diff.x + diff.y
    return heuristic_func


def astar(
    maze: Grid[T],
    start: Coor,
    end: Coor,
    is_adj_valid: Callable[[MazeState[T]], bool],
    edge_weight: Callable[[MazeState[T]], float] = (lambda state: 1),
    heuristic_func: Callable[[Coor, Coor], float] = heur_manhattan(),
    *,
    check_diagonals: bool = False,
    max_iters_func: Callable[[Grid[T]], int] = (lambda grid: grid.height * grid.width * 3),
) -> list[Coor] | None:
    """
    Runs the A* path-planning algorithm on a given maze using the provided functions to customize its behavior.
    :param maze:    The grid / maze
    :param start:   The starting coordinate
    :param end:     The ending coordinate
    :param is_adj_valid:    Returns whether an adjacent coordinate is valid. Parameters are (maze state)
    :param edge_weight:     Returns the edge weight to add to an adjacent node. Parameters are (maze state)
    :param heuristic_func:  Returns the heuristic value for an adjacent node. Parameters are (adjacent coordinate, end coordinate)
    :param check_diagonals: Whether to additionally traverse adjacent diagonals to a coordinate
    :param max_iters_func:  Returns the maximum possible number of algorithm iterations before concluding no path found
    :return:        None if a path cannot be found, or a list of coordinates as a path from start to end (inclusive) in the maze
    """

    def _create_maze_state(cur_pos, adj_pos):
        return MazeState(cur_pos, maze[cur_pos], adj_pos, maze[adj_pos], start, maze[start], end, maze[end])

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = 0

    # Initialize both open and closed list
    open_list: list[Node[Coor]] = []
    closed_list: set[Coor] = set()

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = max_iters_func(maze)

    # what squares do we search
    adjacent_squares = Grid.adjacent()
    if check_diagonals:
        adjacent_squares = Grid.adjacent_diagonal()

    # Loop until you find the end
    while len(open_list):
        outer_iterations += 1

        if outer_iterations > max_iterations:
            # if we hit this point return the path as it is
            # it will not contain the destination
            warn("giving up on pathfinding too many iterations")
            return _return_path(current_node)       

        # Get the current node
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position

        # Ensure node has not been visited yet
        if current_pos in closed_list:
            continue
        closed_list.add(current_pos)

        # Found the goal
        if current_pos == end:
            return _return_path(current_node)

        # Loop over adjacent squares and add new nodes to the queue
        for new_position in adjacent_squares:

            # Get node position
            node_position = current_pos + new_position

            # Make sure within range
            if node_position not in maze:
                continue

            # Make sure child has not been visited yet
            if node_position in closed_list:
                continue

            # Create maze state
            maze_state = _create_maze_state(current_pos, node_position)

            # Make sure walkable terrain
            if not is_adj_valid(maze_state):
                continue

            # Create new node
            child = Node(current_node, node_position)

            # Create the g and h values
            child.g = current_node.g + edge_weight(maze_state)
            child.h = heuristic_func(node_position, end)

            # Child is already in the open list
            if any(map(lambda open_node: child.position == open_node.position and child.g > open_node.g, open_list)):
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    warn("Couldn't get a path to destination")
    return None
