class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        t = r = 0
        for i in range(len(gas)):
            t += gas[i] - cost[i]
            if t < 0:
                r = (i + 1) % len(gas)
                t = 0
        return r


# Time Complexity: O(n)
# Space Complexity: O(1)
