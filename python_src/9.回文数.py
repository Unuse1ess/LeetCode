#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
from typing import *

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) >> 1):
            if x[i] != x[-i - 1]:
                return False
        return True
        
# @lc code=end

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(12321))
print(s.isPalindrome(12321))
