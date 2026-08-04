from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s1 = f = 0
        while True:
            s1 = nums[s1]
            f = nums[nums[f]]
            if s1 == f:
                break
        s2 = 0
        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]
        return s2


# Time Complexity: O(n)
# Space Complexity: O(1)
