class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums), nums


solution = Solution()
assert solution.removeDuplicates(nums=[1, 1, 2]) == 2
assert solution.removeDuplicates(
    nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
