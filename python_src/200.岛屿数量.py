#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import *
from copy import *
from collections import *

class Solution0:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        # access = deepcopy(grid)
        cnt = 0
        # self.grid = grid
        self.access = grid
        access = grid
        self.m = m
        self.n = n
        
        a, b = 0, -1
        queue: Deque[Tuple[int]] = deque()
        # queue: Set[Tuple[int]] = set()
        while True:
            a, b = self.find_new_island(a, b + 1)
            if a == -1:
                return cnt
            cnt += 1
            # queue.add((a, b))
            queue.append((a, b))
            while len(queue) > 0:
                # i, j = queue.pop()
                i, j = queue.popleft()
                if not (0 <= i < m) or not (0 <= j < n):
                    continue
                if access[i][j] == "1":
                    access[i][j] = "2"
                    # queue.update([(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)])
                    queue.extend([(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)])
    def find_new_island(self, a: int, b: int) -> Tuple[int]:
        if b >= self.n:
            b = 0
            a += 1
            
        i, j = a, b
        while i < self.m:
            while j < self.n:
                if self.access[i][j] == "1":
                    return i, j
                j += 1
            i += 1
            j = 0
        return -1, -1

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        i = 0
        cnt = 0
        while i < self.m:
            j = 0
            while j < self.n:
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(i, j)
                j += 1
            i += 1
        return cnt

    def dfs(self, a: int, b: int):
        if not (0 <= a < self.m) or not (0 <= b < self.n):
            return
        if self.grid[a][b] != "1":
            return
        self.grid[a][b] = "2"
        self.dfs(a - 1, b)
        self.dfs(a + 1, b)
        self.dfs(a, b - 1)
        self.dfs(a, b + 1)
# @lc code=end

s = Solution()
print(s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
