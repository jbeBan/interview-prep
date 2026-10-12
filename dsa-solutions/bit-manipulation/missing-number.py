class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        m = len(nums)
        for i in range(len(nums)):
            m ^= i ^ nums[i]
        return m

# Time Complexity: O(n)
# Space Complexity: O(1)
