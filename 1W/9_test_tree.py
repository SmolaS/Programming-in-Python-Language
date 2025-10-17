import unittest
from tree_structure8 import Node, Tree

class TestTreeStructure(unittest.TestCase):
    def test_tree_structure(self):
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

        self.assertEqual(tree.root.value, "A")
        self.assertEqual(
            [child.value for child in tree.root.children],
            ["B", "C"]
        )
        self.assertEqual(
            [child.value for child in b.children],
            ["D", "E"]
        )
        self.assertEqual(
            [child.value for child in c.children],
            ["F"]
        )
        self.assertEqual(
            [child.value for child in f.children],
            ["G"]
        )

if __name__ == "__main__":
    unittest.main()
