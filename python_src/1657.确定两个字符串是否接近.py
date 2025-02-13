#
# @lc app=leetcode.cn id=1657 lang=python3
#
# [1657] 确定两个字符串是否接近
#
from typing import *

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        return c1.keys() == c2.keys() and Counter(c1.values()) == Counter(c2.values())
        
# @lc code=end

s = Solution()
print(s.closeStrings("abc", "bca"))
print(s.closeStrings("a", "aa"))
print(s.closeStrings("cabbba", "abbccc"))

## false
print(s.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))