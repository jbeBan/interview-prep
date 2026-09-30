class Solution:
    def rob(self, nums: list[int]) -> int:
        r2, r1 = 0, 0
        for num in nums:
            r2, r1 = r1, max(num + r2, r1)
        return r1


# Time Complexity: O(n)
# Space Complexity: O(1)
