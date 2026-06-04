from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            char_counts = [0] * 26
            for char in string:
                char_counts[ord(char) - ord("a")] += 1
            anagrams[tuple(char_counts)].append(string)
        return list(anagrams.values())


# Time Complexity: O(n * m) [n: strs length, m: longest string length]
# Space Complexity: O(n * m) [n: strs length, m: longest string length]
