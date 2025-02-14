#
# @lc app=leetcode.cn id=2390 lang=python3
#
# [2390] 从字符串中移除星号
#
from typing import *

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

# @lc code=end

s = Solution()
print(s.removeStars("leet**cod*e"))
print(s.removeStars("erase*****"))
