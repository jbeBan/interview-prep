class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [amount + 1] * (amount + 1)
        d[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    d[a] = min(d[a], 1 + d[a - c])
        return d[amount] if d[amount] <= amount else -1


# Time Complexity: O(n * m) [n: coins length, m: amount]
# Space Complexity: O(m) [m: amount]
