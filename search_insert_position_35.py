class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)


solution = Solution()
assert solution.searchInsert(nums=[1, 3, 5, 6], target=5) == 2
assert solution.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
assert solution.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
assert solution.searchInsert(nums=[1, 3], target=3) == 1

print('done')
