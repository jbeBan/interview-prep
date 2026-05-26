from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums: set[int] = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        return False


# Time Complexity: O(n)
# Space Complexity: O(n)
