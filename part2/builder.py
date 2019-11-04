"""
	CS461 Fall 2019 Homework 2
	Authors: Faruk Ege Hatırnaz
			 Shabnam Sadigova
			 Sıla İnci
			 Dilara Halavurt
			 Doğukan Aydın

	Date: 	 07.11.2019
"""

from anytree import Node, RenderTree, NodeMixin
from anytree.exporter import DotExporter
from States import States


class Builder:
    def __init__(self, x, y, b):
        self.root = Node(str(x) + "M" + str(y) + "C" + str(b))
        self.root_state = States(x, y, b, [])

    def build(self, root, path):
        situation = root.name
        x = int(situation[0:1])
        y = int(situation[2:3])
        b = int(situation[4:])
        state = States(x, y, b, path)
        children = self.get_state_children(state)
        for child in children:
            #child_state = States(child[0], child[1], child[2], state.get_path())
            c = Node(str(child[0]) + "M" + str(child[1]) +
                     "C" + str(child[2]), parent=root)
            self.build(c, state.get_path())
        return root

    def build_tree(self):
        return self.build(self.root, [])

    def get_state_children(self, state):
        return state.get_next_action()


if __name__ == '__main__':
    b = Builder(4, 4, 1)
    root = b.build_tree()
    print(RenderTree(root))
    # DotExporter(root).to_picture("root.png")
    # print(b.get_state_children(b.root_state))
