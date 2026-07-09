from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1] * len(nums)
        pref = 1
        for i in range(len(nums)):
            prods[i] = pref
            pref *= nums[i]
        suff = 1
        for i in range(len(nums) - 1, -1, -1):
            prods[i] *= suff
            suff *= nums[i]
        return prods


# Time Complexity: O(n)
# Space Complexity: O(n)
