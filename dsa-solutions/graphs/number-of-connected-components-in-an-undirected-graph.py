from collections import deque


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        g = [[] for _ in range(n)]
        for s, d in edges:
            g[s].append(d)
            g[d].append(s)

        def bfs(s: int, v: set[int]) -> None:
            v.add(s)
            q = deque([s])
            while q:
                a = q.popleft()
                for b in g[a]:
                    if b in v:
                        continue
                    q.append(b)
                    v.add(b)

        c = 0
        v = set()
        for s in range(n):
            if s in v:
                continue
            bfs(s, v)
            c += 1
        return c


# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
