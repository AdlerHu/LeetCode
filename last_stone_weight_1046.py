class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()
        while stones:
            most_heaviest_stone = stones.pop()

            # most_heaviest_stone is the remaining stone
            if not stones:
                return most_heaviest_stone

            second_heaviest_stone = stones.pop()

            if most_heaviest_stone > second_heaviest_stone:
                for i in range(len(stones)+1):
                    if i == len(stones) or stones[i] >= most_heaviest_stone-second_heaviest_stone:
                        stones.insert(i, most_heaviest_stone -
                                      second_heaviest_stone)
                        break
        return 0


s = Solution()
assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
assert s.lastStoneWeight([1]) == 1
assert s.lastStoneWeight([2, 2]) == 0
assert s.lastStoneWeight([1, 3]) == 2

print('done')
