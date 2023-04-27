class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif digits == [9]:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits=digits[:-1])
            return digits


solution = Solution()
print(solution.plusOne(digits=[1, 2, 3]))
assert solution.plusOne(digits=[1, 2, 3]) == [1, 2, 4]
assert solution.plusOne(digits=[4, 3, 2, 1]) == [4, 3, 2, 2]
assert solution.plusOne(digits=[9]) == [1, 0]

print('done')
