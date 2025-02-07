#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#
from typing import *

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = []
        for a, b in zip(word1, word2):
            ret.extend((a, b))
        a = len(word1)
        b = len(word2)
        if a > b:
            return ''.join(ret + list(word1[b:]))
        else:
            return ''.join(ret + list(word2[a:]))
# @lc code=end

s = Solution()
print(s.mergeAlternately("abc", "pqr"))
print(s.mergeAlternately("ab", "pqrs"))
print(s.mergeAlternately("abcd", "pq"))
