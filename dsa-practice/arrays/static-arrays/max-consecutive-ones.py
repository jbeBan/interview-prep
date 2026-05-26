from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_run: int = 0
        curr_run: int = 0
        for num in nums:
            if num == 0:
                curr_run = 0
            else:
                curr_run += 1
            if curr_run > max_run:
                max_run = curr_run
        return max_run


# Time Complexity: O(n)
# Space Complexity: O(1)
