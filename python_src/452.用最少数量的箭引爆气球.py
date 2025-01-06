#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
from functools import *
from operator import *
from itertools import *

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=itemgetter(0))
        # l, r = points[0]
        # ball = 0
        r = points[0][1]
        arrow = 0
        # for a, b in islice(points, 1, None):
        for a, b in points[1:]:
            if a <= r:
                # l = a
                # r = min(r, b)
                if b < r:
                    r = b
            else:
                arrow += 1
                # l, r = a, b
                r = b

        return arrow + 1
            
# @lc code=end

s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[1,4],[1,3],[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
