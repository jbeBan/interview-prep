class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        m_profit = 0
        l = 0
        for r in range(1, len(prices)):
            diff = prices[r] - prices[l]
            m_profit = max(diff, m_profit)
            if prices[r] < prices[l]:
                l = r
        return m_profit


# Time Complexity: O(n)
# Space Complexity: O(1)
