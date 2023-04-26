class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


solution = Solution()

print(solution.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))

# assert solution.removeElement(nums=[3, 2, 2, 3], val=3) == [2, 2]
# assert solution.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2) == [
#     0, 1, 3, 0, 4]
