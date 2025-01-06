#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from typing import *
from collections import *

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eqt = defaultdict(list)
        ret = []
        for eq, v in zip(equations, values):
            eqt[eq[0]].append((eq[1], v))
            eqt[eq[1]].append((eq[0], 1./v))

        self.eqt = eqt
        self.access = set()
        
        for a, b in queries:
            self.access.clear()
            if a not in eqt or b not in eqt:
                ret.append(-1.)
                continue
            ret.append(self.dfs(a, b))
        return ret

    def dfs(self, v: str, target: str) -> float:
        if v in self.access:
            return -1.
        self.access.add(v)
        for deno, frac in self.eqt[v]:
            if deno == target:
                return frac
            r = self.dfs(deno, target)
            if r != -1.:
                return r * frac
        return -1.
        
# @lc code=end

s = Solution()
print(s.calcEquation(
equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
))
print(s.calcEquation(
equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
))
print(s.calcEquation(
equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
))