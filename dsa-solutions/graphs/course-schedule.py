from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        ind = {i: 0 for i in range(numCourses)}
        adj = {i: [] for i in range(numCourses)}
        for s, d in prerequisites:
            adj[s].append(d)
            ind[d] += 1
        q = deque()
        for n, c in ind.items():
            if c == 0:
                q.append(n)
        f = 0
        while q:
            s = q.popleft()
            f += 1
            for d in adj[s]:
                ind[d] -= 1
                if ind[d] == 0:
                    q.append(d)
        return f == numCourses


# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
