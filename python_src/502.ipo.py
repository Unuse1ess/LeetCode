#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
from typing import *
from heapq import *
from operator import *

# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if min(capital) > w:
            return w
        if max(capital) <= w:
            return sum(nlargest(k, profits)) + w

        size = len(profits)
        proj = sorted(zip(capital, profits), key=itemgetter(0))
        heap = []
        cur = 0
        
        for _ in range(k):
            while cur < size and proj[cur][0] <= w:
                heappush(heap, -proj[cur][1])
                cur += 1

            if len(heap) != 0:
                w -= heappop(heap)
            else:
                break

        return w
        
# @lc code=end

s = Solution()
print(s.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))
print(s.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))

print(s.findMaximizedCapital(1,0,[1,2,3],[1,1,2]))
print(s.findMaximizedCapital(10, 0, [1,2,3], [0,1,2]))