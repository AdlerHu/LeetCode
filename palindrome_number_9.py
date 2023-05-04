class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            reversed = 0
            origin = x
            while x != 0:
                reversed = reversed * 10 + x % 10
                x = x // 10
            return reversed == origin
        return False


s = Solution()
assert s.isPalindrome(121) is True
assert s.isPalindrome(-121) is False
assert s.isPalindrome(10) is False
assert s.isPalindrome(20) is False
assert s.isPalindrome(0) is True

print('Done')
