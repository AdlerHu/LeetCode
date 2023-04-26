class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for symbol in s:
            if not stack:
                stack.append(symbol)
            elif (symbol == ')' and stack[-1] == '(') or (symbol == ']' and stack[-1] == '[') or (symbol == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                stack.append(symbol)

        return not stack


solution = Solution()
assert solution.isValid(s="()") == True
assert solution.isValid(s="()[]{}") == True
assert solution.isValid(s="(]") == False
assert solution.isValid(s="([)]") == False
assert solution.isValid(s="{[]}") == True
