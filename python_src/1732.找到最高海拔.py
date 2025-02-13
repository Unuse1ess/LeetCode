#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#
from typing import *

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        al = 0
        ret = 0
        for n in gain:
            al += n
            if al > ret: ret = al
        return ret
# @lc code=end

s = Solution()
print(s.largestAltitude([-5,1,5,0,-7]))
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))
