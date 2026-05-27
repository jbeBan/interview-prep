from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        beg_idx = 0
        end_idx = len(nums)
        while beg_idx < end_idx:
            if nums[beg_idx] == val:
                nums[beg_idx] = nums[end_idx - 1]
                end_idx -= 1
            else:
                beg_idx += 1
        return end_idx


# Time Complexity: O(n)
# Space Complexity: O(1)
