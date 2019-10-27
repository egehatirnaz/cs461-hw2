from anytree import Node, RenderTree
import heapq
from builder import Builder
from States import States
import queue as Q


def a_star(root, goal):
    # Form a one-element queue consisting of a zero length path that contains only the root node.
    queue = Q.Queue()
    queue.put(root)
    path = {}
    path_weights = {}
    path[root] = None
    path_weights[root] = 0

    while not queue.empty():
        n = queue.get()

        if n == goal:
            break

        for child in n.children:
            new_weight = path_weights[n] + 1  # every level costs 1
            if child not in path_weights: # or new_weight < path_weights[child]:
                path_weights[child] = new_weight
                priority = new_weight # heuristic_func(goal, child)
                queue.put(child)
                path[child] = n

    return path, path_weights


def main():
    b = Builder(6, 6, 1)
    goal = States(0,0,0, [])
    root = b.build_tree()
    #print(RenderTree(root))
    print(a_star(root, goal))

if __name__ == '__main__':
    main()
