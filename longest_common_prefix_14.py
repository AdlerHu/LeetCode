class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        if (len(strs) == 0) :
            return ''

        # 長度最短的string
        ans = min(strs, key=len)

        while len(ans):
            if len([s for s in strs if s.startswith(ans)]) == len(strs):
                return ans
            ans = ans[:-1]

        return ''


solution = Solution()
assert solution.longestCommonPrefix(strs=["flower", "flow", "flight"]) == 'fl'
assert solution.longestCommonPrefix(strs=["dog", "racecar", "car"]) == ''
assert solution.longestCommonPrefix(strs=['']) == ''
assert solution.longestCommonPrefix(strs=['a']) == 'a'

print('done')
