class Solution:
    def checkValidString(self, s: str) -> bool:
        ls, ss = [], []
        for i, c in enumerate(s):
            if c == "(":
                ls.append(i)
            elif c == "*":
                ss.append(i)
            else:
                if not ls and not ss:
                    return False
                if ls:
                    ls.pop()
                else:
                    ss.pop()
        while ls and ss:
            if ls.pop() > ss.pop():
                return False
        return not ls


# Time Complexity: O(n)
# Space Complexity: O(n)
