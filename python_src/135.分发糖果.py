#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
from typing import *

class Solution0:
    def candy(self, ratings: List[int]) -> int:
        import numpy as np

        l = len(ratings)
        if l == 1:
            return 1

        cdy = [1 for _ in ratings]
        idx = np.argsort(ratings)
        for i in idx:
            # print(i)
            if i == 0:
                if ratings[0] < ratings[1] and cdy[0] >= cdy[1]:
                    cdy[1] = cdy[0] + 1
                continue
            if i == l - 1:
                if ratings[l - 1] < ratings[l - 2] and cdy[l - 1] >= cdy[l - 2]:
                    cdy[l - 2] = cdy[l - 1] + 1
                continue
            if ratings[i] < ratings[i - 1] and cdy[i] >= cdy[i - 1]:
                cdy[i - 1] = cdy[i] + 1
            if ratings[i] < ratings[i + 1] and cdy[i] >= cdy[i + 1]:
                cdy[i + 1] = cdy[i] + 1

        # print(cdy)
        return sum(cdy)

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        if l == 1:
            return 1
        
        inc, dec = 1, 0
        cdy = 1
        pre = 1
        for i in range(1, l):
            if ratings[i - 1] <= ratings[i]:
                dec = 0
                inc += 1
                pre = 1 if ratings[i - 1] == ratings[i] else pre + 1
                cdy += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                cdy += dec
                pre = 1

        return cdy

# @lc code=end

print(Solution().candy([1, 0, 2]))
print(Solution().candy([1, 2, 2]))
print(Solution().candy([1,3,2,2,1]))
