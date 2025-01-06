#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
from functools import *
from itertools import *
from operator import *

# @lc code=start
class Solution:
    table = {'(': ')', '[': ']', '{': '}'}
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        
        for c in s:
            if c in Solution.table:
                stack.append(Solution.table[c])
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False
        return len(stack) == 0
# @lc code=end

s = Solution()
print(s.isValid(s = "()"))
print(s.isValid(s = "()[]{}"))
print(s.isValid(s = "(]"))
print(s.isValid(s = "([)]"))
print(s.isValid(s = "{[]}"))
print(s.isValid(s = "([)]"))
print(s.isValid(s = "(("))
print(s.isValid(s = "))"))
print(s.isValid(s = "]"))
print(s.isValid(s = "["))
