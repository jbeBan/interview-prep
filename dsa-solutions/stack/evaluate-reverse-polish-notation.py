from operator import add, sub, mul, truediv


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+": add, "-": sub, "*": mul, "/": truediv}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            rh = stack.pop()
            lh = stack.pop()
            result = operators[token](lh, rh)
            stack.append(int(result) if token == "/" else result)
        return stack.pop()


# Time Complexity: O(n)
# Space Complexity: O(n)
