#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
from typing import *


class Solution0:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.: return 0.
        if n < 0: return self.myPow(1 / x, -n)
        if n == 0: return 1.

        e = n >> 1
        tmp = self.myPow(x, e)

        return tmp * tmp * (x if n & 1 == 1 else 1.)
        
# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.: return 0.
        if n < 0: return self.myPow(1 / x, -n)
        if n == 0: return 1.

        res = 1.
        prod = x
        while n > 0:
            if n & 1 == 1:
                res *= prod
            prod *= prod
            n >>= 1

        return res
        
# @lc code=end

s = Solution()
print(s.myPow(2., 10))
print(s.myPow(2.1, 3))
print(s.myPow(2., -2))
print(s.myPow(2., -200000000))
