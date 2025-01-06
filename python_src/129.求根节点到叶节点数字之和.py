#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
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

class Solution0:
    def dfs(self, root: Optional[TreeNode], num: str) -> int:
        if root is None:
            return 0
        s = num + str(root.val)
        if root.left is None and root.right is None:
            return int(num + str(root.val))
        return self.dfs(root.left, s) + self.dfs(root.right, s)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, "")
            
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], num: int) -> int:
        if root is None:
            return 0
        s = num * 10 + root.val
        if root.left is None and root.right is None:
            return s
        return self.dfs(root.left, s) + self.dfs(root.right, s)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
# @lc code=end

s = Solution()
print(s.sumNumbers(TreeNode.create([1,2,3])))
print(s.sumNumbers(TreeNode.create([4,9,0,5,1])))
