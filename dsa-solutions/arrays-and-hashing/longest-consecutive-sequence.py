from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 in nums_set:
                continue
            length = 1
            while num + length in nums_set:
                length += 1
            longest = max(longest, length)
        return longest


# Time Complexity: O(n)
# Space Complexity: O(n)
