#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#
from typing import *
from math import *

class Solution0:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == "" or str2 == "":
            return str1 + str2

        a = len(str1)
        b = len(str2)

        if a < b:
            if str2[:a] == str1:
                return self.gcdOfStrings(str2[a:], str1)
            else:
                return ""
        else:
            if str1[:b] == str2:
                return self.gcdOfStrings(str1[b:], str2)
            else:
                return ""

class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while True:
            a = len(str1)
            b = len(str2)

            if a == 0 or b == 0:
                return str1 + str2
            
            if a < b:
                if str2[:a] == str1:
                    str2 = str2[a:]
                else:
                    return ""
            else:
                if str1[:b] == str2:
                    str1 = str1[b:]
                else:
                    return ""

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]
# @lc code=end

s = Solution()
print(s.gcdOfStrings("ABCABC", "ABC"))
print(s.gcdOfStrings("ABABAB", "ABAB"))
print(s.gcdOfStrings("LEET", "CODE"))

## ""
print(s.gcdOfStrings("ABCDEF", "ABC"))