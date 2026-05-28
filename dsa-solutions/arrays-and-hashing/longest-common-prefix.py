from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        prefix_len = len(shortest)
        for string in strs:
            for i in range(prefix_len):
                if string[i] != shortest[i]:
                    prefix_len = i
                    break
        return shortest[:prefix_len]


# Time Complexity: O(n * m) [n: strs length, m: shortest string length]
# Space Complexity: O(m) [m: shortest string length]
