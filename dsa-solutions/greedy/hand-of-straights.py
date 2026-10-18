from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        c = Counter(hand)
        sh = sorted(hand)
        for h in sh:
            if not c[h]:
                continue
            for i in range(h, h + groupSize):
                if not c[i]:
                    return False
                c[i] -= 1
        return True


# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
