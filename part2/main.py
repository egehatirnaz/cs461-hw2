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


def search(root, goal):
    """
    We have used the breadth-first search algorithm.
    :param root:
    :param goal:
    :return:
    """
    # Form a one-element queue consisting of a zero length path that contains only the root node.
    queue = Q.Queue()
    queue.put(root)

    number_of_shortest_path = 0

    while not queue.empty():
        n = queue.get()

        if n.name == goal.get_situation():
            return number_of_shortest_path

        for child in n.children:
            queue.put(child)
            if child.name == goal.get_situation():
                number_of_shortest_path = number_of_shortest_path + 1

    return number_of_shortest_path


def main():
    b = Builder(4, 4, 1)
    goal = States(0, 0, 0, [])
    root = b.build_tree()
    # print(RenderTree(root))

    print("Number of shortest path from ", root.name, " to ", goal.get_situation(), " is: ", search(root, goal))


if __name__ == '__main__':
    main()
