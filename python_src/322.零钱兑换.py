#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from typing import *

class Solution0:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp: List[int] = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    tmp = dp[i - c] + 1
                    if tmp < dp[i]:
                        dp[i] = tmp
        return dp[amount] if dp[amount] != amount + 1 else -1
    
# 被设为1的位置处的索引值为可以用coins组合出的数字。
# 每次以上一次的状态向前走c步，即为这些硬币值的线性组合。

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cnt = 0
        path = 1 << amount
        while path & 1 != 1:
            tmp = path
            for c in coins:
                path |= tmp >> c
            if tmp == path:
                return -1
            cnt += 1
        return cnt
# @lc code=end

s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
