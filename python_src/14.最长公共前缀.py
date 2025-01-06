#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import *

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        len0 = len(strs[0])
        cp = ''
        pos = 0
        
        while True:
            if pos == len0:
                return cp
            c = strs[0][pos]
            flag = True
            for s in strs[1:]:
                if len(s) == pos:
                    return cp
                if c != s[pos]:
                    flag = False
                    break
            if flag:
                cp += c
            else:
                break
                
            pos += 1

        return cp
# @lc code=end

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["flower","flow","flowers"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))

