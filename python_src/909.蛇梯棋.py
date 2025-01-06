#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#
from collections import *
from typing import *

# @lc code=start
import numpy as np

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        nn = n * n
        queue = deque()
        def get_pos(i) -> Tuple[int]:
            i -= 1
            row = i // n
            col = i % n
            return n - row - 1, col if row & 1 != 1 else n - col - 1

        visited = set()
        queue.append((1, 0))
        while len(queue) > 0:
            node, step = queue.popleft()
            for i in range(1, 7):
                next_i = node + i
                if next_i > nn:
                    break
                a, b = get_pos(next_i)
                if board[a][b] != -1:
                    next_i = board[a][b]
                if next_i == nn:
                    return step + 1
                if next_i not in visited:
                    queue.append((next_i, step + 1))
                    visited.add(next_i)

        return -1
        
# @lc code=end

s = Solution()
print(s.snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(s.snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,14,-1,-1,-1,-1]]))
print(s.snakesAndLadders(board = [[-1,-1],[-1,3]]))
print(s.snakesAndLadders([[-1,-1,-1],[-1,9,8],[-1,8,9]]))
print(s.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))
print(s.snakesAndLadders([[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]])) # 2
# 4
print(s.snakesAndLadders([[-1,-1,27,13,-1,25,-1],[-1,-1,-1,-1,-1,-1,-1],[44,-1,8,-1,-1,2,-1],[-1,30,-1,-1,-1,-1,-1],[3,-1,20,-1,46,6,-1],[-1,-1,-1,-1,-1,-1,29],[-1,29,21,33,-1,-1,-1]]))
