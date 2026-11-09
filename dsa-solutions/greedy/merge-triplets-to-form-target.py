class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        a = b = c = False
        for t in triplets:
            a |= t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]
            b |= t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2]
            c |= t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2]
            if a and b and c:
                return True
        return False


# Time Complexity: O(n)
# Space Complexity: O(1)
