from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m_num = -1
        count = 0
        for num in nums:
            if count == 0:
                m_num = num
            count += 1 if num == m_num else -1
        return m_num


# Time Complexity: O(n)
# Space Complexity: O(1)
