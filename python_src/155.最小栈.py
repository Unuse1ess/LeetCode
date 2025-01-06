#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
from functools import *
from itertools import *
from operator import *

# @lc code=start
class MinStack:
    def __init__(self):
        self.__stack = []
        self.__min = None

    def push(self, val: int) -> None:
        if self.__min is None or val < self.__min:
            self.__min = val
        self.__stack.append(val)
    def pop(self) -> None:
        if len(self.__stack) != 0:
            val = self.__stack.pop()
            if len(self.__stack) == 0:
                self.__min = None
            elif val == self.__min:
                self.__min = min(self.__stack)
        else:
            self.__min = None
    def top(self) -> int:
        # if len(self.__stack) != 0:
        return self.__stack[-1]
    def getMin(self) -> int:
        return self.__min
# @lc code=end
    MinStack = lambda _: MinStack()

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
methods = ["MinStack", "push","push","push","getMin","pop","top","getMin"][1:]
params = [[],[-2],[0],[-3],[],[],[],[]][1:]

print([m(obj)(*p) for m, p in zip(map(attrgetter, methods), params)])

obj = MinStack()
methods = ["MinStack","push","top","getMin"][1:]
params = [[],[-1],[],[]][1:]

print([m(obj)(*p) for m, p in zip(map(attrgetter, methods), params)])