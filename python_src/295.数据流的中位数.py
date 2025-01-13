#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
from typing import *
from heapq import *
from sortedcontainers import *

class MedianFinder0:
    def __init__(self):
        self.data = SortedList()

    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        n = len(self.data)
        a = (n >> 1) - ((n & 1) ^ 1)
        b = (n >> 1)
        return (self.data[a] + self.data[b]) / 2

# @lc code=start
class MedianFinder:
    def __init__(self):
        self.hmin = [100000]
        self.hmax = [100000]

    def addNum(self, num: int) -> None:
        if num <= -self.hmax[0]:
            heappush(self.hmax, -num)
        else:
            heappush(self.hmin, num)

        d = len(self.hmin) - len(self.hmax)

        if d == 2:
            heappush(self.hmax, -heappop(self.hmin))
        elif d == -1:
            heappush(self.hmin, -heappop(self.hmax))

    def findMedian(self) -> float:
        n = len(self.hmax) + len(self.hmin)
        if n & 1 == 1:
            return self.hmin[0]
        else:
            return (-self.hmax[0] + self.hmin[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

    instance: 'MedianFinder' = None

    @staticmethod
    def MedianFinder_():
        MedianFinder.instance = MedianFinder()

    addNum_ = lambda *args: MedianFinder.instance.addNum(*args)
    findMedian_ = lambda *args: MedianFinder.instance.findMedian(*args)

def run(methods, params):
    print(
        [getattr(MedianFinder, m)(*p)
        for m, p in
        zip(map(lambda s: s + "_", methods), params)]
    )

run(
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
[[], [1], [2], [], [3], []]
)
run(
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"] + ["addNum"] * 4 + ["findMedian"],
[[], [1], [2], [], [3], []] + [[-i] for i in range(4)] + [[]]
)
