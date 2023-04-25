class Solution:
    def twoSum(self, nums: 'list[int]', target: 'int') -> 'list[int]':
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict.get(target - num), i]
            else:
                num_dict[num] = i

        return -1


s = Solution()
assert s.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert s.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
assert s.twoSum(nums=[3, 3], target=6) == [0, 1]
assert s.twoSum(nums=[2, 3, 5, 7, 11, 15], target=9) == [0, 3]
assert s.twoSum(nums=[1, 2, 3, 4, 5], target=20) == -1
print('done')
