class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        cs = []
        sn = sorted(candidates)

        def comb_sum(i: int, s: int, c: list[int]):
            if s == target:
                cs.append(c.copy())
            if s >= target:
                return
            for j in range(i, len(sn)):
                if j > i and sn[j] == sn[j - 1]:
                    continue
                c.append(sn[j])
                comb_sum(j + 1, s + c[-1], c)
                c.pop()

        comb_sum(0, 0, [])
        return cs


# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)
