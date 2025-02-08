#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
from typing import *

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        if size == 1:
            return n <= 1 and ((not flowerbed[0]) or (not n))

        cnt = 0
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            cnt += 1

        for i in range(1, size - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                cnt += 1
            if cnt >= n:
                return True
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            cnt += 1

        return cnt >= n

# @lc code=end

s = Solution()
print(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))

## true
print(s.canPlaceFlowers([1,0,0,0,1,0,0], 2))

print(s.canPlaceFlowers([0], 1))
print(s.canPlaceFlowers([1], 1))
print(s.canPlaceFlowers([0], 0))
print(s.canPlaceFlowers([1], 0))

# print(s.canPlaceFlowers([0, 0], 0))
# print(s.canPlaceFlowers([0, 0], 1))
# print(s.canPlaceFlowers([0, 0], 2))

# print(s.canPlaceFlowers([1, 0], 0))
# print(s.canPlaceFlowers([1, 0], 1))
# print(s.canPlaceFlowers([1, 0], 2))