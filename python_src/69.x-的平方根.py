#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#
from typing import *
from math import *

class Solution0:
    def mySqrt(self, x: int) -> int:
        if x == 0: return x
        l, r = 1, x
        while r >= l:
            mid = (l + r) >> 1
            tmp = mid * mid
            if tmp < x:
                l = mid + 1
            elif tmp > x:
                r = mid - 1
            else:
                return mid
        return r
        
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 5:
            return x >> 1 if x > 1 else x

        C = x = float(x)
        while True:
            x_i = (x + C / x) / 2
            if x - x_i <= 0.5:
                return int(x_i)
            x = x_i

# @lc code=end

s = Solution()
# print(s.mySqrt(4))
# print(s.mySqrt(8))
print([(i, s.mySqrt(i)) for i in range(64)])
