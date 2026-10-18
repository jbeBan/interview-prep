class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        p = l
        l, r = 0, len(nums) - 1
        if target >= nums[p] and target <= nums[r]:
            l = p
        else:
            r = p - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


# Time Complexity: O(log(n))
# Space Complexity: O(1)
