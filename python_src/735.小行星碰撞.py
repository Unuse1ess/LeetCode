#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 小行星碰撞
#
from typing import *

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                size = -ast
                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < size:
                    stack.pop()
                
                if len(stack) > 0:
                    if stack[-1] < 0:
                        stack.append(ast)
                    elif stack[-1] == size:
                        stack.pop()
                else:
                    stack.append(ast)
        return stack
# @lc code=end

s = Solution()
print(s.asteroidCollision([5,10,-5]))
print(s.asteroidCollision([8,-8]))
print(s.asteroidCollision([10,2,-5]))

print(s.asteroidCollision([5,-2,-10]))

## [-2,-1,1,2]
print(s.asteroidCollision([-2,-1,1,2]))

## [-2,-2]
print(s.asteroidCollision([-2,-2,1,-1]))

## [-2,1]
print(s.asteroidCollision([-2,1,1,-1]))