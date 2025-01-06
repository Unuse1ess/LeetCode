#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
from collections import *

class Solution0:
    def addBinary(self, a: str, b: str) -> str:
        res = deque()
        z = ord('0')
        al = len(a)
        bl = len(b)
        l = al if al < bl else bl
        carry = 0
        for i in range(1, l + 1):
            na = ord(a[-i]) - z
            nb = ord(b[-i]) - z
            n = na + nb + carry
            carry = n > 1
            n %= 2
            res.appendleft(chr(n + z))
        start = i + 1
        for i in range(start, al + 1):
            na = ord(a[-i]) - z
            n = na + carry
            carry = n > 1
            n %= 2
            res.appendleft(chr(n + z))
        start = i + 1
        for i in range(start, bl + 1):
            nb = ord(b[-i]) - z
            n = nb + carry
            carry = n > 1
            n %= 2
            res.appendleft(chr(n + z))
        if carry:
            res.appendleft('1')
        return ''.join(res)
        
# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, base=2) + int(b, base=2):b}"
# @lc code=end

s = Solution()
print(s.addBinary(a = "11", b = "1"))
print(s.addBinary(a = "1010", b = "1011"))
