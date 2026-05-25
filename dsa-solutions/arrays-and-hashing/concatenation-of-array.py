from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        ans = [0] * (2 * nums_length)
        for i in range(nums_length):
            ans[i] = nums[i]
            ans[i + nums_length] = nums[i]
        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)
