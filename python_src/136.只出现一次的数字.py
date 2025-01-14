#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        note: Set[int] = set()
        for n in nums:
            if n in note:
                note.remove(n)
            else:
                note.add(n)
        return note.pop()
        
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        key = 40000
        for n in nums:
            key ^= n
        return key ^ 40000
        
# @lc code=end

s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([1]))
