#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#
from typing import *

class Solution0:
    m1 = 0xaaaaaaaa
    m2 = 0xcccccccc
    m4 = 0xf0f0f0f0
    m8 = 0xff00ff00

    def hammingWeight(self, n: int) -> int:
        n = ((n & Solution.m1) >> 1) + (n & (Solution.m1 >> 1))
        n = ((n & Solution.m2) >> 2) + (n & (Solution.m2 >> 2))
        n = ((n & Solution.m4) >> 4) + (n & (Solution.m4 >> 4))
        n = ((n & Solution.m8) >> 8) + (n & (Solution.m8 >> 8))
        return ((n >> 16) & 0xffff) + (n & 0xffff)
        
class Solution1:
    def hammingWeight(self, n: int) -> int:
        return sum(
            map(
                int,
                list(f"{n:b}")
            )
        )

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
# @lc code=end

s = Solution()
print(s.hammingWeight(11))
print(s.hammingWeight(128))
print(s.hammingWeight(2147483645))
