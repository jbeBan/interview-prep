import math


class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2147483648, 2147483647
        r = 0
        while x:
            d, x = int(math.fmod(x, 10)), int(x / 10)
            if r > MAX // 10 or (r == MAX // 10 and d > MAX % 10):
                return 0
            if r < MIN // 10 or (r == MIN // 10 and d < MIN % 10):
                return 0
            r = (r * 10) + d
        return r


# Time Complexity: O(1)
# Space Complexity: O(1)
