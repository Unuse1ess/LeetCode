#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import List
from operator import *

class Solution:
    ops = {'+': add, '-': sub, '*': mul, '/': lambda a, b: int(a / b)}
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s.isdigit() or len(s) >= 2:
                stack.append(int(s))
            else:
                b = stack.pop()
                a = stack.pop()
                # print(f'{a} {b} {ops[s].__name__}')
                stack.append(Solution.ops[s](a, b))
        return stack[-1]
# @lc code=end

s = Solution()
print(s.evalRPN(tokens = ["4", "3", "+", "-2", "2", "*", "+"]))
print(s.evalRPN(tokens = ["4", "3", "-"]))
print(s.evalRPN(tokens = ["4","13","5","/","+"]))
print(s.evalRPN(tokens = ["2","1","+","3","*"]))
print(s.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
