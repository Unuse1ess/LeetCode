#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = [intervals[0]]
        
        for i in intervals[1:]:
            if i[0] <= ret[-1][1]:
                # ret[-1][1] = i[1] if i[1] > ret[-1][1] else ret[-1][1]
                ret[-1][1] = max(ret[-1][1], i[1])
            else:
                ret.append(i)
        return ret
# @lc code=end

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
print(s.merge([[1,4],[0,4]]))
print(s.merge([[1,4],[2,3]]))
