#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
from typing import *
from operator import *

# @lc code=start
class Solution:
    INF = float("inf")
    def maxPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        if size <= 2: return size

        k = Counter()
        tmp: Set[Tuple[float, float]] = set()
        
        for i in range(size):
            tmp.clear()
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                dx = x2 - x1
                if dx == 0:
                    t = Solution.INF
                    b = x1
                else:
                    t = (y2 - y1) / dx
                    b = y1 - t * x1
                    t = round(t, 8)
                    b = round(b, 8)
                    
                tmp.add((t, b))
                
            k.update(tmp)

        return k.most_common(1)[0][1] + 1
        
# @lc code=end

s = Solution()
print(s.maxPoints([[1,1],[2,2],[3,3]]))
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

## 3
print(s.maxPoints([[-6,-1],[3,1],[12,3]]))

## 7
print(s.maxPoints([[0,1],[0,0],[0,4],[0,-2],[0,-1],[0,3],[0,-4]]))

## 2
print(s.maxPoints([[5151,5150],[0,0],[5152,5151]]))

# print(math.log10(1/20000))