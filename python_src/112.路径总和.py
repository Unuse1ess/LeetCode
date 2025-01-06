#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
            node.left = TreeNode(l[i]) if l[i] else None
            if i + 1 < len(l):
                node.right = TreeNode(l[i + 1]) if l[i + 1] else None
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
# @lc code=end

s = Solution()
print(s.hasPathSum(TreeNode.create([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))
print(s.hasPathSum(TreeNode.create([1,2,3]), 5))
print(s.hasPathSum(TreeNode.create([]), 0))
