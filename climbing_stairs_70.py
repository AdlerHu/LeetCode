class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            s1, s2 = 1, 2
            for i in range(n-2):
                s1, s2 = s2, s1+s2
            return s2


solution = Solution()
assert solution.climbStairs(n=1) == 1
assert solution.climbStairs(n=2) == 2
assert solution.climbStairs(n=3) == 3
assert solution.climbStairs(n=4) == 5
print('done')
