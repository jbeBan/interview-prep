from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        freqs = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freqs[count].append(num)
        top_k = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k


# Time Complexity: O(n)
# Space Complexity: O(n)
