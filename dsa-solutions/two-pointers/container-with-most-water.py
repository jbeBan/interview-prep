class Solution:
    def maxArea(self, heights: list[int]) -> int:
        m, l, r = 0, 0, len(heights) - 1
        while l < r:
            m = max(m, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return m


# Time Complexity: O(n)
# Space Complexity: O(1)
