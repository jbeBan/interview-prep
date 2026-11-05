class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(x: int) -> int:
            t = 0
            while x:
                t += (x % 10) ** 2
                x //= 10
            return t

        s, f = n, squareSum(n)
        while s != f:
            s = squareSum(s)
            f = squareSum(squareSum(f))
        return True if f == 1 else False


# Time Complexity: O(log(n))
# Space Complexity: O(1)
