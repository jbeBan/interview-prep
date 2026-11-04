class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                break
        return [l + 1, r + 1]


# Time Complexity: O(n)
# Space Complexity: O(1)
