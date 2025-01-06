#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import *
from itertools import *
from functools import *
from operator import *

class Solution0:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(1, len(digits) + 1):
            n = digits[-i] + carry
            carry = n >= 10
            n %= 10
            digits[-i] = n
        if carry:
            digits.insert(0, 1)
        return digits
        
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(1 + int(reduce(add, map(str, digits))))))
# @lc code=end

s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([9]))
print(s.plusOne([9,9,9,9]))
print(s.plusOne([9,0,9,9]))
print(s.plusOne([0]))
