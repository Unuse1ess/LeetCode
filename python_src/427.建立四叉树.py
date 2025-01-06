#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#
from typing import *
from collections import *

class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft: Node = topLeft
        self.topRight: Node = topRight
        self.bottomLeft: Node = bottomLeft
        self.bottomRight: Node = bottomRight

    def __str__(self):
        queue: Deque[Node] = deque()
        queue.append(self)
        res = []
        while len(queue) > 0:
            node = queue.popleft()
            if node:
                for _, _, attr in Solution.pos_attr(0):
                    queue.append(getattr(node, attr))
                res.append([node.isLeaf, node.val])
            else:
                res.append(None)
        while res[-1] is None:
            res.pop()
        return str(res)

    __repr__ = __str__

class Solution0:
    pos_attr = lambda x: ((0, 0, "topLeft"), (0, x, "topRight"), (x, 0, "bottomLeft"), (x, x, "bottomRight"))
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(i: int, j: int, size: int) -> Tuple[Node, bool]:
            if size == 1:
                return Node(grid[i][j], 1), True
            
            sub_size = size >> 1
            root = Node(1, 0)
            flag = True
            eqflag = True
            for m, n, attr in Solution.pos_attr(sub_size):
                child, rflag = dfs(i + m, j + n, sub_size)
                setattr(root, attr, child)
                flag = flag and rflag
                eqflag = eqflag and grid[i + m][j + n] == grid[i][j]
            if flag and eqflag:
                return Node(grid[i][j], 1), True
            
            return root, False
        
        return dfs(0, 0, len(grid))[0]
        
# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    pos_attr = lambda x: ((0, 0, "topLeft"), (0, x, "topRight"), (x, 0, "bottomLeft"), (x, x, "bottomRight"))
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(i: int, j: int, size: int) -> Node:
            flag = True
            for a, b in ((p, q) for p in range(size) for q in range(size)):
                if grid[i + a][j + b] != grid[i][j]:
                    flag = False
                    break
            if flag:
                return Node(grid[i][j], 1)
            
            root = Node(1, 0)
            subsize = size >> 1
            for m, n, attr in Solution.pos_attr(subsize):
                setattr(root, attr, dfs(i + m, j + n, subsize))
            return root
        return dfs(0, 0, len(grid))

# @lc code=end

s = Solution()
print(s.construct([[0,1],[1,0]]))
print(s.construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]))
