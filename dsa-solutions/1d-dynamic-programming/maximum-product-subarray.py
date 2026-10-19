class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        mp = nums[0]
        cmin, cmax = 1, 1
        for num in nums:
            t = cmax * num
            cmax = max(num, num * cmin, t)
            cmin = min(num, num * cmin, t)
            mp = max(mp, cmax)
        return mp


# Time Complexity: O(n)
# Space Complexity: O(1)
