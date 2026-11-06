class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int) -> float:
            if not x:
                return 0
            if not n:
                return 1
            r = pow(x * x, n // 2)
            return r * x if n % 2 else r

        r = pow(x, abs(n))
        return r if n >= 0 else 1 / r


# Time Complexity: O(log(n))
# Space Complexity: O(log(n))
