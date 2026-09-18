from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cs = []
        sn = sorted(nums)

        def comb_sum(i, s, c):
            if s == target:
                cs.append(c.copy())
                return
            for j in range(i, len(sn)):
                if s + sn[j] > target:
                    return
                c.append(sn[j])
                comb_sum(j, s + sn[j], c)
                c.pop()

        comb_sum(0, 0, [])
        return cs


# Time Complexity: O(n^t/m) [t: target, m: nums min value]
# Space Complexity: O(t/m) [t: target, m: nums min value]
