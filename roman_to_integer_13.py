class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {'M': 1000,
                       'D': 500,
                       'C': 100,
                       'L': 50,
                       'X': 10,
                       'V': 5,
                       'I': 1}
        sum = symbol_dict[s[-1]]
        for i in range(len(s)-1):
            if symbol_dict[s[i]] < symbol_dict[s[i+1]]:
                sum -= symbol_dict[s[i]]
            else:
                sum += symbol_dict[s[i]]
        return sum


solution = Solution()
assert solution.romanToInt(s='III') == 3
assert solution.romanToInt(s='LVIII') == 58
assert solution.romanToInt(s='MCMXCIV') == 1994
print('done')
