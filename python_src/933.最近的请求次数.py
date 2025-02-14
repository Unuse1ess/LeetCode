#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#
from typing import *

# @lc code=start
class RecentCounter:
    def __init__(self):
        self.req = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.req.append(t)

        target = t - 3000
        l, r = self.start, len(self.req) - 1
        while l <= r:
            mid = (l + r) >> 1
            if self.req[mid] < target:
                l = mid + 1
            elif self.req[mid] >= target:
                r = mid - 1
        self.start = l

        return len(self.req) - self.start

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

    instance: Optional["RecentCounter"] = None

    @staticmethod
    def RecentCounter_():
        RecentCounter.instance = RecentCounter()

    ping_ = lambda *args: RecentCounter.instance.ping(*args)

def run(methods, params):
    print([
        getattr(RecentCounter, m)(*p) for m, p in zip(map(lambda x: x + "_", methods), params)
    ])

run(["RecentCounter", "ping", "ping", "ping", "ping"], [[], [1], [100], [3001], [3002]])
run(["RecentCounter", "ping", "ping", "ping", "ping", "ping", "ping", "ping", "ping"], [[], [1], *([[1]] * 4), [100], [3001], [6000]])
