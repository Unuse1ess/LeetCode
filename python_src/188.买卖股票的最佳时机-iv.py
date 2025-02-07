#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
from typing import *

# 对于k次交易的买卖，每个交易都有2个状态（在当前操作下的最大利润，从交易次数的维度来看）：
# 1：买了i次，能维持原来的状态，或从`卖了 (i - 1) 次`的状态转移而来。
#   转移方程为 buy[i] = max{buy[i - 1], sell[i - 1] - prices[i]}
# 2：卖了i次。能维持原来的状态，或从`买了i次`的状态转移而来。
#   转移方程为 sell[i] = max{sell[i - 1], buy[i] + prices[i]}

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)

        if N == 1: return 0

        buy = [-prices[0]] * (k + 1)
        sell = [0] * (k + 1)

        buy[0] = 0

        for price in prices[1:]:
            for i in range(1, k + 1):
                tmp = sell[i - 1] - price
                if tmp > buy[i]: buy[i] = tmp

                tmp = buy[i] + price
                if tmp > sell[i]: sell[i] = tmp

        return sell[k]
# @lc code=end

s = Solution()
print(s.maxProfit(2, [2,4,1]))
print(s.maxProfit(2, [3,2,6,5,0,3]))


print(s.maxProfit(2, [3,3,5,0,0,3,1,4]))
