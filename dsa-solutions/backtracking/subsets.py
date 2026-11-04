class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def helper(i, ints, c, s):
            if i >= len(ints):
                s.append(c.copy())
                return
            c.append(ints[i])
            helper(i + 1, ints, c, s)
            c.pop()
            helper(i + 1, ints, c, s)

        c, s = [], []
        helper(0, nums, c, s)
        return s


# Time Complexity: O(2^n)
# Space Complexity: O(n)
