#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
from typing import *
from collections import *

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors: List[Node] = neighbors if neighbors is not None else []

    def __str_dfs(self, access: Dict[int, List[int]]):
        if self.val in access:
            return
        access[self.val] = [n.val for n in self.neighbors]
        for n in self.neighbors:
            n.__str_dfs(access)

    def __str__(self) -> str:
        ret = dict()
        self.__str_dfs(ret)
        return str(ret)

    @staticmethod
    def create(l: List[List[int]]):
        if len(l) == 0: return None
        tmp = [Node(i + 1) for i in range(len(l))]

        for i in range(len(l)):
            if len(l[i]) == 0:
                continue
            tmp[i].neighbors = [tmp[j - 1] for j in l[i]]

        return tmp[0]

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        self.access: Dict[int, List[int]] = dict()
        self.dfs(node)
        ret = {k: Node(k) for k in self.access}
        for k in self.access:
            if self.access[k]:
                ret[k].neighbors = [ret[i] for i in self.access[k]]
        return ret[1]

    def dfs(self, node: Node):
        if node.val in self.access:
            return
        self.access[node.val] = None

        if node.neighbors:
            self.access[node.val] = [n.val for n in node.neighbors]
            for n in node.neighbors:
                self.dfs(n)
        
# @lc code=end

s = Solution()
print(s.cloneGraph(Node.create([[2,4],[1,3],[2,4],[1,3]])))
print(s.cloneGraph(Node.create([])))
print(s.cloneGraph(Node.create([[]])))
