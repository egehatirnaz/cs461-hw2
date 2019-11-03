from anytree import Node, RenderTree
import heapq
from builder import Builder
from States import States
import queue as Q


def heuristic_func(goal, child):
    return 1


class Node:
    def __init__(self, States, priority):
        self.States = States
        self.priority = priority


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
    root_node = Node(root, 0)
    queue.insert(root_node)

    path = {}
    path_weights = {}
    path[root] = None
    path_weights[root] = 0

    while not queue.empty():
        n = queue.pop()
        n_state = n.States
        print(n_state)
        #print("nstate str:", str(n_state.get_situation()))
        print("goal state str:", str(goal.get_situation()))

        # if str(n_state) == str(goal.get_situation()):
        #     break

        # for child in n_state.children:
        #     new_weight = path_weights[n_state] + 1  # every level costs 1

        #     if child not in path_weights:
        #         path_weights[child] = new_weight
        #         # print(path_weights)
        #         priority = new_weight + heuristic_func(goal, child)
        #         child_node = Node(child, priority)
        #         print(child_node.state)
        #         print(child_node.priority)
        #         queue.insert(child_node)
        #         path[child] = n_state

    return path, path_weights


def main():
    b = Builder(6, 6, 1)
    goal = States(0, 0, 0, [])
    root = b.build_tree()
    # print(RenderTree(root))
    a_star(root, goal)


if __name__ == '__main__':
    main()
