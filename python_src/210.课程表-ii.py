#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#
from typing import *

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            self.graph[a].append(b)

        self.state = {i: 0 for i in range(numCourses)}
        self.stack = []

        for i in range(numCourses):
            if self.state[i] == 0:
                if not self.dfs(i):
                    return []
        return self.stack

    def dfs(self, node: int) -> bool:
        s = self.state[node]
        if s == 0:
            self.state[node] = 1
            for i in self.graph[node]:
                if not self.dfs(i):
                    return False
            self.stack.append(node)
            self.state[node] = 2
        elif s == 1:
            return False

        return True
        
# @lc code=end

s = Solution()
print(s.findOrder(numCourses = 2, prerequisites = [[1,0]]))
print(s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(numCourses = 1, prerequisites = []))
