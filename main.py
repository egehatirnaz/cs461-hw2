"""
	CS461 Fall 2019 Homework 2
	Authors: Faruk Ege Hatırnaz
			 Shabnam Sadigova
			 Sıla İnci
			 Dilara Halavurt
			 Doğukan Aydın

	Date: 	 07.11.2019
"""

from anytree import Node, RenderTree
import heapq
from builder import Builder
from States import States
import queue as Q


def heuristic_func(goal, child):
    goal_str = goal.get_situation()
    goal_x = goal_str[0:1]
    goal_y = goal_str[2:3]

    child_str = child.name
    child_x = child_str[0:1]
    child_y = child_str[2:3]

    boat_capacity = 5

    dx = int(child_x) - int(goal_x)
    dy = int(child_y) - int(goal_y)
    return (dx + dy) / boat_capacity


class NodeWrapper:
    def __init__(self, states, priority):
        self.states = states  # Node
        state_str = str(states.name)  # STR
        self.state_str = state_str
        self.priority = priority

    def __str__(self):
        return self.state_str


class PriorityQueue:

    def __init__(self):
        self.queue = list()

    def insert(self, node):
        if self.size() == 0:
            self.queue.append(node)
        else:
            # traverse the queue to find the right place for new node
            for x in range(0, self.size()):
                # if the priority of new node is greater
                if node.priority >= self.queue[x].priority:
                    # if we have traversed the complete queue
                    if x == (self.size() - 1):
                        # add new node at the end
                        self.queue.insert(x + 1, node)  # changed
                    else:
                        continue
                else:
                    self.queue.insert(x, node)  # changed
                    return True

    def pop(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


def a_star(root, goal):
    #goal_node = Node(goal, -1)
    # Form a one-element queue consisting of a zero length path that contains only the root node.
    queue = PriorityQueue()
    root_node = NodeWrapper(root, 0)
    queue.insert(root_node)

    path = {}
    path_weights = {}
    path[root] = None
    path_weights[root] = 0

    final_path = {}
    final_weight = {}

    while not queue.empty():
        n = queue.pop()  # n -> NodeWrapper

        for child in n.states.children:  # child -> AnyNode
            new_weight = path_weights[n.states] + 1  # every level costs 1
            if child not in path_weights:
                path_weights[child] = new_weight
                priority = new_weight + heuristic_func(goal, child)
                child_node = NodeWrapper(child, priority)
                queue.insert(child_node)
                path[child] = n.states

        if str(n.state_str) == str(goal.get_situation()):
            path[n.states] = n.states
            final_path = path[n.states]
            final_weight = path_weights[n.states]
            break

    return final_path, final_weight


def main():
    b = Builder(6, 6, 1)
    goal = States(0, 0, 0, [])
    root = b.build_tree()
    #print(RenderTree(root))
    path, path_weight = a_star(root, goal)
    print("Shortest path: ", path, "\nPath Weight: ", path_weight)


if __name__ == '__main__':
    main()
