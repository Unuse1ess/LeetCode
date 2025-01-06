#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
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
                if node.left or node.right:
                    queue.append(node.left)
                    queue.append(node.right)
        return str(res)
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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        if root.left is None and root.right is None:
            self.__max = root.val if root.val > self.__max else self.__max
            return root.val
        l = self.dfs(root.left)
        l = l if l > 0 else 0
        r = self.dfs(root.right)
        r = r if r > 0 else 0
        tmp = l + r + root.val
        self.__max = self.__max if self.__max > tmp else tmp
        return root.val + (l if l > r else r)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.__max = -2000
        ret = self.dfs(root)
        return ret if ret > self.__max else self.__max
# @lc code=end

s = Solution()
print(s.maxPathSum(TreeNode.create([1,2,3])))
print(s.maxPathSum(TreeNode.create([-10,9,20,None,None,15,7])))
print(s.maxPathSum(TreeNode.create([10,6,20,None,None,15,7])))
print(s.maxPathSum(TreeNode.create([0])))
print(s.maxPathSum(TreeNode.create([-2,1])))
