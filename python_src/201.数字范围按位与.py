#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#
from typing import *

class Solution0:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0: return 0
        d = right - left
        if d == 0: return left
        if d == 1: return left & right

        while True:
            tmp = right & (right - 1)
            if tmp < left: break
            right = tmp
        return right & left

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right
# @lc code=end

s = Solution()
print(s.rangeBitwiseAnd(left = 5, right = 7))
print(s.rangeBitwiseAnd(left = 0, right = 0))
print(s.rangeBitwiseAnd(left = 1, right = 2147483647))

## 0
print(s.rangeBitwiseAnd(left = 1, right = 4))

## 0
print(s.rangeBitwiseAnd(left = 2, right = 6))

## 0
print(s.rangeBitwiseAnd(left = 3, right = 5))

## 0
print(s.rangeBitwiseAnd(5, 8))