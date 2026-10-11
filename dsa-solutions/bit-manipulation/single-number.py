class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        r = 0
        for num in nums:
            r ^= num
        return r


# Time Complexity: O(n)
# Space Complexity: O(1)
