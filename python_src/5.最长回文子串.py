#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
from typing import *

# TODO: Implement another two solutions

# 定义dp[i, j]为s[i: i - j]是否为回文子串。
# s[i: i]，s[i: i + 1]（即j == 0与j == 1）也是回文的。

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)

        dp = [[True, True, *((False,) * (slen - 1))] for _ in range(slen)]

        idx, cnt = 0, 1

        for i in range(1, slen):
            for j in range(2, i + 2):
                dp[i][j] = dp[i - 1][j - 2] and s[i] == s[i - j + 1]
                if dp[i][j] and j > cnt:
                    idx, cnt = i, j

        return s[idx - cnt + 1: idx + 1]
# @lc code=end

s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("abba"))
print(s.longestPalindrome("abcba"))
print(s.longestPalindrome("aaca"))

## aca
print(s.longestPalindrome("aacabdkacaa"))

## a
print(s.longestPalindrome("a"))
