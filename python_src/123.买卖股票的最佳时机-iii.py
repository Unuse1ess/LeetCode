#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
from typing import *

# 时间逆流法，第一次交易正常买卖，第二次交易先卖后买（倒序遍历）。

class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        if N == 1: return 0

        dp0 = [0] * N
        dp1 = [0] * N
        buy0 = prices[0]
        buy1 = prices[-1]

        for i in range(1, N):
            dp0[i] = dp0[i - 1]
            if prices[i] < buy0:
                buy0 = prices[i]
            else:
                tmp = prices[i] - buy0
                if tmp > dp0[i]: dp0[i] = tmp
            
            dp1[-i - 1] = dp1[-i]
            if prices[-i - 1] > buy1:
                buy1 = prices[-i - 1]
            else:
                tmp = buy1 - prices[-i - 1]
                if tmp > dp1[-i - 1]: dp1[-i - 1] = tmp

        return max(dp0[i] + dp1[i] for i in range(N))

# 对于k次交易的买卖，每个交易都有2个状态（在当前操作下的最大利润）：
# 1：买了i次，能维持原来的状态，或从`卖了 (i - 1) 次`的状态转移而来。
#   转移方程为 buy[i] = max{buy[i - 1], sell[i - 1] - prices[i]}
# 2：卖了i次。能维持原来的状态，或从`买了i次`的状态转移而来。
#   转移方程为 sell[i] = max{sell[i - 1], buy[i] + prices[i]}

# @lc code=start
class Solution:
    # MIN = -1000000
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        if N == 1: return 0

        buy0 = -prices[0]
        sell0 = 0
        buy1 = -prices[0]
        sell1 = 0

        for price in prices:
            if -price > buy0: buy0 = -price

            tmp = buy0 + price
            if tmp > sell0: sell0 = tmp

            tmp = sell0 - price
            if tmp > buy1: buy1 = tmp
            
            tmp = buy1 + price
            if tmp > sell1: sell1 = tmp

        return sell1
# @lc code=end

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([1]))
