from dataclasses import dataclass, field


@dataclass
class Node:
    value: str
    is_word: bool = False
    nodes: dict[str, "Node"] = field(default_factory=dict)


class PrefixTree:
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.nodes:
                n.nodes[c] = Node(c)
            n = n.nodes[c]
        n.is_word = True

    def search(self, word: str) -> bool:
        n = self.root
        for c in word:
            if c not in n.nodes:
                return False
            n = n.nodes[c]
        return n.is_word

    def startsWith(self, prefix: str) -> bool:
        n = self.root
        for c in prefix:
            if c not in n.nodes:
                return False
            n = n.nodes[c]
        return True
