from anytree import Node, RenderTree
import heapq
from builder import Builder


class PriorityQueue:
    def _init_(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def put(self, state, priority):
        heapq.heappush(self.queue, (priority, state))

    def pop(self):
        heapq.heappop(self)


def heuristic_func(goal, child):
    return goal  # degisecek


def a_star(anytree, root, goal):
    queue = PriorityQueue()
    queue.put(root, 0)
    path = {}
    path_weights = {}
    path[root] = None
    path_weights[root] = 0

    while not anytree.is_empty:
        n = queue.pop()

        if n == goal:
            break

        for child in n.children:
            new_weight = path_weights[n] + 1  # every level costs 1
            if child not in path_weights or new_weight < path_weights[child]:
                path_weights[child] = new_weight
                priority = new_weight + heuristic_func(goal, child)
                queue.put(child, priority)
                path[child] = n

    return path, path_weights


def main():
    b = Builder(6, 6, 1)
    root = b.build_tree()
    print(RenderTree(root))

if __name__ == '__main__':
    main()
