from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        ind = {c: 0 for c in range(numCourses)}
        adj = {c: [] for c in range(numCourses)}
        for s, d in prerequisites:
            adj[d].append(s)
            ind[s] += 1
        q = deque()
        for c in ind:
            if ind[c] == 0:
                q.append(c)
        o = []
        while q:
            s = q.popleft()
            o.append(s)
            for d in adj[s]:
                ind[d] -= 1
                if ind[d] <= 0:
                    q.append(d)
        return o if len(o) == numCourses else []


# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
