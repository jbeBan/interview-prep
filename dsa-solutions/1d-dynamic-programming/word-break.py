class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if w == s[i : i + len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


# Time Complexity: O(n * m * t) [n: s length, m: wordDict length, t: max word length]
# Space Complexity: O(n) [n: s length]
