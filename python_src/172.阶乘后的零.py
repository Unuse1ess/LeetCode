#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
from typing import *
from math import *

class Solution0:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        f = factorial(n)
        ret = 0
        while f % 10 == 0:
            f //= 10
            ret += 1
        return ret
        
class Solution1:
    note: Dict[int, int] = dict()
    for i in range(1, 10001):
        if i % 5 == 0:
            note[i] = note.get(i // 5, 0) + 1

    def trailingZeroes(self, n: int) -> int:
        ret = 0
        for i in range(n + 1):
            if i in Solution.note:
                ret += Solution.note[i]
        return ret

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n > 4:
            n //= 5
            cnt += n
        return cnt
# @lc code=end

s = Solution()
print(s.trailingZeroes(3))
print(s.trailingZeroes(5))
print(s.trailingZeroes(0))

print(s.trailingZeroes(10))

print(s.trailingZeroes(10000))

print(s.trailingZeroes(25))
