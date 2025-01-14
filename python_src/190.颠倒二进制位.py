#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#
from typing import *

class Solution0:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res |= ((n >> (31 - i)) & 1) << i
        return res
        
# @lc code=start
class Solution:
    m1 = 0x55555555
    m2 = 0x33333333
    m4 = 0x0f0f0f0f
    m8 = 0x00ff00ff

    def reverseBits(self, n: int) -> int:
        n = ((n << 1) & (Solution.m1 << 1)) | ((n >> 1) & Solution.m1)
        n = ((n << 2) & (Solution.m2 << 2)) | ((n >> 2) & Solution.m2)
        n = ((n << 4) & (Solution.m4 << 4)) | ((n >> 4) & Solution.m4)
        n = ((n << 8) & (Solution.m8 << 8)) | ((n >> 8) & Solution.m8)
        return ((n << 16) | (n >> 16)) & 0xffffffff
# @lc code=end

s = Solution()
print(s.reverseBits(43261596))
print(s.reverseBits(4294967293))
