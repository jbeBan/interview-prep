from dataclasses import dataclass


@dataclass
class Node:
    val: int
    neighbors: list["Node"]


class Solution:
    def cloneGraph(self, node: "Node" | None) -> "Node" | None:
        def dfs(on: "Node", otn: dict["Node", "Node"]) -> "Node":
            if on in otn:
                return otn[on]
            nn = Node(on.val, [])
            otn[on] = nn
            for n in on.neighbors:
                nn.neighbors.append(dfs(n, otn))
            return nn

        return dfs(node, {}) if node else None


# Time Complexity: O(V + E)
# Space Complexity: O(V)
