from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        m_ps = sorted(list(zip(position, speed)), reverse=True)
        for p, s in m_ps:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)


# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
