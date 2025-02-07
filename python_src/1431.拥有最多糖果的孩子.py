#
# @lc app=leetcode.cn id=1431 lang=python3
#
# [1431] 拥有最多糖果的孩子
#
from typing import *

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        least_cand = max(candies) - extraCandies
        return [n >= least_cand for n in candies]
        
# @lc code=end

s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))
print(s.kidsWithCandies([4,2,1,1,2], 1))
print(s.kidsWithCandies([12,1,12], 10))
