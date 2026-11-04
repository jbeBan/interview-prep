class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diff_map:
                return [diff_map[diff], i]
            diff_map[num] = i


# Time Complexity: O(n)
# Space Complexity: O(n)
