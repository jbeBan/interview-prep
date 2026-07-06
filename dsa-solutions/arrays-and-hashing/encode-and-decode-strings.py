from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        e_chars = []
        for s in strs:
            e_chars.append(str(len(s)))
            e_chars.append("#")
            e_chars.append(s)
        return "".join(e_chars)

    def decode(self, s: str) -> List[str]:
        d_strs = []
        i = 0
        while i < len(s):
            count = 0
            while s[i] != "#":
                digit = int(s[i])
                count *= 10
                count += digit
                i += 1
            i += 1
            d_strs.append(s[i : i + count])
            i += count
        return d_strs


# Time Complexity: O(n + m) [n: s length, m: total character count]
# Space Complexity: O(n + m) [n: s length, m: total character count]
