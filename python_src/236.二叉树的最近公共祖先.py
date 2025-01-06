#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
from typing import *
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

    def __str__(self):
        queue = deque()
        queue.append(self)
        res = []
        while len(queue) > 0:
            node: TreeNode = queue.popleft()
            res.append(node.val if node else None)
            if node:
                # if node.left or node.right:
                queue.append(node.left)
                queue.append(node.right)
        
        while res[-1] is None:
            del res[-1]
        return str(res)

    def __repr__(self):
        return str(self)
    @staticmethod
    def create(l: List[int | None]) -> "TreeNode":
        if len(l) == 0:
            return None
        root = TreeNode(l[0])
        queue = deque()
        queue.append(root)
        i = 1
        while i < len(l):
            node: TreeNode = queue.popleft()
            node.left = TreeNode(l[i]) if l[i] is not None else None
            if i + 1 < len(l):
                node.right = TreeNode(l[i + 1]) if l[i + 1] is not None else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 2
        return root

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, p: TreeNode, q: TreeNode):
        while self.__p is None or self.__q is None:
            cur = self.__node[-1]
            if cur[1] == 0:
                cur[1] = 1
                if cur[0].left:
                    self.__node.append([cur[0].left, 0])
            elif cur[1] == 1:
                cur[1] = 2
                if cur[0].val == p.val:
                    self.__p = [i[0] for i in self.__node]
                elif cur[0].val == q.val:
                    self.__q = [i[0] for i in self.__node]

                if cur[0].right:
                    self.__node.append([cur[0].right, 0])
            elif cur[1] == 2:
                self.__node.pop()

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.__node: List[List[TreeNode]] = [[root, 0]]
        self.__p: List[TreeNode] = None
        self.__q: List[TreeNode] = None
        self.dfs(p, q)
        size1 = len(self.__p)
        size2 = len(self.__q)
        if size1 < size2:
            i = size1 - 1
            while self.__p[i].val != self.__q[i].val:
                i -= 1
            return self.__p[i]
        else:
            i = size2 - 1
            while self.__p[i].val != self.__q[i].val:
                i -= 1
            return self.__q[i]

# @lc code=end

s = Solution()
print(s.lowestCommonAncestor(TreeNode.create([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(5), TreeNode(1)))
print(s.lowestCommonAncestor(TreeNode.create([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(5), TreeNode(4)))
print(s.lowestCommonAncestor(TreeNode.create([1,2]), TreeNode(1), TreeNode(2)))
