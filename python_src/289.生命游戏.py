#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
from typing import *
from copy import *

class Solution0:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = len(board)
        w = len(board[0])

        board0 = [[0] * (w + 2)] + [[0] + [board[i][j] for j in range(w)] + [0] for i in range(h)]
        board0.append([0] * (w + 2))
        # print(board0)

        for i in range(1, h + 1):
            for j in range(1, w + 1):
                s = 0
                for y in range(i - 1, i + 2):
                    for x in range(j - 1, j + 2):
                        s += board0[y][x]
                board[i - 1][j - 1] = s - board[i - 1][j - 1]
        # print(board)

        for i in range(h):
            for j in range(w):
                board[i][j] = 0 if board[i][j] < 2 or board[i][j] > 3 else board0[i + 1][j + 1] if board[i][j] == 2 else 1

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = len(board)
        w = len(board[0])

        get_value = lambda i, j: board[i][j] if 0 <= i < h and 0 <= j < w else 0
        
        for i in range(h):
            for j in range(w):
                s = 0
                for y in range(i - 1, i + 2):
                    for x in range(j - 1, j + 2):
                        # v = get_value(y, x)
                        # s += v == 1 or v == -1
                        s += get_value(y, x) & 1
                s -= board[i][j]
                # print(i, j, s)
                # if s < 2 or s > 3:
                #     board[i][j] = -1 if board[i][j] == 1 else 0
                # elif s == 3:
                #     board[i][j] = 2 if board[i][j] == 0 else 1
                if s == 3:
                    board[i][j] |= 2
                elif s == 2:
                    board[i][j] |= (board[i][j] & 1) << 1
        # print(board)
        for i in range(h):
            for j in range(w):
                # board[i][j] = int(board[i][j] > 0)
                board[i][j] >>= 1
# @lc code=end

s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)
print(board)

board = [[1,1],[1,0]]
s.gameOfLife(board)
print(board)

board = [[0]]
s.gameOfLife(board)
print(board)
