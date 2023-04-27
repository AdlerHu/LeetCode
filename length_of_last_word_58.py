class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])


solution = Solution()
assert solution.lengthOfLastWord(s="Hello World") == 5
assert solution.lengthOfLastWord(s="   fly me   to   the moon  ") == 4
assert solution.lengthOfLastWord(s="luffy is still joyboy") == 6

print('done')
