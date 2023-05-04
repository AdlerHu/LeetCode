class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format((int(a, base=2) + int(b, base=2)), 'b')


solution = Solution()
print(solution.addBinary(a="11", b="1"))
assert solution.addBinary(a="11", b="1") == '100'
assert solution.addBinary(a="1010", b="1011") == '10101'

print('done')
