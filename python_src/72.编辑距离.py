#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
from typing import *

class Solution0:
    def minDistance(self, word1: str, word2: str) -> int:
        slen1 = len(word1)
        slen2 = len(word2)

        if slen1 == 0 or slen2 == 0:
            return slen1 + slen2
        
        dp: List[List[int]] = [list(range(slen1 + 1)) for _ in range(slen2 + 1)]

        for i in range(1, slen2 + 1):
            dp[i][0] = i
            for j in range(1, slen1 + 1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[slen2][slen1]
        
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        slen1 = len(word1)
        slen2 = len(word2)

        if slen1 == 0 or slen2 == 0:
            return slen1 + slen2

        dp0: List[int] = list(range(slen1 + 1))
        dp1: List[int] = [0] * (slen1 + 1)

        for i in range(1, slen2 + 1):
            dp1[0] = i
            for j in range(1, slen1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp1[j] = dp0[j - 1]
                else:
                    dp1[j] = 1 + min(dp1[j - 1], dp0[j], dp0[j - 1])

            dp0, dp1 = dp1, dp0

        return dp0[-1]
# @lc code=end

s = Solution()
print(s.minDistance("horse", "ros"))
print(s.minDistance("intention", "execution"))
print(s.minDistance("b", "a"))

# 3
print(s.minDistance("sea", "ate"))