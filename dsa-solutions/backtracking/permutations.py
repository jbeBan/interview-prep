from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rp = [[]]
        for num in nums:
            np = []
            for p in rp:
                for i in range(len(p) + 1):
                    pc = p.copy()
                    pc.insert(i, num)
                    np.append(pc)
            rp = np
        return rp


# Time Complexity: O(n^2 * n!)
# Space Complexity: O(n^2 * n!)
