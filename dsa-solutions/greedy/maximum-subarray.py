class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        m, c = nums[0], 0
        for num in nums:
            c = max(c, 0) + num
            m = max(m, c)
        return m


# Time Complexity: O(n)
# Space Complexity: O(1)
