from dataclasses import dataclass


@dataclass
class Node:
    key: int
    value: int
    prev: "Node" | None = None
    next: "Node" | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self.c = capacity
        self.d = {}
        self.l, self.r = Node(-1, -1), Node(-1, -1)
        self.l.next, self.r.prev = self.r, self.l

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.remove(self.d[key])
        self.insert(self.d[key])
        return self.d[key].value

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key] = Node(key, value)
        self.insert(self.d[key])
        if len(self.d) > self.c:
            lru = self.l.next
            self.remove(lru)
            del self.d[lru.key]

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next, n.prev = n, p

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def insert(self, node: Node) -> None:
        p, n = self.r.prev, self.r
        p.next = n.prev = node
        node.prev, node.next = p, n

        # Time Complexity: O(1)
        # Space Complexity: O(1)
