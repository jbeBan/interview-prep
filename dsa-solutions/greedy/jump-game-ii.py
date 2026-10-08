class Solution:
    def jump(self, nums: list[int]) -> int:
        n = 0
        l = r = 0
        while r < len(nums) - 1:
            e = -1
            for i in range(l, r + 1):
                e = max(e, i + nums[i])
            l, r = r + 1, e
            n += 1
        return n


# Time Complexity: O(n)
# Space Complexity: O(1)
