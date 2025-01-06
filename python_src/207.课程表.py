#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
from typing import *
from collections import *
from operator import *

class Solution0:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 or numCourses == 0:
            return True
        pre = defaultdict(set)
        rev = defaultdict(set)
        prev = -1
        while prev != len(pre):
            prev = len(pre)
            for a, b in prerequisites:
                pre[a].add(b)
                rev[b].add(a)
                for i in rev[a]:
                    if i == a or i == b:
                        return False
                    pre[i].add(b)
                    rev[b].add(i)
                for i in pre[b]:
                    if i == b or i == a:
                        return False
                    rev[i].add(a)
                    pre[a].add(i)
        return True

class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 or numCourses == 0:
            return True

        self.state = {i: 0 for i in range(numCourses)}
        self.graph = defaultdict(list)
        for a, b in prerequisites:
            self.graph[a].append(b)

        for k in self.state:
            if self.state[k] == 0:
                if not self.dfs(k):
                    return False
        return True
    
    def dfs(self, node: int) -> bool:
        s = self.state[node]
        if s == 0:
            self.state[node] = 1
            for i in self.graph[node]:
                if not self.dfs(i):
                    return False
            # self.stack.append(node)
            self.state[node] = 2
        elif s == 1:
            return False

        return True

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 or numCourses == 0:
            return True

        graph = defaultdict(list)
        queue = deque()
        _in = defaultdict(int)

        for a, b in prerequisites:
            graph[a].append(b)
            _in[b] += 1
        
        for k in range(numCourses):
            if _in[k] == 0:
                queue.append(k)

        cnt = 0
        while len(queue) > 0:
            cnt += 1
            node = queue.popleft()
            for i in graph[node]:
                _in[i] -= 1
                if _in[i] == 0:
                    queue.append(i)
                
        return cnt == numCourses

# @lc code=end

s = Solution()
print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
print(s.canFinish(numCourses = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]]))
print(s.canFinish(numCourses = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4],[3,1]]))
print(s.canFinish(numCourses = 5, prerequisites = [[0,1],[3,4],[3,1],[1,2],[2,3]]))
print(s.canFinish(4, [[0,1],[2,3],[1,2],[3,0]]))
print(s.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
print(s.canFinish(3, [[0,1],[0,2],[1,2]]))
