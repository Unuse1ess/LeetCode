#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from typing import List

class Solution0:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        if size == 0:
            return [newInterval]
        
        if newInterval[0] < intervals[0][0]:
            tmp = [newInterval] + intervals
        else:
            i = 0
            tmp = []
            while i < size and newInterval[0] >= intervals[i][0]:
                tmp.append(intervals[i])
                i += 1
            tmp.append(newInterval)
            tmp.extend(intervals[i:])
        
        ret = [tmp[0]]
        
        for i in tmp[1:]:
            if i[0] <= ret[-1][1]:
                # ret[-1][1] = i[1] if i[1] > ret[-1][1] else ret[-1][1]
                ret[-1][1] = max(ret[-1][1], i[1])
            else:
                ret.append(i)
        return ret

        
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        if size == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        # MAX = 1000000
        # l, r = MAX, MAX
        l, r = -1, -1
        ret = [[-1, -1]]
        for i in intervals:
            if newInterval[1] < i[0] or newInterval[0] > i[1]:
                if r != -1:
                    ret.append([l, r])
                    r = -1
                if ret[-1][1] < newInterval[0] and newInterval[1] < i[0]:
                    ret.append(newInterval)
                    l, r = -2, -1

                ret.append(i)
                continue
            if newInterval[0] <= i[1]:
                if l == -1:
                    l = min(newInterval[0], i[0])
                r = max(newInterval[1], i[1])
                continue
            elif newInterval[1] >= i[0]:
                r = max(newInterval[1], i[1])
                continue

        if l == -1 and r == -1:
            ret.append(newInterval)
        elif r != -1:
            ret.append([l, r])

        return ret[1:]
# @lc code=end

s = Solution()
print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
print(s.insert(intervals = [[1,5]], newInterval = [6,8]))
print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[15,16]], newInterval = [6,15]))
print(s.insert(intervals = [[1,5]], newInterval = [0,0]))
print(s.insert(intervals = [[3,5],[12,15]], newInterval = [6,6]))
print(s.insert(intervals = [], newInterval = [5,7]))
