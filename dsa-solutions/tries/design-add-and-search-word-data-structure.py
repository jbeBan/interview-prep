from dataclasses import dataclass, field


@dataclass
class Node:
    is_word: bool = False
    nodes: dict[str, "Node"] = field(default_factory=dict)


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.nodes:
                n.nodes[c] = Node()
            n = n.nodes[c]
        n.is_word = True

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def search(self, word: str) -> bool:
        def rsearch(i: int, n: Node) -> bool:
            if i >= len(word):
                return n.is_word
            c = word[i]
            if c not in n.nodes and c != ".":
                return False
            if c != ".":
                return rsearch(i + 1, n.nodes[c])
            for node in n.nodes.values():
                if rsearch(i + 1, node):
                    return True
            return False

        return rsearch(0, self.root)

    # Time Complexity: O(n) [max two dots in word, lowercase english letters only]
    # Space Complexity: O(n)
