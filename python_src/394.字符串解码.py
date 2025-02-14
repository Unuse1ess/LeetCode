#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from typing import *

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        ret = []
        N = len(s)
        i = 0
        tmp_dig = []
        digit = 0
        lpar_pos = 0
        while i < N:
            if s[i].isalpha():
                ret.append(s[i])
            elif s[i].isdigit():
                tmp_dig.append(s[i])
            elif s[i] == "[":
                lpar = 1
                lpar_pos = i
                digit = 1 if len(tmp_dig) == 0 else int(''.join(tmp_dig))
                tmp_dig.clear()
                i += 1
                while lpar != 0:
                    if s[i] == "[":
                        lpar += 1
                    elif s[i] == "]":
                        lpar -= 1
                    i += 1
                i -= 1
                ret.extend(digit * self.decodeString(s[lpar_pos + 1: i]))
            i += 1
        return ''.join(ret)
# @lc code=end

s = Solution()
print(s.decodeString("3[a]2[bc]"))
print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))
print(s.decodeString("abc3[cd]xyz"))
