#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
from typing import *
from collections import *
from copy import *

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m, self.n = len(board), len(board[0])
        self.board = board
        
        for i in range(self.m):
            if board[i][0] == "O":
                self.dfs(i, 0)
            if board[i][self.n - 1] == "O":
                self.dfs(i, self.n - 1)

        for i in range(self.n):
            if board[0][i] == "O":
                self.dfs(0, i)
            if board[self.m - 1][i] == "O":
                self.dfs(self.m - 1, i)

        i = 0
        while i < self.m:
            j = 0
            while j < self.n:
                board[i][j] = "X" if board[i][j] != "B" else "O"
                j += 1
            i += 1

    def dfs(self, a: int, b: int):
        if not (0 <= a < self.m) or not (0 <= b < self.n):
            return

        if self.board[a][b] != "O":
            return

        self.board[a][b] = "B"
        
        self.dfs(a - 1, b)
        self.dfs(a + 1, b)
        self.dfs(a, b - 1)
        self.dfs(a, b + 1)
        
# @lc code=end

def run(p):
    print('\n'.join(str(l) for l in p))
    print()
    s.solve(p)
    print('\n'.join(str(l) for l in p))
    print()

s = Solution()
run([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
run([["X"]])
run([["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","X"]])
run([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"],["X","X","X","X"]])
run([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])
run([["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]])