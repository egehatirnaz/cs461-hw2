from anytree import Node, RenderTree


def main():
    root = Node("root")
    left = Node("left", parent=root)
    right = Node("right", parent=root)
    middle = Node("middle", parent=root)

    print(RenderTree(root))


if __name__ == '__main__':
    main()
