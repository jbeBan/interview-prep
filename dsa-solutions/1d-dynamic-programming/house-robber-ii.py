class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def r(nums: list[int]):
            p, c = 0, 0
            for num in nums:
                p, c = c, max(c, p + num)
            return c

        return max(r(nums[:-1]), r(nums[1:]))


# Time Complexity: O(n)
# Space Complexity: O(1)
