from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, ints, c, s):
            if i >= len(ints):
                s.append(c.copy())
                return
            c.append(ints[i])
            helper(i + 1, ints, c, s)
            c.pop()
            while i < len(ints) - 1 and ints[i] == ints[i + 1]:
                i += 1
            helper(i + 1, ints, c, s)

        s_nums = sorted(nums)
        c, s = [], []
        helper(0, s_nums, c, s)
        return s


# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)
