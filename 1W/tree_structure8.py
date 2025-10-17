class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, root):
        self.root = root

    def traverse(self, node, depth=0):
        print("  " * depth + node.value)
        for child in node.children:
            self.traverse(child, depth + 1)

    def __str__(self):
        return "Drzewo z korzeniem: " + self.root.value


root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)
f.add_child(g)

tree = Tree(root)
print(tree)
tree.traverse(tree.root)
