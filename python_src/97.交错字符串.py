#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
from typing import *
from collections import *

# 利用Python负数索引简化特例判断 (i == 0 与 j == 0)。
# 可行性在于-1为数组最后一个元素，此时必然为MAX。

class Solution0:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        h1, h2, h3 = Counter(s1), Counter(s2), Counter(s3)
        if h3 != h1 + h2: return False

        slen1 = len(s1)
        slen2 = len(s2)
        slen3 = len(s3)

        if slen1 == 0:
            return s2 == s3
        elif slen2 == 0:
            return s1 == s3

        MAX = slen3 + 1

        dp: List[List[int]] = [[MAX for _ in range(slen1 + 1)] for _ in range(slen2 + 1)]
        dp[0][0] = 0

        for i in range(slen2 + 1):
            for j in range(slen1 + 1):
                if dp[i - 1][j] != MAX and s3[dp[i - 1][j]] == s2[i - 1]:
                    dp[i][j] = dp[i - 1][j] + 1
                elif dp[i][j - 1] != MAX and s3[dp[i][j - 1]] == s1[j - 1]:
                    dp[i][j] = dp[i][j - 1] + 1

        print(dp)
        return dp[slen2][slen1] == slen3

# 在滚动数组的情况下，dp[-1]为2维情况下的dp[i - 1][-1]，而不是dp[i][-1]，
# 因此需要判断特例，或多使用1个数组记录上一次状态。

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        h1, h2, h3 = Counter(s1), Counter(s2), Counter(s3)
        if h3 != h1 + h2: return False

        slen1 = len(s1)
        slen2 = len(s2)
        slen3 = len(s3)

        if slen1 == 0:
            return s2 == s3
        elif slen2 == 0:
            return s1 == s3

        MAX = slen3 + 1

        dp: List[int] = [MAX for _ in range(slen1 + 2)]
        dp[0] = 0

        for j in range(1, slen1 + 1):
            if s3[dp[j - 1]] == s1[j - 1]:
                dp[j] = j
            else:
                break

        for i in range(1, slen2 + 1):
            if dp[0] != MAX and s3[dp[0]] == s2[i - 1]:
                dp[0] += 1
            else:
                dp[0] = MAX
            for j in range(1, slen1 + 1):
                if dp[j] != MAX and s3[dp[j]] == s2[i - 1]:
                    dp[j] += 1
                elif dp[j - 1] != MAX and s3[dp[j - 1]] == s1[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = MAX

        return dp[slen1] == slen3
# @lc code=end

s = Solution()
print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))

print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
print(s.isInterleave(s1 = "", s2 = "", s3 = ""))

print(s.isInterleave("adc", "aabcd", "aadabccd"))
print(s.isInterleave("adc", "aabcd", "adaabccd"))

## true
print(s.isInterleave("a", "b", "ab"))