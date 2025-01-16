#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
from typing import *


class Solution0:
    def singleNumber(self, nums: List[int]) -> int:
        hist = Counter(nums)
        for i in hist:
            if hist[i] == 1:
                return i

"""
Truth table:
a   b   n | b'  a'
__________|_______
0   0   0 | 0   0
0   0   1 | 1   0
0   1   0 | 1   0
0   1   1 | 0   1
1   0   0 | 0   1
1   0   1 | 0   0

Written in SOP
"""

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for n in nums:
            b = ~a & (b ^ n)
            a = ~b & (a ^ n)
        return b

# @lc code=end

s = Solution()
print(s.singleNumber([2,2,3,2]))
print(s.singleNumber([0,1,0,1,0,1,99]))
print(s.singleNumber([1,2,1,2,10,3,3,3,1,2]))
print(s.singleNumber([1,2,0,1,2,0,3,3,3,1,2,0,-9]))

# 29856
print(s.singleNumber([3,5,1,3,1,3,1]))

# print(s.singleNumber([1]))
# print(s.singleNumber([1, 1]))
# print(s.singleNumber([1, 1, 1]))
# print(s.singleNumber([1, 1, 1, 1]))