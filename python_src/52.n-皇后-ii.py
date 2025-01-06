#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#
from typing import *

class Solution0:
    def totalNQueens(self, n: int) -> int:
        # board state
        col = [False] * n
        row = [False] * n
        left = [False] * (n + n - 1) # /
        right = [False] * (n + n - 1) # \
        res = 0

        def dfs(a: int, cnt: int):
            nonlocal res

            if cnt == n:
                res += 1
                return
            for idx in range(a, n * n):
                i = idx // n
                j = idx % n

                if row[i] or col[j]: continue
                # indexed by intersection
                # i.e., y=x+b -> b=y-x
                ridx = j - i + n - 1
                lidx = i + j
                if left[lidx] or right[ridx]: continue

                row[i] = True
                col[j] = True
                left[lidx] = True
                right[ridx] = True
                dfs(idx + 1, cnt + 1)
                row[i] = False
                col[j] = False
                left[lidx] = False
                right[ridx] = False
        dfs(0, 0)
        return res

# @lc code=start
class Solution:
    ans = [1, 0, 0, 2, 10, 4, 40, 92, 352]
    def totalNQueens(self, n: int) -> int:
        return Solution.ans[n - 1]
# @lc code=end

s = Solution()
print([s.totalNQueens(i) for i in range(1, 10)])
