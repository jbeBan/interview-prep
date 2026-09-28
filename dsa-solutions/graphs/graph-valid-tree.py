from collections import deque


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        g = {i: [] for i in range(n)}
        for s, d in edges:
            g[s].append(d)
            g[d].append(s)
        v = {0}
        q = deque([0])
        while q:
            s = q.popleft()
            for d in g[s]:
                if d not in v:
                    q.append(d)
                    v.add(d)
        return len(v) == n


# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
