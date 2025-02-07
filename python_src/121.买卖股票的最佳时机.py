#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import *

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        buy = prices[0]

        for price in prices[1:]:
            if price < buy:
                buy = price
            else:
                tmp = price - buy
                if tmp > ret: ret = tmp
        return ret
# @lc code=end

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
