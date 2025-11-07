class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []


class AhoCorasick:
    def __init__(self, wzorce):
        self.root = Node()
        self._build_trie(wzorce)
        self._build_fail_links()

    def _build_trie(self, wzorce):
        for wzorzec in wzorce:
            node = self.root
            for litera in wzorzec:
                if litera not in node.children:
                    node.children[litera] = Node()
                node = node.children[litera]
            node.output.append(wzorzec)

    def _build_fail_links(self):
        queue = []

        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            node = queue.pop(0)

            for litera, child in node.children.items():
                queue.append(child)

                fail = node.fail
                while fail and litera not in fail.children:
                    fail = fail.fail

                if fail and litera in fail.children:
                    child.fail = fail.children[litera]
                else:
                    child.fail = self.root

                if child.fail.output:
                    child.output += child.fail.output

    def szukaj(self, tekst):
        node = self.root
        znalezione = []

        for i, litera in enumerate(tekst):
            while node and litera not in node.children:
                node = node.fail

            if not node:
                node = self.root
                continue

            node = node.children[litera]

            for wzorzec in node.output:
                pozycja = i - len(wzorzec) + 2
                znalezione.append((wzorzec, pozycja))

        return znalezione


# Test
if __name__ == "__main__":
    wzorce = ["ala", "kot", "pies", "ma", "i"]
    tekst = "ala ma kota i pies biega za kotem"

    ac = AhoCorasick(wzorce)
    wynik = ac.szukaj(tekst)

    print("Znalezione wzorce:")
    for w, p in wynik:
        print(f"- '{w}' na pozycji {p}")
