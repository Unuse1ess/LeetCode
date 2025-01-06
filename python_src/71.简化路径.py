#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#
from functools import *
from itertools import *
from operator import *
import os

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for name in path.split('/'):
            if name == "..":
                if len(stack) != 0:
                    stack.pop()
                continue
            if name != "." and name != "":
                stack.append(name)
        # if len(stack) == 0:
        #     return '/'
        # return reduce(lambda a, b: a + '/' + b, stack, '')
        return '/' + '/'.join(stack)

# @lc code=end
class Solution0:
    def simplifyPath(self, path: str) -> str:
        return os.path.realpath(path)

s = Solution()
print(s.simplifyPath("/.../a/../b/c/../d/./"))
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/home/user/Documents/../Pictures"))
print(s.simplifyPath("/../"))
